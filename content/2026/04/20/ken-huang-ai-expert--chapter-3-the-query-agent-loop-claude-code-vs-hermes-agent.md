---
title: "Chapter 3: The Query / Agent Loop (Claude Code vs. Hermes Agent)"
source: ken-huang-ai-expert
url: https://kenhuangus.substack.com/p/chapter-3-the-query-agent-loop-claude
date: 2026-04-20
type: rss
---

Claude Code treats the agent loop as a sophisticated state machine with named transitions and predictive recovery, enabling granular error handling and real-time streaming that prevents infinite loops through explicit state tracking. Hermes Agent uses a simpler synchronous approach with shared budget enforcement across agent hierarchies, prioritizing resource control and deterministic termination over streaming responsiveness.

---

- **Loop Architecture** Claude Code implements an async generator with 7 named continuation points and explicit state transitions, while Hermes uses a synchronous while loop with dual gates (iteration count + shared budget)

- **Error Recovery Strategy** Claude Code employs predictive recovery with escalating strategies (collapse drain → reactive compact → token escalation → multi-turn recovery), whereas Hermes uses reactive exponential backoff retry loops within budget constraints

- **State Management** Claude Code maintains explicit transition reasons in state objects to prevent infinite loops and enable informed recovery decisions; Hermes relies on iteration counters and budget exhaustion as primary termination mechanisms

- **Streaming vs Batch** Claude Code yields events in real-time through async generators for responsive UX, while Hermes returns final results synchronously after completion

- **Resource Control** Claude Code handles resource pressure through context compression and token budget warnings; Hermes enforces hard limits through thread-safe shared budgets across parent-child agent hierarchies

- **Termination Logic** Claude Code uses model-signaled completion plus multiple recovery fallbacks; Hermes uses deterministic budget exhaustion plus user interrupt capability

- **Production Implications** Choose Claude Code for user-facing applications requiring real-time feedback and sophisticated error recovery; choose Hermes for batch processing, multi-agent coordination, and scenarios requiring strict resource governance

- **Debugging Capability** Claude Code's named transitions and state tracking provide superior post-mortem analysis; Hermes offers simpler linear execution traces with clear budget consumption patterns
