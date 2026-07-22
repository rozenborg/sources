# AI Briefing Feeds

Daily AI-summarized content from curated sources, updated automatically via GitHub Actions.

**How it works:** A [daily GitHub Action](.github/workflows/daily.yaml) runs `pull.py`, which fetches content from 15 sources (RSS feeds, sitemaps, podcasts), summarizes each article via Claude, and commits the results as markdown files. The source health table below is auto-generated on each run.

## Source Health

<!-- SOURCE_HEALTH_START -->
| Source | Type | Last Success | Posts | Status | Notes |
|--------|------|-------------|-------|--------|-------|
| One Useful Thing (Ethan Mollick) | rss | 2026-07-22 | 8 | ✅ |  |
| OpenAI Blog | rss | 2026-07-22 | 0 | ✅ |  |
| Ken Huang \| AI Expert | rss | 2026-07-22 | 145 | ✅ |  |
| Future-Proof Your Career | rss | 2026-07-22 | 45 | ✅ |  |
| The AI Collective | rss | 2026-03-25 | 17 | ❌ | Feed parse error: <unknown>:2:0: syntax error |
| Harvard Business Review | rss | 2026-07-22 | 111 | ✅ |  |
| Real Estate News | rss | 2026-07-22 | 52 | ✅ |  |
| Anthropic Blog | sitemap | 2026-07-22 | 86 | ✅ |  |
| Built In | sitemap | 2026-07-22 | 11 | ✅ |  |
| EY Insights | sitemap | 2026-07-22 | 8 | ✅ |  |
| The a16z Show | podcast | 2026-07-22 | 111 | ✅ |  |
| Dwarkesh Podcast | podcast | 2026-07-22 | 18 | ✅ | Long episodes (2-3 hrs) |
| No Priors | podcast | 2026-07-22 | 19 | ✅ |  |
| Latent Space | podcast | 2026-07-22 | 42 | ✅ |  |
| AI Daily Brief | podcast | 2026-07-22 | 1 | ✅ | Short daily episodes (~10 min) |
<!-- SOURCE_HEALTH_END -->

## Recent Content

<!-- RECENT_CONTENT_START -->
### 2026-07-22
- [Claude Haiku 4 5](content/2026/07/22/anthropic-blog--claude-haiku-4-5.md) — anthropic-blog
- [Claude Sonnet 4 5](content/2026/07/22/anthropic-blog--claude-sonnet-4-5.md) — anthropic-blog
- [Donation Public First Action](content/2026/07/22/anthropic-blog--donation-public-first-action.md) — anthropic-blog
- [Skills](content/2026/07/22/anthropic-blog--skills.md) — anthropic-blog
- [When The Model Cheats By Hacking The Exam](content/2026/07/22/ken-huang-ai-expert--when-the-model-cheats-by-hacking-the-exam.md) — ken-huang-ai-expert

### 2026-07-21
- [Why Physical Ai Is The Next Frontier Applied Intuition](content/2026/07/21/a16z-podcast--why-physical-ai-is-the-next-frontier-applied-intuition.md) — a16z-podcast
- [Exciting Book Announcement And Giveaway Openclaw Ai In Produ](content/2026/07/21/ken-huang-ai-expert--exciting-book-announcement-and-giveaway-openclaw-ai-in-produ.md) — ken-huang-ai-expert
- [Causal Models Need Causal Data Xairas X Cell Model For Drug ](content/2026/07/21/latent-space--causal-models-need-causal-data-xairas-x-cell-model-for-drug-.md) — latent-space
- [Compass Unveils Ai Assistant Brokerage Comparison Tool Launc](content/2026/07/21/real-estate-news--compass-unveils-ai-assistant-brokerage-comparison-tool-launc.md) — real-estate-news

### 2026-07-20
- [Hugging Faces Ceo On Open Source Ai Model Routing And The Fu](content/2026/07/20/a16z-podcast--hugging-faces-ceo-on-open-source-ai-model-routing-and-the-fu.md) — a16z-podcast
- [Rare Disease Research Grants](content/2026/07/20/anthropic-blog--rare-disease-research-grants.md) — anthropic-blog
- [The Hidden Risk In Mcp Connections](content/2026/07/20/ken-huang-ai-expert--the-hidden-risk-in-mcp-connections.md) — ken-huang-ai-expert
- [Agents A Powerful Influence On Private Listing Choice](content/2026/07/20/real-estate-news--agents-a-powerful-influence-on-private-listing-choice.md) — real-estate-news

### 2026-07-19
- [Proof Of Control Assurance Framework For Universal Commerce ](content/2026/07/19/ken-huang-ai-expert--proof-of-control-assurance-framework-for-universal-commerce-.md) — ken-huang-ai-expert
- [The Missing Control Loop For Ai Agents Intent Evidence And R](content/2026/07/19/ken-huang-ai-expert--the-missing-control-loop-for-ai-agents-intent-evidence-and-r.md) — ken-huang-ai-expert
- [Using Chatgpt 56 For Knowledge Work](content/2026/07/19/khemaridh-future-proof--using-chatgpt-56-for-knowledge-work.md) — khemaridh-future-proof

### 2026-07-18
- [Demystifying Kimi K3 The Three Algorithms Behind The 1 Front](content/2026/07/18/ken-huang-ai-expert--demystifying-kimi-k3-the-three-algorithms-behind-the-1-front.md) — ken-huang-ai-expert

### 2026-07-17
- [Amjad Masad On Going Direct Building Replit And The Future O](content/2026/07/17/a16z-podcast--amjad-masad-on-going-direct-building-replit-and-the-future-o.md) — a16z-podcast
- [Owasp Agentic Skills Top 10 Tutorial Video Series](content/2026/07/17/ken-huang-ai-expert--owasp-agentic-skills-top-10-tutorial-video-series.md) — ken-huang-ai-expert

### 2026-07-16
- [Replay 2025 David Sacks On Ai Crypto And Americas Technology](content/2026/07/16/a16z-podcast--replay-2025-david-sacks-on-ai-crypto-and-americas-technology.md) — a16z-podcast
- [Will Claude Cowork Get Replaced By Chatgpt](content/2026/07/16/khemaridh-future-proof--will-claude-cowork-get-replaced-by-chatgpt.md) — khemaridh-future-proof
- [The Lab Of The Future Should Feel Like A Data Center Andy Be](content/2026/07/16/latent-space--the-lab-of-the-future-should-feel-like-a-data-center-andy-be.md) — latent-space
- [Can Nar Build An Ethics Monitoring Tool And Will It](content/2026/07/16/real-estate-news--can-nar-build-an-ethics-monitoring-tool-and-will-it.md) — real-estate-news

### 2026-07-15
- [From The Archive Can Anyone Catch Nvidia The Future Of Chips](content/2026/07/15/a16z-podcast--from-the-archive-can-anyone-catch-nvidia-the-future-of-chips.md) — a16z-podcast
- [Canadian Ai Research](content/2026/07/15/anthropic-blog--canadian-ai-research.md) — anthropic-blog

<!-- RECENT_CONTENT_END -->
