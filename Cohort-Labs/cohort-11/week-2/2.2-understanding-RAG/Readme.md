# Lab 2.2: Build Your First RAG Pipeline

![banner](./assets/b.png)

## The Problem

In Lab 2.1, you handed your Week 1 contract agent a real, multi-page document, and it broke. Either it threw this error:

```
Bad Request - input exceeds the context
```

or it answered slowly, missed clauses that were clearly in the document, or replied with something unrelated to your question.

The cause was one block: **Extract From File** pastes the *entire* document into the AI's prompt (the text the AI reads before answering). That's fine for a small sample file. For a 40-page vendor agreement, an 80-page SaaS contract, or a 200-page M&A document, it breaks. The AI is smart enough. The problem is that every model has a hard limit on how much text it can read at once, so pushing a full contract through it is the wrong design.

Lab 2.1 showed you the failure. **This lab fixes it.**

---

## Build a Pipeline That Reads Only What It Needs

You'll build a **RAG pipeline**. It breaks large contracts into small searchable pieces, stores them, and pulls out exactly the right section when someone asks a question, so it never hits the limit.

**Upload contract → cut it into chunks → store them by meaning → find the right chunks for each question → AI answers**

Once you've built RAG, you'll start spotting it in every serious AI product. By the end of this lab, you will:

- Understand what RAG is and why it exists
- Build a two-workflow system: one that ingests large documents, and one that retrieves from them
- Know what vector embeddings are, and why they're more than a buzzword
- Have a live contract Q&A agent that handles large files and remembers what it's been given

---

## Table of Contents

