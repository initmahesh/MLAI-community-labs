# Lab 2.4 -  Run the Full PM Loop with Claude Skills

![banner](./assets/11.png)

You're a PM at a property management company. The legal team keeps missing lease renewal deadlines. Compliance violations are piling up. A senior stakeholder walks into your office and says: "We should build a tool for this."

Now it's your job to figure out whether that's actually true.

Is this a real problem worth solving? Who exactly has it? What should the product do? And is your spec tight enough to hand to engineering without it falling apart the moment a developer asks a clarifying question?

That's the full PM loop. And in this lab, you're going to run it — for a real use case called a **Compliance Lease Tool** — using Claude Skills to do the heavy lifting at every step.

By the end of this lab, you will:

- Understand what Claude Skills are and why they exist
- Know when to use each skill in a real PM workflow
- Have run market research, user research, a PRD, and a PRD review on a single use case
- See how four skills chain together into a complete discovery-to-spec process

---

## Before You Start

> **A note of thanks:** A big thank you to our mentor, who has worked behind the scenes to make these skills more advanced and useful. Several skills have been updated and improved beyond what you'll find elsewhere — that extra polish is entirely their effort. We're grateful for the time and expertise they've put in to make this lab a better learning experience for everyone.

### Install the skills

Make sure you have all four skills installed in Claude. If you haven't done this yet, go to [How to Add Skills to Claude](../../week%200%20%20-%20foundation/how-to-add-skills-to-claude/readme.md) first and install:

