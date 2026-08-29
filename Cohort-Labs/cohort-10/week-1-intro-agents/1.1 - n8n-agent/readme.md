# Lab 1.1 : Build Your First AI Agent in n8n

![flow](./assets/banner.png)

You're about to build your first AI agent — one that reads contracts and answers questions about them in plain language.

By the end of this lab, you will:

✦ Have a live AI agent running inside n8n
✦ Understand what a system message is and why it controls everything
✦ Know how to connect OpenAI to your workflow and pick the right model
✦ Be able to upload any document and interrogate it with natural language questions

No coding experience needed. Just a browser, an API key, and about 25 minutes.

---

## What Are We Building?

A **Contract Q&A Chatbot.**

Here's the scenario: a user uploads a contract PDF, types a question, and the agent reads the document and replies with a direct answer — payment terms, termination clauses, renewal conditions, all of it. No scrolling through 40 pages. No legal background required.

Here's how the pieces connect:

1. A **Chat Trigger** — listens for the user's message and receives the uploaded file
2. **Extract From File** — pulls readable text out of the PDF so the AI can work with it
3. An **AI Agent** — takes the user's question + the extracted text, reasons over both, and writes a response
4. An **OpenAI Chat Model** — the actual intelligence powering the reasoning

Each of these is a node in n8n. You'll add them one by one, connect them, and watch the data flow through. Let's get into it.

---

## A Quick Mental Model Before You Start

Think of n8n like an assembly line. Each station (node) does one specific job and hands the result to the next station. The data moves left to right input goes in one end, processed output comes out the other.

Your agent is not magic. It's a chain of simple steps:

```
User sends message + file
        ↓
Chat Trigger receives it
        ↓
Extract From File pulls the text out
        ↓
AI Agent reads the text + question, writes an answer
        ↓
Response goes back to the user
```

Once you see it this way, every agent you'll ever build is just a variation of this pattern.

---

## Prerequisites

Make sure you have all four of these before starting:

✅ An **n8n account** — sign up free at n8n.io, the cloud version works fine. [Follow this setup guide](../../week%200%20%20-%20foundation/n8n-loginSetup/Doc.md) to create and configure your account.

