# AI Briefing Feeds

Daily AI-summarized content from curated sources, updated automatically via GitHub Actions.

**How it works:** A [daily GitHub Action](.github/workflows/daily.yaml) runs `pull.py`, which fetches content from 15 sources (RSS feeds, sitemaps, podcasts), summarizes each article via Claude, and commits the results as markdown files. The source health table below is auto-generated on each run.

## Source Health

<!-- SOURCE_HEALTH_START -->
| Source | Type | Last Success | Posts | Status | Notes |
|--------|------|-------------|-------|--------|-------|
| One Useful Thing (Ethan Mollick) | rss | 2026-09-23 | 11 | ✅ |  |
| OpenAI Blog | rss | 2026-09-23 | 0 | ✅ |  |
| Ken Huang \| AI Expert | rss | 2026-09-23 | 190 | ✅ |  |
| Future-Proof Your Career | rss | 2026-09-23 | 62 | ✅ |  |
| The AI Collective | rss | 2026-03-25 | 17 | ❌ | Feed parse error: <unknown>:2:0: syntax error |
| Harvard Business Review | rss | 2026-09-23 | 111 | ✅ |  |
| Real Estate News | rss | 2026-09-23 | 71 | ✅ |  |
| Anthropic Blog | sitemap | 2026-09-23 | 142 | ✅ |  |
| Built In | sitemap | 2026-09-23 | 13 | ✅ |  |
| EY Insights | sitemap | 2026-09-23 | 8 | ✅ |  |
| The a16z Show | podcast | 2026-09-23 | 168 | ✅ |  |
| Dwarkesh Podcast | podcast | 2026-09-23 | 26 | ✅ | Long episodes (2-3 hrs) |
| No Priors | podcast | 2026-09-23 | 28 | ✅ |  |
| Latent Space | podcast | 2026-09-23 | 52 | ✅ |  |
| AI Daily Brief | podcast | 2026-09-23 | 1 | ✅ | Short daily episodes (~10 min) |
<!-- SOURCE_HEALTH_END -->

## Recent Content

<!-- RECENT_CONTENT_START -->
### 2026-09-23
- [Amjad Masad On Rethinking College For The Ai Era](content/2026/09/23/a16z-podcast--amjad-masad-on-rethinking-college-for-the-ai-era.md) — a16z-podcast

### 2026-09-22
- [Why A16Z Is Building A New School For The Ai Era Ben Horowit](content/2026/09/22/a16z-podcast--why-a16z-is-building-a-new-school-for-the-ai-era-ben-horowit.md) — a16z-podcast
- [Chapter 10 Constrained Decoding The 2026 Production Blueprin](content/2026/09/22/ken-huang-ai-expert--chapter-10-constrained-decoding-the-2026-production-blueprin.md) — ken-huang-ai-expert
- [An Oscar Two Asteroids And The Algorithm In Your Sklearn Joh](content/2026/09/22/latent-space--an-oscar-two-asteroids-and-the-algorithm-in-your-sklearn-joh.md) — latent-space
- [Agents Branching Out From Generative Ai As Adoption Grows](content/2026/09/22/real-estate-news--agents-branching-out-from-generative-ai-as-adoption-grows.md) — real-estate-news

### 2026-09-21
- [Ai Safety Language Is Destroying The Debate Steven Sinofsky](content/2026/09/21/a16z-podcast--ai-safety-language-is-destroying-the-debate-steven-sinofsky.md) — a16z-podcast
- [What Is Jev From Typesafe Ai How We Implemented Agentic Soc ](content/2026/09/21/ken-huang-ai-expert--what-is-jev-from-typesafe-ai-how-we-implemented-agentic-soc-.md) — ken-huang-ai-expert
- [Jev System One Models For Prod Not God With Diogo Almeida Ce](content/2026/09/21/latent-space--jev-system-one-models-for-prod-not-god-with-diogo-almeida-ce.md) — latent-space

