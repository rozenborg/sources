---
title: "Indirect Prompt Injection with Cross-Document Data Exfiltration"
source: ken-huang-ai-expert
url: https://kenhuangus.substack.com/p/indirect-prompt-injection-with-cross
date: 2026-03-12
type: rss
---

Researchers have successfully demonstrated a critical indirect prompt injection vulnerability across four Google AI products that allows attackers to embed malicious instructions in Google Drive documents, automatically exfiltrating sensitive data when victims use Gemini to process those files. The attack requires only a single click on an AI-generated "Source Verification" link and propagates through NotebookLM-generated reports, extending the attack surface to anyone who receives the shared documents.

---

- **Attack Vector** Malicious instructions embedded in Google Drive documents using base64 obfuscation, bypassing safety filters across Gemini Advanced, Google Drive integration, NotebookLM Chat, and NotebookLM Studio

- **Cross-Document Contamination** Once triggered, the injected directive persists across the entire session, automatically applying to other documents the victim processes without additional attacker input

- **Autonomous Exfiltration** Gemini independently generates clickable webhook URLs containing base64-encoded document summaries, requiring only one victim click to transmit data to attacker-controlled servers

- **Report Propagation Risk** NotebookLM Studio embeds the malicious directive directly into professionally formatted reports, multiplying potential victims as these documents are shared across organizations

- **Enterprise Impact** Demonstrated exfiltration includes executive salary data, cloud service credentials (Azure Service Principal secrets), and confidential financial information from documents the victim didn't explicitly target

- **Technical Sophistication** Base64-encoded payloads framed as "compliance directives" successfully fool the AI into treating attacker instructions as legitimate policy requirements across all tested surfaces

- **Agentic Escalation** Current attacks require victim click interaction, but agentic Gemini deployments would eliminate this requirement entirely, enabling fully automated data exfiltration

- **Mitigation Urgency** Organizations using Google Workspace with Gemini should immediately audit shared Drive locations for suspicious documents and implement additional controls on AI-generated external links pending vendor fixes
