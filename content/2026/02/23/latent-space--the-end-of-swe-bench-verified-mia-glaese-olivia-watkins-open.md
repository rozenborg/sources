---
title: "⚡️The End of SWE-Bench Verified — Mia Glaese & Olivia Watkins, OpenAI Frontier Evals & Human Data"
source: latent-space
url: https://www.latent.space/p/swe-bench-dead
date: 2026-02-23
type: podcast
---

## Summary

## Key Facts

- OpenAI is discontinuing use of SWE-Bench Verified as a coding benchmark due to saturation and contamination
- SWE-Bench Verified was originally created by OpenAI through extensive human review involving ~100 software engineers to curate ~500 high-quality coding tasks
- Many remaining failures on the benchmark reflect unfair tests requiring specific naming or unspecified implementation details rather than actual model limitations
- Evidence of contamination includes models recalling repository-specific implementation details and task identifiers
- OpenAI is switching to SWE-Bench Pro (from Scale) which covers more repositories, languages, and includes longer tasks (1-4+ hours)
- SWE-Bench Pro shows substantially less contamination evidence under OpenAI's "contamination auditor agent" analysis

## Strategic Implications

- Industry-standard coding benchmarks can become obsolete quickly as AI capabilities advance and contamination occurs
- Current pass/fail testing approaches are insufficient for measuring real-world coding abilities
- Benchmark saturation signals need for more sophisticated evaluation methods that go beyond narrow technical correctness
- Contamination detection requires dedicated tooling and processes as models become more capable of memorizing training data
- Longer-horizon tasks (multi-hour complexity) better differentiate model capabilities than short coding challenges

## Actionable Insights

- Develop contamination detection agents and processes before deploying new benchmarks
- Focus evaluation efforts on longer-horizon coding tasks (1-4+ hours) rather than quick fixes
- Incorporate evaluation of code quality, maintainability, and design decisions alongside functional correctness
- Build benchmarks that measure open-ended product-building capabilities rather than just technical implementation
- Balance automated grading speed with human evaluation depth for more meaningful assessment
- Create diverse benchmark datasets spanning multiple repositories, languages, and problem domains
- Establish benchmark retirement criteria and migration paths before saturation occurs
