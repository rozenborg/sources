# AI Briefing Feeds

Daily AI-summarized content from curated sources, updated automatically via GitHub Actions.

**How it works:** A [daily GitHub Action](.github/workflows/daily.yaml) runs `pull.py`, which fetches content from 15 sources (RSS feeds, sitemaps, podcasts), summarizes each article via Claude, and commits the results as markdown files. The source health table below is auto-generated on each run.

## Source Health

<!-- SOURCE_HEALTH_START -->
| Source | Type | Last Success | Posts | Status | Notes |
|--------|------|-------------|-------|--------|-------|
| One Useful Thing (Ethan Mollick) | rss | 2026-09-08 | 10 | ✅ |  |
| OpenAI Blog | rss | 2026-09-08 | 0 | ✅ |  |
| Ken Huang \| AI Expert | rss | 2026-09-08 | 174 | ✅ |  |
| Future-Proof Your Career | rss | 2026-09-08 | 59 | ✅ |  |
| The AI Collective | rss | 2026-03-25 | 17 | ❌ | Feed parse error: <unknown>:2:0: syntax error |
| Harvard Business Review | rss | 2026-09-08 | 111 | ✅ |  |
| Real Estate News | rss | 2026-09-08 | 66 | ✅ |  |
| Anthropic Blog | sitemap | 2026-09-08 | 120 | ✅ |  |
| Built In | sitemap | 2026-09-08 | 12 | ✅ |  |
| EY Insights | sitemap | 2026-09-08 | 8 | ✅ |  |
| The a16z Show | podcast | 2026-09-08 | 153 | ✅ |  |
| Dwarkesh Podcast | podcast | 2026-09-08 | 24 | ✅ | Long episodes (2-3 hrs) |
| No Priors | podcast | 2026-09-08 | 26 | ✅ |  |
| Latent Space | podcast | 2026-09-08 | 48 | ✅ |  |
| AI Daily Brief | podcast | 2026-09-08 | 1 | ✅ | Short daily episodes (~10 min) |
<!-- SOURCE_HEALTH_END -->

## Recent Content

<!-- RECENT_CONTENT_START -->
### 2026-09-08
- [Openai Researchers On The Future Of Mathematical Reasoning](content/2026/09/08/a16z-podcast--openai-researchers-on-the-future-of-mathematical-reasoning.md) — a16z-podcast
- [Detecting Countering Misuse Aug 2025](content/2026/09/08/anthropic-blog--detecting-countering-misuse-aug-2025.md) — anthropic-blog
- [Disrupting Ai Espionage](content/2026/09/08/anthropic-blog--disrupting-ai-espionage.md) — anthropic-blog

### 2026-09-07
- [Can Open Source Keep Ai Power From Concentrating](content/2026/09/07/a16z-podcast--can-open-source-keep-ai-power-from-concentrating.md) — a16z-podcast

### 2026-09-06
- [Your Ai Doctor Is Coming Julie Yoo](content/2026/09/06/a16z-podcast--your-ai-doctor-is-coming-julie-yoo.md) — a16z-podcast
- [Chapter 2 The Kv Cache Frontier Hybrid Compressed Sparse Att](content/2026/09/06/ken-huang-ai-expert--chapter-2-the-kv-cache-frontier-hybrid-compressed-sparse-att.md) — ken-huang-ai-expert
- [Inside The Book Graph Engineering For Agentic Ai Systems Cha](content/2026/09/06/ken-huang-ai-expert--inside-the-book-graph-engineering-for-agentic-ai-systems-cha.md) — ken-huang-ai-expert
- [33 Questions Executives Ask About Ai](content/2026/09/06/khemaridh-future-proof--33-questions-executives-ask-about-ai.md) — khemaridh-future-proof

### 2026-09-05
- [Aaron Levie On Why Open Ai Wins](content/2026/09/05/a16z-podcast--aaron-levie-on-why-open-ai-wins.md) — a16z-podcast

### 2026-09-04
- [Fei Fei Li The Race To Build World Models For Ai](content/2026/09/04/a16z-podcast--fei-fei-li-the-race-to-build-world-models-for-ai.md) — a16z-podcast
- [Astra Or Gpt6 Inside Openais First Critical Tier Model](content/2026/09/04/ken-huang-ai-expert--astra-or-gpt6-inside-openais-first-critical-tier-model.md) — ken-huang-ai-expert

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

<!-- RECENT_CONTENT_END -->
