---
title: "Troubleshooting Guide: Running Qwen3.5-35B with Reasoning & Tool Calling using vLLM on Nvidia DGX Spark"
source: ken-huang-ai-expert
url: https://kenhuangus.substack.com/p/troubleshooting-guide-running-qwen35
date: 2026-03-14
type: rss
---

Deploying Qwen3.5-35B MOE with reasoning and tool calling capabilities on vLLM requires navigating critical compatibility issues with model architecture recognition and Docker image versions. The standard Nvidia vLLM Docker images ship with outdated Transformers libraries that don't recognize the qwen3_5_moe architecture, making successful deployment dependent on using bleeding-edge container versions or custom builds.

---

- **Architecture Recognition Failure** Standard vLLM Docker images (nvcr.io/nvidia/vllm:26.01-py3) ship with vLLM 0.13.0 and outdated Transformers libraries that don't recognize qwen3_5_moe architecture, causing validation errors during model loading

- **Memory Configuration Critical** The 35B parameter MOE model (10.7B active) with 131K context window and 4-bit AWQ quantization requires precise memory allocation settings to prevent OOM errors on DGX systems

- **Network Binding Dependencies** Port binding issues with --net=host flag indicate container networking conflicts that can block API access even when the model loads successfully

- **Version Compatibility Chain** Success depends on aligning three components: vLLM version, Transformers library version, and model architecture support - a single outdated component breaks the entire pipeline

- **OpenCode Integration Path** The model's reasoning and tool calling capabilities enable direct integration with OpenCode frameworks, requiring specific API endpoint configurations for multi-step reasoning workflows

- **Performance Tuning Required** MOE architecture with 131K context demands optimization of tensor parallelism, pipeline parallelism, and KV cache settings to achieve acceptable inference speeds on multi-GPU setups

- **Container Strategy** Deploy using latest development containers or build custom images with vLLM ≥0.14.0 and compatible Transformers versions to avoid architecture recognition failures
