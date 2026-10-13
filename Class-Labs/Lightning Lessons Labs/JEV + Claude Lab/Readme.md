# Lab: Make Claude Faster and Cheaper with Jev

## Let Jev Decide, Let Claude Write

Say you have a pile of insurance certificates (COIs) and a checklist they all need to meet. You ask Claude to check each one. It works, but Claude reads, thinks and writes a full answer every single time. That's slow, and the cost adds up fast when the pile gets big.

Here's the catch: checking a COI against a checklist isn't writing. It's **deciding**. Pass, fail, or not enough information. And deciding is exactly what Jev is built for.

In this lab you'll run the same check twice, once with Claude alone and once with Jev making the decisions, then compare the results side by side.

Here's the flow for this lab:

- **Run it with Claude only.** See how long it takes and what it costs.
- **Add Jev.** Install the plugin and connect it.
- **Run it again with Jev.** Same documents, same checklist.
- **Compare.** Let the numbers tell you which one wins.

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Part 1: The Problem](#part-1-the-problem)
- [Part 2: The Solution](#part-2-the-solution)
- [Part 3: Set Up the Benchmark Folder](#part-3-set-up-the-benchmark-folder)
- [Part 4: Run the Check with Claude Only](#part-4-run-the-check-with-claude-only)
- [Part 5: Install and Connect Jev](#part-5-install-and-connect-jev)
- [Part 6: Run the Check with Jev and Compare](#part-6-run-the-check-with-jev-and-compare)
- [Next Lab: Extract Key Terms](#next-lab-extract-key-terms)

---

## Prerequisites

✅ **Claude Code Desktop** installed and signed in.

✅ **The benchmark folder.** Download the zip, it has everything you need:

- [coi-benchmark.zip](./coi-benchmark.zip)

It comes with the COI documents, the compliance checklist and the skill that runs the check for you.

---

## Part 1: The Problem

Checking a COI means going through the checklist one line at a time and asking: does this document actually show this? Claude can do it, but it's using a very powerful model that writes full sentences to answer what is really a simple question.

The result:

- **It's expensive.** You pay for all that thinking, on every document.
- **It doesn't scale.** Three COIs is fine. Three thousand is not.

---

## Part 2: The Solution

### What's Jev

**Jev** is a different kind of AI model. It doesn't write anything. You hand it some text and a few questions, and it answers almost instantly, for almost nothing. It's made for **sorting and deciding**.

It can answer in three ways:

- **Pick one** option from a list (like PASS, FAIL or NOT_EVIDENCED).
- **Give a score** on a scale.
- **Say how likely** something is true.

### The Rule

> **Jev decides, Claude writes.**

Jev makes every call. Claude only formats the results into something readable. When you combine them, you get the speed of Jev with the clear writing of Claude.

---

## Part 3: Set Up the Benchmark Folder

1. Download [coi-benchmark.zip](./coi-benchmark.zip).
2. Unzip it.
3. Open the unzipped `coi-benchmark` folder in Claude Code Desktop.

Everything for the check lives in one folder. Once unzipped, you'll see this:

```
coi-benchmark/
│
├── .claude/
│   └── skills/
│       └── coi-benchmark/
│           └── SKILL.md
│
├── coi-documents/
│   ├── AECOM.pdf
│   ├── Caterpillar.pdf
│   ├── Proctor.pdf
│   └── ...any number of COI PDFs
│
├── checklist.csv
│
├── results/
│
└── README.md
```

| Path | What it is | Do you touch it? |
|------|------------|------------------|
| `coi-benchmark/` | The project folder. Open this folder in Claude Code Desktop. | Open it, nothing else |
| `.claude/skills/coi-benchmark/SKILL.md` | The skill behind the `/coi-benchmark` command. It tells Claude how to run the check and build the dashboard. | No |
| `coi-documents/` | The COIs to check. Comes with AECOM, Caterpillar and Proctor. | Yes, add or remove PDFs to change what gets checked |
| `checklist.csv` | The requirements every COI is checked against. | Yes, edit it to change the requirements |
| `results/` | Where each run saves its results. Starts empty. | No, the skill fills it |
| `README.md` | A short guide to the folder. | No |

> **Note:** Open the `coi-benchmark` folder itself, not the folder above it. Claude only finds the skill when this folder is the one you opened.

---

## Part 4: Run the Check with Claude Only

First, set a baseline. Let Claude make every decision on its own.

1. Open Claude Code Desktop and open the `coi-benchmark` folder.
2. Start a new chat.
3. Type this command:

```
/coi-benchmark run with claude
```

Claude checks every COI in `coi-documents/` against `checklist.csv`, saves the run to `results/`, and shows you an **Efficiency Dashboard** with latency, cost and throughput.

![image](./images/8.png)

Keep this run. Jev will be measured against it.

---

## Part 5: Install and Connect Jev

### Install the plugin

In your terminal, run these two commands:

```
claude plugin marketplace add typesafe-ai/skills
claude plugin install typesafe@typesafe-ai
```

![image](./images/3.png)


### Create your API key

Before Claude can reach Jev, you need a Typesafe API key.

1. Go to [https://console.typesafe.ai/](https://console.typesafe.ai/).
2. Enter your email.
3. Agree to the terms and conditions.
![image](./images/5.png)
4. Skip the next steps.
5. Click **Enter console**.
![image](./images/6.png)
6. When asked "Can you chat with Jev, TypeSafe's new model?", click **No**.
7. A message says "TypeSafe only responds with structured decisions". Click **Close**.
8. Click **API keys** in the sidebar.
9. Click **Create API key** and create a new key.
![image](./images/7.png)
10. If your balance shows zero, click **Balance**, then **Add funds**.

> ⚠️ Keep your key private. Don't paste it into any file you might share.

### Add your API key

Now give Claude your key so it can reach Jev. Paste this prompt and replace `TYPESAFE_API_KEY` with your own key when Claude asks for it:

```
i want to add a new kind of AI model called Jev to this workspace. Jev doesn't write anything. you hand it some text plus a few questions, and it answers them almost instantly, for almost nothing. it's made for sorting and deciding.

* Jev is brand new, so you won't know it yet. before anything else, read how it works:
https://docs.typesafe.ai/llms.txt
* i'll use Jev directly through the Typesafe API using a TYPESAFE_API_KEY. follow the official Typesafe docs for the API endpoint, authentication, request format, and response format.
* ask me for my Typesafe API key. keep it somewhere safe on my computer, never inside a file i might share, and never show it back to me.
* Jev can only answer in 3 shapes: pick one option from a list, give a score on a scale, or say how likely something is true. most answers also come back with how sure it is.
* give me full control over when Jev is used. Jev should be off by default and should only be used when i explicitly turn it on or ask to use it. when Jev is off, do not send anything to the Jev API and use the normal model instead.
* do one real test so i can watch it work. make up a short sales email and ask Jev 3 things: how strong a lead is this, what kind of email is it, and does it need a personal reply. show me its answers, how long it took and what it cost. if the test fails, show me the exact error.
* then save what you learned as a reusable skill (or whatever your setup calls a saved instruction), so next time i can say "use Jev to sort these" about any pile of text.

the rule from here on: Jev decides, you write. when Jev isn't sure about something, you make the call yourself. anything you send to Jev leaves my computer, so ask me before sending anything private.
```

> ⚠️ Anything sent to Jev leaves your computer. Never send private documents without checking first.

---

## Part 6: Run the Check with Jev and Compare

Same documents, same checklist. This time Jev makes the decisions.

1. Stay in the `coi-benchmark` folder and start a new chat.
2. Type this command:

```
/coi-benchmark run with jev
```

Jev checks every COI in `coi-documents/`, and Claude only organizes the results. Because your Claude run is already saved in `results/`, you get both side by side in one **Efficiency Dashboard: Claude vs Jev**.

![image](./images/9.png)

### What the Dashboard Measures

The dashboard compares the two runs on three numbers:

| Metric | What it means | Better is | In the example run |
|--------|---------------|-----------|--------------------|
| **Latency** | Total wall-clock time to check all the COIs, from start to finish. | Lower | Claude 19.8 s, Jev 2.8 s |
| **Cost** | What it costs to check all the COIs. | Lower | Claude N/A, Jev $0.00064 |
| **Throughput** | How many COIs get checked per minute. | Higher | Claude 9.07 COIs/min, Jev 63.39 COIs/min |

A few things to know when you read it:

- **Claude's cost shows N/A.** Claude Code doesn't show you the cost of a session inside the chat, so there's no real number for the dashboard to use. Jev's cost is computed from the tokens its API reports back, which is why it has a value.

### What Would Claude's Cost Be?

Since the dashboard can't show it, you can estimate it from Anthropic's [published pricing](https://platform.claude.com/docs/en/about-claude/pricing). Take **3 COIs of 2 pages each, 6 pages in total**:

- **Input:** Anthropic's [PDF docs](https://docs.claude.com/en/docs/build-with-claude/pdf-support) put a page at roughly 1,500 to 3,000 tokens, so 6 pages is about **9,000 to 18,000 tokens**. We'll use about **14,000**, and add about 1,000 for the checklist, so roughly **15,000 input tokens**.
- **Output:** A verdict and a short reason for each of the 21 requirements on each COI comes to roughly **3,000 output tokens**. This is a rough guess, not a measured number.

| Model | Input price | Output price | Estimated cost for 3 COIs |
|-------|-------------|--------------|---------------------------|
| Claude Sonnet 5.5 | $2 / MTok | $10 / MTok | about **$0.06** |
| Claude Opus 5.5 | $4 / MTok | $20 / MTok | about **$0.12** |
| Claude Fable 5.1 | $10 / MTok | $50 / MTok | about **$0.30** |
| **Jev** (measured in the example run) | n/a | n/a | **$0.00064** |

> **Note:** These are estimates, and real sessions usually cost a bit more because of the extra tokens Claude Code uses behind the scenes. Pick the row for the model you're using. At 3 COIs the gap looks tiny, but at 3,000 COIs the same maths turns $0.06 into about $60 and $0.00064 into under $1.

---

## Next Lab: Extract Key Terms

Same COIs, new job. Instead of checking them against a checklist, you'll **pull the key terms out of them**: coverage types, policy limits and important conditions. A router sits in the middle and picks which skill to use. Jev only picks the skill, and Claude does the extraction after.

Start here: [Key Terms Lab](./Key%20Terms%20Lab/Readme.md)

---

## Reference

[Typesafe agent skill docs](https://docs.typesafe.ai/agent-skill)