### 2026-09-20
- [Nas Grandmaster Caz Steve Stoute Ben Horowitz On Paying Hip ](content/2026/09/20/a16z-podcast--nas-grandmaster-caz-steve-stoute-ben-horowitz-on-paying-hip-.md) — a16z-podcast
- [Chapter 9 Ultra Long Context Mastery Dual Chunk Attention Ya](content/2026/09/20/ken-huang-ai-expert--chapter-9-ultra-long-context-mastery-dual-chunk-attention-ya.md) — ken-huang-ai-expert

### 2026-09-19
- [What Makes A Consumer Ai Product Stick Josh Elman](content/2026/09/19/a16z-podcast--what-makes-a-consumer-ai-product-stick-josh-elman.md) — a16z-podcast
- [Chapter 8 Test Time Compute Reasoning Dynamics Deepseek V4 P](content/2026/09/19/ken-huang-ai-expert--chapter-8-test-time-compute-reasoning-dynamics-deepseek-v4-p.md) — ken-huang-ai-expert

### 2026-09-18
- [Databricks Ceo On Ai Pacing Cyber Risk And The Enterprise](content/2026/09/18/a16z-podcast--databricks-ceo-on-ai-pacing-cyber-risk-and-the-enterprise.md) — a16z-podcast
- [Accenture Embedded Evaluation](content/2026/09/18/anthropic-blog--accenture-embedded-evaluation.md) — anthropic-blog
- [Chapter 7 Serving Mega Moe At Scale Colossus Interconnects E](content/2026/09/18/ken-huang-ai-expert--chapter-7-serving-mega-moe-at-scale-colossus-interconnects-e.md) — ken-huang-ai-expert
- [The Overhang](content/2026/09/18/mollick-one-useful-thing--the-overhang.md) — mollick-one-useful-thing
- [Why Diffusion Will Win Ai Inference With Inception Co Founde](content/2026/09/18/no-priors--why-diffusion-will-win-ai-inference-with-inception-co-founde.md) — no-priors

### 2026-09-17
- [The Next Frontier Of Ai Video Is Control](content/2026/09/17/a16z-podcast--the-next-frontier-of-ai-video-is-control.md) — a16z-podcast
- [Life Sciences Verification Program](content/2026/09/17/anthropic-blog--life-sciences-verification-program.md) — anthropic-blog
- [Noam Brown Agent Swarms Alignment Recursive Self Improvement](content/2026/09/17/dwarkesh-podcast--noam-brown-agent-swarms-alignment-recursive-self-improvement.md) — dwarkesh-podcast
- [Gpt 6 Astra Plus Kimi K3 Swarm Route Depth And Width Before ](content/2026/09/17/ken-huang-ai-expert--gpt-6-astra-plus-kimi-k3-swarm-route-depth-and-width-before-.md) — ken-huang-ai-expert
- [How To Improve Your Skills With Evals](content/2026/09/17/khemaridh-future-proof--how-to-improve-your-skills-with-evals.md) — khemaridh-future-proof
- [Ai Tools Are Quickly Becoming Integral To Brokerage Operatio](content/2026/09/17/real-estate-news--ai-tools-are-quickly-becoming-integral-to-brokerage-operatio.md) — real-estate-news

### 2026-09-16
- [The Ai Native Crm](content/2026/09/16/a16z-podcast--the-ai-native-crm.md) — a16z-podcast
- [Openais Defense Factory Turns Vulnerability Work Into A Cont](content/2026/09/16/ken-huang-ai-expert--openais-defense-factory-turns-vulnerability-work-into-a-cont.md) — ken-huang-ai-expert
- [Underwriting Superintelligence Backing Agents You Can Sue Ru](content/2026/09/16/latent-space--underwriting-superintelligence-backing-agents-you-can-sue-ru.md) — latent-space

<!-- RECENT_CONTENT_END -->
