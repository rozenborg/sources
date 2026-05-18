---
title: "Chapter 2: Cancellation & Abort Propagation (Claude Code vs. Hermes Agent)"
source: ken-huang-ai-expert
url: https://kenhuangus.substack.com/p/chapter-2-cancellation-and-abort
date: 2026-05-17
type: rss
---

Hermes chose a thread-scoped interrupt flag approach over AbortController because its tools execute in a fundamentally different environment than Claude Code's async JavaScript runtime. While Claude Code can thread abort signals through every async boundary using browser-native AbortController, Hermes tools run synchronously in thread-isolated Python contexts where cooperative polling is the only reliable cancellation mechanism.

---

- **Architecture divergence** Claude Code uses a push-based model with AbortController.signal propagating through async boundaries, while Hermes implements a pull-based system where tools poll a thread-scoped interrupt flag cooperatively

- **Resource leak prevention** Both systems ensure cancellation reaches every potential leak point - HTTP streams, spawned subprocesses, sub-agent trees, and permission dialogs - but Claude Code uses event listeners while Hermes relies on periodic flag checks

- **Child controller pattern** Claude Code creates hierarchical abort scopes using createChildAbortController with WeakRef memory management, enabling per-tool isolation where sibling errors don't poison entire sessions

- **Signal threading implementation** Claude Code passes abortController.signal as first-class parameters through every network-touching function, with post-await checks to discard completed but cancelled results

- **Subprocess termination** BashTool demonstrates proper cancellation by passing abort signals directly to exec(), ensuring kernel-level process kills follow automatically when users hit Ctrl-C

- **Cleanup orchestration** Graceful shutdown runs under bounded AbortSignal.timeout periods with failsafe timers, applying cancellation patterns recursively to the shutdown process itself

- **Reason propagation** Signal.reason field carries cancellation context ('interrupt', 'sibling_error', permission denials) across the abort tree, enabling downstream components to handle different cancellation types appropriately

- **Production reliability gap** The fundamental difference suggests Claude Code's event-driven approach may handle complex cancellation scenarios more reliably than Hermes's cooperative polling, especially under high concurrency or when tools fail to check interrupt flags frequently
