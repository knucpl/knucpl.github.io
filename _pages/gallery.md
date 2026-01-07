---
layout: page
title: Gallery
permalink: /gallery/
nav: true
nav_order: 6
---

<div class="masonry-grid">
  <div class="grid-sizer"></div>

  {% for it in site.data.gallery %}
    <div class="grid-item">
      <a href="{{ it.full | relative_url }}"
         class="glightbox"
         data-gallery="lab-gallery"
         data-title="{{ it.caption | escape }}">
        <img src="{{ it.thumb | relative_url }}" alt="{{ it.alt }}">
      </a>

      {% if it.caption and it.caption != "" %}
      <div class="grid-caption">{{ it.caption }}</div>
      {% endif %}
    </div>
  {% endfor %}
</div>

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/glightbox/dist/css/glightbox.min.css">

<script src="https://cdn.jsdelivr.net/npm/glightbox/dist/js/glightbox.min.js"></script>
<script>
  const lightbox = GLightbox({
    selector: '.glightbox',
    loop: true,
    touchNavigation: true,
    closeButton: true
  });
</script>

<script>
  (function () {
    var grid = document.querySelector('.masonry-grid');
    if (!grid) return;

    function initMasonry() {
      var msnry = new Masonry(grid, {
        itemSelector: '.grid-item',
        columnWidth: '.grid-sizer',
        percentPosition: true,
        gutter: 16
      });

      if (typeof imagesLoaded === 'function') {
        imagesLoaded(grid).on('progress', function () {
          msnry.layout();
        });
      }
    }

    if (typeof Masonry === 'function') {
      initMasonry();
      return;
    }

    var s = document.createElement('script');
    s.src = "https://unpkg.com/masonry-layout@4/dist/masonry.pkgd.min.js";
    s.onload = initMasonry;
    document.head.appendChild(s);
  })();
</script>

<style>
  .masonry-grid { margin-top: 1rem; }
  .grid-sizer, .grid-item { width: 49%; }
  @media (max-width: 992px) { .grid-sizer, .grid-item { width: 48%; } }
  @media (max-width: 576px) { .grid-sizer, .grid-item { width: 100%; } }

  .grid-item { margin-bottom: 16px; }
  .grid-item img {
    width: 100%;
    height: auto;
    display: block;
    border-radius: 10px;
  }
  .grid-caption {
    font-size: 0.95rem;
    margin-top: 0.4rem;
    line-height: 1.3;
    opacity: 0.85;
  }
</style>

