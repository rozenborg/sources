---
title: "Chapter 3: The Slash Command System (Claude Code vs. Hermes Agent)"
source: ken-huang-ai-expert
url: https://kenhuangus.substack.com/p/chapter-3-the-slash-command-system
date: 2026-05-21
type: rss
---

Claude Code's slash command system represents the operational distinction between human-controlled harness functions and AI model interactions, with only one of three command types actually reaching the model for processing. This architectural choice prevents prompt injection attacks on critical system functions like session clearing and cost reporting while maintaining direct human control over the agent environment.

---

- **Three-tier command architecture** - Local commands (like /clear) execute side effects without touching the model, local-jsx commands (/help, /cost) render React modals, and prompt commands generate content blocks that get injected as synthetic user messages to the model

- **Security through isolation** - Two of three command types never cross the user-model boundary, making core harness functions immune to prompt injection since commands like /cost and /clear are processed entirely by the harness

- **Dynamic registry with lazy loading** - Commands are registered as metadata-only objects with lazy-loaded implementations, enabling fast startup times while supporting runtime visibility changes based on user authentication state

- **Plugin-friendly extensibility** - The system merges built-in commands with plugin commands, MCP commands, and dynamic skills through a unified Command[] array with automatic deduplication and ordering

- **Runtime adaptability** - Command visibility adapts to user state changes through getter functions rather than static values, allowing immediate UI updates when authentication or feature flags change

- **Operational control retention** - The slash system serves as the "operator's console" layer where humans maintain direct, model-bypassing control over session state and harness configuration

- **Implementation efficiency** - Uses discriminated unions for type safety and memoization for performance, with the registry functioning more as a lookup table than a traditional class-based registry system
