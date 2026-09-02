# AI Briefing Feeds

Daily AI-summarized content from curated sources, updated automatically via GitHub Actions.

**How it works:** A [daily GitHub Action](.github/workflows/daily.yaml) runs `pull.py`, which fetches content from 15 sources (RSS feeds, sitemaps, podcasts), summarizes each article via Claude, and commits the results as markdown files. The source health table below is auto-generated on each run.

## Source Health

<!-- SOURCE_HEALTH_START -->
| Source | Type | Last Success | Posts | Status | Notes |
|--------|------|-------------|-------|--------|-------|
| One Useful Thing (Ethan Mollick) | rss | 2026-09-02 | 10 | ✅ |  |
| OpenAI Blog | rss | 2026-09-02 | 0 | ✅ |  |
| Ken Huang \| AI Expert | rss | 2026-09-02 | 169 | ✅ |  |
| Future-Proof Your Career | rss | 2026-09-02 | 57 | ✅ |  |
| The AI Collective | rss | 2026-03-25 | 17 | ❌ | Feed parse error: <unknown>:2:0: syntax error |
| Harvard Business Review | rss | 2026-09-02 | 111 | ✅ |  |
| Real Estate News | rss | 2026-09-02 | 66 | ✅ |  |
| Anthropic Blog | sitemap | 2026-09-02 | 118 | ✅ |  |
| Built In | sitemap | 2026-09-02 | 12 | ✅ |  |
| EY Insights | sitemap | 2026-09-02 | 8 | ✅ |  |
| The a16z Show | podcast | 2026-09-02 | 147 | ✅ |  |
| Dwarkesh Podcast | podcast | 2026-09-02 | 24 | ✅ | Long episodes (2-3 hrs) |
| No Priors | podcast | 2026-09-02 | 25 | ✅ |  |
| Latent Space | podcast | 2026-09-02 | 48 | ✅ |  |
| AI Daily Brief | podcast | 2026-09-02 | 1 | ✅ | Short daily episodes (~10 min) |
<!-- SOURCE_HEALTH_END -->

## Recent Content

<!-- RECENT_CONTENT_START -->
### 2026-09-02
- [Inside Modernas Personalized Cancer Vaccine](content/2026/09/02/a16z-podcast--inside-modernas-personalized-cancer-vaccine.md) — a16z-podcast
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

### 2026-08-27
- [Inside Cursor The Anatomy Of A Generational Startup](content/2026/08/27/a16z-podcast--inside-cursor-the-anatomy-of-a-generational-startup.md) — a16z-podcast
- [Accelerating Scientific Research](content/2026/08/27/anthropic-blog--accelerating-scientific-research.md) — anthropic-blog
- [Advancing Claude For Education](content/2026/08/27/anthropic-blog--advancing-claude-for-education.md) — anthropic-blog
- [Ai For Science Program](content/2026/08/27/anthropic-blog--ai-for-science-program.md) — anthropic-blog
- [Anthropic And Iceland Announce One Of The World S First Nati](content/2026/08/27/anthropic-blog--anthropic-and-iceland-announce-one-of-the-world-s-first-nati.md) — anthropic-blog
- [Anthropic Partners With Allen Institute And Howard Hughes Me](content/2026/08/27/anthropic-blog--anthropic-partners-with-allen-institute-and-howard-hughes-me.md) — anthropic-blog
- [Anthropic Teach For All](content/2026/08/27/anthropic-blog--anthropic-teach-for-all.md) — anthropic-blog
- [Claude For Life Sciences](content/2026/08/27/anthropic-blog--claude-for-life-sciences.md) — anthropic-blog
- [Model Hardware Standard Research Preview](content/2026/08/27/anthropic-blog--model-hardware-standard-research-preview.md) — anthropic-blog
- [Rwandan Government Partnership Ai Education](content/2026/08/27/anthropic-blog--rwandan-government-partnership-ai-education.md) — anthropic-blog
- [Grok Bot Is Surprisingly Good](content/2026/08/27/khemaridh-future-proof--grok-bot-is-surprisingly-good.md) — khemaridh-future-proof
- [Rethinking Legacy Data Infrastructure With Eon Co Founders O](content/2026/08/27/no-priors--rethinking-legacy-data-infrastructure-with-eon-co-founders-o.md) — no-priors
- [Brokerage Leader Concerns About Ai Rebound As The Tech Advan](content/2026/08/27/real-estate-news--brokerage-leader-concerns-about-ai-rebound-as-the-tech-advan.md) — real-estate-news

### 2026-08-26
- [The State Of Ai Macro Apps And Consumer](content/2026/08/26/a16z-podcast--the-state-of-ai-macro-apps-and-consumer.md) — a16z-podcast
- [Anthropic Signs Pledge To Americas Youth Investing In Ai Edu](content/2026/08/26/anthropic-blog--anthropic-signs-pledge-to-americas-youth-investing-in-ai-edu.md) — anthropic-blog
- [Detecting And Countering Malicious Uses Of Claude March 2025](content/2026/08/26/anthropic-blog--detecting-and-countering-malicious-uses-of-claude-march-2025.md) — anthropic-blog
- [Lawrence Livermore National Laboratory Expands Claude For En](content/2026/08/26/anthropic-blog--lawrence-livermore-national-laboratory-expands-claude-for-en.md) — anthropic-blog
- [Our Approach To Understanding And Addressing Ai Harms](content/2026/08/26/anthropic-blog--our-approach-to-understanding-and-addressing-ai-harms.md) — anthropic-blog
- [Usage Policy Update](content/2026/08/26/anthropic-blog--usage-policy-update.md) — anthropic-blog
- [The Gateway Is Not The Identity Attested Trust For Agentic A](content/2026/08/26/ken-huang-ai-expert--the-gateway-is-not-the-identity-attested-trust-for-agentic-a.md) — ken-huang-ai-expert
- [We Have Foundation Models For Language Not For Physics Anima](content/2026/08/26/latent-space--we-have-foundation-models-for-language-not-for-physics-anima.md) — latent-space

<!-- RECENT_CONTENT_END -->
