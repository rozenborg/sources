# AI Briefing Feeds

Daily AI-summarized content from curated sources, updated automatically via GitHub Actions.

**How it works:** A [daily GitHub Action](.github/workflows/daily.yaml) runs `pull.py`, which fetches content from 15 sources (RSS feeds, sitemaps, podcasts), summarizes each article via Claude, and commits the results as markdown files. The source health table below is auto-generated on each run.

## Source Health

<!-- SOURCE_HEALTH_START -->
| Source | Type | Last Success | Posts | Status | Notes |
|--------|------|-------------|-------|--------|-------|
| One Useful Thing (Ethan Mollick) | rss | 2026-08-26 | 9 | ✅ |  |
| OpenAI Blog | rss | 2026-08-26 | 0 | ✅ |  |
| Ken Huang \| AI Expert | rss | 2026-08-26 | 164 | ✅ |  |
| Future-Proof Your Career | rss | 2026-08-25 | 55 | ⚠️ | Feed parse error: <unknown>:2:0: syntax error |
| The AI Collective | rss | 2026-03-25 | 17 | ❌ | Feed parse error: <unknown>:2:0: syntax error |
| Harvard Business Review | rss | 2026-08-26 | 111 | ✅ |  |
| Real Estate News | rss | 2026-08-26 | 62 | ✅ |  |
| Anthropic Blog | sitemap | 2026-08-26 | 101 | ✅ |  |
| Built In | sitemap | 2026-08-26 | 12 | ✅ |  |
| EY Insights | sitemap | 2026-08-26 | 8 | ✅ |  |
| The a16z Show | podcast | 2026-08-26 | 139 | ✅ |  |
| Dwarkesh Podcast | podcast | 2026-08-26 | 22 | ✅ | Long episodes (2-3 hrs) |
| No Priors | podcast | 2026-08-26 | 24 | ✅ |  |
| Latent Space | podcast | 2026-08-26 | 47 | ✅ |  |
| AI Daily Brief | podcast | 2026-08-26 | 1 | ✅ | Short daily episodes (~10 min) |
<!-- SOURCE_HEALTH_END -->

## Recent Content

<!-- RECENT_CONTENT_START -->
### 2026-08-25
- [The New Economics Of Ai Martin Casado Steven Sinofsky](content/2026/08/25/a16z-podcast--the-new-economics-of-ai-martin-casado-steven-sinofsky.md) — a16z-podcast
- [Anthropic Economic Index Insights From Claude Sonnet 3 7](content/2026/08/25/anthropic-blog--anthropic-economic-index-insights-from-claude-sonnet-3-7.md) — anthropic-blog
- [Economic Futures Uk Europe](content/2026/08/25/anthropic-blog--economic-futures-uk-europe.md) — anthropic-blog
- [The Anthropic Economic Index](content/2026/08/25/anthropic-blog--the-anthropic-economic-index.md) — anthropic-blog
- [Wellbeing Research Grants](content/2026/08/25/anthropic-blog--wellbeing-research-grants.md) — anthropic-blog
- [Dylan Patel Anthropic Openai Will Have Most Of The Worlds Co](content/2026/08/25/dwarkesh-podcast--dylan-patel-anthropic-openai-will-have-most-of-the-worlds-co.md) — dwarkesh-podcast
- [Roomvu Lofty Unveil Tools To Boost Agent Visibility In Ai Se](content/2026/08/25/real-estate-news--roomvu-lofty-unveil-tools-to-boost-agent-visibility-in-ai-se.md) — real-estate-news

### 2026-08-24
- [Why Medical Ai Needs A Referee Proteges Engy Ziedan](content/2026/08/24/a16z-podcast--why-medical-ai-needs-a-referee-proteges-engy-ziedan.md) — a16z-podcast
- [Announcing Humanoid Robots And Physical Ai Book By Springer ](content/2026/08/24/ken-huang-ai-expert--announcing-humanoid-robots-and-physical-ai-book-by-springer-.md) — ken-huang-ai-expert

### 2026-08-23
- [Announcing The 10 Part Substack Series The Physics Engineeri](content/2026/08/23/ken-huang-ai-expert--announcing-the-10-part-substack-series-the-physics-engineeri.md) — ken-huang-ai-expert
- [Chapter 1 The Physics Of Llm Inference Roofline Models Memor](content/2026/08/23/ken-huang-ai-expert--chapter-1-the-physics-of-llm-inference-roofline-models-memor.md) — ken-huang-ai-expert
- [How Claudes Text Watermarking Works](content/2026/08/23/ken-huang-ai-expert--how-claudes-text-watermarking-works.md) — ken-huang-ai-expert
- [5 Ai Skills You Need To Learn Today](content/2026/08/23/khemaridh-future-proof--5-ai-skills-you-need-to-learn-today.md) — khemaridh-future-proof

### 2026-08-22
- [Martin Casado On Where The Value Is Going In Ai](content/2026/08/22/a16z-podcast--martin-casado-on-where-the-value-is-going-in-ai.md) — a16z-podcast
- [Proof Of Control For Model Context Protocol](content/2026/08/22/ken-huang-ai-expert--proof-of-control-for-model-context-protocol.md) — ken-huang-ai-expert

### 2026-08-21
- [Microsofts Deputy Ciso On Securing Ai Agents](content/2026/08/21/a16z-podcast--microsofts-deputy-ciso-on-securing-ai-agents.md) — a16z-podcast
- [From Software Engineering To Harness Engineering What Openai](content/2026/08/21/ken-huang-ai-expert--from-software-engineering-to-harness-engineering-what-openai.md) — ken-huang-ai-expert
- [Simulation The New Scaling Law Joon Sung Park Simile Ai](content/2026/08/21/latent-space--simulation-the-new-scaling-law-joon-sung-park-simile-ai.md) — latent-space

### 2026-08-20
- [How Global Networks Are Reshaping Startup Success](content/2026/08/20/a16z-podcast--how-global-networks-are-reshaping-startup-success.md) — a16z-podcast
- [Claude Design Can Make Beautiful Slide Decks](content/2026/08/20/khemaridh-future-proof--claude-design-can-make-beautiful-slide-decks.md) — khemaridh-future-proof
- [From Restoring Sight To Reimagining The Brain With Max Hodak](content/2026/08/20/no-priors--from-restoring-sight-to-reimagining-the-brain-with-max-hodak.md) — no-priors
- [Crmls Expands Recore Tools Childcare Info Now On Redfin List](content/2026/08/20/real-estate-news--crmls-expands-recore-tools-childcare-info-now-on-redfin-list.md) — real-estate-news

### 2026-08-19
- [How Whatnot Built A Global Marketplace](content/2026/08/19/a16z-podcast--how-whatnot-built-a-global-marketplace.md) — a16z-podcast

<!-- RECENT_CONTENT_END -->
