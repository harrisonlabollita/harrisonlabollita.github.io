# harrisonlabollita.github.io

Personal site. Plain Jekyll, one stylesheet, two plugins (feed and sitemap).
Deployed to GitHub Pages by `.github/workflows/jekyll.yml` on push to `master`.

## Local preview

```sh
bundle install
bundle exec jekyll serve --livereload
```

## Where the content lives

| What | Where |
| --- | --- |
| Home page | `index.html` |
| Research narrative | `research.md` |
| Publications | `_data/publications.yml` (generated — see below) |
| Software | `_data/software.yml` |
| Invited talks | `_data/talks.yml` |
| Blog posts | `_posts/YYYY-MM-DD-slug.md` |
| Styling | `assets/css/style.scss` |
| CV PDF | `assets/pdf/cv.pdf` |

## Publications are generated from the CV

The LaTeX CV is the single source of truth for the publication list. After
updating it, regenerate the site's copy rather than editing YAML by hand:

```sh
bin/sync_publications.py ~/path/to/CurriculumVitae/sections/publications.tex
```

Citation counts on `/publications/` are hard-coded in `publications.md` and come
from the CV's `scholar/scholar_stats.tex`. Update them when you refresh the CV.

## Adding a blog post

Create `_posts/2026-09-05-some-title.md`:

```markdown
---
layout: post
title: Some title
date: 2026-09-05
description: One line shown on the writing index.
---

Body text here.
```
