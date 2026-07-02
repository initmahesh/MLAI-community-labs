[← Back to Lab 1 Overview](../readme.md)

**Lesson 1** | [Lesson 2 →](../02-skills-and-design-system/readme.md)

---

# Lesson 1 — Project Foundation

![images](./images/banner.png)



## The Problem We Are Solving

Picture a founder at a 20-person SaaS company. A potential enterprise client sends over a 30-page Master Service Agreement. She needs to sign it by end of week. She has no in-house lawyer, so she either spends 90–120 minutes reading every clause herself, or she pays $400 for an hour of legal time to get a summary she barely understands.

She does this 10 times a month. It is slow, expensive, and she still worries she is missing something — an auto-renewal trap, a liability clause that could sink the company, an IP assignment she did not notice.

This is not a rare edge case. It is the daily reality for hundreds of thousands of founders, operations managers, and freelancers who sign NDAs and MSAs without the legal training to know what they are agreeing to.

## The Solution We Are Building

We are building **ContractIQ** — a web application where a user uploads a contract PDF, and within 30 seconds sees a structured breakdown of every term that matters: what it says, where in the document it appears, and how confident the AI is in its reading.

If something looks off, the user can click into that term and see the exact sentence the AI pulled it from. They can also correct it. And when they have a specific question — "what happens if I miss a payment?" — they can ask it in plain English and get an answer grounded in the actual document, not a generic legal explanation from the internet.

The tool does not replace a lawyer for high-stakes situations. It gives people enough understanding to know when they need one — and saves them the hours they would otherwise spend getting to that point.

---

## Step 1 — Fork the Starter Repository

A starter repository has already been set up with the project structure, configuration files, and workflow rules you will need throughout this course. Your first move is to make your own copy of it.

