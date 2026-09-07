---
layout: page
title: Software
permalink: /software/
standfirst: >-
    Open-source software for computational quantum materials science research.
---

{%- assign featured = site.data.software.led | where: "featured", true -%}

<ul class="pkgs">
  {%- for pkg in featured %}
  <li class="pkg">
    <div class="pkg__head">
      <p class="pkg__name"><a href="{{ pkg.repo }}">{{ pkg.name }}</a></p>
      <span class="pkg__role">{{ pkg.role }}</span>
      <span class="pkg__lang">{{ pkg.language }}</span>
    </div>
    <p class="pkg__desc">{{ pkg.description }}</p>
    <p class="pkg__links">
      <a href="{{ pkg.repo }}">Repository</a>
      {%- if pkg.doi %}<a href="{{ pkg.doi }}">DOI</a>{% endif -%}
      {%- if pkg.paper %}<span>{{ pkg.paper }}</span>{% endif -%}
      {%- if pkg.note %}<span>{{ pkg.note }}</span>{% endif -%}
    </p>
  </li>
  {%- endfor %}
</ul>

<p class="section__more">
  <a href="{{ site.links.github }}">Everything else on GitHub &rarr;</a>
</p>
