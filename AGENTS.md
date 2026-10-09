# Hao Li's personal website

This site uses the al-folio v1.2 starter. Its Git history and origin belong to
`aquatoney/aquatoney.github.io`, not the upstream template repository.

## Content and compatibility

- `_pages/about.md` and `_layouts/about.liquid`: biography, recruitment, contact information, and news.
- `_news/`: acceptance announcements; record date sources in `docs/news-sources.md`.
- `_pages/people.md` and `_data/people.yml`: current students and alumni, with English and Chinese names.
- `_pages/publications.md`: publications at the existing `/pubs/` URL.
- `_bibliography/papers.bib`: the single source of publication data.
- `files/`: existing PDF URLs; preserve filenames and contents.
- `CNAME` and the Google verification HTML file must survive migrations.
- `robots.txt` must point crawlers to `https://haolis.com/sitemap.xml`.
- The production URL is `https://haolis.com`, with an empty `baseurl`.
- Do not invent publication metadata, CV facts, news, or missing PDFs.

## al-folio maintenance

Theme layouts and assets come from pinned gems, primarily `al_folio_core`.
Prefer configuration and content changes. Site-specific overrides are allowed
when needed; record them with the al-folio override audit. See
`docs/BOUNDARIES.md` and `docs/ARCHITECTURE.md` for upstream design context.
Their restrictions on contributing to the upstream starter do not prohibit
intentional overrides in this personal site.

Keep plugin declarations in `Gemfile` and `_config.yml` aligned. Check in the
dependency lockfiles. Preserve the upstream MIT license.

Site appearance lives in `_sass/_site.scss`. Intentional overrides are
`assets/css/main.scss`, `_layouts/about.liquid`, and `_layouts/bib.liquid`.
Publication badges use the existing `ccf` metadata (only A/B/C are displayed);
`award_name` and `award_url` provide direct, visible award recognition.
News uses short paper names and first-person wording ("Our paper…").
Acceptance items declare `venue`; `_data/news_venues.yml` supplies CCF A badges
automatically. Award items declare `award` and `award_url`. The News include
adds punctuation and "Congratulations to the team!" for these items; leave
their body without a final period. Other news renders as ordinary Markdown.

## Validation

```sh
npm ci
npm run lint:prettier
bundle exec al-folio upgrade audit --no-fail
JEKYLL_ENV=production bundle exec jekyll build
python3 bin/check-site.py _site
```

Use `_config.local.yml` for localhost previews. Migration branches and PRs build
but do not deploy. Pushes to `master` deploy to GitHub Pages after the build and
checks pass; merging into `master` is a production publication step.
