---
title: "Chapter 4: Permission Systems and Safety Guardrails (Claude Code vs. Hermes Agent)"
source: ken-huang-ai-expert
url: https://kenhuangus.substack.com/p/chapter-4-permission-systems-and
date: 2026-04-21
type: rss
---

Hermes' regex-based safety checking is fast but fragile, while Claude Code's multi-layered permission system with ML classifiers and organizational controls is built for production deployments where blocking rm -rf /* matters more than millisecond response times. The architectural difference reveals itself most clearly in multi-agent scenarios where Hermes relies on TUI threading locks while Claude Code delegates permissions hierarchically through coordinator nodes.

---

- **Detection Approach** Claude Code uses ML classifiers with confidence scoring plus static rules, while Hermes relies on 30+ hardcoded regex patterns that can be bypassed through Unicode obfuscation despite normalization attempts

- **Multi-Agent Coordination** Claude Code implements hierarchical delegation where swarm workers inherit parent permissions and coordinators centralize approval decisions, versus Hermes' threading locks that serialize approval prompts but don't prevent permission escalation

- **Organizational Controls** Claude Code enforces org-level policies that users cannot override (org > user > config > classifier priority), while Hermes stores all approvals in user-controlled config.yaml files with no administrative enforcement layer

- **Permission Granularity** Claude Code offers five distinct modes from fully interactive to fully automated with plan-based approval workflows, compared to Hermes' binary dangerous/safe classification with three storage scopes (once/session/permanent)

- **Bypass Resistance** Claude Code's classifier can catch novel attack patterns and novel phrasings of dangerous commands, while Hermes' static regex approach requires manual pattern updates for each new evasion technique discovered

- **Production Readiness** Claude Code includes audit logging, decision provenance tracking, and coordinator mode for headless deployments, versus Hermes' TUI-centric design that breaks in containerized environments where approval dialogs cannot render

- **Performance vs Safety Tradeoff** Hermes prioritizes sub-millisecond regex matching over comprehensive coverage, suitable for development environments, while Claude Code's multi-stage pipeline optimizes for zero false negatives in production scenarios where escaped destructive commands have business impact
