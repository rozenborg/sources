---
title: "Designing Hermes Agent from Scratch: A Systems Deep Dive"
source: ken-huang-ai-expert
url: https://kenhuangus.substack.com/p/designing-hermes-agent-from-scratch
date: 2026-06-08
type: rss
---

OpenAI's new Hermes Agent represents a fundamental shift from traditional chatbots to a production-grade agent runtime built around a persistent control loop that enforces strict boundaries between language model reasoning and actual system effects. The architecture demonstrates how to build reliable, scalable AI agents through SQLite-backed persistence, tiered prompt caching, isolated subagent spawning, and comprehensive guardrails that can handle everything from CLI sessions to multi-platform gateways without breaking down.

---

- **Control Loop Architecture** - Hermes inverts typical agent design by making the execution loop the core product, with tools as registered data rather than hardcoded functions, enabling session persistence across restarts and multiplexing across platforms like Telegram, Discord, and Slack

- **Three-Tier Prompt Strategy** - System prompts split into stable (identity, tools, behavioral rules), context (project files, caller messages), and volatile (memory, timestamps) tiers to maintain provider-side prefix cache efficiency while allowing dynamic content updates

- **Independent Iteration Budgets** - Each agent gets thread-safe iteration limits (90 for parents, 50 for subagents) that operate independently rather than sharing counters, allowing delegation without starving parent sessions while preventing runaway execution

- **Tool Registry with AST Discovery** - Tools self-register at import time through AST scanning of the tools directory, with toolsets providing curatorial filtering for security (read-only bots), economics (fewer schemas), and subagent contracts rather than separate codebases

- **SQLite as Memory Bus** - SessionDB provides WAL-mode concurrent access with FTS5 search, parent/child session linking for compression lineage, and source tagging across platforms, replacing fragile JSONL approaches that fail under gateway concurrency

- **Subagent Isolation Model** - delegate_task spawns fresh AIAgent instances with restricted toolsets, clean history, and separate budgets, returning only final results while maintaining intermediate traces in isolated sessions for security and debugging

- **Production Guardrails Throughout** - Comprehensive error handling includes retry state resets per turn, empty content guards, surrogate sanitization, tool approval hooks, and budget refunds for programmatic operations, addressing failure modes that break prototype agents in production

- **SOC Application Blueprint** - The architecture maps directly to Security Operations Centers with tiered toolsets (triage/investigate/respond), evidence lineage through session IDs, human-in-loop approvals for destructive actions, and parallel IOC enrichment through delegation patterns