✅ An **OpenAI API key** — go to platform.openai.com, create an account, and generate a key under API Keys. [Watch this video](https://youtu.be/J3y1dOpz9R4?si=fBqIP0TTShbH_6-n) for a step-by-step walkthrough.

✅ The **starter workflow file** — [download n8n-workflow.json](https://pragyaallc-my.sharepoint.com/:u:/g/personal/sachin_parmar_legalgraph_ai/IQCxwBn3DSxjTrx2_WxRoFTeAQ1ni4W0bV2cKybboqYJYC8?e=JQfaYk)

✅ The **sample contract PDF** — [download the sample contract](https://pragyaallc-my.sharepoint.com/:b:/g/personal/sachin_parmar_legalgraph_ai/IQC2WQJhhIuyRq5JrVY13FwNAdwS4M5gB5w-qzBAm9V4mRQ?e=XyvLU4) (a fictional vendor agreement we've prepared for this lab)

> ✓ Tip. n8n gives you a small free OpenAI credit when you start. It's enough to get going, but it won't last through all the labs. Add $5 of credits to your OpenAI account now and you won't have to think about it again.

---

## Two Ways to Build This

| | **Path A: Import the Workflow** | **Path B: Build from Scratch** |
|---|---|---|
| **Best for** | Getting up and running fast | Understanding every component |
| **Time** | ~5 minutes | ~25 minutes |
| **What you do** | Import a pre-built file and configure it | Add and connect each node yourself |

Both paths produce the same working agent. Path B is recommended if this is your first time — building it node by node is how you actually internalize how agents work.

---

## Path A: Import the Workflow

**Step 1. Create a new workflow.**

Open your n8n account and click **"Create Workflow"** in the top right. You'll land on a blank canvas — this is your build surface.

![flow](./assets/create-workflow.png)

---

**Step 2. Import the starter file.**

Click the **three-dot menu (⋮)** at the top right, select **"Import from File"**, and upload the `n8n-workflow.json` file from the prerequisites.

Your canvas will populate with all the nodes already connected.

![flow](./assets/import-workflow.png)

---

**Step 3. Verify the connections.**

Every node should be linked with a visible line. If anything looks disconnected, drag the small circle on the right edge of that node and connect it to the next one.

![flow](./assets/connected-nodes.png)

> ✓ Tip. If your agent isn't responding, the first thing to check is always node connections. One broken link stops the entire workflow silently.

---

**Step 4. Add your OpenAI API key.**

Click the **"OpenAI Chat Model"** node. In the settings panel, click **"Credential"** → **"Create New Credential"** → paste your API key → Save.

n8n encrypts and stores it. You won't need to paste it again across any of the labs.

![flow](./assets/add-api-key.gif)

> ★ Your API key is tied to your OpenAI billing account. Never paste it into a public file or share it in a message. Treat it like a password.

> ★ **Save your API key before you paste it here.** Once you save a credential in n8n, the key is encrypted — you cannot view or retrieve it again. Copy it to a password manager or a secure note *before* entering it. If you lose it, you'll need to generate a new one from platform.openai.com and update the credential.

---

**Step 5. Open the chat and test.**

Click **"Open Chat"** at the bottom of the canvas. Upload the sample contract PDF and ask: *"What are the payment terms?"*

Jump to the **Testing Your Agent** section at the bottom to try more questions.

---

## Path B: Build from Scratch

This is the path that actually teaches you something. You'll add each node yourself, connect them, and see exactly what each one contributes. By the end, you'll understand not just *how* it works but *why* it's built this way.

Open n8n, click **"Create Workflow"**, and let's go.

---

### Step 1. Add the Chat Trigger

Every workflow needs a starting point — something that tells n8n "start running now." That's what a **Trigger** does.

Click **"Add Node"** on the canvas.

![flow](./assets/9.png)

Search for **Chat Trigger** and select it.

![flow](./assets/1.png)

> **Why a Chat Trigger?** Because we're building a chatbot. The Chat Trigger is what listens for incoming messages. Every time a user sends something — whether it's a question or an uploaded file — this node wakes up and kicks off the rest of the workflow. No trigger, no workflow. It's the on-switch.

---

### Step 2. Set the Event to "On a New Chat Message"

Click on the trigger node's output point and select **"On a new chat message"** as the event type.

![flow](./assets/2.png)

> **What's an event?** Triggers don't just activate randomly — they listen for a specific thing to happen. In this case, the event is a new chat message arriving. When it does, n8n fires the workflow. You could have other triggers listen for emails, form submissions, webhook calls, or a timer. The event type determines what activates your agent.

---

### Step 3. Allow File Uploads

Right now the chat can only receive text. We need it to also accept a PDF. Inside the Chat Trigger settings, click **"Add Field"** and enable **"Allow File Upload"**.

![flow](./assets/12.png)

![flow](./assets/3.png)

> **Why do we need this?** Our agent needs to read a contract — and contracts live in PDF files, not in text boxes. Enabling file upload is what gives users the ability to hand the document to the agent. Without this, the chatbot is just... a chatbot. With it, it becomes a document-aware assistant.

---

### Step 4. Test the Trigger

Before building further, let's confirm the trigger is actually working.

Click **"Open Chat"** at the bottom of the canvas. Upload the sample contract and type any question — it doesn't matter what yet.

![flow](./assets/13.png)

Now click on the Chat Trigger node in the canvas. You'll see exactly what it captured.

![flow](./assets/4.png)

![flow](./assets/5.png)

> **What you're looking at:** The node received two things — your text message (as a readable string) and the uploaded file (as binary data). Binary data is raw file bytes — it's not readable text yet. That's the problem we solve in the next step. The agent can't read binary; it needs actual words. This is exactly why Extract From File exists.

---

### Step 5. Add the Extract From File Node

Here's something most people don't think about: when a user uploads a PDF, the file doesn't arrive as readable text. It arrives as **binary data** — the raw bytes that make up the file. Your AI model can't read bytes. It needs actual words. So before we can hand the contract to the agent, we need to extract the text out of it first.

That's exactly what this node does. Click **"Add Node"**, search for **Extract From File**, and select it.

You'll see a list of actions — choose **"Extract from PDF"**.

![flow](./assets/6.png)

> **Why this node?** Think of it like this: the PDF is a locked box and the file contents are inside. The Chat Trigger hands us the box. Extract From File is the key — it opens it and pulls out the readable text. Once we have the text, the AI can reason over it like any other document. Without this step, the agent would receive raw bytes it can't understand, and your workflow would fail silently.

---

### Step 6. Configure the File Input

Inside the Extract From File settings, find **"Input Binary Field"** and set it to `data0`.

![flow](./assets/14.png)

> **What is `data0`?** When the Chat Trigger receives a file, it stores it internally under the key `data0`. That's the name n8n gives the first attached file. You can see it in the left panel after running the trigger. By telling Extract From File to look at `data0`, you're pointing it to exactly where the file is sitting. If you upload multiple files, they'd be `data1`, `data2`, and so on.

---

### Step 7. Test the Extraction

Let's confirm it's working. Open the chat again, upload the contract, and send a query. Then click the Extract From File node.

![flow](./assets/7.png)

You should now see the full text content of the contract in the output — every clause, every paragraph, all of it as readable text. That's exactly what gets handed to the AI in the next step.

> ✓ If you see text in the output, you're good to continue. If you see an error, double-check that the Input Binary Field is set to `data0` and that the file you uploaded is a PDF.

---

### Step 8. Add the AI Agent Node

Here's where things get interesting. Click **"Add Node"**, search for **Agent**, and select it. Connect it to the Extract From File node.

![flow](./assets/8.png)

> **What is an Agent node?** This is the brain of the workflow. The Agent node takes inputs — in our case, the user's question and the extracted contract text — combines them with a set of instructions (the system message), and sends everything to an AI model. The model reads it all and writes back a response. The Agent node is the orchestrator. It doesn't do the reasoning itself — it packages everything up and hands it to the model.

---

### Step 9. Configure the User Message

Before you touch anything, here's the most important concept in this entire lab — the difference between a **System Message** and a **User Message**. These two fields control everything the agent does.

| | **System Message** | **User Message** |
|---|---|---|
| **What it is** | The agent's standing instructions — its role, rules, and how it should respond | The question or input from the person using the agent |
| **Who writes it** | You, the builder | The end user, at runtime |
| **When it runs** | Once, before every conversation starts | Every time the user sends a message |
| **Example** | "You are a contract review expert. Only answer from the contract. Always cite the clause." | "What are the payment terms in this contract?" |
| **Think of it as** | The job description you give a new hire | The task you give them on a given day |

The system message shapes every single response. The user message is what changes each time someone asks a question. You control the system message completely — and that's where all the product decisions live.

Now let's configure both.

Inside the Agent settings, find **"Source for Prompt (User Message)"** and set it to **"Define Below"**.

Then click **"Add Option"** and add a **System Message** field.

You now have two inputs to fill: the user message and the system message.

![flow](./assets/15.png)

In the **User Message** field, add both of these:

```
User Query: {{ $('Chat Trigger').item.json.chatInput }}

File Context: {{ $('Extract From File').item.json.text }}
```

![flow](./assets/10.gif)

> **What's happening here?** The double curly braces `{{ }}` are n8n expressions — they pull live data from other nodes. The first line grabs exactly what the user typed in the chat. The second line grabs the full contract text from the extraction step. You're now combining both into a single prompt that the AI receives. The model will see the user's question and the entire document side by side, and reason over both at once.

---

### Step 10. Write the System Message

This is the most important part of the entire lab.

The system message is the agent's job description. It tells the model who it is, what it should do, what it should never do, and how it should format its answers. You write it once and it runs at the start of every conversation.

In the **System Message** field, paste this:

```
Role
You are an AI Contract Assistant.

Instructions
1. Always use the contract content provided before answering.
2. Search for relevant clauses based on the user query.
3. Extract only the most relevant contract content.
4. If multiple clauses match, use the most relevant one.
5. Answer directly and concisely. Do not explain your internal process.
6. If no information is found, say: "This information is not mentioned in the contract."

Guardrails
1. Never make assumptions.
2. Never provide legal advice.
3. Never answer without checking the contract first.
4. If contract language is unclear, say: "This may need professional legal review."
5. Never say things like "I searched the contract", "Based on my analysis", or "I extracted..."

Response Format
Answer: [Direct answer]
Evidence: [Relevant clause/section]
```

![flow](./assets/16.png)

> **Why does this prompt matter so much?** The model has no idea who it is or what it's for until you tell it. Without a system message, it would answer any question, from any domain, based on its general training — including making things up. The system message is what transforms a general-purpose AI into a focused contract assistant. The guardrails stop hallucination. The response format ensures answers are always grounded in the document. This is the single highest-leverage thing you control as a PM building on AI.

---

### Step 11. Add the Language Model

The Agent node knows how to orchestrate. But it needs a brain to do the actual reasoning. That's the language model.

Click **"Add Node"**, search for **Language Model**, and choose **"OpenAI Chat Model"**. Connect it to the Agent node as a sub-node (it attaches below the agent, not inline).

![flow](./assets/11.png)

> **Why is this separate?** Because the model is swappable. Today you're using OpenAI. Tomorrow you might want to use Claude or a local model. By keeping the model as its own node, you can swap it without touching anything else in the workflow. This modularity is the entire point of building in n8n.

**Which model should you select?** Inside the OpenAI Chat Model node, open the **Model** dropdown and select **`gpt-5-mini`**.

| Model | Best for | Relative cost |
|---|---|---|
| **gpt-5-mini** | Document Q&A, clause extraction, structured output — this lab | Low |
| **gpt-4.1-mini** | Fallback if gpt-5-mini isn't available on your account tier | Lower |
| **gpt-4.1-nano** | Maximum cost savings — simpler documents, less precise extraction | Lowest |

> **Why gpt-5-mini for this lab?** Three reasons: speed, cost, and fit. Our agent's job is narrow — extract relevant clauses and answer a direct question. That doesn't require the full reasoning depth of gpt-4.1. gpt-5-mini handles document Q&A well, costs significantly less per token, and responds faster. Model selection is always a cost-capability trade-off. As your agents grow more complex — multi-step reasoning, conflicting clauses, long contracts — you'll revisit this decision.

---

### Step 12. Add Your OpenAI API Key

Inside the OpenAI Chat Model settings, click **"Credential"** → **"Create New Credential"** → paste your API key → Save.

![flow](./assets/add-api-key.gif)

> **What is an API key?** It's how OpenAI knows who's making the request and which account to charge. When n8n sends your prompt to OpenAI, it includes your key in the request. OpenAI's servers verify it, run the model, and send the response back. The whole round trip — question in, answer out — happens in about a second. You pay per round trip, which is why model choice is a cost decision as much as a capability one.

> ★ **Save your API key before you paste it.** Once stored in n8n, the key is encrypted and cannot be viewed or retrieved again. Copy it to a password manager *before* entering it here. If you lose it, you'll need to generate a new key from platform.openai.com — your old one won't be recoverable.

---

## Testing Your Agent

Your agent is live. Open the chat, upload the sample contract, and try these one at a time:

*"What is this contract about?"*

*"What are the key terms I should know before signing?"*

*"What happens if either party wants to terminate early?"*

*"Are there any auto-renewal clauses?"*

Watch how it responds — specific, grounded in the document, citing the actual clause. That consistency isn't accidental. It's exactly what the system message told it to do.

![flow](./assets/agent-response.png)

> **Why doesn't it make things up?** Because the system message told it to only answer from the contract, and the user message contains the entire contract text. This technique is called **grounding** — you constrain the model to reason over a specific source rather than its general training knowledge. Grounding is one of the most important reliability patterns in production AI. Without it, models hallucinate. With it, they stay on topic and cite their sources.

---

## What You Built

![flow](./assets/design.png)

You just built a working AI agent from scratch. Here's what you now understand that most people don't:

**Triggers are the on-switch.** Every workflow needs something that says "start now." The Chat Trigger listens for messages and fires the workflow. Change the trigger and you change when and how the agent activates.

**Binary data needs processing.** A PDF file isn't readable text — it's bytes. Extract From File is what converts it. Skip this step and the AI sees gibberish. This pattern (receive → process → pass forward) repeats constantly in agent building.

**The Agent node is the orchestrator.** It doesn't reason on its own — it packages the user's question, the document context, and the system instructions, then hands everything to the model. Understanding what it assembles is how you debug and improve agent behavior.

**The system message is where product decisions live.** Tone, scope, guardrails, output format — all of it comes from one block of plain text you wrote. Two agents running the same model can behave completely differently because of their system messages. This is the PM's highest-leverage tool.

**Models are swappable.** The OpenAI node is just one option. Swap it for Claude, Gemini, or a local model without touching the rest of the workflow. This is why the architecture separates orchestration from reasoning.

---

## Known Issues

These are the most common problems learners hit in this lab. Check here before asking for help.

---

**OpenAI credits exhausted**

Your agent stops responding with an error like `429 - You exceeded your current quota` or `insufficient_quota`. This means your OpenAI account has no remaining credits.

Fix: go to **platform.openai.com → Billing → Add payment method** and add $5 of credits. Your API key stays the same — just retry in n8n once billing is active.

> ✓ Tip. n8n gives you a small OpenAI credit when you start. It's enough for a few test runs but won't last through all the labs. Add credits now and you won't have to think about it mid-session.

---

**Model not available — permission error**

You may see an error like `model_not_found` or `The model does not exist or you do not have access to it`. This usually means your OpenAI account hasn't been granted access to that model tier.

Fix: go to **platform.openai.com → Settings → Limits** and verify which models your account can access. Free-tier and new accounts often have restrictions. If `gpt-5-mini` is blocked, try `gpt-3.5-turbo` as a fallback while your account upgrades.

---

> ✓ This list grows as cohort members surface new issues. If you hit something not covered here, bring it to the session — it'll be added for the next cohort.

---

## What's Next

In the next lab, you'll take this same concept and build it as a real prototype using **Claude Code** — moving from a visual canvas to actual working code.

Save this n8n workflow. You'll come back to it.

---

[→ Continue to Lab 1.2: Build Your First Prototype with Claude Code](../1.2%20-%20claude-prototype/readme.md)
