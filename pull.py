#!/usr/bin/env python3
"""
Daily AI briefing feed puller.
Fetches content from configured sources, summarizes via Claude, writes markdown.
Run via GitHub Actions or locally: python pull.py
"""

import json
import re
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

import yaml

from fetchers import fetch_rss, fetch_sitemap, fetch_podcast

# ---------------------------------------------------------------------------
# Config & state
# ---------------------------------------------------------------------------

def load_config(path="feeds.yaml") -> dict:
    with open(path) as f:
        return yaml.safe_load(f)


def load_state(path="state.json") -> dict:
    p = Path(path)
    if p.exists():
        with open(p) as f:
            return json.load(f)
    return {"sources": {}}


def save_state(state: dict, path="state.json"):
    with open(path, "w") as f:
        json.dump(state, f, indent=2, default=str)


# ---------------------------------------------------------------------------
# Markdown output
# ---------------------------------------------------------------------------

def slugify(text: str, max_len: int = 60) -> str:
    """Convert text to a filesystem-safe slug."""
    s = text.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s[:max_len]


def write_article(article: dict, content_dir: str = "content") -> str:
    """Write a markdown file for an article. Returns the file path."""
    dt = article.get("date") or datetime.now(timezone.utc)
    date_str = dt.strftime("%Y-%m-%d") if hasattr(dt, "strftime") else str(dt)[:10]
    year, month, day = date_str[:4], date_str[5:7], date_str[8:10]

    slug = slugify(article.get("title", "untitled"))
    filename = f"{article['source_id']}--{slug}.md"

    dir_path = Path(content_dir) / year / month / day
    dir_path.mkdir(parents=True, exist_ok=True)
    file_path = dir_path / filename

    # Build markdown
    lines = [
        "---",
        f'title: "{article.get("title", "Untitled")}"',
        f'source: {article["source_id"]}',
        f'url: {article.get("url", "")}',
        f'date: {date_str}',
        f'type: {article.get("source_type", "unknown")}',
        "---",
        "",
        "## Summary",
        "",
    ]

    if article.get("summary"):
        lines.append(article["summary"])
    else:
        lines.append("*No summary generated.*")

    lines.append("")

    file_path.write_text("\n".join(lines), encoding="utf-8")
    return str(file_path)


# ---------------------------------------------------------------------------
# README generation
# ---------------------------------------------------------------------------

START_HEALTH = "<!-- SOURCE_HEALTH_START -->"
END_HEALTH = "<!-- SOURCE_HEALTH_END -->"
START_RECENT = "<!-- RECENT_CONTENT_START -->"
END_RECENT = "<!-- RECENT_CONTENT_END -->"


def _status_emoji(source_state: dict) -> str:
    """Determine status emoji based on last_success and last_error."""
    last_success = source_state.get("last_success")
    last_error = source_state.get("last_error")

    if not last_success:
        return "\u274c"  # Red X — never succeeded

    try:
        success_dt = datetime.fromisoformat(str(last_success))
    except (ValueError, TypeError):
        return "\u274c"

    age = datetime.now(timezone.utc) - success_dt.replace(tzinfo=timezone.utc)
    if age > timedelta(days=3):
        return "\u274c"  # Red X — stale
    if last_error:
        return "\u26a0\ufe0f"  # Warning — recovered but had error
    return "\u2705"  # Green check


def _build_health_table(state: dict, config: dict) -> str:
    """Build the markdown source health table."""
    lines = [
        "| Source | Type | Last Success | Posts | Status | Notes |",
        "|--------|------|-------------|-------|--------|-------|",
    ]
    for source in config.get("sources", []):
        sid = source["id"]
        ss = state.get("sources", {}).get(sid, {})
        last_success = ss.get("last_success", "—")
        if last_success and last_success != "—":
            last_success = str(last_success)[:10]  # Just the date part
        posts = ss.get("posts_total", 0)
        emoji = _status_emoji(ss)
        notes = ss.get("last_error") or source.get("notes", "")
        if notes and len(notes) > 50:
            notes = notes[:47] + "..."
        # Escape pipes in name/notes to avoid breaking markdown table
        name = source['name'].replace("|", "\\|")
        notes = notes.replace("|", "\\|") if notes else ""
        lines.append(
            f"| {name} | {source['type']} | {last_success} | {posts} | {emoji} | {notes} |"
        )
    return "\n".join(lines)


