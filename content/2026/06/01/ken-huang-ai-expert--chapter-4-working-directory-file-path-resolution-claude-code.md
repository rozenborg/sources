---
title: "Chapter 4: Working Directory & File-Path Resolution (Claude Code vs. Hermes Agent)"
source: ken-huang-ai-expert
url: https://kenhuangus.substack.com/p/chapter-4-working-directory-and-file
date: 2026-06-01
type: rss
---

Claude Code uses global state with AsyncLocalStorage overrides while Hermes uses per-environment Python objects to solve working directory resolution, but both harnesses face the same fundamental challenge: maintaining consistent file path interpretation across hundreds of tool calls when LLMs produce relative paths that must be resolved to absolute filesystem locations before any syscall executes.

---

- **Path Resolution Pipeline** Both systems funnel every model-generated path through a single expansion function that handles tilde notation, platform-specific formatting, and Unicode normalization before filesystem access

- **Concurrent Agent Isolation** Claude Code leverages AsyncLocalStorage to give each parallel subagent its own working directory context, while Hermes uses per-environment objects to prevent agents from interfering with each other's filesystem state

- **Shell State Persistence** Both harnesses inject `pwd -P` markers after bash commands to reconstruct persistent shell state across subprocess boundaries, since each command runs in a fresh shell that doesn't preserve directory changes

- **Symlink Canonicalization** Critical security measure where both systems resolve symlinks to physical paths using `realpathSync`/`pwd -P` to ensure permission checks operate on actual filesystem locations rather than symbolic references

- **Sandbox Boundary Enforcement** Automatic cwd reset mechanisms detect when agents navigate outside allowed directories and silently restore them to the original anchor directory without breaking the user experience

- **Unicode Normalization Defense** Both systems apply NFC normalization to handle macOS APFS returning NFD filenames while user input is typically NFC, preventing false path mismatches that would break permission validation

- **Defensive Filesystem Access** Protection against blocking operations through pre-flight checks for FIFOs, sockets, and special devices that could hang the harness indefinitely during path resolution

- **Implementation Trade-offs** Claude Code's approach requires more complex state management but provides finer concurrency control, while Hermes' per-environment design is simpler but less flexible for advanced parallel agent scenarios
