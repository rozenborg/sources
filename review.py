#!/usr/bin/env python3
"""
Source review web app.
Run:  python review.py
Then: http://localhost:5001
"""

import json
from datetime import datetime, timezone
from pathlib import Path

import yaml
from flask import Flask, jsonify, request, Response

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
CONTENT_DIR = BASE_DIR / "content"
FEEDS_PATH = BASE_DIR / "feeds.yaml"
REVIEWS_PATH = BASE_DIR / "reviews.json"

# ---------------------------------------------------------------------------
# Data helpers
# ---------------------------------------------------------------------------

_feeds_cache: dict | None = None


def load_feeds() -> dict[str, dict]:
    """Load feeds.yaml → {source_id: source_config}."""
    global _feeds_cache
    if _feeds_cache is None:
        with open(FEEDS_PATH) as f:
            config = yaml.safe_load(f)
        _feeds_cache = {s["id"]: s for s in config.get("sources", [])}
    return _feeds_cache


def load_reviews() -> dict:
    if REVIEWS_PATH.exists():
        with open(REVIEWS_PATH) as f:
            return json.load(f)
    return {"reviews": {}}


def save_reviews(data: dict):
    with open(REVIEWS_PATH, "w") as f:
        json.dump(data, f, indent=2, default=str)


def parse_article(path: Path) -> dict | None:
    """Parse a content markdown file into a structured dict."""
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return None

    parts = text.split("---", 2)
    if len(parts) < 3:
        return None

    try:
        meta = yaml.safe_load(parts[1])
    except yaml.YAMLError:
        return None

    if not isinstance(meta, dict):
        return None

    body = parts[2].strip()
    rel_path = str(path.relative_to(BASE_DIR))

    return {
        "path": rel_path,
        "title": meta.get("title", "Untitled"),
        "source": meta.get("source", "unknown"),
        "url": meta.get("url", ""),
        "date": str(meta.get("date", "")),
        "type": meta.get("type", "unknown"),
        "body": body,
    }


def load_all_articles() -> list[dict]:
    """Load all articles sorted by date descending."""
    articles = []
    for md_path in CONTENT_DIR.rglob("*.md"):
        article = parse_article(md_path)
        if article:
            articles.append(article)
    articles.sort(key=lambda a: a["date"], reverse=True)
    return articles


# ---------------------------------------------------------------------------
# API routes
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    return Response(HTML_TEMPLATE, content_type="text/html")


@app.route("/api/articles")
def api_articles():
    articles = load_all_articles()
    reviews = load_reviews()["reviews"]
    feeds = load_feeds()

    for a in articles:
        review = reviews.get(a["path"])
        a["review_status"] = review["status"] if review else None
        a["reviewed_at"] = review["reviewed_at"] if review else None
        source_config = feeds.get(a["source"], {})
        a["source_name"] = source_config.get("name", a["source"])

    # Filters
    source_filter = request.args.get("source")
    type_filter = request.args.get("type")
    status_filter = request.args.get("status")

    if source_filter:
        articles = [a for a in articles if a["source"] == source_filter]
    if type_filter:
        articles = [a for a in articles if a["type"] == type_filter]
    if status_filter:
        if status_filter == "unreviewed":
            articles = [a for a in articles if a["review_status"] is None]
        else:
            articles = [a for a in articles if a["review_status"] == status_filter]

    return jsonify({"articles": articles, "total": len(articles)})


@app.route("/api/sources")
def api_sources():
    feeds = load_feeds()
    articles = load_all_articles()

    source_counts: dict[str, int] = {}
    for a in articles:
        source_counts[a["source"]] = source_counts.get(a["source"], 0) + 1

    sources = []
    for sid, config in feeds.items():
        sources.append({
            "id": sid,
            "name": config.get("name", sid),
            "type": config.get("type", "unknown"),
            "article_count": source_counts.get(sid, 0),
        })

    sources.sort(key=lambda s: s["name"])
    return jsonify({"sources": sources})


