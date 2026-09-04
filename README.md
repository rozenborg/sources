# AI Briefing Feeds

Daily AI-summarized content from curated sources, updated automatically via GitHub Actions.

**How it works:** A [daily GitHub Action](.github/workflows/daily.yaml) runs `pull.py`, which fetches content from 15 sources (RSS feeds, sitemaps, podcasts), summarizes each article via Claude, and commits the results as markdown files. The source health table below is auto-generated on each run.

## Source Health

<!-- SOURCE_HEALTH_START -->
| Source | Type | Last Success | Posts | Status | Notes |
|--------|------|-------------|-------|--------|-------|
| One Useful Thing (Ethan Mollick) | rss | 2026-09-04 | 10 | ✅ |  |
| OpenAI Blog | rss | 2026-09-04 | 0 | ✅ |  |
| Ken Huang \| AI Expert | rss | 2026-09-04 | 171 | ✅ |  |
| Future-Proof Your Career | rss | 2026-09-04 | 58 | ✅ |  |
| The AI Collective | rss | 2026-03-25 | 17 | ❌ | Feed parse error: <unknown>:2:0: syntax error |
| Harvard Business Review | rss | 2026-09-04 | 111 | ✅ |  |
| Real Estate News | rss | 2026-09-04 | 66 | ✅ |  |
| Anthropic Blog | sitemap | 2026-09-04 | 118 | ✅ |  |
| Built In | sitemap | 2026-09-04 | 12 | ✅ |  |
| EY Insights | sitemap | 2026-09-04 | 8 | ✅ |  |
| The a16z Show | podcast | 2026-09-04 | 149 | ✅ |  |
| Dwarkesh Podcast | podcast | 2026-09-04 | 24 | ✅ | Long episodes (2-3 hrs) |
| No Priors | podcast | 2026-09-04 | 26 | ✅ |  |
| Latent Space | podcast | 2026-09-04 | 48 | ✅ |  |
| AI Daily Brief | podcast | 2026-09-04 | 1 | ✅ | Short daily episodes (~10 min) |
<!-- SOURCE_HEALTH_END -->

## Recent Content

<!-- RECENT_CONTENT_START -->
### 2026-09-04
- [Fei Fei Li The Race To Build World Models For Ai](content/2026/09/04/a16z-podcast--fei-fei-li-the-race-to-build-world-models-for-ai.md) — a16z-podcast

### 2026-09-03
- [The 100B Niches Hiding Inside Payments](content/2026/09/03/a16z-podcast--the-100b-niches-hiding-inside-payments.md) — a16z-podcast
- [Upcoming Keynote On Hands On Graph Engineering With Claude C](content/2026/09/03/ken-huang-ai-expert--upcoming-keynote-on-hands-on-graph-engineering-with-claude-c.md) — ken-huang-ai-expert
- [Should You Trust Grok Bot To Manage Your Life](content/2026/09/03/khemaridh-future-proof--should-you-trust-grok-bot-to-manage-your-life.md) — khemaridh-future-proof
- [Redefining Chip Architecture With Arm Ceo Rene Haas](content/2026/09/03/no-priors--redefining-chip-architecture-with-arm-ceo-rene-haas.md) — no-priors

### 2026-09-02
- [Inside Modernas Personalized Cancer Vaccine](content/2026/09/02/a16z-podcast--inside-modernas-personalized-cancer-vaccine.md) — a16z-podcast
- [Anthropics Fable 51 Guide Reads Like A Manual For Agent Prod](content/2026/09/02/ken-huang-ai-expert--anthropics-fable-51-guide-reads-like-a-manual-for-agent-prod.md) — ken-huang-ai-expert
- [The Harness Advantage In Autonomous Red Teaming Why Frontier](content/2026/09/02/ken-huang-ai-expert--the-harness-advantage-in-autonomous-red-teaming-why-frontier.md) — ken-huang-ai-expert

### 2026-09-01
- [Daniel Litt The Mathematicians Guide To Ai](content/2026/09/01/a16z-podcast--daniel-litt-the-mathematicians-guide-to-ai.md) — a16z-podcast
- [Enterprise Frontier Safeguards](content/2026/09/01/anthropic-blog--enterprise-frontier-safeguards.md) — anthropic-blog
- [Improving Alignment Security Efforts](content/2026/09/01/anthropic-blog--improving-alignment-security-efforts.md) — anthropic-blog
- [Ajeya Cotra Inside The Openai Agent Swarm That Hacked Huggin](content/2026/09/01/dwarkesh-podcast--ajeya-cotra-inside-the-openai-agent-swarm-that-hacked-huggin.md) — dwarkesh-podcast
- [How A 5 Decade Brokerage Leader Thinks About Ai In Real Esta](content/2026/09/01/real-estate-news--how-a-5-decade-brokerage-leader-thinks-about-ai-in-real-esta.md) — real-estate-news

### 2026-08-31
- [Gavin Baker Why Ai Demand Is Outrunning Compute Supply](content/2026/08/31/a16z-podcast--gavin-baker-why-ai-demand-is-outrunning-compute-supply.md) — a16z-podcast
- [The Rise And Fall Of Agent Civilizations](content/2026/08/31/dwarkesh-podcast--the-rise-and-fall-of-agent-civilizations.md) — dwarkesh-podcast
- [Chapter 1 The Physics Of Llm Inference Memory Walls Arithmet](content/2026/08/31/ken-huang-ai-expert--chapter-1-the-physics-of-llm-inference-memory-walls-arithmet.md) — ken-huang-ai-expert
- [Agency And Agents](content/2026/08/31/mollick-one-useful-thing--agency-and-agents.md) — mollick-one-useful-thing
- [Former Meta Exec Tapped As New Redfin Ceo](content/2026/08/31/real-estate-news--former-meta-exec-tapped-as-new-redfin-ceo.md) — real-estate-news
- [Kw Partnership Adds New Ai Tools For Agents Exps Nexus Expan](content/2026/08/31/real-estate-news--kw-partnership-adds-new-ai-tools-for-agents-exps-nexus-expan.md) — real-estate-news

### 2026-08-30
- [Why A16Z Launched The Machine Age Fund Jen Kha](content/2026/08/30/a16z-podcast--why-a16z-launched-the-machine-age-fund-jen-kha.md) — a16z-podcast
- [Has Chatgpt Overtaken Claude Cowork](content/2026/08/30/khemaridh-future-proof--has-chatgpt-overtaken-claude-cowork.md) — khemaridh-future-proof

### 2026-08-29
- [Why 1200 Ai Agents Started Working Together Ryan Greenblatt](content/2026/08/29/a16z-podcast--why-1200-ai-agents-started-working-together-ryan-greenblatt.md) — a16z-podcast
- [Multi Agent Design Patterns Architectural Topologies Failure](content/2026/08/29/ken-huang-ai-expert--multi-agent-design-patterns-architectural-topologies-failure.md) — ken-huang-ai-expert

### 2026-08-28
- [The Infrastructure Behind The Machine Age](content/2026/08/28/a16z-podcast--the-infrastructure-behind-the-machine-age.md) — a16z-podcast
- [Expanding Support For Scientists](content/2026/08/28/anthropic-blog--expanding-support-for-scientists.md) — anthropic-blog
- [Grok Bot Is Here Maestro Shows Where The Real Risks Are](content/2026/08/28/ken-huang-ai-expert--grok-bot-is-here-maestro-shows-where-the-real-risks-are.md) — ken-huang-ai-expert

<!-- RECENT_CONTENT_END -->
