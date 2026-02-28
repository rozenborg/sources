---
title: "We’ve Been Testing AI Safety Wrong. Here’s How to Fix It."
source: ken-huang-ai-expert
url: https://kenhuangus.substack.com/p/weve-been-testing-ai-safety-wrong
date: 2026-02-27
type: rss
---

## Summary

- Current AI safety evaluations assume model failures are rare, discrete events measured through isolated jailbreak prompts and attack success rates

- **Critical flaw**: AI model failures actually form continuous "behavioral attraction basins" - large, interconnected regions where semantically similar prompts produce the same failure modes

- Traditional "unit-test" approach patches individual incidents while leaving underlying vulnerability regions intact and exploitable

- New research methodology uses MAP-Elites algorithm to map entire failure landscapes rather than cataloging isolated incidents

- **Key strategic shift needed**: Move from asking "Can I break it?" to "Where does it fail and how large are those failure regions?"

- Essential questions for proper evaluation:
  - Size and boundaries of failure regions
  - Whether failures are connected basins or fragmented pockets  
  - Where refusal flips to compliance
  - How failure patterns differ across model families

- **Actionable insight**: Safety teams should adopt quality-diversity optimization to illuminate complete behavioral spaces, not just find individual exploits

- Current patching strategies fail because they address symptoms (individual prompts) rather than root causes (underlying behavioral regions)

- **Implementation approach**: Frame vulnerability discovery as mapping terrain rather than incident collection - similar to systems engineering principles

- Cross-institutional research validates findings across multiple AI model families and use cases

- **Strategic implication**: Organizations using current evaluation methods may have false confidence in their AI safety measures due to unmapped failure basins
