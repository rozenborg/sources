---
title: "Token Is All You Need: Finding 0days with LLMs and Agentic AI"
source: ken-huang-ai-expert
url: https://kenhuangus.substack.com/p/token-is-all-you-need-finding-0days
date: 2026-04-13
type: rss
---

Large language models have fundamentally democratized zero-day vulnerability discovery, with AI systems now finding more exploitable bugs in weeks than expert researchers previously discovered in entire careers. This shift has crossed from research curiosity to industrial-scale capability, as evidenced by AI systems discovering over 500 high-severity vulnerabilities in heavily audited codebases like Linux kernel and Firefox, plus 13 of 14 OpenSSL CVEs assigned in 2025.

---

- **Carlini Loop breakthrough** - Simple bash for-loop methodology that processes each source file independently with CTF-style prompting, achieving massive scale while avoiding human reviewer bias accumulation across codebases

- **Commercial AI security tools** - Anthropic's Claude Code Security found 22 Firefox vulnerabilities in one month (more than Mozilla's entire 2025 bounty program), while OpenAI's Codex Security discovered 11,000+ high-impact bugs across major projects in 30 days

- **Democratization evidence** - Independent researchers using $5 prompts are earning CVEs in Django and FastAPI, while AISLE autonomous system achieved 93% hit rate on OpenSSL vulnerabilities, signaling barrier-to-entry collapse from years of training to subscription access

- **Hybrid tooling emergence** - RAPTOR combines LLM reasoning with traditional tools (Semgrep, CodeQL, AFL++) through nine-stage analysis pipelines, including OSS forensics capabilities and automated crash analysis with deterministic replay debugging

- **False positive mitigation** - OpenAnt's five-stage verification funnel addresses LLMs' tendency to agree with vulnerability assertions, achieving 99.98% false positive elimination through progressive filtering before expensive LLM analysis

- **Scale and speed advantage** - AI systems process thousands of files in hours through parallelization while maintaining fresh analytical perspective per file, far exceeding human capacity and avoiding accumulated assumptions

- **Critical infrastructure impact** - Discovery of 23-year-old Linux kernel vulnerabilities and consistent findings in most security-tested codebases demonstrates AI capability against previously "exhaustively" audited systems
