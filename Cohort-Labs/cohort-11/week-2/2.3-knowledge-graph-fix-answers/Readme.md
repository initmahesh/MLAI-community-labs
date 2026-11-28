# Lab 2.3: Fix Incomplete Answers with a Knowledge Graph

![banner](./images/kg.jpg)

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Part 1: Where We Started: Plain LLM on a Document](#part-1-where-we-started-plain-llm-on-a-document)
- [Part 2: Stress-Test RAG with a Loan Agreement](#part-2-stress-test-rag-with-a-loan-agreement)
- [Part 3: The Fix Is a Knowledge Graph](#part-3-the-fix-is-a-knowledge-graph)
- [Part 4: Create Your InfraNodus API Key](#part-4-create-your-infranodus-api-key)
- [Part 5: Import the Workflow](#part-5-import-the-workflow)
- [Part 6: Add Your API Keys](#part-6-add-your-api-keys)
- [Part 7: Create the Data Table for Your Graph](#part-7-create-the-data-table-for-your-graph)
- [Part 8: Build the Graph and Ask Again](#part-8-build-the-graph-and-ask-again)
- [Quick Reference](#quick-reference)

---

## Overview

In [Lab 2.1](../2.1-understanding-RAG/Readme.md) and [Lab 2.2](../2.2-n8n-agenticRAG/Readme.md), RAG let your agent answer questions from large contracts. But ask for something whose answer is **spread across many pages**, and it gives an answer that looks right but is incomplete.

In this lab, you'll break RAG on purpose with a loan agreement, then fix it with a **knowledge graph**. Instead of searching blindly, the agent first finds how the facts connect, then searches for exactly those.

**Question → find connected nodes in the graph → enhance the question → RAG fetches the right chunks → complete answer**

By the end, you'll have an n8n workflow that answers "What is the interest rate?" with the real number, not just the formula.

---

## Prerequisites

✅ **Agentic workflow** from Lab 2.2. You can download it [from here](https://pragyaallc-my.sharepoint.com/:u:/g/personal/anushka_srivastava_legalgraph_ai/IQCa6buQ_4CLSb6iZU4ZK0FbAXUB4ryLH9Q0NKz68mXT_fk?e=nduyOL).

✅ **Sample file:** [Loan Agreement (PDF)](https://pragyaallc-my.sharepoint.com/:b:/g/personal/anushka_srivastava_legalgraph_ai/IQD7-tDNZkS3TbNqhwLdU1e-AahWyPT4ozHCQZ_igvhqNJM?e=hMyrkk)

✅ **Workflow:** [n8n Workflow JSON](https://pragyaallc-my.sharepoint.com/:u:/g/personal/anushka_srivastava_legalgraph_ai/IQCQx6LyxdnbQq65DzlNsgNIAYPSxSqCCliALuKzEAXGgvw?e=fmpRo6) (for Part 5)

✅ **Graph table:** [ci_graphs.csv](https://pragyaallc-my.sharepoint.com/:x:/g/personal/anushka_srivastava_legalgraph_ai/IQAco6jA1r2BQo1KRO4cUzg5ATCW6XhjYibqkJ7gy1tCBAY?e=2zbwJH) (for Part 7)

---

## Part 1: Where We Started: Plain LLM on a Document

In Week 1, we created an AI agent that answers questions from a contract. It works well on documents of roughly **4 to 100 pages**, but it breaks on bigger contracts.

![assets](images/1.png)

Every AI model has a **context window**: a hard limit on how much text it can read in one request. A bigger contract either gets rejected or silently cut off. And even if it fit, sending everything on every question is **expensive**, **slow** and **less accurate**.

We solved this problem using **RAG**. It cuts the document into chunks and sends the LLM only the ones that match the question. [Lab 2.1](../2.1-understanding-RAG/Readme.md) covers it in full.

![assets](images/2.png)

---

## Part 2: Stress-Test RAG with a Loan Agreement

In [Lab 2.2](../2.2-n8n-agenticRAG/Readme.md), the test contract was easy for RAG: every fact sat in one clause, so a few chunks were enough. Real contracts aren't always that simple. Let's try one that isn't.

**Action items**:

1. Open your Lab 2.2 workflow in n8n. Open the **OpenAI Chat Model** node and change **Model** to **gpt-5.4-mini**.
2. Click **Execute Workflow**, open the upload form and upload the **Loan Agreement** from Prerequisites.
3. Once ingestion finishes, open the chat and ask:

```
What is the interest rate on this loan?
```

![assets](images/3.png)

**What happened**: The agent could not identify the interest rate. It described what the agreement mentions and stopped, without giving the actual number.

That's because the rate isn't written in one place. It is made up of several pieces (the spread, the benchmark, the index floor), and they are **spread across the document**. RAG only brought back some of them.

Is the information missing from the document? No. When a human reviewed the document, they found that **everything exists**. It is just **spread widely across 200 pages**:

![assets](images/4.png)

---

## Part 3: The Fix Is a Knowledge Graph

A **knowledge graph** stores the important things in a document and **how they connect**. Each thing is a dot (like `Interest Rate`, `Spread` or `Index Floor`), and each connection is a line between two dots.

Think of it like a mind map of your contract. RAG gives you a pile of separate paragraphs. A knowledge graph gives you the map that shows which ones belong together, even if they sit hundreds of pages apart.

We have a case study for knowledge graph. You can review it [here](https://www.canva.com/design/DAFvShweAOA/kdjT-q5zYy5Y3sxOJc98jg/edit) if you're interested.

Here is the n8n workflow we'll use. It builds the graph from your contract, then uses it to answer questions:

![assets](images/5.png)

The workflow has two flows. **Flow 1** runs once per contract and builds everything. **Flow 2** runs every time you ask a question.

**Flow 1: Add a contract**

| Node | What it does |
|---|---|
| **Upload Contract (Form)** | Shows the form where you upload the contract PDF. This starts the flow. |
| **Setup** | Gives the contract a unique `contract_id` and notes its file name. |
| **Extract PDF Text** | Reads the PDF and pulls out the text, one item per page. |
| **Clean Text** | Tidies the text and removes page numbers and repeated headers. Tags each page, so answers can cite page numbers. |
| **Pages to Items** | Turns the cleaned text into one item per page for the RAG side. |
| **Recursive Character Text Splitter** | Cuts each page into chunks of about 800 characters, with a 100-character overlap. |
| **Default Data Loader** | Loads each chunk and attaches its `contract_id` and page number. |
| **Embeddings** | Turns each chunk into an embedding (a list of numbers that captures its meaning). |
| **Simple Vector Store** | Stores the chunks and their embeddings, so they can be searched by meaning. |
| **Ontology Agent** | Reads the whole contract and lists its entities, concepts, relationships, conditions and dependencies (for example: *Interest Rate → consists of → Base Rate*). |
| **Ontology Model** | The OpenAI model (gpt-5.4-mini) that powers the Ontology Agent. |
| **Ontology Schema** | Forces the Ontology Agent to reply in a fixed format, so the next nodes can read it. |
| **Build InfraNodus Statements** | Turns each relationship, condition and dependency into a short plain sentence for InfraNodus. |
| **InfraNodus Build Graph** | Sends those sentences to InfraNodus, which finds the key concepts and groups them into topics. This is where your API key goes. |
| **Normalize Graph** | Merges the Ontology Agent's relationships with InfraNodus's key concepts into one graph of nodes and labelled links. |
| **Save Graph** | Saves the graph in your `ci graphs` data table, under the contract's `contract_id`. |

**Flow 2: Ask questions**

| Node | What it does |
|---|---|
| **Chat** | Receives your question from the chat window. |
| **Mode (Graph ON/OFF)** | The switch. It holds a `use_knowledge_graph` setting (`true` or `false`) that decides whether the agent uses the knowledge graph or plain RAG. Use it to compare answers. |
| **Get Graph** | Reads the saved graphs from the `ci graphs` data table. |
| **Pick Contract** | Picks the most recently saved contract and passes along your question, its graph, its search index and the ON/OFF setting. |
| **Orchestration Agent** | The brain. If the graph is ON, it asks the graph what your question connects to and writes an enhanced query. If OFF, it uses your question as it is. Then it gets the chunks and writes a short, one-line answer. |
| **Chat Model** | The OpenAI model (gpt-4.1-mini) that powers the Orchestration Agent and the Retrieval Agent. |
| **knowledge_graph** | A tool that finds the graph nodes your question mentions and follows their connections two steps out. It returns the related nodes and relationships. When the mode is OFF, it returns nothing useful and the agent skips it. |
| **retrieval_agent** | Takes the enhanced query (or your original question, when the graph is OFF), searches the contract and returns the best chunks with their page, section and why they matched. |
| **contract_chunks** | The search tool the Retrieval Agent uses. It looks up the 6 closest chunks in the vector store. |
| **Embeddings (Query)** | Turns the enhanced query into an embedding, so it can be matched against the stored chunks. |

### What is InfraNodus?

**InfraNodus** is a tool that turns text into a knowledge graph. You give it a document, and it finds the key concepts, connects the ones that appear together, and draws them as a graph you can explore. It also groups related concepts into clusters, so you can see at a glance which topics belong together.

You could build a graph like this by hand, but for a 200-page contract that would take days. InfraNodus does it in one step, and it can be called from n8n through an **API key**. In this lab, n8n sends your contract to InfraNodus, gets the graph back, and uses it to answer questions.

Next, you'll set up an account and an API key for it.

---

## Part 4: Create Your InfraNodus API Key

**What it is**: A key that lets n8n send your contract to InfraNodus and get the knowledge graph back.

**Action items**:

1. Go to [infranodus.com](https://infranodus.com) and click **Sign up** (one click).

![assets](images/6.png)

2. Click **Continue with Google**.

![assets](images/7.png)

3. Set a **username**, agree to the **terms and privacy policy** and click **Create account**. Your account is created.

![assets](images/8.png)

4. In the **What brings you here?** popup, select **AI workflows and agents** and click **Continue**.

![assets](images/9.png)

5. Click **Settings** at the top right, then **API & MCP**.

![assets](images/10.png)

6. Click **Create API KEY**.

![assets](images/11.png)

7. Enter a name for the key, for example `contract-review`, and click **Create**.

![assets](images/12.png)

8. **Copy the API key** and save it somewhere safe. You'll need it later in this lab.

> **Note**: Treat the key like a password. Don't share it or paste it into screenshots.

**Output**: You have an InfraNodus API key saved.

---

## Part 5: Import the Workflow

**What it is**: The workflow JSON you downloaded in Prerequisites. The graph-building steps and the question-answering steps are already built and connected.

**Action items**:

1. In n8n, click **+ New Workflow**.
2. Click the **three-dot menu (⋮)** in the top right → **Import from file** (`Cmd+Shift+I` on Mac / `Ctrl+Shift+I` on Windows).
3. Select the workflow JSON you downloaded.

![assets](images/13.png)

**Output**: The nodes appear on the canvas, already connected. One thing is missing: your InfraNodus key.

---

## Part 6: Add Your API Keys

The workflow needs two keys: one for InfraNodus and one for OpenAI.

**Action items**:

1. Open the **InfraNodus Build Graph** node.
2. Under **Headers**, find **Authorization**.
3. In the **Value** field, replace `PASTE_YOUR_INFRANODUS_API_KEY` with your API key. Keep `Bearer ` and the space before it, like this:

```
Bearer YOUR_API_KEY
```

![assets](images/14.png)

4. Select the same credential on the other three OpenAI nodes: **Chat Model**, **Embeddings** and **Embeddings (Query)**.

**Output**: n8n can now talk to both InfraNodus and OpenAI.

---

## Part 7: Create the Data Table for Your Graph

**What it is**: A table inside n8n where the workflow saves the graph it builds, so it can use it when you ask questions.

**Why we need it**: The **Save Graph** node writes the graph to this table, and the **Get Graph** node reads it back when you ask a question. Without it, the graph has nowhere to live.

**Action items**:

1. Click the **n8n logo** in the top left.

![assets](images/16.png)

2. Switch to the **Data tables** tab.

![assets](images/17.png)

3. Click **Create data table**.

![assets](images/18.png)

4. Switch to **Import CSV**, enter the name `ci graphs`, and upload the **ci_graphs.csv** file from Prerequisites. Keep **My CSV file contains a header row** ticked.

![assets](images/19.png)

![assets](images/20.png)

5. Click **Create**. On the next screen you'll see the columns found in the CSV. Click **Create** again.

![assets](images/21.png)

6. The table is created.

![assets](images/22.png)

7. Now go back to your flow: click the **n8n logo** in the top left and select your workflow.

![assets](images/23.png)

8. Open the **Save Graph** node. Under **Data table**, choose **From list**, then select **ci graphs**.

![assets](images/24.png)

![assets](images/25.png)

9. Do the same in the **Get Graph** node (in the chat part of the flow): under **Data table**, choose **From list** and select **ci graphs**.

![assets](images/26.png)

**Output**: Both nodes point to your `ci graphs` table. The workflow is ready to run.

---

## Part 8: Build the Graph and Ask Again

**Action items**:

1. Click **Execute Workflow**. The first flow waits for you to submit the form.

![assets](images/27.png)

Open the **Upload Contract (Form)** and upload the **sample contract** (the Loan Agreement from Prerequisites).

![assets](images/28.png)

2. Click **Submit** and wait until every node in the first flow turns green.

![assets](images/29.png)

3. To see the saved data, click the **n8n logo** in the top left, switch to the **Data tables** tab and click the **ci graphs** table.

![assets](images/30.png)

You'll see a **new row** added for your contract. It holds the graph, the ontology and a summary of the key topics.

![assets](images/31.png)

4. Now go back to your workflow. The second flow (**Part 2 - Ask questions**) is the one that answers. Click **Open chat** and ask the same question from the stress test:

```
What is the interest rate on this loan?
```

![assets](images/32.png)

5. Now open [infranodus.com](https://infranodus.com), **refresh the page** and click the **three parallel lines** in the top left corner. Your graph will be visible.

![assets](images/33.png)

6. Under **Your Text Graphs**, click your graph. It is named `contract-intel-` followed by an ID.

![assets](images/34.png)

7. The graph opens. Click on it and you'll see the **connected nodes**: the spread, the benchmark, the index floor and the other concepts, linked together.

![assets](images/35.png)

**Output**: This time you get the actual rate, not just the formula. The graph connected the spread, the benchmark and the index floor, so nothing was missed.

### Test with the knowledge graph ON and OFF

You can run the same question with and without the knowledge graph and compare the answers. The switch is the **Mode (Graph ON/OFF)** node, between **Chat** and **Get Graph**.

1. Double-click the **Mode (Graph ON/OFF)** node.
2. Under **Fields to Set**, find `use_knowledge_graph` and choose a value:
   - **true**: RAG + knowledge graph. The agent builds an enhanced query from the graph.
   - **false**: RAG only. The agent sends your plain question to the vector store.
3. Close the node, open the chat and ask the same question again.

![assets](images/mode-switch.png)

Try `false` first to see the incomplete answer from plain RAG, then switch to `true` to see the difference. You don't need to upload the contract again, because the graph and the chunks are already saved.

### What happens behind the scenes

![assets](images/36.png)

Your question goes through these steps. You can open the execution and watch each one:

| Step | Node | What it does |
|---|---|---|
| 1 | **Chat** → **Mode (Graph ON/OFF)** → **Get Graph** → **Pick Contract** | Takes your question, adds the ON/OFF setting, loads the saved graphs from the `ci graphs` table and picks the latest contract. |
| 2 | **Orchestration Agent** → `knowledge_graph` tool | *(Only when the mode is ON.)* Sends your original question to the graph. The tool finds the nodes your question mentions (like `Interest Rate`), follows their connections two steps out, and returns up to 50 relationships (source, relation, target, page). |
| 3 | **Orchestration Agent** | *(Only when the mode is ON.)* Writes an **enhanced query** using only what the graph returned. It does not add numbers or facts of its own. For example: *what makes up the interest rate, what it is calculated from, how often it resets and which conditions affect it.* |
| 4 | `retrieval_agent` → `contract_chunks` | Searches the contract's vector store with the enhanced query (or your original question, when the mode is OFF) and sends back the 6 best chunks, each with its page, section and the reason it matched. |
| 5 | **Orchestration Agent** | Answers in one short line, using only those chunks and the graph's values. If neither contains the answer, it says *Not found in the contract*. |

So instead of searching with just "What is the interest rate?", RAG now searches with a query that already names the spread, the benchmark and the floor.

---

## Quick Reference

| Problem | Cause | Fix |
|---|---|---|
| Plain LLM fails on large contracts | The document is too big to send in full | Use RAG |
| Answer gives only part of the interest rate | The pieces are spread across the document and RAG only fetched some | Use a knowledge graph to find what the question connects to |
| InfraNodus step fails | The API key is missing or wrong in the **InfraNodus Build Graph** node | Paste your key after `Bearer ` in the Authorization header |
| **Save Graph** or **Get Graph** shows an error | The node isn't pointing to your data table | Select **ci graphs** with **From list** in both nodes |
| OpenAI nodes show errors | A node is missing the credential | Select the same credential on Ontology Model, Chat Model, Embeddings and Embeddings (Query) |
| Want to compare answers with and without the graph | The graph is used only when the mode is ON | Set `use_knowledge_graph` to `true` or `false` in the **Mode (Graph ON/OFF)** node |
| Chat says no contract found | No contract has been uploaded yet | Run the upload form first, then ask your question |

