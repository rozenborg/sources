---
title: "Chapter 2: Tool Architecture and the Tool Contract (Claude Code vs. Hermes Agent)"
source: ken-huang-ai-expert
url: https://kenhuangus.substack.com/p/chapter-2-tool-architecture-and-the
date: 2026-04-19
type: rss
---

Claude Code enforces tool safety through compile-time types and conservative defaults, while Hermes relies on runtime registration and global concurrency rules. Claude's approach catches integration errors during development, but Hermes offers more deployment flexibility through dynamic tool availability and configuration-driven limits.

---

- **Type Safety Philosophy** - Claude Code uses Zod schemas for both TypeScript inference and runtime validation, catching tool integration bugs at compile time. Hermes uses JSON Schema for runtime-only validation, relying on careful handler implementation.

- **Concurrency Control** - Claude Code makes each tool declare its safety properties via methods that can inspect input parameters. Hermes uses global frozen sets that categorize tools by safety class, with special handling for path-scoped operations.

- **Default Safety Posture** - Claude Code's `TOOL_DEFAULTS` assume every tool is serial, stateful, and requires permission checks unless explicitly overridden. Hermes requires developers to manually add tools to the `_PARALLEL_SAFE_TOOLS` set to enable concurrency.

- **Dynamic Availability** - Hermes tools can conditionally appear based on environment state through `check_fn` callbacks, silently omitting unavailable tools from the model's schema. Claude Code tools are statically available once registered.

- **Permission Architecture** - Claude Code implements a two-layer system where general permissions run first, then tool-specific `checkPermissions` methods can override or modify the decision. Hermes handles permissions globally without per-tool customization hooks.

- **Context Overflow Protection** - Both systems guard against large outputs consuming context windows, but Claude Code's `maxResultSizeChars` saves overflow to files while Hermes' `_DEFAULT_MAX_READ_CHARS` returns error messages with pagination hints.

- **Deployment Trade-offs** - Choose Claude Code for type-safe development environments where catching tool contract violations early matters. Choose Hermes for production deployments requiring runtime tool availability decisions and configuration-driven limits.
