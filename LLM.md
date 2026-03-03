# LLM.md

## What is this?

A self-growing GitHub repo that fills up with AI-summarized content daily. GitHub Actions runs `pull.py` every day at 8:00 UTC, which fetches from 15 sources, summarizes via Claude API, writes markdown to `content/`, and commits. The README health table and recent content section are auto-generated.

This is NOT an app. There's no database, no UI, no CLI framework. The filesystem is the database. The README is the dashboard. Git history is the audit log.

## Repo structure

- `pull.py` — main entry point. Loads config, loops through sources, writes markdown, updates state + README
- `fetchers.py` — all content fetching (RSS, sitemaps, podcasts), text extraction, Whisper transcription, Claude summarization. Plain functions, no classes
- `feeds.yaml` — source config. If it's in the file, it's active. Remove to deactivate
- `state.json` — dedup (seen URLs) + per-source health stats. Committed to git on every run
- `docs/index.html` — **review app** (GitHub Pages SPA). Browse and triage content from any browser/device. Fetches content from GitHub API, syncs reviews via Cloudflare Worker. Features: branch selector (review content from any branch/PR), cross-device review sync, light/dark theme. See "Web review app" section below
- `workers/reviews-api/` — Cloudflare Worker + KV for persisting reviews across devices. Deployed alongside the existing `workers/substack-proxy/`
- `workers/summarize-api/` — Cloudflare Worker for on-demand summary regeneration. Fetches article URL, calls Claude API, returns new summary. API key passed from browser via `X-Anthropic-Key` header
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

## Web review app (docs/index.html)

A GitHub Pages SPA for browsing and triaging content from anywhere (phone, tablet, any browser). It reads content directly from GitHub and syncs reviews via a Cloudflare Worker.

**Architecture:**
- Static HTML/CSS/JS served by GitHub Pages from the `docs/` folder on `main`
- Content fetched via GitHub API (Trees API for file listing) + `raw.githubusercontent.com` (file contents). Only 2 API calls per session; raw content has no rate limit
- Reviews persisted in Cloudflare KV via `workers/reviews-api/` Worker
- Falls back to localStorage if the Worker is not configured

**Features:**
- Browse view with master-detail split layout (article list on left, content on right). Filter by source, date, status
- Review mode with Tinder-style card queue, keyboard shortcuts (arrow keys), and touch swipe. Rate each as pass/save/star
- Branch selector — switch between branches to review content from PRs before merging
- Branch hot-loading — when a non-main branch is selected, the entire app (HTML/CSS/JS) is fetched from that branch via `raw.githubusercontent.com` and loaded via `document.write()`. This enables testing UI/code changes on mobile without merging to main. A `sessionStorage` guard (`__bl`) prevents infinite reload loops. On main, the bootstrapper has zero overhead (single localStorage check)
- Cross-device review sync — rate articles on your phone, see ratings on your laptop
- Light/dark theme toggle (top-right corner)
- Settings panel (gear icon) — configure Worker URL, auth token, Anthropic API key, Summarize API URL, and GitHub token, all stored in localStorage
- Summary regeneration — "Regenerate" button on each card calls the summarize-api Worker to re-summarize from the source URL. "Save" button commits the updated summary back to the repo via GitHub API

**One-time setup:**
1. Enable GitHub Pages: repo Settings → Pages → Source: "Deploy from a branch" → `main` → `/docs`
2. Create KV namespace: `cd workers/reviews-api && wrangler kv:namespace create REVIEWS`
3. Paste the namespace ID into `workers/reviews-api/wrangler.toml`
4. Set auth secret: `wrangler secret put AUTH_TOKEN` → enter any random string
5. Deploy: `wrangler deploy`
6. Open the GitHub Pages URL → click gear icon → enter Worker URL (e.g. `https://reviews-api.rozenborg.workers.dev`) + the auth token you chose

**Key gotchas:**
- GitHub API unauthenticated rate limit is 60 requests/hour. The SPA uses only 2 API calls per page load (branches + tree), so this is plenty. All file content comes from `raw.githubusercontent.com` which has no rate limit
- The SPA is deployed from `main` branch only. When a non-main branch is selected, the bootstrapper hot-loads that branch's `docs/index.html` (both content *and* app code). A cache-busting query param (`?_=Date.now()`) is used, but `raw.githubusercontent.com` CDN may still serve stale content for up to ~5 minutes after a push
- CORS: the Worker allows requests from `rozenborg.github.io` and `localhost`. If you serve from a different domain, update the origin check in `workers/reviews-api/worker.js`
- js-yaml and marked.js are loaded from CDN (`cdn.jsdelivr.net`). If offline, the SPA won't work

## GitHub secrets required

- `ANTHROPIC_API_KEY` — for Claude summarization
- `OPENAI_API_KEY` — for Whisper transcription (podcasts only)
