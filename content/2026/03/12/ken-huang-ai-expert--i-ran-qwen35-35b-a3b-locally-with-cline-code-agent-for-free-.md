---
title: "I Ran Qwen3.5-35B-A3B Locally with Cline Code Agent For Free, Forever"
source: ken-huang-ai-expert
url: https://kenhuangus.substack.com/p/i-ran-a-35b-ai-coding-agent-locally
date: 2026-03-12
type: rss
---

A local deployment of Alibaba's Qwen3.5-35B using Mixture of Experts architecture achieves 35 tokens per second on Mac Mini M4 hardware, delivering 3.5x faster performance than dense models while eliminating API costs and maintaining complete data privacy for AI-assisted coding workflows.

---

- **Hardware requirements** Mac Mini M4 with 64GB unified memory successfully runs 35-billion parameter model compressed to 20GB through 4-bit quantization and MoE architecture that activates only 3B parameters per token

- **Performance advantage** MoE model generates 35.2 tokens/second versus 10.0 tokens/second for equivalent dense 32B model, making real-time coding assistance viable on consumer hardware

- **Technical stack** omlx inference server provides OpenAI-compatible API for Apple Silicon, enabling seamless integration with existing tools while keeping all processing local

- **Cost elimination** Zero ongoing API fees compared to cloud-based solutions, with complete data sovereignty as no code or prompts leave the local machine

- **Integration challenges** Multiple streaming API bugs required custom fixes for Cline VS Code extension compatibility, particularly around model's internal "thinking" blocks that interfere with token streaming

- **Production viability** 35 tokens/second throughput enables practical AI coding sessions with minimal latency, approaching cloud service responsiveness for most development tasks

- **Replication pathway** Complete setup process documented with fixed codebase available, making this configuration reproducible for teams requiring private AI development assistance
