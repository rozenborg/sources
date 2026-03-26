# AI Briefing Feeds

Daily AI-summarized content from curated sources, updated automatically via GitHub Actions.

**How it works:** A [daily GitHub Action](.github/workflows/daily.yaml) runs `pull.py`, which fetches content from 15 sources (RSS feeds, sitemaps, podcasts), summarizes each article via Claude, and commits the results as markdown files. The source health table below is auto-generated on each run.

## Source Health

<!-- SOURCE_HEALTH_START -->
| Source | Type | Last Success | Posts | Status | Notes |
|--------|------|-------------|-------|--------|-------|
| One Useful Thing (Ethan Mollick) | rss | 2026-03-26 | 2 | ✅ |  |
| OpenAI Blog | rss | 2026-03-26 | 0 | ✅ |  |
| Ken Huang \| AI Expert | rss | 2026-03-26 | 31 | ✅ |  |
| Future-Proof Your Career | rss | 2026-03-26 | 11 | ✅ |  |
| The AI Collective | rss | 2026-03-25 | 17 | ⚠️ | Feed parse error: <unknown>:2:0: syntax error |
| Harvard Business Review | rss | 2026-03-26 | 38 | ✅ |  |
| Real Estate News | rss | 2026-03-26 | 14 | ✅ |  |
| Anthropic Blog | sitemap | 2026-03-26 | 22 | ✅ |  |
| Built In | sitemap | 2026-03-26 | 6 | ✅ |  |
| EY Insights | sitemap | 2026-03-26 | 7 | ✅ |  |
| The a16z Show | podcast | 2026-03-26 | 27 | ✅ |  |
| Dwarkesh Podcast | podcast | 2026-03-26 | 5 | ✅ | Long episodes (2-3 hrs) |
| No Priors | podcast | 2026-03-26 | 4 | ✅ |  |
| Latent Space | podcast | 2026-03-26 | 13 | ✅ |  |
| AI Daily Brief | podcast | 2026-03-26 | 1 | ✅ | Short daily episodes (~10 min) |
<!-- SOURCE_HEALTH_END -->

## Recent Content

<!-- RECENT_CONTENT_START -->
### 2026-03-25
- [Submarines And The Future Of Defense Manufacturing](content/2026/03/25/a16z-podcast--submarines-and-the-future-of-defense-manufacturing.md) — a16z-podcast
- [Create An Onboarding Plan For Ai Agents](content/2026/03/25/hbr--create-an-onboarding-plan-for-ai-agents.md) — hbr
- [Getting Ready For Agentic Ai](content/2026/03/25/hbr--getting-ready-for-agentic-ai.md) — hbr
- [Intentbased Access Control A Technical Primer](content/2026/03/25/ken-huang-ai-expert--intentbased-access-control-a-technical-primer.md) — ken-huang-ai-expert

### 2026-03-24
- [The Missing Power Layer Of Modern Warfare](content/2026/03/24/a16z-podcast--the-missing-power-layer-of-modern-warfare.md) — a16z-podcast
- [Moltbookthreat Modeling Report](content/2026/03/24/ken-huang-ai-expert--moltbookthreat-modeling-report.md) — ken-huang-ai-expert
- [Why There Is No Alphafold For Materials Ai For Materials Dis](content/2026/03/24/latent-space--why-there-is-no-alphafold-for-materials-ai-for-materials-dis.md) — latent-space
- [Sourcere Launches Mls Data Tracker State Wide Mls Adds Realr](content/2026/03/24/real-estate-news--sourcere-launches-mls-data-tracker-state-wide-mls-adds-realr.md) — real-estate-news

### 2026-03-23
- [Why Every Satellite Needs Earth Northwood Ceo On A16Z](content/2026/03/23/a16z-podcast--why-every-satellite-needs-earth-northwood-ceo-on-a16z.md) — a16z-podcast
- [To Scale Ai Agents Successfully Think Of Them Like Team Memb](content/2026/03/23/hbr--to-scale-ai-agents-successfully-think-of-them-like-team-memb.md) — hbr
- [Do You Have An Openclaw Strategy](content/2026/03/23/ken-huang-ai-expert--do-you-have-an-openclaw-strategy.md) — ken-huang-ai-expert

### 2026-03-22
- [Claude Is Coming For Your Messaging Apps](content/2026/03/22/khemaridh-future-proof--claude-is-coming-for-your-messaging-apps.md) — khemaridh-future-proof

### 2026-03-21
- [Agent Skill Trust Signing Service](content/2026/03/21/ken-huang-ai-expert--agent-skill-trust-signing-service.md) — ken-huang-ai-expert
- [The Day Metas Ai Agent Broke Least Privilege A Maestro Deep ](content/2026/03/21/ken-huang-ai-expert--the-day-metas-ai-agent-broke-least-privilege-a-maestro-deep-.md) — ken-huang-ai-expert

### 2026-03-20
- [Inside Palantir Building Software That Matters With Shyam Sa](content/2026/03/20/a16z-podcast--inside-palantir-building-software-that-matters-with-shyam-sa.md) — a16z-podcast
- [The Community Edition When Agents Miss The Fine Print](content/2026/03/20/ai-collective--the-community-edition-when-agents-miss-the-fine-print.md) — ai-collective
- [Terence Tao Kepler Newton And The True Nature Of Mathematica](content/2026/03/20/dwarkesh-podcast--terence-tao-kepler-newton-and-the-true-nature-of-mathematica.md) — dwarkesh-podcast
- [Join Me At Rsa Conference 2026 Lets Connect](content/2026/03/20/ken-huang-ai-expert--join-me-at-rsa-conference-2026-lets-connect.md) — ken-huang-ai-expert
- [Dreamer The Personal Agent Os David Singleton](content/2026/03/20/latent-space--dreamer-the-personal-agent-os-david-singleton.md) — latent-space
- [Andrej Karpathy On Code Agents Autoresearch And The Loopy Er](content/2026/03/20/no-priors--andrej-karpathy-on-code-agents-autoresearch-and-the-loopy-er.md) — no-priors

### 2026-03-19
- [Ai Just Gave You Superpowers Now What](content/2026/03/19/a16z-podcast--ai-just-gave-you-superpowers-now-what.md) — a16z-podcast
- [Our Favorite Management Tips On Leading With Ai](content/2026/03/19/hbr--our-favorite-management-tips-on-leading-with-ai.md) — hbr
- [Strategy Summit 2026 Why Ai Means Radical Change](content/2026/03/19/hbr--strategy-summit-2026-why-ai-means-radical-change.md) — hbr
- [What The Best Ai Users Do Differentlyand How To Level Up All](content/2026/03/19/hbr--what-the-best-ai-users-do-differentlyand-how-to-level-up-all.md) — hbr
- [Owasp Aivss Project Announces The Release Of V08 Scoring Sys](content/2026/03/19/ken-huang-ai-expert--owasp-aivss-project-announces-the-release-of-v08-scoring-sys.md) — ken-huang-ai-expert
- [The Complete Guide To Claude Skills](content/2026/03/19/khemaridh-future-proof--the-complete-guide-to-claude-skills.md) — khemaridh-future-proof

<!-- RECENT_CONTENT_END -->
