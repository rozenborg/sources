---
title: "Chapter 13: MCP Integration — Connecting Agents to the World (Claude Code vs. Hermes Agent)"
source: ken-huang-ai-expert
url: https://kenhuangus.substack.com/p/chapter-13-mcp-integration-connecting
date: 2026-04-30
type: rss
---

MCP integration represents a critical infrastructure decision for enterprise AI agents, with Claude Code and Hermes taking fundamentally different architectural approaches that reflect their respective runtime environments. Claude Code treats MCP as a first-class citizen with TypeScript-native async handling, while Hermes solves the complex threading challenge of running async MCP protocols from synchronous Python with sophisticated reconnection and credential safety features.

---

- **Connection Architecture** Claude Code instantiates MCP clients at session start and injects them directly into the QueryEngine constructor, making MCP servers a required dependency. Hermes runs a dedicated daemon thread with its own asyncio event loop, bridging sync agent calls to async MCP protocols via thread-safe coroutine scheduling.

- **Tool Discovery and Namespacing** Both systems use prefixed naming but with different separators - Claude Code uses `mcp__server__tool` with double underscores, while Hermes uses `mcp_server_tool` with single underscores. Claude Code refreshes tool lists dynamically when servers send change notifications mid-conversation.

- **Credential Security** Hermes implements comprehensive credential stripping using compiled regex patterns that redact GitHub tokens, API keys, Bearer tokens, and other sensitive data from error messages before they reach the LLM. Claude Code relies on TypeScript's type safety but lacks explicit credential sanitization.

- **Server-Initiated LLM Requests** Hermes supports the full MCP sampling specification through its SamplingHandler class, allowing MCP servers to request LLM completions with rate limiting (configurable RPM), model selection, and thread-based execution. Claude Code's implementation status for sampling requests is not detailed in the source material.

- **Failure Recovery** Hermes implements exponential backoff reconnection (1s to 60s, max 5 attempts) with individual server failure isolation - one server failing doesn't impact others. Claude Code's failure handling appears less robust, with connections tied to session lifecycle.

- **Sub-Agent Dependencies** Claude Code's AgentTool type includes `requiredMcpServers` field, allowing sub-agents to declare MCP dependencies that the coordinator ensures are connected before spawning. This provides clean dependency management for multi-agent workflows.

- **Production Readiness** Hermes shows more enterprise-focused features including configurable timeouts, environment variable interpolation, safe environment handling for subprocess spawning, and comprehensive error handling. Claude Code prioritizes developer experience with cleaner integration patterns.
