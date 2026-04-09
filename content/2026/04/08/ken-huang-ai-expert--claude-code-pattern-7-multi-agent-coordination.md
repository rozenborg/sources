---
title: "Claude Code Pattern 7: Multi-Agent Coordination"
source: ken-huang-ai-expert
url: https://kenhuangus.substack.com/p/claude-code-pattern-7-multi-agent
date: 2026-04-08
type: rss
---

The Claude harness uses AgentTool for complex multi-agent coordination, allowing intelligent delegation through multiple execution modes including fork subagents that inherit parent context, async background agents, and isolated worktree execution. This pattern enables sophisticated task decomposition where specialized agents can work in parallel while the system manages resource allocation, progress tracking, error handling, and inter-agent communication through a centralized orchestrator.

---

- **Execution Mode Routing** AgentTool supports sync subagents (blocking), async background agents (non-blocking), fork subagents (context inheritance), teammates (named routing), and remote agents (environment isolation) with automatic selection based on subagent_type parameter and feature flags

- **Resource Management** System handles full agent lifecycle including MCP server dependency checking with 30-second timeout, recursive fork prevention to avoid infinite nesting, and automatic cleanup of worktrees based on whether changes were made

- **Worktree Isolation** Agents can execute in isolated git worktrees with filesystem separation, automatic path translation notices for fork agents, and intelligent cleanup that preserves worktrees with changes while removing unchanged ones

- **Progress Coordination** Sync agents provide real-time progress updates with backgrounding hints after threshold, message forwarding between parent and child, and automatic transition to async execution if user triggers background mode

- **Context Inheritance Strategy** Fork subagents inherit parent's system prompt for API cache efficiency, receive full conversation history and tool access, and include worktree path translation notices when running in isolation

- **Inter-Agent Communication** Named agents register in agent name registry for SendMessage routing, async agents provide output file paths for result sharing, and team coordination enables ongoing collaboration between multiple agents

- **Error Handling & Recovery** Robust error handling for missing agent types, permission denials, failed MCP server connections, and abortion scenarios with proper cleanup and resource deallocation

- **Strategic Implications** This pattern enables complex AI workflows where specialized agents handle specific domains (coding, testing, research, analysis) while maintaining resource efficiency through context sharing and isolation boundaries
