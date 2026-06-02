---
title: "Why Video Agent models are next — Ethan He, xAI Grok Imagine"
source: latent-space
url: https://www.latent.space/p/video-agents
date: 2026-06-01
type: podcast
---

Ethan He argues that the next breakthrough in video generation isn't building better diffusion models, but creating video agents that can iteratively plan, generate, edit and refine content using LLMs for orchestration. Having built Grok Imagine in just three months at xAI, he believes video models derive their intelligence primarily from language model foundations rather than video training data itself.

---

- **Small team advantage** xAI's Grok Imagine team shipped a frontier video model in 3 months with minimal meetings and maximum iteration speed, proving small teams can outperform large ones when communication bandwidth is reduced and everyone aligns on goals

- **Debugging over algorithms** Most model quality improvements came from finding tiny bugs in data and training pipelines rather than novel algorithmic breakthroughs, highlighting the importance of rapid iteration cycles over theoretical advances

- **Compute becoming the bottleneck again** As coding models enable researchers to implement ideas in hours rather than weeks, the limiting factor shifts back to having enough GPU resources to test all generated hypotheses

- **Video models bootstrap from images** All video generation systems require training image models first because videos lack natural language associations and need synthetic captions, while images provide denser text-visual mappings for language understanding

- **VAE compression critical** Video models can't train on raw pixels due to token count (1M+ per image), requiring variational autoencoders to compress visual data into manageable latent representations before diffusion transformer training

- **LLMs unlock video intelligence** The core insight is that video models get their reasoning capabilities from language model foundations rather than video training data, suggesting future advances will come from better LLM integration rather than improved diffusion architectures

- **Video agents as next evolution** Similar to how coding went from one-shot generation to multi-turn reasoning agents, video generation will evolve toward systems that can plan entire creative workflows with editing, critique, and iteration capabilities

- **Real-time interactive world models** Future applications like Flipbook's JIT video UI represent the trajectory toward generative interfaces that go directly from user intent to pixels, potentially replacing traditional HTML/CSS development
