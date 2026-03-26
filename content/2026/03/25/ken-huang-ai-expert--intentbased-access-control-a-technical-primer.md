---
title: "Intent‑Based Access Control: A Technical Primer"
source: ken-huang-ai-expert
url: https://kenhuangus.substack.com/p/intentbased-access-control-a-technical
date: 2026-03-25
type: rss
---

Intent-Based Access Control shifts authorization from static "who can do what" role assignments to dynamic "for what purpose, under what conditions" validation that evaluates specific tasks against fine-grained resource constraints at runtime. This architectural change becomes critical as AI agents require granular permission controls that can't be hijacked even if the underlying LLM logic is compromised or misdirected.

---

- **Core paradigm shift** IBAC moves from subject:role authorization to subject:task:context tuples, asking "for this specific task and context, is this action over these resources allowed?" rather than broad role-based permissions

- **Runtime protection model** Even if LLM logic gets hijacked or mis-guided, the authorization engine still enforces only what was permitted by the original declared intent, creating a security boundary independent of AI behavior

- **Four-component technical stack** Minimal IBAC requires an intent parser (LLM/classifier), policy mapper (converts intents to authorization tuples), authorization engine (Cedar/OPA/OpenFGA), and tool gateway that blocks unauthorized calls

- **Lightweight ontology approach** Rather than requiring global unified ontologies, IBAC works with domain-specific vocabularies covering User/Agent, Task, Action, Resource, and Constraint entities with simple relations between them

- **Fine-grained constraint enforcement** System can express complex policies like "for clinical_note_review task, read table:patients where sensitivity=phi, max 100 rows, time_bound=15m, but no export/delete"

- **Zero-trust architecture enablement** IBAC provides the semantic backbone for least-privilege authorization in agentic AI systems where traditional perimeter-based security models fail

- **Policy evaluation at every tool call** Each agent action generates authorization tuples that get evaluated in real-time, preventing privilege escalation through prompt injection or model drift
