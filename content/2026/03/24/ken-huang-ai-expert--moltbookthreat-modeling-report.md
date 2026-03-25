---
title: "MoltbookThreat Modeling Report"
source: ken-huang-ai-expert
url: https://kenhuangus.substack.com/p/moltbookthreat-modeling-report
date: 2026-03-24
type: rss
---

The Moltbook-OpenClaw ecosystem represents a catastrophic failure of AI agent security, with over 1.6 million agents compromised through multiple attack vectors including supply chain poisoning, database breaches, and fundamental architectural vulnerabilities that remain unpatched despite acquisitions by OpenAI and Meta. The 1,184 malicious skills in the ClawHavoc campaign and nine disclosed CVEs demonstrate that rapid AI agent adoption has far outpaced security controls, creating systemic risks across the entire autonomous agent landscape.

---

- **Supply Chain Compromise** ClawHavoc campaign infiltrated 1,184+ malicious skills across ClawHub with only basic GitHub account requirements, affecting ~300,000 users through Atomic macOS Stealer payloads and demonstrating complete absence of code review controls

- **Database Breach Impact** Supabase misconfiguration exposed 1.5 million API tokens, 35,000 email addresses, and 4,060 private conversations containing plaintext OpenAI/Anthropic keys, amplifying credential theft across the agent ecosystem

- **Persistent Memory Exploitation** OpenClaw's SOUL.md and MEMORY.md files enable attackers to convert point-in-time exploits into permanent behavioral modifications, allowing delayed execution attacks that persist across agent sessions indefinitely

- **Critical RCE Vulnerability** CVE-2026-25253 (CVSS 8.8) provides one-click remote code execution through Cross-Site WebSocket Hijacking, with public exploit code enabling container escape and arbitrary command execution via malicious URLs

- **Indirect Prompt Injection Vector** Moltbook posts function as attack vectors for visiting agents, with cybersecurity researchers identifying the platform as a "lethal trifecta" combining private data access, untrusted content exposure, and external communication capabilities

- **Acquisition Response Inadequate** Despite OpenAI acquiring Steinberger and Meta acquiring Moltbook, fundamental architectural risks remain unaddressed, with current mitigations like VirusTotal scanning treating symptoms rather than root causes

- **Agent-to-Human Ratio Anomaly** The 88:1 bot-to-human ratio (1.6M agents, 17K owners) suggests either massive automation or artificial inflation, indicating potential manipulation of adoption metrics that influenced acquisition decisions
