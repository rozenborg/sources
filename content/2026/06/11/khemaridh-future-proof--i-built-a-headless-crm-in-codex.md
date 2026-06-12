---
title: "I built a "headless CRM" in Codex"
source: khemaridh-future-proof
url: https://khemaridh.substack.com/p/i-built-a-headless-crm-in-codex
date: 2026-06-11
type: rss
---

The author built a custom "headless CRM" using OpenAI's Codex that analyzes Gmail and iMessage conversations to automatically recommend which contacts to reconnect with based on predefined follow-up cadences. This personal AI agent runs entirely through text commands within the ChatGPT mobile app, requiring no traditional interface while providing weekly "tickler" suggestions for prospects, clients, and network contacts who are overdue for outreach.

---

- **Technical Architecture** Uses open-source CLIs (Gog for Google Suite, imsg for iMessage) connected through Codex to create a text-based contact management system accessible via mobile ChatGPT app

- **Security Implementation** Implements read-only API access, contact allowlists, and narrow approval gates to prevent unauthorized sending or data modification while still accessing communication histories

- **Follow-up Automation** Calculates overdue contacts using different cadences (prospects: 14 days, clients: 28 days, network: 42 days) and automatically surfaces reconnection recommendations every Friday at 9am

- **Mobile-First Design** Specifically built for iPhone usage since the author conducts 90% of communications through email and iMessage on mobile, leveraging Codex's improved mobile experience

- **Custom Skill Development** Created a specialized "cos-tickle" skill with helper Python scripts that parse contact data, calculate overdue periods, and generate prioritized outreach lists grouped by contact type

- **Workflow Integration** Replaces traditional CRM interfaces with natural language queries, allowing users to ask contextual questions about contacts without clicking through dashboards or forms

- **Strategic Positioning** Represents a shift toward "headless" business tools that eliminate traditional UIs in favor of AI-powered text interactions, potentially indicating future direction of productivity software
