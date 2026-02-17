# LLM.md

## What is this?

A self-growing GitHub repo that fills up with AI-summarized content daily. GitHub Actions runs `pull.py` every day at 8:00 UTC, which fetches from 15 sources, summarizes via Claude API, writes markdown to `content/`, and commits. The README health table and recent content section are auto-generated.

This is NOT an app. There's no database, no UI, no CLI framework. The filesystem is the database. The README is the dashboard. Git history is the audit log.

## Repo structure

- `pull.py` — main entry point. Loads config, loops through sources, writes markdown, updates state + README
- `fetchers.py` — all content fetching (RSS, sitemaps, podcasts), text extraction, Whisper transcription, Claude summarization. Plain functions, no classes
- `feeds.yaml` — source config. If it's in the file, it's active. Remove to deactivate
- `state.json` — dedup (seen URLs) + per-source health stats. Committed to git on every run
- `content/YYYY/MM/DD/source--slug.md` — auto-generated summaries with YAML frontmatter
- `.github/workflows/daily.yaml` — cron schedule + manual trigger

## How to run locally

```bash
source .venv/bin/activate  # Python 3.11+
export ANTHROPIC_API_KEY=...
export OPENAI_API_KEY=...   # only needed for podcast Whisper transcription
python pull.py
```

## Key gotchas

- **Feed parsing in CI**: feedparser's default HTTP client gets blocked by Cloudflare on Substack feeds in GitHub Actions. The `_fetch_feed()` helper fetches with httpx (browser headers) first, then passes raw content to feedparser. Don't bypass this.
- **Feed proxy**: GitHub Actions IPs are blocked by Substack entirely (HTTP 403, `host_not_allowed`), so browser headers alone aren't enough. Substack feed URLs in `feeds.yaml` are routed through a Cloudflare Worker proxy (`substack-proxy.rozenborg.workers.dev`). Worker source is in `workers/substack-proxy/`. Deploy with `cd workers/substack-proxy && npx wrangler deploy`.
- **HBR feed worker**: HBR blocks all cloud/CI IPs and its legacy Feedburner RSS is dead. A dedicated Cloudflare Worker (`hbr-feed.rozenborg.workers.dev`) scrapes HBR topic pages from the edge and generates RSS. Modeled on the RSSHub HBR route — extracts `data-title`/`data-url` attributes from `.stream-item` elements. Worker source is in `workers/hbr-feed/`. Deploy with `cd workers/hbr-feed && npx wrangler deploy`.
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
3. **Source expansion** — add more non-AI-exclusive sources that sometimes cover AI (McKinsey, etc.). HBR added via self-hosted worker (`hbr-feed.rozenborg.workers.dev`) that scrapes topic pages → RSS, with keyword filtering for AI content

## GitHub secrets required

- `ANTHROPIC_API_KEY` — for Claude summarization
- `OPENAI_API_KEY` — for Whisper transcription (podcasts only)
