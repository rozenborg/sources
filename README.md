# AI Briefing Feeds

Daily AI-summarized content from curated sources, updated automatically via GitHub Actions.

**How it works:** A [daily GitHub Action](.github/workflows/daily.yaml) runs `pull.py`, which fetches content from 15 sources (RSS feeds, sitemaps, podcasts), summarizes each article via Claude, and commits the results as markdown files. The source health table below is auto-generated on each run.

## Source Health

<!-- SOURCE_HEALTH_START -->
| Source | Type | Last Success | Posts | Status | Notes |
|--------|------|-------------|-------|--------|-------|
| One Useful Thing (Ethan Mollick) | rss | 2026-05-27 | 5 | ✅ |  |
| OpenAI Blog | rss | 2026-05-27 | 0 | ✅ |  |
| Ken Huang \| AI Expert | rss | 2026-05-27 | 99 | ✅ |  |
| Future-Proof Your Career | rss | 2026-05-27 | 29 | ✅ |  |
| The AI Collective | rss | 2026-03-25 | 17 | ❌ | Feed parse error: <unknown>:2:0: syntax error |
| Harvard Business Review | rss | 2026-05-27 | 76 | ✅ |  |
| Real Estate News | rss | 2026-05-27 | 34 | ✅ |  |
| Anthropic Blog | sitemap | 2026-05-27 | 46 | ✅ |  |
| Built In | sitemap | 2026-05-27 | 8 | ✅ |  |
| EY Insights | sitemap | 2026-05-27 | 8 | ✅ |  |
| The a16z Show | podcast | 2026-05-27 | 73 | ✅ |  |
| Dwarkesh Podcast | podcast | 2026-05-27 | 11 | ✅ | Long episodes (2-3 hrs) |
| No Priors | podcast | 2026-05-27 | 12 | ✅ |  |
| Latent Space | podcast | 2026-05-27 | 27 | ✅ |  |
| AI Daily Brief | podcast | 2026-05-27 | 1 | ✅ | Short daily episodes (~10 min) |
<!-- SOURCE_HEALTH_END -->

## Recent Content

<!-- RECENT_CONTENT_START -->
### 2026-05-27
- [Marc Rowan On Private Markets Software Repricing And Capital](content/2026/05/27/a16z-podcast--marc-rowan-on-private-markets-software-repricing-and-capital.md) — a16z-podcast
- [Housewhisper Adds Lead Boosting Tools Hive Mls Debuts User S](content/2026/05/27/real-estate-news--housewhisper-adds-lead-boosting-tools-hive-mls-debuts-user-s.md) — real-estate-news

### 2026-05-26
- [Robin Hanson On Prediction Markets Gambling And The Future O](content/2026/05/26/a16z-podcast--robin-hanson-on-prediction-markets-gambling-and-the-future-o.md) — a16z-podcast
- [Kiyoung Choi Representative Director Anthropic Korea](content/2026/05/26/anthropic-blog--kiyoung-choi-representative-director-anthropic-korea.md) — anthropic-blog
- [How To Compete Against Agentic Startups](content/2026/05/26/hbr--how-to-compete-against-agentic-startups.md) — hbr
- [Choosing To Stay Human](content/2026/05/26/mollick-one-useful-thing--choosing-to-stay-human.md) — mollick-one-useful-thing

### 2026-05-25
- [Why Ai Isnt Killing Saas Yet](content/2026/05/25/a16z-podcast--why-ai-isnt-killing-saas-yet.md) — a16z-podcast
- [Chris Olah Pope Leo Encyclical](content/2026/05/25/anthropic-blog--chris-olah-pope-leo-encyclical.md) — anthropic-blog
- [Managers Are Struggling To Keep Up With The Ai Productivity ](content/2026/05/25/hbr--managers-are-struggling-to-keep-up-with-the-ai-productivity-.md) — hbr
- [Why Static Authorization Is Failing In The Age Of Ai Agents](content/2026/05/25/ken-huang-ai-expert--why-static-authorization-is-failing-in-the-age-of-ai-agents.md) — ken-huang-ai-expert

### 2026-05-24
- [Lessons In Founder Mode And Ai](content/2026/05/24/khemaridh-future-proof--lessons-in-founder-mode-and-ai.md) — khemaridh-future-proof

