---
title: "Found from Claude Code: Chapter 1: The Harness Paradigm"
source: ken-huang-ai-expert
url: https://kenhuangus.substack.com/p/found-from-claude-code-chapter-1
date: 2026-04-02
type: rss
---

The Claude Code harness paradigm redefines production AI deployment from a model-centric to a system-centric approach, where the infrastructure layer between the language model and external world becomes the critical control mechanism. Rather than focusing on making models smarter, the harness constrains and directs model capabilities through structured tools, permission systems, and state management to ensure reliable and safe outcomes.

---

- **Control over intelligence**: The fundamental shift from improving model output to building control systems around models, where the harness provides reliability and safety regardless of the underlying model's capabilities

- **Five core challenges addressed**: Action space constraint through structured tools, conversation state management across multiple turns, safety enforcement via permissions, graceful failure handling, and resource optimization including cost and token management

- **QueryEngine architecture**: The central harness component maintains persistent state including conversation history (mutableMessages), cancellation controls (abortController), permission audit trails (permissionDenials), and usage tracking (totalUsage)

- **Async generator pattern**: The streaming response mechanism through AsyncGenerator enables real-time user feedback and responsive AI systems rather than blocking operations

- **Permission-first safety model**: Every action requires explicit evaluation against user permissions, safety classifiers, and operational context before execution, with all denials logged for system improvement

- **Production reliability focus**: Network failures, API errors, and unexpected outputs are treated as expected conditions requiring systematic detection, recovery attempts, and clear error surfacing

- **Resource management imperative**: Token budgets and API costs are first-class concerns requiring active tracking, conversation compaction, and user budget enforcement at the infrastructure level
