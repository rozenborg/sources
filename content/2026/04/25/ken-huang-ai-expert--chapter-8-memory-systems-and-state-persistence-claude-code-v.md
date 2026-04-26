---
title: "Chapter 8: Memory Systems and State Persistence (Claude Code vs. Hermes Agent)"
source: ken-huang-ai-expert
url: https://kenhuangus.substack.com/p/chapter-8-memory-systems-and-state
date: 2026-04-25
type: rss
---

Claude Code uses file-backed memory for portability and crash safety, while Hermes employs SQLite FTS5 for searchable episodic recall. Both systems reveal the critical distinction between working memory (current session), episodic memory (searchable history), and procedural memory (reusable skills), with complementary approaches that production agents need to combine.

---

- **Persistence Strategy** Claude Code uses eager flush to disk before API calls, ensuring user messages survive crashes even if the assistant response fails. Hermes uses SQLite WAL mode with jitter retry to handle write contention without convoy effects.

- **Memory Types** Both implement the three-layer memory model: working memory (conversation state), episodic memory (searchable past sessions), and procedural memory (skills/playbooks). Claude Code handles this with transcript files and CLAUDE.md attachments; Hermes uses FTS5 search and curated markdown files.

- **Cache Management** Claude Code maintains LRU file state caches that clone to child agents and propagate changes back to parents. Hermes uses frozen snapshots that never change mid-session to keep Anthropic prompt cache prefixes stable, saving 80-90% of input token costs.

- **Context Compaction** Claude Code writes "preserved tail" segments after compaction so resumed sessions can reconstruct post-compaction state correctly. Hermes prevents mid-session system prompt mutations to maintain cache stability across long conversations.

- **Search and Recall** Hermes implements two-stage recall: FTS5 finds matching messages, then Gemini Flash summarizes results focused on the query. Claude Code relies on automatic CLAUDE.md injection with deduplication across both LRU eviction and session-scoped path tracking.

- **Procedural Growth** Hermes can autonomously create new skills from experience, writing reusable skill files that future sessions discover. Claude Code focuses on curated memory attachments rather than self-expanding procedural knowledge.

- **Production Implications** File-based approaches offer portability and inspection benefits but lack search capabilities. Database approaches enable full-text search and structured queries but require more infrastructure. Production systems need hybrid approaches combining both patterns.