@app.route("/api/stats")
def api_stats():
    articles = load_all_articles()
    reviews = load_reviews()["reviews"]

    total = len(articles)
    counts = {"pass": 0, "save": 0, "star": 0}
    for a in articles:
        review = reviews.get(a["path"])
        if review:
            s = review.get("status")
            if s in counts:
                counts[s] += 1

    reviewed = sum(counts.values())
    return jsonify({
        "total": total,
        "reviewed": reviewed,
        "unreviewed": total - reviewed,
        **counts,
    })


@app.route("/api/review", methods=["POST"])
def api_review():
    data = request.get_json()
    path = data.get("path")
    status = data.get("status")

    if not path:
        return jsonify({"error": "path is required"}), 400
    if status not in ("pass", "save", "star", None):
        return jsonify({"error": "status must be pass, save, star, or null"}), 400

    reviews = load_reviews()

    if status is None:
        reviews["reviews"].pop(path, None)
    else:
        reviews["reviews"][path] = {
            "status": status,
            "reviewed_at": datetime.now(timezone.utc).isoformat(),
        }

    save_reviews(reviews)
    return jsonify({"ok": True, "path": path, "status": status})


# ---------------------------------------------------------------------------
# HTML template (single-page app)
# ---------------------------------------------------------------------------

HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Source Review</title>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<style>
/* ── Reset & Base ─────────────────────────────────────────────── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
    --bg:           #0f1117;
    --bg-card:      #1a1d27;
    --bg-hover:     #22252f;
    --border:       #2a2d3a;
    --text:         #e4e4e7;
    --text-muted:   #71717a;
    --type-rss:     #22c55e;
    --type-sitemap: #a855f7;
    --type-podcast: #f97316;
    --st-pass:      #71717a;
    --st-save:      #3b82f6;
    --st-star:      #eab308;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
    background: var(--bg);
    color: var(--text);
    line-height: 1.6;
    min-height: 100vh;
}

a { color: var(--st-save); text-decoration: none; }
a:hover { text-decoration: underline; }

/* ── Header ───────────────────────────────────────────────────── */
#header {
    position: sticky; top: 0; z-index: 100;
    background: var(--bg-card);
    border-bottom: 1px solid var(--border);
    padding: 12px 24px;
    display: flex; justify-content: space-between; align-items: center;
    flex-wrap: wrap; gap: 8px;
}
.header-left { display: flex; align-items: center; gap: 16px; }
.header-left h1 { font-size: 16px; font-weight: 700; white-space: nowrap; }

.nav-btn {
    background: none; border: none; color: var(--text-muted);
    font-size: 13px; font-weight: 500; padding: 6px 14px;
    cursor: pointer; border-radius: 6px; transition: all .15s;
}
.nav-btn:hover { color: var(--text); background: var(--bg-hover); }
.nav-btn.active { background: var(--bg-hover); color: var(--text); }

.header-stats {
    display: flex; align-items: center; gap: 12px;
    font-size: 12px; color: var(--text-muted);
}
.stat-dot {
    display: inline-block; width: 7px; height: 7px; border-radius: 50%;
    margin-right: 3px; vertical-align: middle;
}

/* ── Filters ──────────────────────────────────────────────────── */
.filters-bar {
    display: flex; gap: 10px; padding: 14px 24px;
    border-bottom: 1px solid var(--border);
    background: var(--bg-card); flex-wrap: wrap;
}
.filters-bar select, .filters-bar input {
    background: var(--bg); border: 1px solid var(--border);
    color: var(--text); padding: 7px 10px; border-radius: 6px;
    font-size: 13px; outline: none;
}
.filters-bar select:focus, .filters-bar input:focus {
    border-color: var(--st-save);
}
.filters-bar input { flex: 1; min-width: 140px; }

/* ── Type badge ───────────────────────────────────────────────── */
.type-badge {
    display: inline-block; font-size: 10px; font-weight: 700;
    text-transform: uppercase; letter-spacing: .5px;
    padding: 2px 7px; border-radius: 4px;
}
.type-badge[data-type="rss"]     { background: rgba(34,197,94,.15);  color: var(--type-rss); }
.type-badge[data-type="sitemap"] { background: rgba(168,85,247,.15); color: var(--type-sitemap); }
.type-badge[data-type="podcast"] { background: rgba(249,115,22,.15); color: var(--type-podcast); }

