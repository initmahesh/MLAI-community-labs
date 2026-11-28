# Lab 2.2: Agentic RAG — Contract Intelligence

![banner](./assets/agentic-rag-flow.png)

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [How Agentic RAG Decides When to Search](#how-agentic-rag-decides-when-to-search)
- [Part 1: Import the Workflow](#part-1-import-the-workflow)
- [Part 2: Add Your OpenAI Key](#part-2-add-your-openai-key)
- [Part 3: Upload Your Contract](#part-3-upload-your-contract)
- [Part 4: Ask Questions and Watch the Routing](#part-4-ask-questions-and-watch-the-routing)
- [Quick Reference](#quick-reference)
- [What's Next](#whats-next)

---

## Overview

In [Lab 2.1](../2.1-understanding-RAG/Readme.md), you built a RAG pipeline that answers questions from a contract. But type **"Hi"** into it, and it still searches the whole contract before it replies. That's wasted time and money.

The fix: let the system decide **before** it searches. A contract question gets a search; anything else gets a direct reply. That one decision is what makes RAG **agentic**.

Here's the flow for this lab:

- **Run the workflow.** See "Hi" skip the search while contract questions go through it.

The diagram above shows the workflow you'll be running. **Reading the contract** happens once, when you upload it. **Answering a message** happens every time you send one: the Intent Router checks the message first, then either replies directly or searches the contract.

---

## Prerequisites

✅ **Lab 2.1 done.** You know how chunking, embeddings and vector search work.

✅ **n8n account** and an **OpenAI API key** with credit (from Week 1).

✅ **Download these files:**

- [n8n Workflow JSON](https://pragyaallc-my.sharepoint.com/:u:/g/personal/anushka_srivastava_legalgraph_ai/IQCa6buQ_4CLSb6iZU4ZK0FbAXUB4ryLH9Q0NKz68mXT_fk?e=nduyOL)
- [Test Contract](https://pragyaallc-my.sharepoint.com/:w:/g/personal/sachin_parmar_legalgraph_ai/IQAbCBMxqrFrT6hzD6t9oCdpAR8pdsHtVaZf2O5HiyGq5jY?e=4s3M8D) (keep it in `.docx` format)

---

## How Agentic RAG Decides When to Search

Before you open n8n, you need to know what's different, because that difference is what you'll be watching for in this lab.

The Lab 2.1 pipeline had one path: every message went straight to the contract search. This lab's workflow adds one step at the front that decides whether to search at all.

| Traditional RAG (Lab 2.1) | Agentic RAG (this lab) |
|---|---|
| Searches for every message, even "Hi" | Checks the message first and searches only when needed |
| One fixed path | Two paths: reply directly, or search the contract |

That new step is called the **Intent Router**. Here's how a message moves through the workflow:

1. The **Intent Router** decides whether the message needs the contract.
2. If **no**, the **Direct Response Agent** replies straight away.
3. If **yes**, the **Query Rewriter** sharpens the question, and the **RAG Agent** searches the contract and answers with citations.

So now you know what to look for. Next, let's get this workflow into your n8n.

---

## Part 1: Import the Workflow

**What it is**: The workflow JSON you downloaded in Prerequisites. It's the full Agentic RAG system described above, with the upload pipeline, the Intent Router and both answer paths already built.

**Why import it**: The ingestion part is the same as Lab 2.1, and you've already built that once. Importing it lets you skip rebuilding and spend your time on what's new: the routing.

**Action items**:

1. In n8n, click **+ New Workflow**.
2. Click the **three-dot menu (⋮)** in the top right → **Import from file** (`Cmd+Shift+I` on Mac / `Ctrl+Shift+I` on Windows).
3. Select the workflow JSON you downloaded.

![assets](assets/11.png)

**Output**: You'll see three groups of nodes on the canvas: **Document Ingestion** at the top, the **Intent Router** fork, and the **Query & Answer** pipeline. Everything is already connected.

The workflow is in place, but it can't run yet. Every agent needs OpenAI, and n8n doesn't have your key.

---

## Part 2: Add Your OpenAI Key

Three nodes need the key. Create the credential once, then select it on each node.

**Action items**:

1. Click **OpenAI Chat Model** → under **Credential**, click **Create New** → paste your API key → **Save**.

   > **Note**: This one node powers all four agents: Intent Router, Query Rewriter, RAG Agent and Direct Response Agent.

![assets](assets/8.png)

2. Click **Embeddings OpenAI** (in the ingestion section) → select the same credential.
3. Click **Embeddings OpenAI1** (in the query section) → select the same credential.

   > **Note**: No API key yet? Get one at [platform.openai.com](https://platform.openai.com) and add a small amount of credit. If your n8n account came with free OpenAI credits, you can use those instead.

**Output**: All three OpenAI nodes use the same credential.

Now the workflow can run, but there's no contract to search yet. Let's give it one.

---

## Part 3: Upload Your Contract

This is the same ingestion you did in Lab 2.1: read, chunk, embed, store.

**Action items**:

1. Click **Execute Workflow** (▶ at the bottom of the canvas).

![assets](assets/9.png)

2. Open the **On Form Submission** node and click the **Test URL**.
3. In the form that opens, upload the test contract and click **Submit**.
4. Go back to the canvas and wait for every ingestion node to turn green. This takes about 5–15 seconds.

**Output**: Your contract is stored and ready to be searched.

Now for the real test: is the "Hi" problem actually fixed?

---

## Part 4: Ask Questions and Watch the Routing

**Action items**:

1. Open the **When chat message received** node → click **Open Chat**.

![assets](assets/10.png)

2. Type **"Hi"**. Only the **Intent Router** and **Direct Response Agent** light up. No search, instant reply. That's the fix working.

![assets](assets/12.png)

3. Now ask **"What is the contract about?"**. This time it takes the other path: **Query Rewriter → RAG Agent → Vector Search Tool**, and answers with citations.

![assets](assets/13.png)

   **What the Query Rewriter does.** The **AI Node — Query Rewriter** is a query enhancer. People ask short, casual questions, but the contract uses formal wording, and vector search can miss the right chunk if the words don't line up. So before the search, this AI node rewrites the question into a better search query, adding the terms the contract is likely to use.

   In the screenshot above, *"what is this contract about?"* is turned into:

   > *purpose and scope of the agreement, Purpose of Agreement, Scope of Agreement, 'Purpose', 'Scope', 'Objective', 'Whereas', 'Recitals'*

   Those are the headings where a contract states what it's about. The search then finds the right chunks, and the **RAG Agent** answers from them. Click the node's **Embeddings OpenAI1** step in the logs to see the rewritten query that was actually searched.

4. Try a few messages from each column and watch which path lights up:

| General (no search) | Contract (full search) |
|---|---|
| "Hello" | "Who are the parties involved?" |
| "How are you?" | "What are the key terms and obligations?" |
| "What can you do?" | "What is the interest rate?" |
| | "When is the maturity date?" |

**Output**: General messages get instant replies, and contract questions get answers with citations.
---

## Quick Reference

| Problem | Cause | Fix |
|---|---|---|
| "Hi" triggers a contract search | Traditional RAG searches on every message | Put an Intent Router before the search |
| OpenAI nodes show errors | One of the three nodes is missing the credential | Select the same credential on the Chat Model and both Embeddings nodes |

---

## What's Next

Your agent now decides whether a message needs the contract before it searches.
But your web app doesn't know about that yet. It still talks to your backend the old way, one message and one webhook at a time.
In the next lab, you'll give your agent a **web layer**, so you can chat with it from your own app.

[Go to Lab 2.4: Agentic RAG Web App →](../2.4-agenticRAG-web-app/Readme.md)
