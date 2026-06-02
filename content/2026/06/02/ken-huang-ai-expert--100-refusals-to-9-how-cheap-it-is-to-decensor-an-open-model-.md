---
title: "100 Refusals to 9: How Cheap It Is to Decensor an Open Model — and Why That’s a Policy Problem"
source: ken-huang-ai-expert
url: https://kenhuangus.substack.com/p/100-refusals-to-9-how-cheap-it-is
date: 2026-06-02
type: rss
---

Open-weight AI models can now be stripped of safety guardrails in 44 minutes on a $400 laptop, with success rates dropping refusals from 100% to just 9% while preserving full model capabilities. This represents a fundamental shift from safety circumvention requiring expert data scientists to a simple automated process accessible to anyone with internet access and basic hardware.

---

- **Technical breakthrough confirmed** A reproduction on Intel integrated GPU validated that "abliteration" removes safety refusals by targeting a single mathematical direction in model activation space, achieving 91% refusal reduction with minimal capability loss (KL divergence 0.063)

- **Massive scale adoption** Over 6,000 abliterated models now exist on Hugging Face, up from 600 in 2024, indicating rapid mainstream adoption of safety-bypassing techniques across the open model ecosystem

- **Cost asymmetry crisis** Safety alignment training costs millions in compute and human feedback, while removing those protections requires essentially zero marginal cost and runs automatically on consumer hardware millions already own

- **Irreversible release problem** Unlike API-based models where companies retain control, open-weight models cannot be recalled once downloaded—creating permanent loss of oversight with no ability to monitor usage or enforce policies

- **Policy gap widening** Current regulatory frameworks assume controllable deployment, but abliteration exposes that meaningful governance exists only until the moment weights become public, forcing entirely new approaches to AI safety governance

- **Capability gap closing** Open models now trail leading closed models by less than one year according to international safety assessments, meaning this circumvention technique will soon apply to frontier-level AI systems

- **Dual-use enforcement challenge** The same mathematical techniques enabling beneficial research applications can be instantly repurposed for harm, with no technical method to distinguish legitimate research from malicious use cases post-release
