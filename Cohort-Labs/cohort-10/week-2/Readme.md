# Week 2: Make Your Agent Handle Real Documents

Welcome to Week 2 of the AI PM Certification.

In Week 1, you built a working AI agent. It read a contract, answered questions, and felt like something real. This week, you find out why that agent breaks on real documents — and you build the architecture that fixes it.

The fix is called RAG. By the end of this week, you'll understand it well enough to build it, explain it to a stakeholder, and extend it into an agentic system that self-checks its own answers before showing them to you.

Each lab builds directly on the last. Work through them in order. No prior ML experience needed — just the n8n account and OpenAI key from Week 1.

---

## The Labs

### [Lab 2.1 — Why Your Agent Breaks on Real Contracts](./2.1-why-we-need-RAG/Readme.md)

Before you fix anything, you need to see what's actually broken. You'll take the agent from Week 1 and run it on a large contract — one that's closer to what real documents look like. It either fails outright or gives you a degraded answer. Either way, you'll understand exactly why.

This lab is short. It's a diagnostic, not a build. But it sets up everything that follows — once you see the failure mode, the solution in Lab 2.2 will make complete sense.

**Time:** ~15 minutes

---

### [Lab 2.2 — Build Your First RAG Pipeline](./2.2-understanding-RAG/Readme.md)

This is where you build the fix. You'll create a two-workflow system: one that ingests a large contract and breaks it into searchable chunks, and one that retrieves exactly the right chunk when a user asks a question — without hitting context limits.

Along the way, you'll learn what embeddings actually are, why chunk size and overlap matter, what the Recursive Text Splitter does differently, and how to configure a vector store that actually works on PDF documents. By the end, you'll have a live contract Q&A system that handles large files correctly.

**Time:** ~40 minutes

---

### [Lab 2.3 — Agentic RAG: Contract Intelligence](./2.3-n8n-agenticRAG/Readme.md)

Basic RAG works, but it takes an answer at face value. This lab makes the system agentic: it cites the exact clause it used for every answer, self-checks its own accuracy with a Faithfulness Judge, and automatically retries when its first answer isn't reliable enough.

Think of it as turning your contract Q&A system into a cautious legal research assistant — one that refuses to guess, always shows its sources, and double-checks its own work before telling you anything.

**Time:** ~50 minutes

---

> If you get stuck in any lab, each one has troubleshooting guidance built in. Read the error carefully — most issues in these labs have a one-line fix.
