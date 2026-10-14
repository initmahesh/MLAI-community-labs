# Lab: Set Up Your Jev API Key

**Jev** is a **System 1** model from [Typesafe](https://docs.typesafe.ai/agent-skill): built for fast decisions, not writing, it picks an option, scores it, or gives a probability in an instant.

In this lab, you'll install the Jev plugin, create your Typesafe API key, connect it to Claude, and run a quick test.

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Step 1: Install the Jev Plugin](#step-1-install-the-jev-plugin)
- [Step 2: Create Your API Key](#step-2-create-your-api-key)
- [Step 3: Add Your API Key to Claude](#step-3-add-your-api-key-to-claude)
- [Step 4: Check the Test Results](#step-4-check-the-test-results)
- [What You Learned](#what-you-learned)
- [Reference](#reference)

---

## Prerequisites

✅ **Claude Code Desktop** installed and signed in.

✅ **Claude Code available in your terminal.** You'll run two `claude plugin` commands in Step 1.

---

## Step 1: Install the Jev Plugin

The plugin is what teaches Claude about Jev: what it can do and how to call it.

In your terminal, run these two commands:

```
claude plugin marketplace add typesafe-ai/skills
claude plugin install typesafe@typesafe-ai
```

The first command adds Typesafe's skill marketplace. The second installs the Typesafe plugin from it.

![image](./images/2.png)

---

## Step 2: Create Your API Key

Before Claude can reach Jev, you need a Typesafe API key.

1. Go to [https://console.typesafe.ai/](https://console.typesafe.ai/).
2. Enter your email.
3. Agree to the terms and conditions.

![image](./images/3.png)

4. Skip the next steps.
5. Click **Enter console**.

![image](./images/4.png)

6. When asked "Can you chat with Jev, TypeSafe's new model?", click **No**.
7. A message says "TypeSafe only responds with structured decisions". Click **Close**.
8. Click **API keys** in the sidebar.
9. Click **Create API key** and create a new key.

![image](./images/5.png)

10. Copy the key and keep it somewhere safe for the next step.
11. If your balance shows zero, click **Balance**, then **Add funds**.

![image](./images/6.png)

> ⚠️ Keep your key private. Don't paste it into any file you might share, and never commit it to GitHub.

---

## Step 3: Add Your API Key to Claude

Now give Claude your key. Open Claude Code Desktop, start a new chat, and paste this prompt. When Claude asks for your API key, paste the one you just created.

```
I want to integrate Jev, a fast, low-cost AI model for classification, scoring, and decision-making, into my existing Claude Code workspace.

1. Understand Jev
First, read the official documentation: https://docs.typesafe.ai/llms.txt

2. Set Up the API
Connect Jev using the official Typesafe API and TYPESAFE_API_KEY. Ask me for my API key, store it securely on my computer, and never expose or commit it.

3. Configure Jev
Jev supports three operations: Choice, Score, and Probability. Keep Jev OFF by default and use it only when I explicitly request it. Otherwise, use Claude normally.

4. Run a Real Test
Create a sample sales email and use Jev to evaluate:
- Lead quality
- Email type
- Whether a personalized reply is needed

Show actual responses, confidence scores, latency, and available cost. If the test fails, show the exact error.

5. Create a Reusable Skill
Save the working integration as a Claude Code skill so I can invoke it anytime by saying "Use Jev to sort these."

Important Rules:
- Jev decides, Claude writes.
- If Jev is uncertain, Claude makes the final decision.
- Always ask permission before sending private data to Jev.
```

Here is what each part of the prompt does:

| Part | What it does |
|------|--------------|
| **1. Understand Jev** | Claude reads Typesafe's docs first, so it uses the API correctly. |
| **2. Set Up the API** | Claude asks for your key and stores it on your computer instead of in your project. |
| **3. Configure Jev** | Jev stays off unless you ask for it. The three operations are **Choice** (pick an option), **Score** (rate something) and **Probability** (how likely is it). |
| **4. Run a Real Test** | Claude sends a sample email to Jev, so you see a real response before trusting it. |
| **5. Create a Reusable Skill** | The working setup is saved as a skill, so you can call Jev later with one sentence. |

![image](./images/7.png)

> ⚠️ Anything sent to Jev leaves your computer. Never send private documents without checking first.

---

## Step 4: Check the Test Results

Claude runs the sample sales email through Jev and shows you the results. You should see:

| What to look for | What it tells you |
|------------------|-------------------|
| **Lead quality** | A Choice or Score decision from Jev, for example high or low. |
| **Email type** | A Choice decision, for example inquiry, complaint or follow-up. |
| **Personalized reply needed** | A yes or no decision, with how likely Jev thinks it is. |
| **Confidence scores** | How sure Jev is about each decision. |
| **Latency** | How long each call took. Expect well under a second. |
| **Cost** | What the calls cost, worked out from the tokens the API reports back. |

![image](./images/8.png)

Then confirm the skill was saved. Start a **new chat** and type:

```
Use Jev to sort these.
```

Claude should recognise the saved skill and ask you what to sort and whether it can send the data to Jev.

![image](./images/9.png)

**If the test fails,** Claude shows the exact error. These are the usual causes:

| Problem | Likely cause | Fix |
|---------|--------------|-----|
| Authentication error (401) | The key was copied wrongly or has extra spaces. | Create a new key in the console and give it to Claude again. |
| Balance or payment error | Your balance is zero. | In the console, click **Balance**, then **Add funds**. |
| Claude doesn't know what Jev is | The plugin isn't installed. | Run the two commands in [Step 1](#step-1-install-the-jev-plugin) again, then start a new chat. |

---

## What You Learned

- **Jev needs a plugin and a key.** The plugin teaches Claude how to call it, and the key is what lets the calls through.
- **Jev is off by default.** It only runs when you ask for it, so Claude keeps working as usual otherwise.
- **Jev makes three kinds of decisions.** Choice, Score and Probability.
- **Jev decides, Claude writes.** If Jev is unsure, Claude makes the final call.
- **Your key stays private.** It's stored on your computer, never in a project you share.

---

## Reference

- [Typesafe agent skill docs](https://docs.typesafe.ai/agent-skill)
- [Typesafe LLM docs](https://docs.typesafe.ai/llms.txt)
- [Typesafe console](https://console.typesafe.ai/)
