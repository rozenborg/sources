---
title: "Claude Code Harness Pattern 2: Tool Architecture and the Tool Contract"
source: ken-huang-ai-expert
url: https://kenhuangus.substack.com/p/claude-code-harness-pattern-2-tool
date: 2026-04-03
type: rss
---

The Claude Code harness establishes a comprehensive tool interface that serves as the critical contract between AI models and external capabilities, enabling type-safe validation, behavioral optimization, and permission controls while maintaining clean separation between model reasoning and harness execution.

---

- **Tool Identity Management** The interface uses name, aliases, and searchHint fields to enable tool discovery and backward compatibility, with aliases supporting renamed tools and searchHints enabling keyword-based tool discovery in large tool sets.

- **Execution Pipeline** The call method receives validated input, execution context, recursive tool access, parent message attribution, and progress callbacks, returning structured ToolResult objects that can modify conversation state and context.

- **Dynamic Documentation** The description method generates context-aware tool descriptions for system prompts, varying based on input parameters, session type, and available permissions to optimize model tool selection.

- **Type-Safe Validation** Zod schemas in inputSchema and outputSchema fields provide runtime validation and compile-time typing, with optional JSON schema export for model consumption and structured input validation.

- **Behavioral Properties** Methods like isConcurrencySafe, isReadOnly, and isDestructive enable the harness to make intelligent execution decisions about parallel execution, caching, and safety controls without understanding tool internals.

- **Permission Integration** The checkPermissions method validates tool usage against user permissions and context, returning structured PermissionResult objects that can deny, allow, or request user confirmation for tool execution.

- **Presentation Layer** User-facing methods like userFacingName and render functions separate internal tool mechanics from user interface concerns, enabling consistent tool presentation across different interaction contexts.
