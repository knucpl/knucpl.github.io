---
layout: about
title: About
permalink: /
# subtitle: <a href='#'>Affiliations</a>. Address. Contacts. Motto. Etc.

# profile:
#   align: right
#   image: prof_pic.jpg
#   image_circular: false # crops the image to make it circular
#   more_info: >
#     <p>555 your office number</p>
#     <p>123 your address street</p>
#     <p>Your City, State 12345</p>

selected_papers: false # includes a list of papers marked as "selected={true}"
social: true # includes social icons at the bottom of the page

announcements:
  enabled: true # includes a list of news items
  scrollable: true # adds a vertical scroll bar if there are more than 3 news items
  limit: 5 # leave blank to include all the news in the `_news` folder

latest_posts:
  enabled: false
  scrollable: true # adds a vertical scroll bar if there are more than 3 new posts items
  limit: 3 # leave blank to include all the blog posts
---


<style>
  /* Fixed aspect ratio: the height never changes between slides, so the content below stays put */
  #homeCarousel{
    border-radius: 12px;
    overflow: hidden;
  }
  #homeCarousel .carousel-item{
    aspect-ratio: 3 / 2;
  }
  #homeCarousel .carousel-item img{
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
    display: block;
  }
</style>

<div id="homeCarousel" class="carousel slide mb-4" data-ride="carousel" data-interval="false">
  <ol class="carousel-indicators">
    <li data-target="#homeCarousel" data-slide-to="0" class="active"></li>
    <li data-target="#homeCarousel" data-slide-to="1"></li>
  </ol>

  <div class="carousel-inner">

    <div class="carousel-item active">
      <img src="{{ '/assets/img/gallery/261016_01.jpg' | relative_url }}" alt="Our group at the 2026 KMS Autumn Meeting">
    </div>

    <div class="carousel-item">
      <img src="{{ '/assets/img/gallery/260327.jpeg' | relative_url }}" alt="Our group">
    </div>

  </div>

  <a class="carousel-control-prev" href="#homeCarousel" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>

  <a class="carousel-control-next" href="#homeCarousel" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>

<script>
  // Auto-advance every 7 s; any slide change (including manual ones) restarts the count
  document.addEventListener('DOMContentLoaded', function () {
    if (!window.jQuery) return;
    var $c = jQuery('#homeCarousel');
    var timer;
    function restart() {
      clearTimeout(timer);
      timer = setTimeout(function () { $c.carousel('next'); }, 7000);
    }
    $c.on('slid.bs.carousel', restart);
    restart();
  });
</script>

<!-- Write your biography here. Tell the world about yourself. Link to your favorite [subreddit](http://reddit.com). You can put a picture in, too. The code is already in, just name your picture `prof_pic.jpg` and put it in the `img/` folder.

Put your address / P.O. box / other info right below your picture. You can also disable any of these elements by editing `profile` property of the YAML header of your `_pages/about.md`. Edit `_bibliography/papers.bib` and Jekyll will render your [publications page](/al-folio/publications/) automatically.

Link to your social media connections, too. This theme is set up to use [Font Awesome icons](https://fontawesome.com/) and [Academicons](https://jpswalsh.github.io/academicons/), like the ones below. Add your Facebook, Twitter, LinkedIn, Google Scholar, or just disable all of them. -->