- [`/market-research`](https://pragyaallc-my.sharepoint.com/:t:/g/personal/sachin_parmar_legalgraph_ai/IQCwxLJr3-XKTqU_Xo9ktzMlARtfX5VuIeD4dvhfm3adAw8?e=z6cbPU) — [Click here to download](https://pragyaallc-my.sharepoint.com/:t:/g/personal/sachin_parmar_legalgraph_ai/IQCwxLJr3-XKTqU_Xo9ktzMlARtfX5VuIeD4dvhfm3adAw8?e=z6cbPU)
- [`/user-research`](https://pragyaallc-my.sharepoint.com/:t:/g/personal/sachin_parmar_legalgraph_ai/IQBPyAg9PRnPRLl8FAjilaatAbZcPQa13cR03K-BzxfSRRw?e=sZKa6g) — [Click here to download](https://pragyaallc-my.sharepoint.com/:t:/g/personal/sachin_parmar_legalgraph_ai/IQBPyAg9PRnPRLl8FAjilaatAbZcPQa13cR03K-BzxfSRRw?e=sZKa6g)
- [`/prd`](https://pragyaallc-my.sharepoint.com/:u:/g/personal/sachin_parmar_legalgraph_ai/IQD-iEZXjtZvToj0fHILqJNwAf_o0T-WDD8Omf5NA263sh0?e=NTtQd0) — [Click here to download](https://pragyaallc-my.sharepoint.com/:u:/g/personal/sachin_parmar_legalgraph_ai/IQD-iEZXjtZvToj0fHILqJNwAf_o0T-WDD8Omf5NA263sh0?e=NTtQd0) 
- [`/prd-eval`](https://pragyaallc-my.sharepoint.com/:t:/g/personal/sachin_parmar_legalgraph_ai/IQAyfjRxdSesTrKfM8Ve_DTlAfFycMQrxZzPZiWQlhT081A?e=aghFMh) — [Click here to download](https://pragyaallc-my.sharepoint.com/:t:/g/personal/sachin_parmar_legalgraph_ai/IQAyfjRxdSesTrKfM8Ve_DTlAfFycMQrxZzPZiWQlhT081A?e=aghFMh)


---

### Create your project workspace

Every report you generate in this lab should live in one place — a dedicated project folder in Claude. This keeps all four outputs together so you can reference earlier work as you move through the loop.

**Step 1.** On your Desktop, create a new folder called `compliance-lease-tool`.

**Step 2.** Open the Claude desktop app. Click on the Choose a folder.

![flow](./assets/1.png)


From this point on, run every skill from inside this project. Each report will be saved to the folder and available in all future conversations within the project.

> This is how professional PM teams use Claude — not as a series of one-off chats, but as a persistent workspace where every output is stored, searchable, and connected. By the end of this lab, your project folder will contain four documents that tell the full story of the Compliance Lease Tool from market landscape to reviewed specification.

---

## What Are Claude Skills?

Before we build anything, here's the mental model.

A Claude Skill is a saved prompt you trigger with a slash command. When you type `/market-research`, Claude doesn't just answer generically — it follows a specific framework, outputs in a specific format, and covers specific sections every time.

Think of it like hiring a specialist. You could ask a generalist "tell me about the market for lease compliance tools" and get a paragraph. Or you could engage a market research analyst who always delivers: market size, key players, trends, whitespace, and strategic implications — in a consistent format you can act on.

That's what a skill does. It turns Claude from a conversational tool into a structured analyst.

| Without Skills | With Skills |
|---|---|
| Different output every session | Same structure, every time |
| You direct every step | One command runs the whole framework |
| Easy to miss sections | Built-in completeness |
| Hard to share with teammates | Standardized across your team |

The four skills in this lab map directly to the PM workflow. You'll use them in order — and by the end, you'll have a full picture of the problem, the users, and the product.

---

## What Happens Behind the Scenes

When you type a skill command in Claude Cowork, it doesn't just generate text. It runs a structured process you can actually watch in real time.

Here's what happens, step by step:

**1. Claude reads the skill and builds a plan.**

Before doing anything, Claude reads the instructions saved in your skill file and creates an execution plan. You'll see this appear in the **Progress** section on the left side of the screen — a list of steps Claude intends to take to complete the task.

![flow](./assets/12.png)

This is Claude thinking out loud before it acts. Each step in the plan maps to a section of the skill's output — for example, a market research skill might plan: research market size → identify key players → find whitespace → assess buying motion → write strategic summary.

**2. Claude works through the plan step by step.**

Watch the Progress section as Claude runs. Each step checks off as it completes. You can see exactly where Claude is in the process at any moment — it's not a black box.

![flow](./assets/12.png)

**3. Claude uses tools when it needs them.**

Skills don't just generate from training knowledge. When a skill needs current information — live market data, recent competitor news, pricing pages — Claude automatically calls **Web Search** to pull it in.

You'll see this appear in the Progress section as a tool call:

```
Searching the web for: "lease compliance software market size 2024"
Searching the web for: "proptech compliance SaaS competitors"
```

![flow](./assets/12.png)

Claude decides on its own when a web search is needed. You don't trigger it manually — the skill's instructions tell it when to reach for live data vs. when to reason from what it already knows.

**4. Claude assembles the final report.**

Once all the steps are complete, Claude combines everything — the plan outputs, the search results, its own reasoning — into the structured report the skill defines. What lands in the chat is the finished document, not the working notes.

> This is what separates a skill from a prompt. A prompt asks Claude to do something once. A skill gives Claude a repeatable process with defined steps, built-in tool use, and a consistent output format. The plan you see in Progress is that process running live.

---

## The Use Case: Compliance Lease Tool

Here's the context you'll be working with throughout this lab.

A property management company manages 200+ commercial leases across multiple cities. Each lease has renewal windows, compliance obligations, and regulatory requirements tied to local law. Right now, everything lives in spreadsheets. The legal team tracks deadlines manually. Things get missed. When they do, the company faces penalties.

The ask from leadership: build a tool that tracks lease compliance automatically, flags upcoming deadlines, and alerts the right people before anything is violated.

That's the idea. But an idea from leadership is not a product. It's a hypothesis. Your job starts here.

---

## Step 1: Market Research

### Why market research comes first

Before you talk to a single user or write a single requirement, you need to answer one question: is this a real problem at scale, or is it a problem unique to this company?

If the market is crowded with mature solutions, you're not building a product — you're rebuilding something that already exists. If the market is empty, it might mean opportunity, or it might mean no one actually wants this. Either way, you can't make that call without looking at the landscape first.

Market research tells you: what's out there, who's buying it, what they're paying for it, and where the gaps are. It's the difference between building into a market and building into a void.

### Run the skill

Open Claude Cowork and type:

```
/market-research Compliance Lease Tool for commercial property management — a SaaS product that tracks lease compliance obligations, renewal deadlines, and regulatory requirements across a portfolio of leases

After the report is complete, save it as a file called market-research-report.md in the project workspace.
```

![flow](./assets/2.png)

Claude will run the full market research framework. Read the output carefully. Look for:

- How big is this market? Is it growing?
- Who are the existing players? What do they cover well, and what do they miss?
- What does the whitespace look like — where is no one playing?
- What's the buying motion? Who in an organization pays for this?

> The output of this step is not a decision. It's a map. You're orienting yourself before you take a single step. PMs who skip this end up building products that already exist or building for markets too small to matter. Ten minutes of market research saves months of wasted engineering.

![flow](./assets/3.png)

---

## Step 2: User Research

### Why user research comes after market research

The market tells you what's out there. Users tell you what's actually broken.

These are different things. A market might have ten products and still have a problem no one has solved well. Or a market might look empty because users have learned to live with the problem rather than buy software for it.

User research is how you move from "there might be something here" to "here is specifically what people struggle with and what they wish they had." Without it, you're writing requirements based on what you think users need — which is almost always wrong in some important way.


### Run the skill

This step runs as three separate messages. Follow them in order.

**Message 1 — trigger the skill:**

```
/user-research and Save this report as a file called user-research-report.md in the project workspace.
```

![flow](./assets/4.png)

**Message 2 — when Claude asks for your research input, paste this exactly:**

```
Lease Administrator (8 years in commercial real estate):
"I manage renewal dates in a shared Google Sheet. Every Monday morning I check it manually. Last quarter I missed a 90-day notice window on a downtown property because the sheet wasn't updated after a lease amendment. That cost us a $40,000 penalty. I need something that updates automatically when leases change and sends me reminders before it's too late — not after."

Legal Compliance Officer (works across 3 cities with different regulations):
"The hardest part is that lease compliance isn't the same in every jurisdiction. What I have to track in San Francisco is completely different from what I track in Austin. No tool handles this. They give me one template and expect me to make it work everywhere. I end up maintaining separate tracking systems per city. It's a mess."

Portfolio Manager (oversees 200+ leases):
"I don't need to see every lease. I need a dashboard that tells me what needs my attention today. Red, amber, green. That's it. Right now I get a 40-row spreadsheet emailed to me every Friday and I have to find the urgent items myself. I've asked the team to highlight them in red but half the time they don't."
```

![flow](./assets/5.png)



Read the output. Look for:

- What are the top pain points across all three users?
- Are they asking for the same thing or different things?
- What would a solution need to do at minimum to solve the core problem?
- What would make it genuinely better than what they have today?

> User research is where your assumptions go to die — in a good way. You came in thinking the product was about "tracking deadlines." The users just told you it's about jurisdiction-specific compliance, automatic updates on lease changes, and a prioritized attention dashboard. Those are different requirements. You wouldn't have known that without asking.

---

## Step 3: Write the PRD

### Why the PRD comes after research

Research gives you understanding. A PRD gives engineering something to build.

These are not the same document. A research readout says "users struggle with multi-jurisdiction compliance tracking." A PRD says "the system will maintain a compliance rule library per jurisdiction, allow admins to map leases to jurisdictions, and flag items where the applicable rule has changed since the last review." One is an insight. The other is a specification.

The PRD is where you make the hard decisions: what's in scope and what isn't, what the product does and what it doesn't, what success looks like and how you'll measure it. Without a PRD, engineering builds their best guess of what you meant. With a PRD, everyone is working from the same document.

### Run the skill

This is where saving your earlier reports pays off. You already have the market research and user research in the project workspace — no need to retype anything.

Before you run the skill, there's one concept to know: the **@ symbol**.

In Claude, typing `@` followed by a filename attaches that file directly into your message as context. Claude reads the full contents of the file before it responds — the same way you'd attach a document to an email. You don't have to paste anything. You just reference it.

![flow](./assets/6.png)

This step runs as two messages.

**Message 1 — trigger the skill and attach your saved reports using @:**

```
/prd

@market-research-report.md @user-research-report.md

Use these two reports as your research input. The product is a Compliance Lease Tool for commercial property management.Save this PRD as a file called prd-v1.md in the project workspace.
```

When you type `@`, Claude will show a dropdown of files available in your project workspace. Select `market-research-report.md` first, then `user-research-report.md`. Both will be attached as context before the skill runs.

![flow](./assets/7.png)



Claude will read both reports and generate a full PRD from them: problem statement, goals, user personas, feature requirements, out of scope, success metrics, and open questions — all grounded in the research you already ran.

![flow](./assets/8.png)

---

## Step 4: PRD Eval

### Why you always review your own PRD

You wrote the PRD. That means you're the worst person to review it.

When you write a document, your brain fills in the gaps automatically. You know what you meant, so you read what you meant — not what you actually wrote. An engineer reading the same doc doesn't have that context. They'll find every ambiguity. The question is whether they find it before they start building or after they've built the wrong thing.

The PRD Eval skill acts like a senior PM reading your draft before it goes to engineering. It looks for: missing sections, vague requirements, undefined edge cases, unmeasurable success metrics, and scope that's too wide to ship in a reasonable timeframe.

### Run the skill

No copy-pasting needed. Use `@` to attach the PRD file directly, the same way you did in Step 3.

**Message 1 — trigger the skill and attach your PRD:**

```
/prd-evaluator @prd-compliance-lease-tool.md. Save this evaluation as a file called prd-eval-report.md in the project workspace.
```

When you type `@`, select `prd-compliance-lease-tool.md` from the dropdown. Claude will read the full document before running the evaluation.

![flow](./assets/9.png)


Read the feedback carefully. Look for:

- What sections are flagged as incomplete or ambiguous?
- Which requirements could an engineer interpret in more than one way?
- Are the success metrics actually measurable?
- What's in scope that probably shouldn't be in a v1?

Go back to your PRD, address the gaps, and run `/prd-evaluator @prd-compliance-lease-tool.md` again on the updated file.

> Running the eval twice — before and after revisions — is where the real value is. The first pass shows you what's missing. The second pass confirms you've closed the gaps.

![flow](./assets/10.png)

---

## What You Just Built

You ran the full PM loop on a real product idea — from "someone told me we should build this" to a reviewed, gap-closed product specification.

**Market research sets the context.** You entered the problem with a map of the competitive landscape, an understanding of who buys this category of product, and a sense of where the gaps are. You didn't write a single requirement without knowing what already exists.

**User research replaces assumptions with evidence.** Three users told you exactly what's broken and what they need. The requirements you wrote in the PRD came from their words — not from what you assumed they'd want.

**The PRD translates insight into specification.** Research tells you what to build. The PRD tells engineering how to build it. One without the other stalls. Research with no spec stays in a deck. A spec with no research ships the wrong thing.

**PRD Eval catches what you can't see.** You're too close to your own work to find its gaps. A structured review before the doc goes to engineering is one of the highest-leverage habits a PM can build. It takes 10 minutes and saves days of mid-sprint clarification.

**Skills make the process repeatable.** You ran four different frameworks with four slash commands. The next product idea you evaluate — next week, next month, on a different team — runs through the exact same process. Consistent inputs produce consistent quality.

---

