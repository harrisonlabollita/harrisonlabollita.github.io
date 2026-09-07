---
layout: page
title: Publications
permalink: /publications/
standfirst: >-
  Peer-reviewed articles and preprints, some invited talks.
  ★ marks equal contribution.

contents:
  - title: Articles &amp; preprints
    anchor: articles
  - title: Invited talks
    anchor: talks
---

<div class="stats">
  <span><strong>{{ site.data.publications | size }}</strong> publications</span>
  <span><strong>{{ site.data.talks | size }}</strong> invited talks</span>
  <span><strong>1404</strong> citations</span>
  <span><strong>17</strong> h-index</span>
  <span><a href="{{ site.links.scholar }}">Google Scholar</a></span>
</div>

<h2 id="articles">Articles and preprints</h2>

<ol class="pubs">
  {%- for pub in site.data.publications %}
  {%- include publication.html pub=pub %}
  {%- endfor %}
</ol>

<h2 id="talks">Invited talks</h2>

<ul class="talks">
  {%- for talk in site.data.talks %}
  <li class="talk">
    <p class="talk__title">{{ talk.title }}</p>
    <p class="talk__where">
      <span>{{ talk.where }}, {{ talk.place }}</span>
      <span class="talk__date">{{ talk.date }}</span>
    </p>
  </li>
  {%- endfor %}
</ul>
