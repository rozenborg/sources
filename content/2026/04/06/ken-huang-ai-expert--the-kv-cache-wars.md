---
title: "The KV Cache Wars?"
source: ken-huang-ai-expert
url: https://kenhuangus.substack.com/p/the-kv-cache-wars
date: 2026-04-06
type: rss
---

The KV cache has become the critical bottleneck limiting what agentic AI can actually accomplish at scale, as memory requirements for storing key-value projections explode linearly with context length while computation costs grow quadratically. This infrastructure challenge now determines whether AI agents can maintain multi-day conversations, process million-token contexts, or coordinate complex multi-model workflows — making KV cache optimization the real battlefield beneath flashier benchmark competitions.

---

- **Memory explosion at scale** - A 70B parameter model with 128K context requires 42GB just for KV cache storage, consuming most available GPU memory before model weights are even loaded

- **Dual bottleneck structure** - Prefill stage creates massive compute/memory spikes slowing time-to-first-token, while decode stage creates memory bandwidth pressure that caps generation throughput

- **Linear scaling trap** - KV cache grows linearly across four dimensions simultaneously: context length, transformer layers, batch size, and number of key-value heads, creating multiplicative resource demands

- **Architectural constraint** - Current query tokens must compute relationships to every prior token in the sequence, making this a fundamental limitation rather than an implementation choice that can be easily optimized away

- **Three-front war emerging** - Industry attacking through eviction/sparse attention (reducing storage), quantization/compression (shrinking storage), and hierarchical memory systems (relocating storage)

- **Agent capability ceiling** - Context windows measured in millions of tokens and persistent multi-day agent memory become impossible without solving the underlying memory architecture problem

- **Compute vs memory tradeoff** - KV caching correctly trades quadratic compute costs for linear memory costs, but the memory costs now dominate at the scale required for advanced agentic workflows