Go to this URL in your browser: [https://github.com/sachin0034-tech/dev-os](https://github.com/sachin0034-tech/dev-os)

![images](./images/1.png)

In the top-right corner of the page, click the **Fork** button. GitHub will ask you where to fork it — select your own account and click **Create fork**.

![images](./images/2.png)

![images](./images/3.png)

---

**Here's the interesting part — what does "forking" actually mean?**

On GitHub, a repository is a project folder stored in the cloud. Every file, every decision, every version of the code lives there. The problem is: it belongs to someone else. You can't save your work into their copy.

Forking creates your own version under your account. Think of it like photocopying a recipe from someone's cookbook — you get the full original, and now you can scribble notes in the margins without touching their book. The original repository stays untouched. Your fork is yours to commit to, experiment on, and share.

> **Learn more:** [GitHub forks →](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)

---

## Step 2 — Clone Your Fork to Your Computer

The fork now exists on GitHub — but it's still in the cloud. To actually work with the files, you need them on your local machine.

Click the green **Code** button on your fork's page, make sure **HTTPS** is selected, and copy the URL shown.

![images](./images/4.png)

Open your terminal and run:

```bash
git clone <paste the URL you copied here>
```

![images](./images/5.png)

---

**You might be wondering — what did that command just do?**

Cloning downloads the entire repository from GitHub onto your machine. It's the difference between a document you can only read online and one you can open, edit, and save locally. From this point on, you work on the local copy and push changes back to GitHub when you are ready to save them.

> **Learn more:** [Git cloning →](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

---

## Step 3 — Open the Project in VS Code

Open VS Code. Go to **File > Open Folder** and select the `dev-os` folder that was just created by the clone command.

![images](./images/6.png)

You will see a file tree on the left side. Here is what each part of the project contains and why it is there.

![images](./images/7.png)

```
dev-os/
├── CLAUDE.md
├── docs/
│   ├── design.md
│   └── ContractIQ_PRD.md
└── skills/
    ├── engineering-planner/
    │   └── SKILL.md
    ├── implementation-specs/
    │   └── SKILL.md
    ├── security-foundation/
    │   └── SKILL.md
    ├── frontend-setup/
    │   └── SKILL.md
    └── design-system/
        └── SKILL.md
```

---

**Here's the interesting part — this project is built to be understood by Claude, not just by you.**

Every file in this structure serves a specific purpose for your AI coding assistant. Let's walk through each one.

---

**`CLAUDE.md`**

This is the instruction manual for Claude Code. Every time you open a Claude Code session inside this project, Claude reads this file first — before doing anything else. It defines what stage of development you're in, which rules apply, and what Claude is allowed to do.

**You might be wondering — why does an AI need a separate instructions file?**

Every new Claude session starts completely fresh. Claude has no memory of what you built yesterday or what decisions you made last week. `CLAUDE.md` solves this. It's a permanent record of your project's rules that Claude re-reads every session, so you never have to re-explain context from scratch.

Think of it as your project's constitution — the rules that stay in effect no matter who is working on it or when.

> **Learn more:** [CLAUDE.md and persistent context →](https://docs.anthropic.com/en/docs/claude-code/memory)

---

**`docs/ContractIQ_PRD.md`**

This is the Product Requirements Document — the same document you've been reading in this lesson. It defines the problem, the users, the features, the database schema, the pricing, and the metrics. Every technical decision in this course traces back to something written here.

When you run a skill like `/engineering-planner`, Claude reads this document to understand what it's building before producing a single line of output. The PRD is the source of truth for everything.

---

**`docs/design.md`**

The design system for ContractIQ — the colors, fonts, spacing rules, and component patterns that every page in the app will follow. When Claude builds a new screen, it refers here first so the product looks and feels consistent without you having to describe the style on every prompt.

---

**`skills/`**

**This is where everything starts to connect.**

The `skills/` folder contains five subfolders, each named after a slash command. Type `/engineering-planner` into Claude Code and Claude reads the `SKILL.md` file inside that folder and follows its instructions exactly — every time, for every session, for every teammate on the project.

Think of a skill like a detailed job description you hand to Claude. Instead of explaining the same task from scratch each session, you write the instructions once and Claude executes them consistently.

Here's what each skill does and when you'll use it:

| Skill | What it does | When you run it |
|-------|-------------|-----------------|
| `/engineering-planner` | Reads the PRD and produces an architecture plan, data models, and API contracts | Lesson 3 |
| `/implementation-specs` | Takes the architecture plan and breaks it into file-by-file build instructions | Lesson 3 |
| `/security-foundation` | Audits the planned code for security gaps before anything ships | Lab 3 |
| `/frontend-setup` | Scaffolds the Next.js application with the design system already baked in | Lab 2 |
| `/design-system` | Enforces the rules in `design.md` at the component level throughout all UI work | Lab 2 |

> **Learn more:** [The Complete Guide to Building Skills for Claude →](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf)

---

Each lesson from here works the same way: you run a skill, review what Claude produces, and move to the next stage only when the output looks right. The `skills/` directory is the engine that drives that flow.

The project is open on your machine and the structure makes sense. But `docs/engineering/` doesn't exist yet — there's no architecture plan, no database schema, no list of files to build. Before writing a single line of code, those documents need to exist. Code improvised without a plan falls apart mid-build; code written from a solid plan holds together.

In Lesson 2, you'll look closely at all five skills and the design system before putting either to use. In Lesson 3, you'll run the first two skills and watch an engineering plan generate itself directly from the PRD.

---

## Claude Concepts Covered in This Lesson

| Concept | Where we covered it | Learn more |
|---------|---------------------|------------|
| **CLAUDE.md** | **Step 3** — "Every time you open a Claude Code session inside this project, Claude reads this file first. It defines what stage of development you're in, which rules apply, and what Claude is allowed to do." | [Claude Code memory →](https://docs.anthropic.com/en/docs/claude-code/memory) |
| **Skills / slash commands** | **Step 3** — "Type `/engineering-planner` into Claude Code and Claude reads the `SKILL.md` file inside that folder and follows its instructions exactly — every time, for every session, for every teammate on the project." | [Skills guide →](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf) |
| **PRD as source of truth** | **Step 3** — "When you run a skill like `/engineering-planner`, Claude reads this document to understand what it's building before producing a single line of output." | [Prompt engineering →](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) |

---

[← Back to Lab 1 Overview](../readme.md)

**Lesson 1** | [Lesson 2 →](../02-skills-and-design-system/readme.md)
