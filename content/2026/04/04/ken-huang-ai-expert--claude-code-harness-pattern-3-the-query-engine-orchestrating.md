---
title: "Claude Code Harness Pattern 3: The Query Engine — Orchestrating AI Conversations"
source: ken-huang-ai-expert
url: https://kenhuangus.substack.com/p/claude-code-harness-pattern-3-the
date: 2026-04-04
type: rss
---

The QueryEngine is Claude Code's central conversation orchestrator, implementing a sophisticated infinite loop that processes user messages, streams model responses, executes tools, and manages state across multi-turn conversations. Its async generator architecture enables real-time streaming while sophisticated error recovery strategies including context collapse, reactive compaction, and escalation ensure resilience against common failure modes like token limits.

---

- **Core Architecture** - QueryEngine maintains conversation state through mutableMessages array, tracks token usage/costs, and orchestrates the infinite query loop that handles request-response cycles until terminal conditions are met

- **Streaming Design** - Uses async generators to yield incremental results rather than blocking, enabling real-time text streaming, progress updates, and responsive user experience during long tool executions

- **Error Recovery Hierarchy** - Implements layered recovery strategies: context collapse (cheapest, local), reactive compaction (API-based summarization), token limit escalation (64K retry), and multi-turn continuation for long responses

- **State Management** - Separates full conversation history (mutableMessages) from compacted API views, tracks recovery attempts to prevent infinite loops, and maintains rich message type hierarchy for different conversation events

- **Cost Controls** - Enforces token budgets, tracks cumulative usage across sessions, implements maximum turn limits, and provides fallback model handling when primary model fails

- **Tool Orchestration** - Partitions tool_use blocks into concurrent-safe batches, executes tools in parallel where possible, and feeds results back through the conversation loop until model indicates completion

- **Production Resilience** - Withholds recoverable errors from users during recovery attempts, provides comprehensive logging/telemetry, and ensures graceful degradation through multiple fallback mechanisms
