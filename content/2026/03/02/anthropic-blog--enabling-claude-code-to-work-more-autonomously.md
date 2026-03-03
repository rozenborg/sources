---
title: "Enabling Claude Code To Work More Autonomously"
source: anthropic-blog
url: https://www.anthropic.com/news/enabling-claude-code-to-work-more-autonomously
date: 2026-03-02
type: sitemap
---

Anthropic has transformed Claude Code into a more autonomous development platform with native VS Code integration, checkpointing for safe task delegation, and advanced features like subagents and background processing that enable parallel development workflows. The upgrades position Claude Code to handle complex, multi-step development projects while maintaining developer control through automatic rollback capabilities.

---

- **VS Code Extension Launch** Native IDE integration in beta provides real-time change visualization through sidebar panels with inline diffs, expanding beyond terminal-only usage
- **Checkpoint System** Automatic code state saves before each change with instant rollback via Esc or /rewind command, enabling safe delegation of ambitious refactoring and exploration tasks  
- **Subagent Architecture** Parallel task execution allows simultaneous frontend/backend development or specialized workflow delegation within single projects
- **Background Process Management** Long-running tasks like dev servers operate independently without blocking Claude's progress on other development work
- **Enhanced Terminal Interface** Improved status visibility and searchable prompt history (Ctrl+r) for better command reuse and editing capabilities
- **Claude Agent SDK Expansion** Renamed platform now supports custom agentic experiences with subagent and hooks functionality for specialized use cases like compliance and security
- **Sonnet 4.5 Integration** More powerful underlying model becomes default, enabling handling of longer and more complex development tasks across all surfaces