/* ── Review badge ─────────────────────────────────────────────── */
.review-badge {
    display: inline-flex; align-items: center; gap: 4px;
    font-size: 10px; font-weight: 600; text-transform: uppercase;
}
.review-badge::before {
    content: ""; width: 6px; height: 6px; border-radius: 50%;
}
.review-badge[data-status="pass"]::before { background: var(--st-pass); }
.review-badge[data-status="save"]::before { background: var(--st-save); }
.review-badge[data-status="star"]::before { background: var(--st-star); }
.review-badge[data-status="pass"] { color: var(--st-pass); }
.review-badge[data-status="save"] { color: var(--st-save); }
.review-badge[data-status="star"] { color: var(--st-star); }

/* ── Browse view: article list ────────────────────────────────── */
.article-row {
    display: grid;
    grid-template-columns: 88px 68px 150px 1fr 72px;
    gap: 10px; align-items: center;
    padding: 11px 24px;
    border-bottom: 1px solid var(--border);
    cursor: pointer; transition: background .1s;
    font-size: 13px;
}
.article-row:hover { background: var(--bg-hover); }
.article-row.reviewed { opacity: .45; }
.article-row.reviewed:hover { opacity: .7; }
.article-row.expanded { background: var(--bg-hover); opacity: 1; }