### 2026-05-23
- [Compound Engineering Vs Gstack Vs Karpathys Autoresearch Vs ](content/2026/05/23/ken-huang-ai-expert--compound-engineering-vs-gstack-vs-karpathys-autoresearch-vs-.md) — ken-huang-ai-expert

### 2026-05-22
- [Hugging Faces Clem Delangue On Open Source Ai And The Llm Bu](content/2026/05/22/a16z-podcast--hugging-faces-clem-delangue-on-open-source-ai-and-the-llm-bu.md) — a16z-podcast
- [Reiner Pope Chip Design From The Bottom Up](content/2026/05/22/dwarkesh-podcast--reiner-pope-chip-design-from-the-bottom-up.md) — dwarkesh-podcast
- [The Best Manufacturers Build Ai With Workers Not For Them](content/2026/05/22/hbr--the-best-manufacturers-build-ai-with-workers-not-for-them.md) — hbr
- [A Recursive Project Improvement Loop](content/2026/05/22/ken-huang-ai-expert--a-recursive-project-improvement-loop.md) — ken-huang-ai-expert
- [Designing Agentic Ai Systems With The Orchideas Framework](content/2026/05/22/ken-huang-ai-expert--designing-agentic-ai-systems-with-the-orchideas-framework.md) — ken-huang-ai-expert
- [What Brokerages Must Do To Leverage The Future Of Ai](content/2026/05/22/real-estate-news--what-brokerages-must-do-to-leverage-the-future-of-ai.md) — real-estate-news

### 2026-05-21
- [How Superhuman Took Over Silicon Valley Email](content/2026/05/21/a16z-podcast--how-superhuman-took-over-silicon-valley-email.md) — a16z-podcast
- [Companies Hiring Machine Learning Engineers](content/2026/05/21/builtin-com--companies-hiring-machine-learning-engineers.md) — builtin-com
- [Chapter 3 The Slash Command System Claude Code Vs Hermes Age](content/2026/05/21/ken-huang-ai-expert--chapter-3-the-slash-command-system-claude-code-vs-hermes-age.md) — ken-huang-ai-expert
- [Is Notion Ai Ready For Prime Time](content/2026/05/21/khemaridh-future-proof--is-notion-ai-ready-for-prime-time.md) — khemaridh-future-proof
- [Giving Agents Computers Ivan Burazin Daytona](content/2026/05/21/latent-space--giving-agents-computers-ivan-burazin-daytona.md) — latent-space
- [The Story Behind Cerebras 63 Billion Ipo With Founder And Ce](content/2026/05/21/no-priors--the-story-behind-cerebras-63-billion-ipo-with-founder-and-ce.md) — no-priors

### 2026-05-20
- [Marc Andreessen On Ai California And The Future Of America J](content/2026/05/20/a16z-podcast--marc-andreessen-on-ai-california-and-the-future-of-america-j.md) — a16z-podcast
- [Widening Conversation Ai](content/2026/05/20/anthropic-blog--widening-conversation-ai.md) — anthropic-blog
- [Will Ai First Devices Replace Smartphone](content/2026/05/20/builtin-com--will-ai-first-devices-replace-smartphone.md) — builtin-com
- [An Implementation Checklist To Claude Code In Large Codebase](content/2026/05/20/ken-huang-ai-expert--an-implementation-checklist-to-claude-code-in-large-codebase.md) — ken-huang-ai-expert
- [Google Io 2026 Was Not Just A Model Launch It Was Google Sho](content/2026/05/20/ken-huang-ai-expert--google-io-2026-was-not-just-a-model-launch-it-was-google-sho.md) — ken-huang-ai-expert
- [Railway The Agent Native Cloud Jake Cooper](content/2026/05/20/latent-space--railway-the-agent-native-cloud-jake-cooper.md) — latent-space
- [Revive Elevates Ai Platform Rayse Inks Deal With Momentum Ml](content/2026/05/20/real-estate-news--revive-elevates-ai-platform-rayse-inks-deal-with-momentum-ml.md) — real-estate-news

<!-- RECENT_CONTENT_END -->
