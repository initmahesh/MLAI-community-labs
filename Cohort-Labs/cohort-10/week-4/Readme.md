# Week 4: Build Systems That Think in Teams

Welcome to Week 4 of the AI PM Certification.

In Week 3 you measured how well a single agent performs. This week you move past single agents entirely. The problem with one agent doing everything is that it gets confused — ask it two different kinds of questions and the answers start blending together. The fix is to stop asking one agent to know everything and start building systems where each agent knows one thing very well.

That's what multi-agent architecture is. This week you'll build it two ways — inside Azure AI Foundry without code, and inside n8n with a workflow.

---

## The Labs

### [Lab — Build, Deploy & Evaluate Your First AI Agent in Azure AI Foundry](./4.1-azureaifoundary-agent/Readme.md)

Before you can build a multi-agent system, you need to know how a single agent works inside Azure AI Foundry. You'll build a contract-review agent, give it a knowledge base, publish it to Microsoft Teams, and run a live evaluation — all without writing a line of code. This is the foundation everything else in Week 4 sits on.

---

### [Lab — Build a Multi-Agent Workflow in Azure AI Foundry](./4.3-multiagent-workflow-azure-aifoundary/Readme.md)

You built a multi-agent system in n8n. Now you build one in Foundry using its native Workflow canvas — no code, just nodes. A Router Agent reads every incoming question and decides whether the HR Policy Agent or the Company Info Agent should answer it. You'll wire the whole thing together, test both branches live, and see exactly why routing to a specialist beats asking one agent to know everything.

---

### [Lab — Add Risk Intelligence and Conversation Memory to Your Contract Assistant](./4.5-n8n-rag-multiagent/Readme.md)

You pick up the Agentic RAG workflow from Lab 2.3 and extend it into a full multi-agent pipeline. A Contract Orchestrator receives every contract question and routes it to one of two specialists — `contract_agent` for factual clause retrieval from the vector store, and `risk_agent` for severity analysis backed by a Snowflake risk database. Off-topic messages go to `generic_question_agent`, which returns pre-written responses from MongoDB instead of letting the LLM improvise. A single shared memory node ties all five agents together so follow-up questions like "is that risky?" work correctly across turns.

---
