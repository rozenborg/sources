# LLM.md

## What is this?

A self-growing GitHub repo that fills up with AI-summarized content daily. GitHub Actions runs `pull.py` every day at 8:00 UTC, which fetches from 15 sources, summarizes via Claude API, writes markdown to `content/`, and commits. The README health table and recent content section are auto-generated.

This is NOT an app. There's no database, no UI, no CLI framework. The filesystem is the database. The README is the dashboard. Git history is the audit log.

## Repo structure

- `pull.py` — main entry point. Loads config, loops through sources, writes markdown, updates state + README
- `fetchers.py` — all content fetching (RSS, sitemaps, podcasts), text extraction, Whisper transcription, Claude summarization. Plain functions, no classes
- `feeds.yaml` — source config. If it's in the file, it's active. Remove to deactivate
- `state.json` — dedup (seen URLs) + per-source health stats. Committed to git on every run
- `review.py` — local Flask web app for triaging content. Run `python review.py` → `http://localhost:5001`. Browse view uses a master-detail split layout (article list on left, selected article content on right). Filter by source, date, status. Review mode shows a Tinder-style card queue with keyboard shortcuts (arrow keys) and touch swipe. Rate each as pass/save/star. Includes a light/dark theme toggle (top-right corner). Stores decisions in `reviews.json`
- `reviews.json` — review decisions (`{path: {status, reviewed_at}}`). Created by review.py, not committed
- `content/YYYY/MM/DD/source--slug.md` — auto-generated summaries with YAML frontmatter
- `.github/workflows/daily.yaml` — cron schedule + manual trigger

## How to run locally

```bash
source .venv/bin/activate  # Python 3.11+
export ANTHROPIC_API_KEY=...
export OPENAI_API_KEY=...   # only needed for podcast Whisper transcription
python pull.py
```

To review fetched content locally:
```bash
pip install flask pyyaml
python review.py           # http://localhost:5001
```

## Key gotchas

- **Python version**: `pull.py` targets 3.11+ but `review.py` uses `from __future__ import annotations` so it works on 3.9+. Keep that import if adding new-style type hints (e.g. `dict | None`) to review.py.

- **Feed parsing in CI**: feedparser's default HTTP client gets blocked by Cloudflare on Substack feeds in GitHub Actions. The `_fetch_feed()` helper fetches with httpx (browser headers) first, then passes raw content to feedparser. Don't bypass this.
- **Feed proxy**: GitHub Actions IPs are blocked by Substack entirely (HTTP 403, `host_not_allowed`), so browser headers alone aren't enough. Substack feed URLs in `feeds.yaml` are routed through a Cloudflare Worker proxy (`substack-proxy.rozenborg.workers.dev`). Worker source is in `workers/substack-proxy/`. Deploy with `cd workers/substack-proxy && npx wrangler deploy`.
- **HBR feed**: HBR's Atom feed at `http://feeds.hbr.org/harvardbusiness` covers all published content (~25 recent entries). Entries include category tags (`hbp-subject` scheme) like "Generative AI", "AI and machine learning", etc. Our keyword filter on titles picks up relevant articles. Feed summaries are brief (1-2 sentences); full article text is behind a paywall, so trafilatura may only extract limited content.
- **Sitemap keyword filtering**: keywords are matched against URL slugs BEFORE fetching pages (cheap pre-filter). This avoids wasting HTTP requests on irrelevant content from large sitemaps (Built In has 34K+ articles).
- **Substack RSS body**: Substack feeds embed full article text in the RSS `<content>` field. `_rss_body_text()` detects this and uses it directly, avoiding a redundant HTTP fetch.
- **README sentinel comments**: The health table and recent content sections live between `<!-- SOURCE_HEALTH_START/END -->` and `<!-- RECENT_CONTENT_START/END -->` markers. Everything outside those markers is preserved.
- **state.json seen_urls**: This is the dedup mechanism. URLs are added after successful processing. If the process crashes mid-run, state isn't saved, so re-runs may reprocess some articles (which is fine — markdown files are path-deterministic).
- **Pipe characters in source names**: Source names containing `|` (like "Ken Huang | AI Expert") are escaped in the README table builder to avoid breaking markdown.

## Source types

- **`rss`** — standard RSS/Atom feeds, including Substack. Tries inline RSS body first, then fetches the URL and extracts via trafilatura
- **`sitemap`** — recursive XML sitemap parsing with `url_pattern` and `keywords` filters. Respects `lookback_days`
- **`podcast`** — parses RSS for audio enclosure URLs, downloads audio, transcribes via Whisper API, summarizes

## Current priorities

1. **Smart podcast transcripts** — avoid unnecessary Whisper usage:
   - Latent Space: full transcripts in RSS `<description>` field. Change to `type: rss`
   - Dwarkesh: full transcripts on Substack pages (`dwarkesh.com/p/{slug}`). Change to `type: rss` — trafilatura extracts it
   - AI Daily Brief: RSS has `<podcast:transcript>` tags linking to SRT files. Add SRT fetch/parse
   - a16z and No Priors: no free transcripts available, keep Whisper
2. **Title display** — README recent content titles are derived from slugs (Title Case), could be improved to use actual article titles from frontmatter
3. **Source expansion** — add more non-AI-exclusive sources that sometimes cover AI (McKinsey, etc.). HBR added via Atom feed (`feeds.hbr.org`) with keyword filtering for AI content

## GitHub secrets required

- `ANTHROPIC_API_KEY` — for Claude summarization
- `OPENAI_API_KEY` — for Whisper transcription (podcasts only)
