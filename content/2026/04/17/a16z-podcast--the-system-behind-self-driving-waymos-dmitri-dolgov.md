---
title: "The System Behind Self-Driving: Waymo’s Dmitri Dolgov"
source: a16z-podcast
url: https://a16z.simplecast.com/episodes/from-models-to-mobility-building-waymo-with-dmitri-dolgov-p2z80L_O
date: 2026-04-17
type: podcast
---

Waymo's success in delivering hundreds of thousands of weekly autonomous rides stems from treating self-driving as a complete system engineering challenge rather than just an AI modeling problem, requiring integrated approaches to sensor fusion, simulation-based training, and real-world validation that fundamentally differ from driver-assistance technologies.

---

- **System-first approach** - Waymo prioritizes building comprehensive systems for training, evaluation, and deployment rather than focusing solely on improving individual AI models, recognizing that real-world autonomy requires orchestrating multiple technical components

- **Sensor fusion architecture** - The platform integrates data from LiDAR, radar, and cameras simultaneously rather than relying on any single sensor type, creating redundant perception capabilities that work across different weather and lighting conditions

- **Simulation-driven development** - Waymo uses extensive simulation environments to train and test autonomous driving scenarios that would be too dangerous or rare to encounter during real-world testing, accelerating the development cycle

- **Critic model validation** - The company employs "critic" AI models that evaluate driving decisions made by the primary autonomous system, providing an additional layer of safety assessment before deployment

- **Full autonomy vs. assistance distinction** - True self-driving requires the system to handle 100% of driving tasks without human backup, demanding fundamentally different safety standards and capabilities compared to driver-assistance features

- **Global scaling challenges** - Expanding autonomous driving internationally requires adapting to different traffic patterns, road infrastructure, and regulatory environments rather than simply deploying the same technology everywhere

- **AI advancement integration** - Recent breakthroughs in artificial intelligence are being incorporated to improve decision-making and handling of edge cases, but within the broader systems framework rather than replacing it entirely
