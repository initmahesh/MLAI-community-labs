# Week 4: Build Systems That Think in Teams

Welcome to Week 4 of the AI PM Certification.

In Week 3 you measured how well a single agent performs. This week you move past single agents entirely. The problem with one agent doing everything is that it gets confused — ask it two different kinds of questions and the answers start blending together. The fix is to stop asking one agent to know everything and start building systems where each agent knows one thing very well.

That's what multi-agent architecture is. This week you'll build it two ways — inside Azure AI Foundry without code, and inside n8n with a workflow.

---

## The Labs

### [Lab 4.1 — Build, Deploy & Evaluate Your First AI Agent in Azure AI Foundry](./4.1-azureaifoundary-agent/Readme.md)

Before you can build a multi-agent system, you need to know how a single agent works inside Azure AI Foundry. You'll build a contract-review agent, give it a knowledge base, publish it to Microsoft Teams, and run a live evaluation — all without writing a line of code. This is the foundation everything else in Week 4 sits on.

---

### [Lab 4.2 — Build a Multi-Agent Contract Assistant in n8n](./4.2-n8n-multiagent/Readme.md)

Now you build a real multi-agent system: one that accepts a contract PDF, routes it through a chain of specialist agents — a risk detector, a clause extractor, a summarizer — and returns a structured report. Each agent has one job. Together they do something no single agent could do reliably on its own.

---

### [Lab 4.3 — Build a Multi-Agent Workflow in Azure AI Foundry](./4.3-multiagent-workflow-azure-aifoundary/Readme.md)

You built a multi-agent system in n8n. Now you build one in Foundry using its native Workflow canvas — no code, just nodes. A Router Agent reads every incoming question and decides whether the HR Policy Agent or the Company Info Agent should answer it. You'll wire the whole thing together, test both branches live, and see exactly why routing to a specialist beats asking one agent to know everything.

---
