#!/usr/bin/env python3
"""Check generated same-site links and assets without making network requests."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        for attr in ("href", "src", "poster"):
            if values.get(attr):
                self.links.append(values[attr])


def main():
    site = Path(sys.argv[1] if len(sys.argv) > 1 else "_site").resolve()
    pages = list(site.rglob("*.html"))
    if not pages or not (site / "index.html").is_file():
        raise SystemExit("No generated site found; run the Jekyll build first.")
    missing = set()
    checked = 0
    for page in pages:
        parser = Links()
        parser.feed(page.read_text(encoding="utf-8"))
        for link in parser.links:
            url = urlsplit(link)
            if url.scheme and url.scheme not in {"http", "https"}:
                continue
            if url.netloc and url.netloc not in {"haolis.com", "localhost:4000", "127.0.0.1:4000"}:
                continue
            if not url.path:
                continue
            path = unquote(url.path)
            target = site / path.lstrip("/") if path.startswith("/") else page.parent / path
            checked += 1
            if not target.is_file() and not (target / "index.html").is_file():
                missing.add((str(page.relative_to(site)), link))
    for page, link in sorted(missing):
        print(f"Missing: {page} -> {link}")
    if missing:
        raise SystemExit(f"{len(missing)} broken local links/assets")
    print(f"Checked {len(pages)} HTML pages and {checked} local links/assets: OK")


if __name__ == "__main__":
    main()
