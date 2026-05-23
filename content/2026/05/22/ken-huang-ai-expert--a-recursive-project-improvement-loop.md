---
title: "A Recursive Project-Improvement Loop"
source: ken-huang-ai-expert
url: https://kenhuangus.substack.com/p/a-recursive-project-improvement-loop
date: 2026-05-22
type: rss
---

AI coding agents are evolving from producing disconnected code patches to building cumulative project intelligence, but most setups still lack the coordination systems needed to prevent conflicting edits, preserve decisions, and ensure each agent interaction improves the project for future work. Compound Orchestrator introduces a project-local operating model that transforms agent work from ephemeral chat sequences into a durable system of planning contracts, review gates, and compound learning.

---

- **Coordination bottleneck identified** - Modern agents can generate quality code but struggle with preventing conflicting edits, maintaining current documentation, and preserving design decisions beyond chat transcripts
- **Six HTML planning contracts** - The system uses browser-readable artifacts (PRD, users, architecture, planning, spec, test-cases) that serve as visible contracts reviewable by both humans and AI agents
- **Parallel drafting, serial integration** - Discovery agents work simultaneously on different planning documents, but spec acceptance and integration are deliberately serialized to prevent conflicts and ensure coherence
- **Two-round review enforcement** - Reviews require explicit author revisions and reviewer re-acceptance rather than one-pass feedback, ensuring review comments actually improve the work
- **README maintenance gates** - Every project interaction must update documentation to remove stale information and add current context, ensuring future agents start with accurate project understanding
- **Compound learning architecture** - Each agent interaction leaves behind better planning contracts, clearer ownership tracking, and durable decision records that make subsequent work more efficient
- **Open source implementation** - The Compound Orchestrator framework is publicly available on GitHub, providing immediate tooling for teams wanting to implement this coordination approach
