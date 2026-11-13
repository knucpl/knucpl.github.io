#!/usr/bin/env python
"""Update Scopus cited-by counts for the publications in _bibliography/papers.bib.

Counts come from Elsevier's Scopus Search API (DOI queries, `citedby-count`),
which works with a self-registered API key, and are written to
_data/scopus_citations.yml, keyed by lower-case DOI, for _layouts/bib.liquid.
See https://dev.elsevier.com/tecdoc_cited_by_in_scopus.html.

The API key is read from the SCOPUS_API_KEY environment variable (a GitHub
Actions secret). It is sent only in a request header, never in a URL, and is
masked in error messages, so it does not show up in logs or the saved file.

Scopus attribution rules: every displayed count must be labelled as coming from
Scopus and link to the list of citing documents on scopus.com, and cached
counts must be refreshed at least weekly.
"""

import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime

import yaml

BIB_FILE = "_bibliography/papers.bib"
OUTPUT_FILE = "_data/scopus_citations.yml"
API_URL = "https://api.elsevier.com/content/search/scopus"
BATCH_SIZE = 10  # DOIs per search query
PAGE_SIZE = 25  # results per page (the maximum for keys without a Scopus subscription)
CITEDBY_URL = "https://www.scopus.com/inward/citedby.uri?partnerID=HzOxMe3b&scopus_id={scopus_id}&origin=inward"
SECRET_PARAMS = {"apikey", "insttoken", "access_token"}


class FatalApiError(Exception):
    """An error that makes the whole run unreliable (bad key, quota, outage)."""


def load_dois(path: str) -> list:
    """Return the unique, lower-cased DOIs found in the bib file."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    dois = []
    pattern = re.compile(r"^\s*doi\s*=\s*[{\"](.+?)[}\"]\s*,?\s*$", re.IGNORECASE | re.MULTILINE)
    for match in pattern.finditer(text):
        doi = match.group(1).replace("\\_", "_").strip().lower()
        if doi and doi not in dois:
            dois.append(doi)
    return dois


def strip_secrets(url: str) -> str:
    """Use https and drop any credential query parameters from a URL."""
    parts = urllib.parse.urlsplit(url)
    query = [(k, v) for k, v in urllib.parse.parse_qsl(parts.query) if k.lower() not in SECRET_PARAMS]
    return urllib.parse.urlunsplit(("https", parts.netloc, parts.path, urllib.parse.urlencode(query), ""))


def api_error_text(error: urllib.error.HTTPError, headers: dict) -> str:
    """Return Elsevier's error status from a failed response, with credentials masked."""
    try:
        body = json.loads(error.read().decode("utf-8", "replace"))
        status = body.get("service-error", {}).get("status", {})
        text = f" ({status.get('statusCode', '')}: {status.get('statusText', '')})"
    except Exception:
        return ""
    for secret in (headers.get("X-ELS-APIKey"), headers.get("X-ELS-Insttoken")):
        if secret:
            text = text.replace(secret, "***")
    return text


def api_get(params: dict, headers: dict, retries: int = 2) -> dict:
    """GET the Scopus Search API and return the decoded JSON, retrying transient errors."""
    url = API_URL + "?" + urllib.parse.urlencode(params)
    for attempt in range(retries + 1):
        try:
            request = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.load(response)
        except urllib.error.HTTPError as e:
            detail = api_error_text(e, headers)
            if e.code in (401, 403):
                raise FatalApiError(f"HTTP {e.code}{detail}: the API key (or institution token) was rejected.")
            if e.code == 429:
                raise FatalApiError(f"HTTP 429{detail}: the API key's quota is exhausted.")
            if attempt == retries:
                raise FatalApiError(f"HTTP {e.code}{detail} after {retries + 1} attempts.")
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
            if attempt == retries:
                raise FatalApiError(f"Request failed after {retries + 1} attempts: {e}")
        time.sleep(2 * (attempt + 1))


