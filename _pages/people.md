---
layout: page
title: People
permalink: /people/
description: Our research group at Xi’an Jiaotong University.
nav: true
nav_order: 1
---

<div class="people-page">
  {% assign groups = 'phd_students,masters_students,alumni' | split: ',' %}
  {% assign headings = 'Ph.D. Students,Master’s Students,Alumni' | split: ',' %}
  {% for group in groups %}
    <section class="people-section" aria-labelledby="{{ group }}">
      <h2 id="{{ group }}">{{ headings[forloop.index0] }}</h2>
      <ul class="people-list">
        {% for person in site.data.people[group] %}
          <li>
            <span class="person-name">{{ person.name }}</span>
            <span class="person-name-zh" lang="zh">{{ person.name_zh }}</span>
          </li>
        {% endfor %}
      </ul>
    </section>
  {% endfor %}
</div>
