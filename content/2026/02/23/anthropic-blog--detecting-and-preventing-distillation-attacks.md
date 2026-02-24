---
title: "Detecting And Preventing Distillation Attacks"
source: anthropic-blog
url: https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks
date: 2026-02-23
type: sitemap
---

## Summary

## Key Facts

- Three Chinese AI labs (DeepSeek, Moonshot, MiniMax) conducted large-scale distillation attacks against Claude
- Combined attacks generated over 16 million exchanges through approximately 24,000 fraudulent accounts
- Attack scales: MiniMax (13M exchanges), Moonshot (3.4M exchanges), DeepSeek (150K exchanges)
- Labs violated terms of service and regional access restrictions through proxy services and fraudulent accounts
- Attacks targeted Claude's most advanced capabilities: agentic reasoning, tool use, coding, and computer vision
- Attribution achieved through IP correlation, request metadata, infrastructure indicators, and industry partner corroboration

## Strategic Implications

- **National Security Risk**: Distilled models lack safeguards, enabling potential bioweapon development and malicious cyber activities
- **Export Control Circumvention**: Attacks undermine US export controls by allowing foreign labs to acquire American AI capabilities without direct chip access
- **Military Applications**: Foreign governments can integrate unprotected AI capabilities into military, intelligence, and surveillance systems
- **Competitive Advantage Erosion**: Illicit distillation allows competitors to acquire capabilities at fraction of normal development time and cost
- **Authoritarian Enhancement**: Enables offensive cyber operations, disinformation campaigns, and mass surveillance capabilities

## Technical Capabilities

- **Detection Systems**: Behavioral fingerprinting, coordinated activity identification, chain-of-thought elicitation detection
- **"Hydra Cluster" Architecture**: Proxy services manage 20,000+ fraudulent accounts simultaneously with load balancing
- **Real-time Adaptation**: MiniMax pivoted within 24 hours when Anthropic released new model during active campaign
- **Chain-of-thought Extraction**: Prompts designed to extract internal reasoning processes for training data generation

## Actionable Insights

- **Strengthen Access Controls**: Enhanced verification for educational accounts, security research programs, and startup pathways
- **Industry Coordination Required**: Share technical indicators with AI labs, cloud providers, and authorities
- **Monitor Proxy Networks**: Track commercial proxy services reselling frontier model access at scale
- **Pattern Recognition**: Detect massive volume, repetitive structures, and capability-focused content patterns
- **Develop Countermeasures**: Implement product, API, and model-level safeguards to reduce distillation efficacy
- **Policy Response Needed**: Coordinate action among industry players, policymakers, and global AI community within narrow time window
