---
title: "Designing Agentic AI Systems with the ORCHIDEAS Framework"
source: ken-huang-ai-expert
url: https://kenhuangus.substack.com/p/designing-agentic-ai-systems-with
date: 2026-05-22
type: rss
---

ORCHIDEAS presents a secure-by-construction framework for building agentic AI systems that embeds security as structural architectural invariants rather than bolt-on checks, addressing the fundamental vulnerability that AI agents can be steered by adversarial inputs while making autonomous decisions with potentially high-consequence outcomes. The framework integrates with the Cloud Security Alliance's MAESTRO threat modeling to provide both design structure and threat coverage for production AI agent deployments targeting Level 1-2 autonomy.

---

- **Architectural Philosophy** - Security becomes a structural property of the system rather than runtime checks, where violating security invariants requires explicitly bypassing architecture rather than simply failing to add a validation layer

- **Nine-Pillar Design Sequence** - Implementation follows A-I-D-C-R-H-O-E-S order (Autonomy, Identity & Intent, Data governance, Context, Runtime, Human oversight, Observability, Evaluation, Scalability) while using ORCHIDEAS as mnemonic for completeness checking

- **Identity Innovation** - Introduces Intent-Based Access Control (IBAC) that requires actions to trace back to attested intent tokens, addressing the "uncanny valley" where agents are workloads by execution but human-like in decision-making

- **Autonomy Stratification** - Establishes five-level autonomy model analogous to autonomous vehicle classifications, with most production deployments targeting Level 1-2 with explicit boundaries enforced by interface design rather than policy checks

- **Data Lifecycle Coverage** - Addresses full agent data pipeline from training data lineage through RAG corpus governance to agent memory persistence, with classification propagation ensuring derived data inherits source restrictions

- **Defense Integration** - Maps each pillar to established security principles (Saltzer-Schroeder, zero trust, capability-based security) and MAESTRO threat layers, preventing novel attack vectors like RAG corpus poisoning and autonomy creep

- **Compositionality Requirement** - Ensures secure components compose into secure systems with predictable emergent properties, critical for multi-agent environments where component interactions can create unexpected authorization paths
