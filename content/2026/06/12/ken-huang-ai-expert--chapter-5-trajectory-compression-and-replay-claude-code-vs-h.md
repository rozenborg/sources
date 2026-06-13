---
title: "Chapter 5: Trajectory Compression and Replay (Claude Code vs. Hermes Agent)"
source: ken-huang-ai-expert
url: https://kenhuangus.substack.com/p/chapter-5-trajectory-compression
date: 2026-06-12
type: rss
---

Claude Code's append-only JSONL approach embeds compression into the live session through selective field stripping and byte-level dead-branch excision, making 150MB session files resume in under 10ms. Hermes separates concerns entirely, using a post-hoc batch compressor that calls auxiliary LLMs to summarize the compressible middle of completed trajectories, achieving higher compression ratios at the cost of API calls and semantic fidelity.

---

- **Compression timing divergence** Claude Code performs structural compression during the session (field stripping, progress message filtering, compaction boundaries as inline system messages) while Hermes uses post-session semantic compression via auxiliary LLM calls to summarize trajectory middles

- **Storage architecture trade-offs** Claude Code's append-only JSONL with byte-level pre-filtering enables sub-10ms loads of 150MB files but leaves dead branches on disk forever, while Hermes's clean ShareGPT format optimizes for HuggingFace dataset consumption and fine-tuning pipelines

- **Replay vs consumption patterns** Claude Code's loadTranscriptFromFile serves production resume scenarios where sessions continue mid-flight, while Hermes's compressed trajectories primarily feed training loops and evaluation harnesses rather than operational continuation

- **Compression strategy fundamentals** Claude Code achieves lossless structural compression through deterministic surgery (no LLM calls), while Hermes achieves higher ratios by replacing 20+ tool call turns with 750-token summaries via cheap models like Gemini Flash

- **Head-tail protection policies** Both systems preserve trajectory anchors but differ in granularity - Claude Code uses compaction boundaries with preserved segments, while Hermes protects first occurrence of each role plus last N turns with explicit token budgeting

- **Auditability surfaces** Claude Code preserves rich per-message metadata for session fidelity, while Hermes attaches compression_metrics blocks (tokens saved, compression ratio, compressed region indices) optimized for post-hoc analysis

- **Production applicability** Use Claude Code's approach for interactive, long-lived sessions requiring resume capability; use Hermes's approach when trajectories serve as training artifacts or audit records with fixed downstream consumers

- **Defensive cyber use case** 90-iteration threat hunts compress from ~180K to ~8K tokens by preserving IOC alerts verbatim, summarizing routine recon tool calls, and maintaining remediation decisions while tagging MITRE ATT&CK techniques
