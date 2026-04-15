---
title: "Intent-Based Access Control(IBAC) for Coding Agents"
source: ken-huang-ai-expert
url: https://kenhuangus.substack.com/p/intent-based-access-controlibac-for
date: 2026-04-14
type: rss
---

Organizations deploying AI coding agents across departments face a critical blind spot: traditional access controls can't parse natural language intent, allowing an HR analyst's "clean up old files" to potentially trigger the same destructive infrastructure commands as a DevOps engineer's request. DistributedApps.ai has open-sourced agentctl, the first Intent-Based Access Control (IBAC) system that intercepts prompts, classifies semantic intent, and enforces policies based on meaning rather than keywords — preventing cross-departmental privilege escalation in agentic workflows.

---

- **Security Gap Identified** Multi-department adoption of coding agents (Claude Code, Gemini CLI, Cline) creates privilege escalation risks when natural language prompts from different roles execute identical destructive actions
- **IBAC Architecture** Four-layer control plane: natural language interception, LLM-powered intent classification, policy mapping via Cedar rules, and runtime enforcement before agent execution
- **Unified Policy Engine** Single governance layer normalizes heterogeneous tool calls across agent runtimes (Claude's "Read" = OpenClaw's "code_read" = canonical "read" action) enabling consistent security policies
- **Enterprise Compliance** Addresses audit blind spots by creating unified JSONL logging across all agent actions, critical for HIPAA, SOC 2, and PCI-DSS requirements in multi-agent environments  
- **Open Source Availability** Full implementation available at github.com/kenhuangus/agentctl with adapter support for major coding agents and Cedar policy examples for immediate deployment
- **Competitive Advantage** First-mover solution for enterprise agentic AI governance — organizations can establish mature access controls before competitors recognize the vulnerability
- **Implementation Priority** Deploy in development environments first using environment-based policies (dev/staging/prod) and time-based rules to validate intent classification accuracy before production rollout
