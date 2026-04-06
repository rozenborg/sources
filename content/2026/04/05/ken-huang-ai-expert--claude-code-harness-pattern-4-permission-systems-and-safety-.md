---
title: "Claude Code Harness Pattern 4: Permission Systems and Safety Guardrails"
source: ken-huang-ai-expert
url: https://kenhuangus.substack.com/p/claude-code-harness-pattern-4-permission
date: 2026-04-05
type: rss
---

The permission system is the critical safety layer that determines whether Claude's tools can execute, using multiple operational modes that balance automation with human oversight. This system routes tool execution requests through different approval mechanisms based on deployment context — from fully interactive approval to automated classification to plan-based authorization.

---

- **Multi-mode architecture** supports five permission strategies: default (interactive approval), auto (classifier-based), plan (pre-approve strategy), acceptEdits (code-focused), and bubble (inherit parent permissions)

- **Permission context inheritance** enables workspace isolation through additionalWorkingDirectories and rule precedence by source (config, user, org, classifier), maintaining consistent security boundaries across agent hierarchies

- **Central evaluation pipeline** routes all tool executions through canUseTool function, which evaluates against full permission context and returns allow/deny/ask decisions with audit metadata

- **Rule-based overrides** allow organizations to define alwaysAllow, alwaysDeny, and alwaysAsk patterns that can bypass default mode behavior for specific tools or operations

- **Background agent support** uses shouldAvoidPermissionPrompts flag to route decisions away from interactive dialogs, enabling autonomous operation without user interruption

- **Coordinator integration** implements awaitAutomatedChecksBeforeDialog for multi-agent systems where centralized permission management waits for automated security checks before user prompts

- **Plan mode workflow** requires upfront strategy approval then enables autonomous execution within approved scope, with prePlanMode field supporting return to previous permission state after completion