def search_dois(dois: list, headers: dict) -> list:
    """Return the Scopus Search entries matching any of the DOIs, following pagination."""
    query = " OR ".join(f"DOI({doi})" for doi in dois)
    entries, start = [], 0
    while True:
        results = api_get({"query": query, "count": PAGE_SIZE, "start": start}, headers).get("search-results", {})
        page = [entry for entry in results.get("entry") or [] if "error" not in entry]
        entries.extend(page)
        start += PAGE_SIZE
        if not page or start >= int(results.get("opensearch:totalResults") or 0):
            return entries
        time.sleep(0.3)


def parse_entry(entry: dict) -> dict:
    """Pick the fields bib.liquid needs: count, Scopus ID and citing-documents link."""
    scopus_id = str(entry.get("dc:identifier", "")).replace("SCOPUS_ID:", "").strip()
    links = {}
    for link in entry.get("link") or []:
        if isinstance(link, dict) and link.get("@href"):
            links[link.get("@ref") or link.get("@rel")] = link["@href"]
    if links.get("scopus-citedby"):
        url = strip_secrets(links["scopus-citedby"])
    elif scopus_id:
        url = CITEDBY_URL.format(scopus_id=scopus_id)
    else:
        url = None
    return {
        "citations": int(entry.get("citedby-count") or 0),
        "scopus_id": scopus_id,
        "url": url,
    }


def load_existing(path: str) -> dict:
    if not os.path.exists(path):
        return {}
    try:
        with open(path, encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    except Exception as e:
        print(f"Warning: could not read {path}: {e}. It will be rewritten.")
        return {}


def main() -> int:
    api_key = os.environ.get("SCOPUS_API_KEY", "").strip()
    if not api_key:
        print("SCOPUS_API_KEY is not set; skipping the Scopus citation update.")
        return 0
    if not re.fullmatch(r"[0-9a-fA-F]{32}", api_key):
        print(
            f"Warning: SCOPUS_API_KEY does not look like an Elsevier API key "
            f"(expected 32 hexadecimal characters, got {len(api_key)} characters). Check that it was copied completely."
        )

    headers = {"Accept": "application/json", "X-ELS-APIKey": api_key}
    insttoken = os.environ.get("SCOPUS_INSTTOKEN", "").strip()
    if insttoken:
        headers["X-ELS-Insttoken"] = insttoken

    dois = load_dois(BIB_FILE)
    print(f"Found {len(dois)} DOIs in {BIB_FILE}.")

    papers = {}
    try:
        for i in range(0, len(dois), BATCH_SIZE):
            batch = dois[i : i + BATCH_SIZE]
            for entry in search_dois(batch, headers):
                doi = str(entry.get("prism:doi") or "").strip().lower()
                if doi not in batch:
                    continue
                paper = parse_entry(entry)
                # A DOI can match more than one Scopus record (e.g. an erratum); keep the most cited one.
                if paper["url"] and (doi not in papers or paper["citations"] > papers[doi]["citations"]):
                    papers[doi] = paper
            time.sleep(0.3)
    except FatalApiError as e:
        print(f"Error: {e} {OUTPUT_FILE} was left unchanged.")
        return 1

    for doi in dois:
        if doi in papers:
            print(f"Found: {doi} - Scopus citations: {papers[doi]['citations']}")
        else:
            print(f"Not in Scopus: {doi}")

    if dois and not papers:
        print(f"Error: none of the {len(dois)} DOIs were found in Scopus. {OUTPUT_FILE} was left unchanged.")
        return 1

    print(f"{len(papers)} found, {len(dois) - len(papers)} not in Scopus.")

    existing = load_existing(OUTPUT_FILE)
    if existing.get("papers") == papers:
        print("No changes in Scopus citation data. Skipping file update.")
        return 0

    output = {"metadata": {"last_updated": datetime.now().strftime("%Y-%m-%d")}, "papers": papers}
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        yaml.dump(output, f, width=1000, sort_keys=True, allow_unicode=True)
    print(f"Scopus citation data saved to {OUTPUT_FILE}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
