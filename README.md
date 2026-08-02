# AI Briefing Feeds

Daily AI-summarized content from curated sources, updated automatically via GitHub Actions.

**How it works:** A [daily GitHub Action](.github/workflows/daily.yaml) runs `pull.py`, which fetches content from 15 sources (RSS feeds, sitemaps, podcasts), summarizes each article via Claude, and commits the results as markdown files. The source health table below is auto-generated on each run.

## Source Health

<!-- SOURCE_HEALTH_START -->
| Source | Type | Last Success | Posts | Status | Notes |
|--------|------|-------------|-------|--------|-------|
| One Useful Thing (Ethan Mollick) | rss | 2026-08-02 | 9 | ✅ |  |
| OpenAI Blog | rss | 2026-08-02 | 0 | ✅ |  |
| Ken Huang \| AI Expert | rss | 2026-08-02 | 151 | ✅ |  |
| Future-Proof Your Career | rss | 2026-08-02 | 48 | ✅ |  |
| The AI Collective | rss | 2026-03-25 | 17 | ❌ | Feed parse error: <unknown>:2:0: syntax error |
| Harvard Business Review | rss | 2026-08-02 | 111 | ✅ |  |
| Real Estate News | rss | 2026-08-02 | 56 | ✅ |  |
| Anthropic Blog | sitemap | 2026-08-02 | 93 | ✅ |  |
| Built In | sitemap | 2026-08-02 | 12 | ✅ |  |
| EY Insights | sitemap | 2026-08-02 | 8 | ✅ |  |
| The a16z Show | podcast | 2026-08-02 | 121 | ✅ |  |
| Dwarkesh Podcast | podcast | 2026-08-02 | 18 | ✅ | Long episodes (2-3 hrs) |
| No Priors | podcast | 2026-08-02 | 21 | ✅ |  |
| Latent Space | podcast | 2026-08-02 | 44 | ✅ |  |
| AI Daily Brief | podcast | 2026-08-02 | 1 | ✅ | Short daily episodes (~10 min) |
<!-- SOURCE_HEALTH_END -->

## Recent Content

<!-- RECENT_CONTENT_START -->
### 2026-08-01
- [Marc Andreessen And Chris Dixon Whats At Stake In Crypto Reg](content/2026/08/01/a16z-podcast--marc-andreessen-and-chris-dixon-whats-at-stake-in-crypto-reg.md) — a16z-podcast
- [Maestro Analysis Of Openai And Anthropic Agent Hacking Incid](content/2026/08/01/ken-huang-ai-expert--maestro-analysis-of-openai-and-anthropic-agent-hacking-incid.md) — ken-huang-ai-expert

### 2026-07-31
- [Decagons Playbook For Building Enterprise Ai Applications](content/2026/07/31/a16z-podcast--decagons-playbook-for-building-enterprise-ai-applications.md) — a16z-podcast
- [One Week Three Conferences My Las Vegas Ai Security Itinerar](content/2026/07/31/ken-huang-ai-expert--one-week-three-conferences-my-las-vegas-ai-security-itinerar.md) — ken-huang-ai-expert
- [Building An Autonomous Enterprise For Real World Services Wi](content/2026/07/31/no-priors--building-an-autonomous-enterprise-for-real-world-services-wi.md) — no-priors

### 2026-07-30
- [Ai For Americas Small Businesses Lassie](content/2026/07/30/a16z-podcast--ai-for-americas-small-businesses-lassie.md) — a16z-podcast
- [Investigating Incidents Cybersecurity Evals](content/2026/07/30/anthropic-blog--investigating-incidents-cybersecurity-evals.md) — anthropic-blog
- [Harness Engineering As The Umbrella Discipline](content/2026/07/30/ken-huang-ai-expert--harness-engineering-as-the-umbrella-discipline.md) — ken-huang-ai-expert
- [Cowork Comes To The Cloud](content/2026/07/30/khemaridh-future-proof--cowork-comes-to-the-cloud.md) — khemaridh-future-proof

### 2026-07-29
- [Ai Micro Dramas Generative Media And The Future Of Creativit](content/2026/07/29/a16z-podcast--ai-micro-dramas-generative-media-and-the-future-of-creativit.md) — a16z-podcast
- [How Ai Teams Are Turning Emerging Tech Real World Products](content/2026/07/29/builtin-com--how-ai-teams-are-turning-emerging-tech-real-world-products.md) — builtin-com

### 2026-07-28
- [Fei Fei Li On Spatial Intelligence And Robotics](content/2026/07/28/a16z-podcast--fei-fei-li-on-spatial-intelligence-and-robotics.md) — a16z-podcast
- [We Scored 4570 Agents Against Owasp Aivss And Csa Maestro](content/2026/07/28/ken-huang-ai-expert--we-scored-4570-agents-against-owasp-aivss-and-csa-maestro.md) — ken-huang-ai-expert
- [Codex From 0 To 10M Users Building Chatgpt Work Akshay Natha](content/2026/07/28/latent-space--codex-from-0-to-10m-users-building-chatgpt-work-akshay-natha.md) — latent-space
- [Lone Wolf Investing In Ai With Recruitment Retention Tools](content/2026/07/28/real-estate-news--lone-wolf-investing-in-ai-with-recruitment-retention-tools.md) — real-estate-news
- [Lpt Parent Acquires Ai Company Focused On Iding Consumer Int](content/2026/07/28/real-estate-news--lpt-parent-acquires-ai-company-focused-on-iding-consumer-int.md) — real-estate-news

### 2026-07-27
- [Steven Sinofsky Ai Doesnt Need New Rules Yet](content/2026/07/27/a16z-podcast--steven-sinofsky-ai-doesnt-need-new-rules-yet.md) — a16z-podcast
- [Cognizant Anthropic](content/2026/07/27/anthropic-blog--cognizant-anthropic.md) — anthropic-blog
- [Position Open Weights Models](content/2026/07/27/anthropic-blog--position-open-weights-models.md) — anthropic-blog
- [Better Informed Sellers Are Raising The Stakes For Cmas](content/2026/07/27/real-estate-news--better-informed-sellers-are-raising-the-stakes-for-cmas.md) — real-estate-news
- [Compass Chief Economist Has His Eye On The Ai Housing Boom](content/2026/07/27/real-estate-news--compass-chief-economist-has-his-eye-on-the-ai-housing-boom.md) — real-estate-news

### 2026-07-26
- [Ben Horowitz The Fight Over Open Source Ai](content/2026/07/26/a16z-podcast--ben-horowitz-the-fight-over-open-source-ai.md) — a16z-podcast
- [Agentic Ai Cves Anatomy Of A New Attack Surface](content/2026/07/26/ken-huang-ai-expert--agentic-ai-cves-anatomy-of-a-new-attack-surface.md) — ken-huang-ai-expert
- [Jensen Makes The Case For Open Source Ai](content/2026/07/26/khemaridh-future-proof--jensen-makes-the-case-for-open-source-ai.md) — khemaridh-future-proof

<!-- RECENT_CONTENT_END -->
