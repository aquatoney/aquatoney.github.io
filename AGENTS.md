# Hao Li's personal website

This site uses the al-folio v1.2 starter. Its Git history and origin belong to
`aquatoney/aquatoney.github.io`, not the upstream template repository.

## Content and compatibility

- `_pages/about.md`: biography, recruitment, contact information, selected papers.
- `_pages/publications.md`: publications at the existing `/pubs/` URL.
- `_bibliography/papers.bib`: the single source of publication data.
- `files/`: existing PDF URLs; preserve filenames and contents.
- `CNAME` and the Google verification HTML file must survive migrations.
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

## Validation

```sh
npm ci
npm run lint:prettier
bundle exec al-folio upgrade audit --no-fail
JEKYLL_ENV=production bundle exec jekyll build
python3 bin/check-site.py _site
```

Use `_config.local.yml` for localhost previews. Migration branches build but
do not deploy; production publication is a separate step after review.
