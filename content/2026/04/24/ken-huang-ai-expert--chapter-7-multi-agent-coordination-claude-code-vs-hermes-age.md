---
title: "Chapter 7: Multi-Agent Coordination (Claude Code vs. Hermes Agent)"
source: ken-huang-ai-expert
url: https://kenhuangus.substack.com/p/chapter-7-multi-agent-coordination
date: 2026-04-24
type: rss
---

Multi-agent coordination breaks the single-context ceiling by decomposing complex tasks into parallel, specialized execution streams with isolated state management. Claude Code optimizes for cache efficiency and filesystem isolation through git worktrees, while Hermes focuses on thread-based parallelism with interrupt propagation and depth limiting to prevent runaway delegation trees.

---

- **Cache optimization strategy** Claude Code's fork mode passes the parent's rendered system prompt directly to children, enabling API-level cache reuse, while Hermes constructs fresh AIAgent instances per child with independent token budgets

- **Isolation mechanisms** Claude Code uses git worktrees for filesystem isolation that auto-cleanup when unchanged, whereas Hermes relies on thread separation with six different execution backends (local, Docker, SSH, Modal, Daytona, Singularity)

- **Interrupt handling** Hermes maintains `_active_children` lists with lock-based interrupt cascading down delegation trees, while Claude Code races agent iterators against background promotion signals for mid-execution state changes

- **Delegation constraints** Both systems prevent infinite nesting - Claude Code enforces flat team rosters where teammates cannot spawn teammates, Hermes uses `MAX_DEPTH = 2` with `_delegate_depth` tracking

- **Parallel execution models** Claude Code supports five coordination modes (fork, worktree, async, SendMessage routing, teammate constraints) while Hermes caps concurrent children at 3 via ThreadPoolExecutor with batch completion tracking

- **Model aggregation capability** Hermes uniquely offers mixture-of-agents pattern that fans identical queries to multiple frontier models (claude-opus, gemini-pro, gpt-5, deepseek) then synthesizes responses through a dedicated aggregator

- **Architectural trade-off** Claude Code optimizes for UI responsiveness and cache efficiency in TypeScript/React context, while Hermes prioritizes Python-native threading with robust error handling and diverse execution environments

- **Use case alignment** Choose Claude Code for cache-sensitive workflows requiring filesystem isolation, choose Hermes for CPU-intensive parallel processing or when you need model diversity through mixture-of-agents coordination