- [The Big Idea: Why RAG Exists](#the-big-idea-why-rag-exists)
- [Understanding RAG: The Complete Picture](#understanding-rag-the-complete-picture)
- [Prerequisites](#prerequisites)
- [Two Ways to Build This](#two-ways-to-build-this)
- [Import the Workflow](#import-the-workflow)
- [Test Everything](#test-everything)
- [What You Learned](#what-you-learned)
- [The Problem with This RAG Setup](#the-problem-with-this-rag-setup)
- [Troubleshooting Steps](#-troubleshooting-steps)

---

## The Big Idea: Why RAG Exists

An AI model only knows what it was trained on. It has never seen your contracts, so on its own it answers from general knowledge. That's not good enough. **RAG (Retrieval Augmented Generation)** fixes this.

**Think of it like this.** You've just joined a law firm as a consultant. You've read thousands of contracts, but not *this* firm's contracts, deals or clients. So before answering any question, you go to the filing room, pull the right folder, read the right pages, and *then* answer.

**That's RAG: the AI goes to the filing room first.**

The filing room is a **vector store**, a database that sorts text by *meaning* rather than alphabetically or by date. When someone asks a question, the system finds the pieces of text closest in meaning, hands them to the AI, and the AI answers from that material.

```
User asks a question
        ↓
System searches the vector store for relevant context
        ↓
Retrieved chunks land in the AI's prompt
        ↓
AI answers from that specific material
```

The system is made of two separate workflows, called pipelines:

| | **Pipeline 1: Ingestion** (the filing) | **Pipeline 2: Retrieval** (the looking-up) |
|---|---|---|
| **When it runs** | Once per document | Every time someone asks a question |
| **What it does** | Breaks the document into chunks, turns each chunk into a vector embedding, and stores it in the vector store | Finds the most relevant chunks, passes them to the AI agent, and the agent answers |

You file a document once and search it as often as you like.

---

## Understanding RAG: The Complete Picture

Want to go deeper? This section explains what RAG stands for, why AI models hit a reading limit, how the two pipelines work step by step, and what a vector actually is. It's optional. You can skip straight to [Prerequisites](#prerequisites) and come back later.

<details>
<summary><b>👉 Click to read the complete picture</b></summary>

<br>

### What the name means

| Word | What it means in practice |
|---|---|
| **Retrieval** | Before the AI answers, it *retrieves* the relevant pieces of your document from a search index |
| **Augmented** | The AI's prompt is *augmented* (extended) with that retrieved context |
| **Generation** | The AI *generates* an answer using both its training knowledge and the retrieved material |

- **Without RAG:** `question → AI → answer (from training only)`
- **With RAG:** `question → search index → relevant chunks → AI → answer (from your document)`

### Why the context window is the bottleneck

A model's **context window** is the most text it can read in one request, like its working memory. Whatever doesn't fit, it doesn't see. It's measured in **tokens**, the small pieces of text a model reads (roughly ¾ of a word each).

| Model | Context Window | Approx. Page Limit |
|---|---|---|
| GPT-4o mini | 128,000 tokens | ~96 pages |
| GPT-4o | 128,000 tokens | ~96 pages |
| Claude Sonnet | 200,000 tokens | ~150 pages |

A 150-page M&A agreement can reach 120,000 tokens by itself. Add the instructions, the chat history and room for the answer, and you're over the limit. The model then errors out or quietly drops whatever doesn't fit.

Even when a contract does fit, sending all of it is:

- **Expensive:** you pay per token. Sending 100,000 tokens to answer a question about payment terms means paying for 99,900 tokens of irrelevant text.
- **Slow:** more tokens take longer to process, so users wait.
- **Less accurate:** research shows models lose focus when buried in irrelevant text. The right clause is in there, but so are 90 pages of noise.

RAG fixes all three by sending only what matters.

### The two pipelines

**Ingestion** (once per document). After this, your 150-page contract lives in the vector store as thousands of small, searchable pieces.

```
PDF Upload
    ↓
Text Extraction (binary → readable text)
    ↓
Chunking (break into ~800 character pieces)
    ↓
Embedding (each chunk → vector of numbers)
    ↓
Vector Store (store the vectors, indexed by meaning)
```

**Retrieval** (every question). The AI never sees the full contract, only the question plus the 5 most relevant chunks: about 3,000–5,000 tokens instead of 100,000. The document isn't made smaller; the AI just reads the part that matters.

```
User Question: "What are the payment terms?"
    ↓
Embed the question (question → vector of numbers)
    ↓
Search the vector store (find chunks with similar vectors)
    ↓
Top 5 most relevant chunks retrieved
    ↓
Chunks + original question → AI model
    ↓
AI answers from the retrieved context
```

### What is a vector, actually?

An **embedding model** turns a piece of text into a long list of numbers, called a **vector**:

```
"Payment is due within 30 days of invoice."
→ [0.23, -0.81, 0.44, 0.12, ..., 0.67]  (1536 numbers)
```

Think of those numbers as a location on a map of meaning (a map with 1,536 dimensions instead of two). Text with similar meaning lands close together, even when the words are different.

So if a user asks *"When do invoices need to be paid?"*, the question gets its own location on the map, and the system returns the nearest chunks. "Payment due within 30 days" and "net-30 payment obligation" both come back, even though neither shares a keyword with the question. This is **semantic search**: matching meaning, not words.

### Putting it together: back to the law firm

A partner asks you: *"What are the termination conditions in the Acme deal?"* You don't answer from memory. You go to the filing room, pull the Acme folder, turn to the termination clause, read it, then answer.

| At the law firm | In RAG |
|---|---|
| The **filing room** | The vector store |
| **Pulling the folder** | Retrieval |
| **Reading the clause** | The retrieved context landing in the AI's prompt |
| **Answering the partner** | Generation |

> The AI is not the filing room. It is the consultant. The vector store is the filing room.

</details>

---

## Prerequisites

✅ The **n8n workflow file**: [download the pre-built workflow JSON](https://drive.google.com/file/d/1bsHT4DsEvLFZv2WPBdnXJoEAfEn9R6Ka/view?usp=sharing) to import into n8n

✅ An **n8n account**: the same one from Lab 2.1. You'll create new workflows inside it.

✅ An **OpenAI API key**: already set up in n8n from Lab 2.1. Add it again only if you're starting fresh.

✅ A **sample contract (PDF)**: [download the contract in PDF format](https://pragyaallc-my.sharepoint.com/:b:/g/personal/sachin_parmar_legalgraph_ai/IQCIDp0RA0UYS7g3WGOXOH0uAaJOpNKBwgibUIiks0hCkpc?e=n0XlBh)

✅ A **sample contract (Docx)**: [download the contract in Docx format](https://pragyaallc-my.sharepoint.com/:w:/g/personal/sachin_parmar_legalgraph_ai/IQAbCBMxqrFrT6hzD6t9oCdpAR8pdsHtVaZf2O5HiyGq5jY?e=4s3M8D). If the PDF gives you an error, use this one instead (see [Troubleshooting](#-troubleshooting-steps)).

---

## Two Ways to Build This

| | **Import the Workflow** | **Build from Scratch** |
|---|---|---|
| **Best for** | Getting up and running fast | Understanding every block and setting |
| **What you do** | Import a ready-made file and add your OpenAI credentials | Add and configure each block yourself |

Both give you the same two workflows. 👉 **[Build from Scratch →](./build-from-scratch/Readme.md)**, then come back here to [Test Everything](#test-everything).

---

## Import the Workflow

**Step 1. Create a new workflow.** Log into n8n and click **"Create Workflow"** to open a blank canvas.

![image](./assets/img-4.png)

**Step 2. Import the ready-made file.** Click the **three-dot menu (⋮)** in the top-right corner, select **"Import from file"**, and choose the JSON file from [Prerequisites](#prerequisites). Both workflows, ingestion and retrieval, load onto the canvas.

![image](./assets/img-5.png)

**Step 3. Add your OpenAI credentials** to the **embedding** and **model** blocks.

---

## Test Everything

### Step 1: Fill the filing room

Open the ingestion workflow, click **"Execute Workflow"**, upload the sample contract and submit. Every block should complete successfully. Do this first: you can't search a filing room that's empty.

![flow](./assets/1.24.png)

### Step 2: Ask it questions

Open the retrieval workflow, click **"Execute Workflow"**, then **"Open Chat"**.

![flow](./assets/1.25.png)

Ask *"What is this contract about?"* and watch the execution in the background: the agent calls the vector store, retrieves the relevant chunks, and builds its answer from them.

![flow](./assets/1.26.png)

Then try:

- *"What are the names of the parties in the contract?"*
- *"Are there any auto-renewal clauses?"*

Every answer comes from the stored document, not the model's general training. The agent is reading from the filing room. Answers look generic? See [Troubleshooting](#-troubleshooting-steps).

---

## What You Learned

![flow](./assets/banner0.png)

- **RAG separates memory from reasoning.** The vector store remembers your documents; the model only reasons over what it's handed. That's what makes the system flexible: swap the model and the store stays; add documents and the model doesn't change.
- **Embeddings turn meaning into coordinates.** Similar meanings sit near each other, which is how a question about "invoice terms" finds "payment obligations".
- **The system message is a routing instruction.** "Always call the vector store first" is a product decision, not a technical one. Without it, the agent decides for itself and won't always get it right. The system message is where you enforce behavior, in every agent you build.
- **Chunking connects large documents to searchable answers.** You can't hand an AI a 200-page contract in one go, so you cut it into pieces. Chunk size is one of the most important choices in RAG: too big and the AI is buried in irrelevant text; too small and the answer lacks context.
- **Two workflows, one system.** Ingestion runs once per document; retrieval runs once per question. Because they're separate, you can change one without touching the other: adjust chunking without changing the chat, or upgrade the chat without reprocessing documents.

---

## The Problem with This RAG Setup

The system works. Now try to break it 🤔 Open the chat and type *"Hi"*.

The agent goes straight to the vector store. It turns "Hi" into a vector, searches every chunk of your contract, pulls the 5 closest matches into the prompt, and after all that, replies *"Hello! How can I help you with the contract?"* **It ran the full retrieval pipeline for a greeting.**

Scale that up. In a 10-message chat with 3 real questions and "thanks", "got it", "ok" in between, every message runs the full pipeline, even the one-word replies. That costs you in three ways:

| Problem | What happens |
|---|---|
| **Token cost** | 5 chunks of ~800 characters is roughly 1,000 extra tokens per message, on top of the question and answer. For "Hi", you paid for 5 clauses about termination and payment schedules that had nothing to do with anything. |
| **Latency** | The embedding call, the search and the bigger prompt all add time. A greeting takes as long as a complex legal question, and users notice. |
| **Noise in the context** | For a vague or casual message, the "closest" chunks are basically random. The model gets irrelevant contract text and has to work around it. |

> **Why does this happen?** Your system message says *"always call the Simple Vector Store tool first."* The agent obeys every time, with no exceptions. It has no way to judge when retrieval is useful and when it isn't.

What you need is an agent that decides for itself: it retrieves when it should, skips it when it shouldn't, and routes each message to the right behavior. That's **Agentic RAG**, and you build it in the next lab.

---

## 🔧 Troubleshooting Steps

Check here before asking for help.

**You see this error when running the workflow with the PDF**

![banner](./assets/9089.png)

1. Open the **Default Data Loader** and change the data format from **PDF** to **Docx**.

![banner](./assets/9000.png)

2. Upload the `.docx` file, not the `.pdf`.

If you're not seeing this error, carry on with the current workflow.

---

**Answers are generic, or the agent says it doesn't have the information**

Check two things: the **Memory Key** in the retrieval tool matches the one from ingestion exactly, and the **same OpenAI embedding credential** is used in both workflows.

---

## What's Next

You've built the core of a document-aware AI system and seen its first limit: it retrieves blindly on every message. In the next lab, you'll give the agent the judgment to decide when to search, when to skip, and how to handle chats that mix contract questions with small talk, without wasting tokens or adding delay.

[Go to Lab 2.3: Agentic RAG →](../2.3-n8n-agenticRAG/Readme.md)
