# Week 2: Make Your Agent Handle Real Documents

Welcome to Week 2 of the AI PM Certification.

In Week 1, you built a working AI agent. It read a contract, answered questions, and felt like something real. This week, you find out why that agent breaks on real documents — and you build the architecture that fixes it.

The fix is called RAG. By the end of this week, you'll understand it well enough to build it, explain it to a stakeholder, and extend it into an agentic system that self-checks its own answers before showing them to you.

Each lab builds directly on the last. Work through them in order. No prior ML experience needed — just the n8n account and OpenAI key from Week 1.

---

## The Labs

### [Lab 2.1 — Fix Your Agent on Large Contracts with RAG in n8n](./2.1-understanding-RAG/Readme.md)

This lab has two parts. First, you take the agent from Week 1 and run it on a large contract, one that's closer to what real documents look like. It either fails outright or gives you a degraded answer, and you'll understand exactly why.

Then you build the fix: a two-workflow system, one that ingests a large contract and breaks it into searchable chunks, and one that retrieves exactly the right chunk when a user asks a question, without hitting context limits.

Along the way, you'll learn what embeddings actually are, why chunk size and overlap matter, what the Recursive Text Splitter does differently, and how to configure a vector store that actually works on PDF documents. By the end, you'll have a live contract Q&A system that handles large files correctly.

**Time:** ~55 minutes

---

### [Lab 2.2 — Agentic RAG: Contract Intelligence](./2.2-n8n-agenticRAG/Readme.md)

Basic RAG works, but it takes an answer at face value. This lab makes the system agentic: it cites the exact clause it used for every answer, self-checks its own accuracy with a Faithfulness Judge, and automatically retries when its first answer isn't reliable enough.

Think of it as turning your contract Q&A system into a cautious legal research assistant — one that refuses to guess, always shows its sources, and double-checks its own work before telling you anything.

**Time:** ~50 minutes

---

### [Lab 2.3 — Knowledge Graph RAG](./2.3-knowledge-graph-RAG/Readme.md)

Agentic RAG still struggles when one answer is spread across several clauses. Search finds the passages that *look similar* to your question and misses the clauses that link to them. This lab adds a **knowledge graph**: Graphify reads a loan agreement and turns it into dots and lines, and you chat with it in an app and watch which parts of the graph each answer comes from.

You open one Colab notebook, run it, and use the app in your browser. There is nothing to set up on your own computer.

**Time:** ~30 minutes

---

### [Lab 2.4 — Give Your Agentic RAG a Web Layer](./2.4-agenticRAG-web-app/Readme.md)

Your backend just got smarter — it now decides whether a question even needs the contract before it retrieves anything. Your web app from Week 1 doesn't know that happened yet. This lab reconnects the two: rewiring the app to match the new ingestion/chat split, and restyling it from a real design system instead of an improvised palette.

**Time:** ~35 minutes

---

> If you get stuck in any lab, each one has troubleshooting guidance built in. Read the error carefully — most issues in these labs have a one-line fix.