.article-row .date { color: var(--text-muted); font-size: 12px; font-variant-numeric: tabular-nums; }
.article-row .source-name { color: var(--text-muted); font-size: 12px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.article-row .title { font-weight: 500; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }

/* ── Browse view: expanded body ───────────────────────────────── */
.article-body {
    max-height: 0; overflow: hidden;
    transition: max-height .35s ease;
    background: var(--bg-card);
    border-bottom: 1px solid var(--border);
}
.article-body.open { max-height: 3000px; }

.article-body-inner {
    padding: 16px 24px 20px 24px;
}

.article-meta-expanded {
    display: flex; gap: 12px; align-items: center;
    margin-bottom: 14px; font-size: 13px;
}

.inline-actions {
    display: flex; gap: 6px; margin-top: 16px; padding-top: 14px;
    border-top: 1px solid var(--border);
}
.mini-btn {
    padding: 5px 14px; border-radius: 5px; border: 1px solid var(--border);
    font-size: 12px; font-weight: 600; cursor: pointer; transition: all .12s;
    background: var(--bg);
}
.mini-btn:hover { transform: scale(1.04); }
.mini-pass { color: var(--st-pass); border-color: var(--st-pass); }
.mini-save { color: var(--st-save); border-color: var(--st-save); }
.mini-star { color: var(--st-star); border-color: var(--st-star); }
.mini-btn.active-status { background: var(--bg-hover); }

/* ── Markdown content ─────────────────────────────────────────── */
.md h2 { font-size: 15px; font-weight: 700; margin: 18px 0 8px; color: var(--text); }
.md h3 { font-size: 14px; font-weight: 600; margin: 14px 0 6px; }
.md ul, .md ol { padding-left: 20px; }
.md li { margin-bottom: 5px; font-size: 14px; line-height: 1.7; }
.md strong { color: #f0f0f3; }
.md p { margin-bottom: 8px; font-size: 14px; }
.md a { color: var(--st-save); }

/* ── Review view ──────────────────────────────────────────────── */
.review-controls {
    display: flex; justify-content: space-between; align-items: center;
    max-width: 740px; margin: 0 auto; padding: 16px 24px 0;
    font-size: 13px; color: var(--text-muted);
}
.toggle-label { display: flex; align-items: center; gap: 6px; cursor: pointer; }
.toggle-label input { accent-color: var(--st-save); }

.card-container {
    max-width: 740px; margin: 0 auto; padding: 16px 24px;
}

.review-card {
    background: var(--bg-card); border: 1px solid var(--border);
    border-radius: 12px; padding: 28px 32px;
    position: relative; transition: transform .3s ease, opacity .3s ease;
    transform-origin: center;
}
.review-card.swipe-left  { transform: translateX(-130%) rotate(-6deg); opacity: 0; }
.review-card.swipe-right { transform: translateX(130%) rotate(6deg);  opacity: 0; }
.review-card.swipe-up    { transform: translateY(-130%); opacity: 0; }
.review-card.entering    { animation: cardIn .25s ease-out; }

@keyframes cardIn {
    from { opacity: 0; transform: scale(.96) translateY(8px); }
    to   { opacity: 1; transform: scale(1) translateY(0); }
}

.card-header { margin-bottom: 20px; padding-bottom: 16px; border-bottom: 1px solid var(--border); }
.card-title  { font-size: 20px; font-weight: 700; line-height: 1.35; margin-bottom: 10px; }
.card-meta   { display: flex; gap: 10px; align-items: center; color: var(--text-muted); font-size: 13px; flex-wrap: wrap; }
.card-prev   { margin-top: 8px; font-size: 12px; color: var(--text-muted); }

.card-body {
    font-size: 14px; line-height: 1.8;
    max-height: 58vh; overflow-y: auto;
    scrollbar-width: thin; scrollbar-color: var(--border) transparent;
}

/* ── Action buttons ───────────────────────────────────────────── */
.review-actions {
    display: flex; justify-content: center; gap: 14px;
    max-width: 740px; margin: 0 auto; padding: 20px 24px;
}
.action-btn {
    flex: 1; max-width: 170px; padding: 14px 20px;
    border: 2px solid var(--border); border-radius: 10px;
    font-size: 15px; font-weight: 700; cursor: pointer;
    transition: all .12s; display: flex; flex-direction: column;
    align-items: center; gap: 3px; background: var(--bg);
}
.action-btn kbd { font-size: 10px; color: var(--text-muted); font-family: inherit; font-weight: 400; }
.action-btn:hover { transform: scale(1.05); }
.action-btn:active { transform: scale(.97); }

.action-pass { color: var(--st-pass); border-color: #3f3f46; }
.action-pass:hover { background: #1c1c20; }
.action-save { color: var(--st-save); border-color: #1e40af; }
.action-save:hover { background: #172554; }
.action-star { color: var(--st-star); border-color: #854d0e; }
.action-star:hover { background: #422006; }

/* ── Empty state ──────────────────────────────────────────────── */
.empty-state {
    display: flex; flex-direction: column; align-items: center;
    justify-content: center; padding: 80px 24px; color: var(--text-muted);
    text-align: center;
}
.empty-state .empty-icon { font-size: 48px; margin-bottom: 16px; }
.empty-state h2 { font-size: 20px; color: var(--text); margin-bottom: 8px; }
.empty-state p { font-size: 14px; margin-bottom: 20px; }
.empty-state button {
    background: var(--bg-card); border: 1px solid var(--border);
    color: var(--text); padding: 8px 20px; border-radius: 6px;
    cursor: pointer; font-size: 13px;
}
.empty-state button:hover { background: var(--bg-hover); }

/* ── Responsive ───────────────────────────────────────────────── */
@media (max-width: 768px) {
    .article-row {
        grid-template-columns: 1fr;
        gap: 3px; padding: 10px 16px;
    }
    .article-row .date { font-size: 11px; }
    .article-row .source-name { font-size: 11px; }
    .article-row .title { white-space: normal; }

    .review-card { padding: 20px; border-radius: 8px; }
    .card-title { font-size: 17px; }
    .review-actions { gap: 8px; padding: 16px; }
    .action-btn { padding: 12px 14px; font-size: 14px; }
    .filters-bar { padding: 10px 16px; }
    .filters-bar select, .filters-bar input { font-size: 12px; padding: 6px 8px; }
    #header { padding: 10px 16px; }
    .article-body-inner { padding: 14px 16px; }
}
</style>
</head>
<body>

<!-- ── Header ─────────────────────────────────────────────────── -->
<header id="header">
    <div class="header-left">
        <h1>Source Review</h1>
        <nav>
            <button class="nav-btn active" id="nav-browse" onclick="showView('browse')">Browse</button>
            <button class="nav-btn" id="nav-review" onclick="showView('review')">Review</button>
        </nav>
    </div>
    <div class="header-stats" id="header-stats"></div>
</header>

<!-- ── Browse view ────────────────────────────────────────────── -->
<main id="view-browse" class="view">
    <div class="filters-bar" id="filters-bar">
        <select id="filter-source" onchange="loadBrowse()">
            <option value="">All Sources</option>
        </select>
        <select id="filter-type" onchange="loadBrowse()">
            <option value="">All Types</option>
            <option value="rss">RSS</option>
            <option value="sitemap">Sitemap</option>
            <option value="podcast">Podcast</option>
        </select>
        <select id="filter-status" onchange="loadBrowse()">
            <option value="">All Status</option>
            <option value="unreviewed">Unreviewed</option>
            <option value="pass">Pass</option>
            <option value="save">Save</option>
            <option value="star">Star</option>
        </select>
        <input type="text" id="filter-search" placeholder="Search titles..." oninput="renderBrowseList()">
    </div>
    <div id="article-list"></div>
</main>

<!-- ── Review view ────────────────────────────────────────────── -->
<main id="view-review" class="view" style="display:none">
    <div class="review-controls">
        <label class="toggle-label">
            <input type="checkbox" id="show-reviewed" onchange="loadReviewQueue()">
            Show reviewed
        </label>
        <span id="review-counter"></span>
    </div>
    <div class="card-container" id="card-container"></div>
    <div class="review-actions" id="review-actions" style="display:none">
        <button class="action-btn action-pass" onclick="reviewAction('pass')">Pass<kbd>&#8592;</kbd></button>
        <button class="action-btn action-star" onclick="reviewAction('star')">Star<kbd>&#8593;</kbd></button>
        <button class="action-btn action-save" onclick="reviewAction('save')">Save<kbd>&#8594;</kbd></button>
    </div>
</main>

<!-- ── Empty state (shared) ───────────────────────────────────── -->
<div id="empty-state" class="empty-state" style="display:none"></div>

<script>
/* ── State ────────────────────────────────────────────────────── */
let browseArticles = [];
let reviewQueue = [];
let reviewIdx = 0;
let currentExpanded = null;
let animating = false;

/* ── Helpers ──────────────────────────────────────────────────── */
function esc(s) {
    const d = document.createElement('div');
    d.textContent = s;
    return d.innerHTML;
}
function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }

/* ── Stats ────────────────────────────────────────────────────── */
async function refreshStats() {
    const r = await fetch('/api/stats');
    const s = await r.json();
    document.getElementById('header-stats').innerHTML =
        `<span>${s.unreviewed} unreviewed</span>` +
        `<span style="opacity:.3">/</span>` +
        `<span>${s.total} total</span>` +
        `<span><span class="stat-dot" style="background:var(--st-star)"></span>${s.star}</span>` +
        `<span><span class="stat-dot" style="background:var(--st-save)"></span>${s.save}</span>` +
        `<span><span class="stat-dot" style="background:var(--st-pass)"></span>${s.pass}</span>`;
}

/* ── View switching ───────────────────────────────────────────── */
function showView(v) {
    document.getElementById('view-browse').style.display  = v === 'browse' ? '' : 'none';
    document.getElementById('view-review').style.display   = v === 'review' ? '' : 'none';
    document.getElementById('empty-state').style.display   = 'none';
    document.getElementById('nav-browse').classList.toggle('active', v === 'browse');
    document.getElementById('nav-review').classList.toggle('active', v === 'review');
    if (v === 'browse') loadBrowse();
    else loadReviewQueue();
}

/* ══════════════════════════════════════════════════════════════
   BROWSE VIEW
   ══════════════════════════════════════════════════════════════ */

async function loadSourceFilter() {
    const r = await fetch('/api/sources');
    const d = await r.json();
    const sel = document.getElementById('filter-source');
    d.sources.forEach(s => {
        const o = document.createElement('option');
        o.value = s.id;
        o.textContent = `${s.name} (${s.article_count})`;
        sel.appendChild(o);
    });
}

async function loadBrowse() {
    const params = new URLSearchParams();
    const src  = document.getElementById('filter-source').value;
    const typ  = document.getElementById('filter-type').value;
    const stat = document.getElementById('filter-status').value;
    if (src)  params.set('source', src);
    if (typ)  params.set('type', typ);
    if (stat) params.set('status', stat);

    const r = await fetch('/api/articles?' + params);
    const d = await r.json();
    browseArticles = d.articles;
    currentExpanded = null;
    renderBrowseList();
}

function renderBrowseList() {
    const search = document.getElementById('filter-search').value.toLowerCase();
    const list = document.getElementById('article-list');
    list.innerHTML = '';

    // Sort: unreviewed first, then by date desc
    const sorted = [...browseArticles].sort((a, b) => {
        const ar = a.review_status ? 1 : 0;
        const br = b.review_status ? 1 : 0;
        if (ar !== br) return ar - br;
        return b.date.localeCompare(a.date);
    });

    let shown = 0;
    for (const art of sorted) {
        if (search && !art.title.toLowerCase().includes(search)) continue;
        list.appendChild(buildRow(art));
        shown++;
    }

    if (shown === 0) {
        list.innerHTML = '<div class="empty-state"><p>No articles match your filters.</p></div>';
    }
}

function buildRow(art) {
    const wrapper = document.createElement('div');

    // Row
    const row = document.createElement('div');
    row.className = 'article-row' + (art.review_status ? ' reviewed' : '');
    row.innerHTML =
        `<span class="date">${esc(art.date)}</span>` +
        `<span class="type-badge" data-type="${art.type}">${art.type}</span>` +
        `<span class="source-name" title="${esc(art.source_name)}">${esc(art.source_name)}</span>` +
        `<span class="title" title="${esc(art.title)}">${esc(art.title)}</span>` +
        `<span>${art.review_status ? `<span class="review-badge" data-status="${art.review_status}">${art.review_status}</span>` : ''}</span>`;

    // Expandable body
    const body = document.createElement('div');
    body.className = 'article-body';
    body.innerHTML =
        `<div class="article-body-inner">` +
            `<div class="article-meta-expanded">` +
                `<a href="${esc(art.url)}" target="_blank" rel="noopener">Open original &#8594;</a>` +
            `</div>` +
            `<div class="md">${marked.parse(art.body)}</div>` +
            `<div class="inline-actions">` +
                `<button class="mini-btn mini-pass ${art.review_status==='pass'?'active-status':''}" onclick="event.stopPropagation();inlineReview('${esc(art.path)}','pass',this)">Pass</button>` +
                `<button class="mini-btn mini-star ${art.review_status==='star'?'active-status':''}" onclick="event.stopPropagation();inlineReview('${esc(art.path)}','star',this)">Star</button>` +
                `<button class="mini-btn mini-save ${art.review_status==='save'?'active-status':''}" onclick="event.stopPropagation();inlineReview('${esc(art.path)}','save',this)">Save</button>` +
            `</div>` +
        `</div>`;

    row.addEventListener('click', () => {
        if (currentExpanded && currentExpanded !== body) {
            currentExpanded.classList.remove('open');
            currentExpanded.previousElementSibling.classList.remove('expanded');
        }
        const open = body.classList.toggle('open');
        row.classList.toggle('expanded', open);
        currentExpanded = open ? body : null;
    });

    wrapper.appendChild(row);
    wrapper.appendChild(body);
    return wrapper;
}

async function inlineReview(path, status, btn) {
    await fetch('/api/review', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ path, status }),
    });

    // Update local state
    const art = browseArticles.find(a => a.path === path);
    if (art) {
        art.review_status = status;
        art.reviewed_at = new Date().toISOString();
    }

    // Update row UI: highlight the active button, update row badge
    const actions = btn.parentElement;
    actions.querySelectorAll('.mini-btn').forEach(b => b.classList.remove('active-status'));
    btn.classList.add('active-status');

    // Update the row's review badge column
    const row = actions.closest('.article-body').previousElementSibling;
    const badgeCol = row.children[4];
    badgeCol.innerHTML = `<span class="review-badge" data-status="${status}">${status}</span>`;
    row.classList.add('reviewed');

    refreshStats();
}

/* ══════════════════════════════════════════════════════════════
   REVIEW VIEW
   ══════════════════════════════════════════════════════════════ */

async function loadReviewQueue() {
    const r = await fetch('/api/articles');
    const d = await r.json();
    const showRev = document.getElementById('show-reviewed').checked;

    const unreviewed = d.articles.filter(a => !a.review_status);
    const reviewed   = d.articles.filter(a =>  a.review_status);

    unreviewed.sort((a, b) => b.date.localeCompare(a.date));
    reviewed.sort((a, b) => b.date.localeCompare(a.date));

    reviewQueue = showRev ? [...unreviewed, ...reviewed] : unreviewed;
    reviewIdx = 0;
    renderCard();
}

function renderCard() {
    const container = document.getElementById('card-container');
    const counter   = document.getElementById('review-counter');
    const actions   = document.getElementById('review-actions');
    const empty     = document.getElementById('empty-state');

    if (reviewIdx >= reviewQueue.length) {
        container.innerHTML = '';
        actions.style.display = 'none';
        empty.style.display = 'flex';
        empty.innerHTML =
            `<div class="empty-icon">&#10003;</div>` +
            `<h2>All caught up!</h2>` +
            `<p>${reviewQueue.length === 0 ? 'No articles to review.' : 'You\'ve reviewed everything in the queue.'}</p>` +
            `<button onclick="showView('browse')">Browse reviewed articles</button>`;
        counter.textContent = `${reviewQueue.length} of ${reviewQueue.length}`;
        return;
    }

    empty.style.display = 'none';
    actions.style.display = 'flex';

    const art = reviewQueue[reviewIdx];
    counter.textContent = `${reviewIdx + 1} of ${reviewQueue.length}`;

    const prevBadge = art.review_status
        ? `<div class="card-prev">Previously: <span class="review-badge" data-status="${art.review_status}">${art.review_status}</span></div>`
        : '';

    container.innerHTML =
        `<div class="review-card entering" id="current-card">` +
            `<div class="card-header">` +
                `<div class="card-title">${esc(art.title)}</div>` +
                `<div class="card-meta">` +
                    `<span class="type-badge" data-type="${art.type}">${art.type}</span>` +
                    `<span>${esc(art.source_name)}</span>` +
                    `<span>${art.date}</span>` +
                    `<a href="${esc(art.url)}" target="_blank" rel="noopener" onclick="event.stopPropagation()">Open original &#8594;</a>` +
                `</div>` +
                prevBadge +
            `</div>` +
            `<div class="card-body md">${marked.parse(art.body)}</div>` +
        `</div>`;
}

async function reviewAction(status) {
    if (animating || reviewIdx >= reviewQueue.length) return;
    animating = true;

    const card = document.getElementById('current-card');
    const art = reviewQueue[reviewIdx];

    const cls = { pass: 'swipe-left', save: 'swipe-right', star: 'swipe-up' }[status];
    card.classList.add(cls);

    // Fire API (non-blocking)
    fetch('/api/review', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ path: art.path, status }),
    }).then(() => refreshStats());

    await sleep(300);
    reviewIdx++;
    renderCard();
    animating = false;
}

/* ── Keyboard shortcuts ───────────────────────────────────────── */
document.addEventListener('keydown', (e) => {
    if (document.getElementById('view-review').style.display === 'none') return;
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT') return;
    switch (e.key) {
        case 'ArrowLeft':  e.preventDefault(); reviewAction('pass'); break;
        case 'ArrowRight': e.preventDefault(); reviewAction('save'); break;
        case 'ArrowUp':    e.preventDefault(); reviewAction('star'); break;
    }
});

/* ── Touch swipe ──────────────────────────────────────────────── */
let touchX = 0, touchY = 0;
const SWIPE_MIN = 80;

document.addEventListener('touchstart', e => {
    touchX = e.changedTouches[0].screenX;
    touchY = e.changedTouches[0].screenY;
}, { passive: true });

document.addEventListener('touchend', e => {
    if (document.getElementById('view-review').style.display === 'none') return;
    const dx = e.changedTouches[0].screenX - touchX;
    const dy = e.changedTouches[0].screenY - touchY;
    if (Math.abs(dx) > SWIPE_MIN && Math.abs(dx) > Math.abs(dy)) {
        dx < 0 ? reviewAction('pass') : reviewAction('save');
    } else if (dy < -SWIPE_MIN && Math.abs(dy) > Math.abs(dx)) {
        reviewAction('star');
    }
}, { passive: true });

/* ── Init ─────────────────────────────────────────────────────── */
(async function init() {
    await loadSourceFilter();
    await Promise.all([loadBrowse(), refreshStats()]);
})();
</script>
</body>
</html>
"""

# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("Source Review → http://localhost:5001")
    app.run(host="0.0.0.0", port=5001, debug=True)
