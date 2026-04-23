---
title: "Chapter 5: Tool Orchestration and Execution (Claude Code vs. Hermes Agent)"
source: ken-huang-ai-expert
url: https://kenhuangus.substack.com/p/chapter-5-tool-orchestration-and
date: 2026-04-22
type: rss
---

Claude Code's execution model balances speed with safety through explicit per-tool concurrency declarations, while Hermes Agent opts for global heuristics that may sacrifice some precision for broader tool compatibility without modification.

---

- **Concurrency Safety Architecture** - Claude Code requires each tool to implement `isConcurrencySafe()` with parsed inputs, enabling granular decisions. Hermes uses global tool name sets plus path-overlap detection, making it easier to add tools but potentially less precise for edge cases.

- **Execution Flow Control** - Claude Code partitions tool sequences into alternating concurrent/serial batches, allowing fast reads followed by safe writes. Hermes makes a single parallel/serial decision per batch, which may serialize unnecessarily when mixed operations could be optimized.

- **Context Propagation** - Claude Code immediately applies context changes (like directory switches) in serial batches while deferring them in concurrent ones. Hermes doesn't differentiate context handling by execution mode, potentially missing state dependencies.

- **Streaming Integration** - Claude Code's `StreamingToolExecutor` begins running tools as their blocks arrive during model streaming, reducing perceived latency. Hermes waits for complete tool batches before execution decisions.

- **Error Recovery** - Claude Code generates synthetic `tool_result` blocks for interrupted executions via `yieldMissingToolResultBlocks`, maintaining conversation consistency. Hermes relies on ThreadPoolExecutor exception capture without explicit conversation repair.

- **Resource Management** - Hermes provides superior background process tracking through `ProcessRegistry` with output buffering and automatic completion notifications. Claude Code appears to handle processes more ephemerally within individual tool executions.

- **Production Considerations** - Claude Code's explicit safety contracts make it more suitable for environments where tool interactions are well-understood. Hermes' heuristic approach works better for rapidly evolving tool sets where declaring safety properties per tool is impractical.
