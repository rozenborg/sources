---
title: "Chapter 15: Structured Output and Schema-Constrained Generation (Claude Code vs. Hermes Agent)"
source: ken-huang-ai-expert
url: https://kenhuangus.substack.com/p/chapter-15-structured-output-and
date: 2026-05-02
type: rss
---

Claude Code's synthetic tool approach eliminates the complexities of provider-specific JSON modes by wrapping structured output as a standard tool call, while Hermes Agent focuses on infrastructure-level structured output for batch processing and dataset generation. The key architectural difference is that Claude Code handles validation within the query engine itself, whereas Hermes implements explicit retry loops and feeds validation errors back as conversation messages.

---

- **Implementation Philosophy** Claude Code uses a "synthetic tool trick" that wraps JSON schemas as fake tool definitions, leveraging the model's existing tool-calling machinery for validation. Hermes Agent implements explicit tool-use forcing with custom retry loops and error feedback injection.

- **Validation Strategy** Claude Code validates within the tool call itself using AJV compilation, throwing telemetry-safe errors that trigger automatic retries. Hermes validates externally using jsonschema, then feeds specific validation errors back as conversation messages for model self-correction.

- **Retry Budget Management** Claude Code tracks structured output attempts separately from regular tool calls with a default 5-retry limit and typed error results (error_max_structured_output_retries). Hermes implements configurable retry loops with rich error context but no specialized retry tracking.

- **Cross-Provider Portability** Claude Code's synthetic tool approach works across any provider supporting function calling without relying on provider-specific JSON mode flags. Hermes uses the same tool-forcing pattern but implements it explicitly in Python rather than through harness abstraction.

- **Scale and Infrastructure** Hermes excels at infrastructure-level structured output through batch_runner.py, which enforces consistent schemas across thousands of parallel extractions and JSONL trajectory formats. Claude Code focuses on single-query structured output with query engine integration.

- **Performance Optimization** Claude Code implements identity-caching for compiled schemas (80-call workflows drop from 110ms to 4ms AJV overhead). Hermes optimizes for multiprocessing distribution and normalized tool statistics for dataset compatibility.

- **Error Handling Granularity** Claude Code provides typed error subtypes distinguishable from other failure modes, while Hermes offers detailed field-level validation errors with JSON path information for debugging complex schema violations.
