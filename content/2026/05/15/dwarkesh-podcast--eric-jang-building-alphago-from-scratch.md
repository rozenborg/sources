---
title: "Eric Jang – Building AlphaGo from scratch"
source: dwarkesh-podcast
url: https://www.dwarkesh.com/p/eric-jang
date: 2026-05-15
type: podcast
---

AlphaGo's Monte Carlo Tree Search provides a superior approach to reinforcement learning compared to current LLM training methods, offering precise action targets at every step rather than forcing models to solve the credit assignment problem across 100,000+ token sequences. Eric Jang's reconstruction reveals how stepping backward to 2017's cleaner AI primitives illuminates pathways for more efficient learning in future general AI systems.

---

- **MCTS superiority** Monte Carlo Tree Search suggests strictly better actions at each move, creating clear training targets that sidestep the credit assignment problem plaguing current policy gradient RL methods in LLMs

- **Credit assignment crisis** Current LLM reinforcement learning must determine which specific tokens among 100k+ in a trajectory produced the correct answer, creating massive inefficiency compared to AlphaGo's step-by-step guidance

- **Human learning parallels** The way humans learn resembles AlphaGo's precise feedback system more than naive policy gradient methods, suggesting MCTS-style approaches could unlock more natural AI training

- **Autoresearch capabilities** LLMs already automate implementation and hyperparameter optimization effectively, but struggle with higher-level research decisions like question selection and escaping dead ends

- **Intelligence explosion indicators** The current state of automated research reveals which cognitive tasks are ready for acceleration and which remain bottlenecks for recursive self-improvement

- **Primitive intelligence framework** AlphaGo demonstrates the cleanest example of core intelligence components - search, learning from experience, and self-play - that will likely underpin more general future AI systems

- **Modern reconstruction value** Building historical AI breakthroughs with contemporary tools reveals both how far techniques have advanced and which fundamental principles remain most powerful
