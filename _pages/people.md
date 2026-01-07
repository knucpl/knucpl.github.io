---
layout: page
title: People
permalink: /people/
nav: true
nav_order: 3
---


<style>
  .members-grid{
    --cols: 2;
    display: grid;
    grid-template-columns: repeat(var(--cols), minmax(0, 1fr));
    gap: 48px 24px;
    align-items: start;
    text-align: center;
    margin-top: 24px;
  }

  @media (max-width: 900px){
    .members-grid{ --cols: 2; }
  }
  @media (max-width: 520px){
    .members-grid{ --cols: 1; }
  }

  .member-photo{
    width: 165px;
    height: 180px;
    border-radius: 50%;
    object-fit: cover;
    object-position: center 0%;
    display: block;
    margin: 0 auto 14px auto;
    box-shadow: 0 6px 18px rgba(0,0,0,0.12);
  }

  .member-name{
    font-size: 1.7rem;
    font-weight: 500;
    margin: 0;
    line-height: 1.25;
  }
  .member-role{
    font-weight: bold;
    font-size: 1.2rem;
    margin-top: 0px;
    margin-bottom: 10px;
    opacity: 0.85;
  }
  .member-degree{
    font-size: 0.9rem;
    margin-top: 0px;
    margin-bottom: 0px;
    opacity: 0.85;
  }
  .member-date{
    font-size: 0.7rem;
    margin-top: 0px;
    margin-bottom: 0px;
    opacity: 0.85;
  }
</style>

<style>
  .pi-grid{
    display: grid;
    grid-template-columns: 200px 1fr;
    gap: 28px;
    align-items: start;
    margin-top: 24px;
  }
  @media (max-width: 700px){
    .pi-grid{
      grid-template-columns: 1fr;
      text-align: center;
    }
  }

  .pi-name{
    font-size: 1.9rem;
    font-weight: 600;
    margin: 0 0 6px 0;
  }
  /* .pi-title{
    font-size: 1.1rem;
    opacity: 0.85;
    margin-bottom: 12px;
  } */

  .pi-cv ul{
    margin-top: 6px;
  }
</style>

<div class="pi-grid">
  <div>
    <img class="member-photo"
         src="{{ '/assets/img/people/kwonil.png' | relative_url }}"
         alt="">
    <div class="social"><div class="contact-icons">{% include social.liquid %}</div></div>
  </div>

  <div class="pi-cv" markdown="1">

## Kwonil Kim | 김권일
Assistant Professor<br />
School of Earth System Sciences, College of Natural Sciences<br />
Kyungpook National University

**Education**  
  - (Feb 2023) Ph.D. in Atmospheric Sciences, Kyungpook National University
  - (Aug 2015) B.S. in Astronomy and Atmospheric Sciences, Kyungpook National University

**Experiences**  
  - (Sep 2025–present) Assistant Professor, Kyungpook National University
  - (Aug 2023–Aug 2025) Postdoctoral research associate, Stony Brook University
  - (Mar 2023–Jul 2023) Postdoctoral research associate, Kyungpook National University


</div>
</div>


<br />
<br />

# Lab Members
<div class="members-grid" style="--cols:2;">

  <div class="member-card">
    <img class="member-photo" src="{{ '/assets/img/people/seri.png' | relative_url }}" alt="">
    <p class="member-name">Seri Park<br />박세리</p>
    <p class="member-role">M.S. student</p>
    <p class="member-degree">B.S. (Feb 2026)</p>
    <p class="member-date">Member since Jan 2026</p>
  </div>

  <div class="member-card">
    <img class="member-photo" src="{{ '/assets/img/people/hyeonsik.png' | relative_url }}" alt="">
    <p class="member-name">HyeonSik Yoon<br />윤현식</p>
    <p class="member-role">M.S. student</p>
    <p class="member-degree">B.S. (Feb 2026)</p>
    <p class="member-date">Member since Jan 2026</p>
  </div>

  <div class="member-card">
    <img class="member-photo" src="{{ '/assets/img/people/seokhyun.png' | relative_url }}" alt="">
    <p class="member-name">Seokhyun Jang<br />장석현</p>
    <p class="member-role">B.S. student</p>
    <p class="member-date">Member since Jan 2026</p>
  </div>

  <div class="member-card">
    <img class="member-photo" src="{{ '/assets/img/people/jungmin.png' | relative_url }}" alt="">
    <p class="member-name">Jungmin Lee<br />이정민</p>
    <p class="member-role">B.S. student<span style="font-size:0.5em;"> (B.S.–M.S. integrated)</span></p>
    <p class="member-date">Member since Jan 2026</p>
  </div>

</div>