---
title: "The Computational Wall: Why the Defense Trilemma and the NP-Hardness of Reward Hacking Detection Demand a New Security Posture for AI"
source: ken-huang-ai-expert
url: https://kenhuangus.substack.com/p/the-computational-wall-why-the-defense
date: 2026-05-02
type: rss
---

AI security faces a mathematical crisis where the most common defenses cannot work as designed, and the fallback strategy of monitoring for reward hacking runs into computational impossibility walls. Three separate mathematical proofs—covering wrapper defenses, reward hacking detection, and alignment completeness—converge on the same conclusion: the engineering goal must shift from elimination to management of bounded, characterized failure.

---

- **Defense Trilemma Reality** The mathematical proof shows wrapper defenses around AI models cannot simultaneously maintain continuity, utility preservation, and completeness—topology guarantees some unsafe prompts will pass through unchanged, making "complete" filtering impossible by construction.

- **NP-Hard Detection Wall** Reward hacking detection is computationally intractable at scale, with semantic self-verification proven NP-complete and alignment to large value sets requiring exponential overhead, making uniform monitoring strategies fundamentally unscalable.

- **Training Alignment Paradox** Better training-time alignment is necessary to flatten safety boundaries but insufficient alone, as failure modes persist through fine-tuning and agentic systems can fail at architectural levels beyond model behavior.

- **Procurement Language Crisis** Current compliance requirements demanding "complete" defenses are mathematically impossible, forcing vendors to claim undeliverable guarantees and explaining inevitable failures as edge cases rather than structural properties.

- **Defense Architecture Imperative** Effective AI security requires uncorrelated defense layers with deterministic architectural mediation for consequential actions, not behavioral trust in model outputs for high-stakes decisions like code execution or financial transactions.

- **Continuous Monitoring Mandate** AI security must adopt continuous process frameworks similar to SOC 2 rather than one-shot certifications, focusing monitoring resources on safety-critical slices rather than attempting uniform coverage.

- **Policy Realignment Needed** Regulators must treat training-time alignment as critical infrastructure, require correlation analysis of defense layers, and mandate architectural mediation for consequential actions in critical deployments.
