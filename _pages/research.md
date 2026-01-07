---
layout: page
title: Research
permalink: /research/
nav: true
nav_order: 2
---

<style>
  #researchCarousel{
    --carousel-h: 700px;
  }
  #researchCarousel .carousel-item{
    height: var(--carousel-h);
    background: rgba(0,0,0,0.03);
  }
  #researchCarousel .carousel-item img{
    height: 100%;
    width: 100%;
    object-fit: contain;
    object-position: center;
    display: block;
  }

</style>

<div id="researchCarousel" class="carousel slide mb-4" data-ride="carousel" data-interval="6000">
  <ol class="carousel-indicators">
    <li data-target="#researchCarousel" data-slide-to="0" class="active"></li>
    <li data-target="#researchCarousel" data-slide-to="1"></li>
    <li data-target="#researchCarousel" data-slide-to="2"></li>
  </ol>

  <div class="carousel-inner">

    <div class="carousel-item active">
      <img src="{{ '/assets/img/research/01.png' | relative_url }}" alt="01.png">
    </div>

    <div class="carousel-item">
      <img src="{{ '/assets/img/research/02.png' | relative_url }}" alt="02.png">
    </div>

    <div class="carousel-item">
      <img src="{{ '/assets/img/research/03.png' | relative_url }}" alt="03.png">
    </div>

  </div>

  <a class="carousel-control-prev" href="#researchCarousel" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>

  <a class="carousel-control-next" href="#researchCarousel" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>

<script>
  (function () {
    var carousel = document.getElementById('researchCarousel');
    if (!carousel) return;

    var counter = document.getElementById('researchCarouselCounter');
    var total = carousel.querySelectorAll('.carousel-item').length;

    function setCounter(activeIndex){
      if (!counter) return;
      counter.textContent = (activeIndex + 1) + " / " + total;
    }

    // initial
    var active = carousel.querySelector('.carousel-item.active');
    var initIndex = Array.prototype.indexOf.call(carousel.querySelectorAll('.carousel-item'), active);
    setCounter(Math.max(0, initIndex));

    // Bootstrap 4 event
    carousel.addEventListener('slide.bs.carousel', function (e) {
      // e.to = next index in Bootstrap 4
      if (typeof e.to === "number") setCounter(e.to);
    });
  })();
</script>

<ul style="font-size: 1.4rem;">
  <li>고해상도 레이더로 집중호우, 대설 등 추적 관측연구</li>
  <li>차세대 레이더 모의 프로그램 활용 연구</li>
  <li>구름/강수 발달 메커니즘 연구</li>
  <li>강수입자 발달 연구</li>
  <li>강수 내 역학(바람) 연구</li>
</ul>