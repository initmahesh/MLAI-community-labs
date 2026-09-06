# Lab 2.1: Why Your Agent Breaks on Real Contracts

In Week 1 you built something real. An AI agent that reads a contract and answers questions about it. It worked. You tested it. It gave you accurate answers from the document.

Now we're going to break it on purpose.

Not because something is wrong with what you built — but because the thing that breaks it is the exact reason RAG exists. Once you see the failure, the solution in Lab 2.2 will make complete sense.

---

## What You're Going to Do

Go back to the agent you built in [Lab 1.1 — Build Your First AI Agent in n8n](../../week-1-pm-agent-lan/1.1%20-%20n8n-agent/readme.md), or you can download the workflow from here:

✅ **Starter workflow file** — [Download n8n-workflow.json](https://pragyaallc-my.sharepoint.com/:u:/g/personal/sachin_parmar_legalgraph_ai/IQCxwBn3DSxjTrx2_WxRoFTeAQ1ni4W0bV2cKybboqYJYC8?e=JQfaYk)

Open the workflow. Before you run it, click the **OpenAI Chat Model** node and make sure the model is set to **`gpt-4o-mini`**. Then run it — but this time, instead of the small sample contract, upload a larger one.

Use any multi-page contract you have access to. A real vendor agreement, an employment contract, an NDA with many clauses. Anything over 30–40 pages works. If you don't have one, [download this larger test contract](https://drive.google.com/file/d/1RMzUyryxh88qiXTW6psH6lEfrhQ8H2ZQ/view).

Ask it the same question you used in Week 1:

*"What are the payment terms?"*

---

## What Happens

You'll see one of two things.

**Option A — a rate limit error:**

```
Bad Request - input exceeds the context
```

![flow](./assets/1.png)

**Option B — a slow, degraded, or incomplete answer:**

The agent responds, but slowly. Or it misses clauses that are clearly in the document. Or it answers a different question than the one you asked.

Both are the same underlying problem showing up differently.

---

## Why This Happens

Here's what your Week 1 workflow actually does under the hood.

When a user uploads a contract, the **Extract From File** node pulls the entire document text out as one giant string. That string then gets pasted directly into the AI Agent's user message field — right next to the user's question:

```
User Query: {{ $('Chat Trigger').item.json.chatInput }}

File Context: {{ $('Extract From File').item.json.text }}
```

For the small sample contract in Week 1, that worked fine. The document was short enough to fit.

But every AI model has a **context window** — a hard limit on how many tokens (roughly: words) it can process in a single request. It's like working memory. The model can only hold so much in its head at once.

| Model | Context Window | Approx. Page Limit |
|---|---|---|
| GPT-3.5 Turbo | 16,000 tokens | ~12 pages |
| GPT-4o mini | 128,000 tokens | ~96 pages |
| GPT-4o | 128,000 tokens | ~96 pages |

A 100-page contract easily hits 80,000–120,000 tokens. Add the system message, the user question, and the expected response — and you're at the limit or over it.

When you go over, one of two things happens:

- The API rejects the request entirely — that's the 429 rate limit error
- The model processes what fits and silently drops the rest — that's the degraded answer

Neither is a bug. Both are the model doing exactly what it's designed to do. The architecture is the problem, not the model.

> Think of it like trying to read a 200-page contract by stuffing every page through a mail slot at once. The slot has a fixed size. Some pages don't make it through. The reader on the other side answers from whatever landed — not the full document.

---

## The Real Problem

Even if you had an infinite context window, sending an entire contract on every single question would be:

- **Expensive.** You're billed per token. Sending 100,000 tokens every time someone asks "what are the payment terms?" costs money for text that has nothing to do with payment terms.
- **Slow.** Processing 100,000 tokens takes time. Your users wait.
- **Unreliable.** Research consistently shows that AI models perform worse when buried in irrelevant context. The relevant clause is in there — but so are 90 pages of unrelated content. The model loses focus.

The current architecture is: *send everything, hope the model finds the right part.*

That's not good enough for production.

---

## What the Fix Looks Like

Instead of sending the whole document every time, the system should:

1. Break the contract into smaller pieces when it's first uploaded
2. Store those pieces in a searchable index
3. When a user asks a question, find only the relevant pieces
4. Send just those pieces to the model — not the whole document

That's RAG. And that's exactly what you'll build in the next lab.

The agent stops being a document reader. It becomes a document searcher.

---

## What You Just Learned

You didn't just see an error. You saw the architectural limit of the approach you built in Week 1 — and why that approach can't scale to real contracts.

**Context windows are finite.** Every model has a token limit. Stuffing an entire document into a single prompt works for small files and breaks for real ones. This isn't a model problem — it's an architecture problem.

**Sending more isn't always better.** More tokens mean more cost, more latency, and often worse answers. Precision beats volume. The model performs best when it gets the right 500 words, not the whole 80 pages.

**The failure was the lesson.** The agent you built in Week 1 is exactly how most people start. And exactly what you'll move past in Lab 2.2.

---

[Go to Lab 2.2: Build Your First RAG Pipeline](../2.2-understanding-RAG/Readme.md)