def _build_recent_content(content_dir: str = "content", days: int = 7) -> str:
    """Build recent content links grouped by date."""
    content_path = Path(content_dir)
    if not content_path.exists():
        return "*No content yet.*"

    # Collect all markdown files
    files_by_date = {}
    for md_file in sorted(content_path.rglob("*.md"), reverse=True):
        parts = md_file.parts
        # Expect: content/YYYY/MM/DD/filename.md
        try:
            idx = parts.index("content")
            year, month, day = parts[idx + 1], parts[idx + 2], parts[idx + 3]
            date_key = f"{year}-{month}-{day}"
        except (ValueError, IndexError):
            continue

        if date_key not in files_by_date:
            files_by_date[date_key] = []
        files_by_date[date_key].append(md_file)

    if not files_by_date:
        return "*No content yet.*"

    # Show last N days
    lines = []
    cutoff = (datetime.now(timezone.utc) - timedelta(days=days)).strftime("%Y-%m-%d")
    for date_key in sorted(files_by_date.keys(), reverse=True):
        if date_key < cutoff:
            break
        lines.append(f"### {date_key}")
        for md_file in sorted(files_by_date[date_key]):
            # Parse title from frontmatter
            title = md_file.stem.split("--", 1)[-1].replace("-", " ").title()
            source_id = md_file.stem.split("--", 1)[0]
            rel_path = md_file.as_posix()
            lines.append(f"- [{title}]({rel_path}) \u2014 {source_id}")
        lines.append("")

    return "\n".join(lines) if lines else "*No recent content.*"


def update_readme(state: dict, config: dict, readme_path: str = "README.md"):
    """Regenerate auto-generated sections of README.md."""
    p = Path(readme_path)
    if p.exists():
        content = p.read_text(encoding="utf-8")
    else:
        content = _default_readme()

    # Replace health table
    health_table = _build_health_table(state, config)
    content = _replace_section(content, START_HEALTH, END_HEALTH, health_table)

    # Replace recent content
    recent = _build_recent_content()
    content = _replace_section(content, START_RECENT, END_RECENT, recent)

    p.write_text(content, encoding="utf-8")


def _replace_section(content: str, start_marker: str, end_marker: str, new_body: str) -> str:
    """Replace content between sentinel markers."""
    pattern = re.escape(start_marker) + r".*?" + re.escape(end_marker)
    replacement = f"{start_marker}\n{new_body}\n{end_marker}"
    if start_marker in content:
        return re.sub(pattern, replacement, content, flags=re.DOTALL)
    else:
        # Markers not found — append
        return content + f"\n\n{replacement}\n"


def _default_readme() -> str:
    return f"""# AI Briefing Feeds

Daily AI-summarized content from curated sources, updated automatically via GitHub Actions.

## Source Health

{START_HEALTH}
{END_HEALTH}

## Recent Content

{START_RECENT}
{END_RECENT}
"""


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

FETCHERS = {
    "rss": fetch_rss,
    "sitemap": fetch_sitemap,
    "podcast": fetch_podcast,
}


def process_source(source: dict, state: dict, settings: dict) -> tuple[int, str | None]:
    """
    Process a single source. Returns (new_article_count, error_or_none).
    Updates state in place.
    """
    sid = source["id"]
    now = datetime.now(timezone.utc).isoformat()

    # Ensure source state exists
    if sid not in state["sources"]:
        state["sources"][sid] = {
            "last_success": None,
            "last_error": None,
            "posts_total": 0,
            "last_run": None,
            "seen_urls": [],
        }

    ss = state["sources"][sid]
    ss["last_run"] = now
    seen_urls = set(ss.get("seen_urls", []))

    source_type = source.get("type", "rss")
    fetcher = FETCHERS.get(source_type)
    if not fetcher:
        error = f"Unknown source type: {source_type}"
        ss["last_error"] = error
        return 0, error

    try:
        articles = fetcher(source, seen_urls, settings)

        count = 0
        for article in articles:
            path = write_article(article)
            print(f"    Wrote: {path}")
            # Track URL
            ss["seen_urls"].append(article["url"])
            count += 1

        ss["last_success"] = now
        ss["last_error"] = None
        ss["posts_total"] = ss.get("posts_total", 0) + count
        return count, None

    except Exception as e:
        error = str(e)
        ss["last_error"] = error
        return 0, error


def main():
    config = load_config()
    state = load_state()
    settings = config.get("settings", {})

    print(f"=== AI Briefing Feeds Pull ===")
    print(f"Sources: {len(config.get('sources', []))}")
    print(f"Lookback: {settings.get('lookback_days', 3)} days")
    print()

    total_new = 0
    errors = []

    for source in config.get("sources", []):
        sid = source["id"]
        print(f"[{sid}]")

        count, error = process_source(source, state, settings)

        if error:
            print(f"  ERROR: {error}")
            errors.append((sid, error))
        else:
            print(f"  OK: {count} new articles")
            total_new += count
        print()

    # Save state and update README
    save_state(state)
    update_readme(state, config)

    print(f"=== Done ===")
    print(f"New articles: {total_new}")
    if errors:
        print(f"Errors: {len(errors)}")
        for sid, err in errors:
            print(f"  {sid}: {err}")

    # Exit with error code if ALL sources failed
    if errors and len(errors) == len(config.get("sources", [])):
        sys.exit(1)


if __name__ == "__main__":
    main()
