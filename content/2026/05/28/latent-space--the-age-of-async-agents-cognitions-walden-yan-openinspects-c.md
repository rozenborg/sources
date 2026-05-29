---
title: "The Age of Async Agents — Cognition's Walden Yan & OpenInspect's Cole Murray"
source: latent-space
url: https://www.latent.space/p/cognition
date: 2026-05-28
type: podcast
---

AI agents have evolved from in-IDE assistants to autonomous background systems that can handle complete development workflows from specification to pull request, with Devin's commits jumping from 16% to 80% of Cognition's codebase since January and the company seeing 7x growth in merged PRs following December's model capability leap.

---

- **Model inflection point** - December 2024 models (Claude Opus 4.5, GPT 5.2) reached autonomous capability threshold enabling "spec to pull request" workflows with minimal human intervention

- **Architecture debate** - "Harness in the box" vs "out of the box" designs, with security concerns favoring separation of the AI "brain" from execution environments to prevent secret exfiltration

- **Repository setup challenge** - Getting agents properly configured with dependencies, credentials, and working environments remains the hardest technical problem for deployment

- **Infrastructure complexity** - Background agents require full VMs rather than containers, with fast snapshot/restore capabilities, proper secret scoping, and multi-platform support for real application testing

- **Business model tension** - Open source creators struggle to monetize $20/seat products while competing with managed services, leading some to focus on consulting rather than SaaS

- **Enterprise adoption** - Companies need significant onboarding support, integration work, and cultural change management to successfully deploy autonomous coding agents at scale

- **Code quality concerns** - Pure autonomous coding without review processes leads to codebase degradation within 2 weeks, requiring AI-native linting and review systems

- **Hybrid workflows emerging** - Tools like Windsurf 2.0 enable handoffs between local foreground agents and cloud background agents, expanding use cases beyond engineering to PM and SRE workflows
