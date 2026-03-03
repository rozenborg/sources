---
title: "Claude Code Security"
source: anthropic-blog
url: https://www.anthropic.com/news/claude-code-security
date: 2026-02-20
type: sitemap
---

Anthropic launches Claude Code Security, an AI-powered vulnerability scanner that reads and reasons about code like human security researchers, capable of finding complex logic flaws and access control issues that traditional rule-based tools miss. The company claims their AI has already discovered over 500 previously undetected vulnerabilities in production open-source codebases, some hidden for decades.

---

- **AI-powered static analysis** - Goes beyond pattern matching to understand component interactions and data flow, catching business logic flaws and broken access controls that rule-based scanners miss
- **Multi-stage verification** - Each finding undergoes automated re-examination to filter false positives, with severity ratings and confidence scores to help teams prioritize fixes
- **Proven track record** - Anthropic's team found 500+ vulnerabilities in production open-source code using Claude Opus 4.6, representing decades-old bugs that escaped expert review
- **Human-in-the-loop workflow** - All patches require developer approval through a dashboard interface, with Claude suggesting fixes but never auto-applying changes
- **Limited research preview** - Available now to Enterprise and Team customers with expedited free access for open-source maintainers to refine capabilities
- **Defensive urgency** - Anthropic warns attackers will use similar AI capabilities to find exploits faster, positioning this as a defensive tool to patch vulnerabilities before they're exploited
- **Integration advantage** - Built into existing Claude Code platform, allowing teams to review findings and iterate on fixes within familiar development workflows
