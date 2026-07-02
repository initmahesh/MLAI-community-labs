# Lesson 2.2 — Skills: Stop Rewriting Prompts, Start Running Skills

---

## Where You Are

In Lesson 2.1 you learned how built-in slash commands work — `/init`, `/cost`, `/context` — and why invoking a skill is faster than describing an action. Those are skills Claude Code ships with.

This lesson is about building your own **skills**. Same mechanism, but you define the prompt, the output structure, and the behavior. By the end you'll have three skills — `/market-research`, `/user-research`, and `/prd` — that you'll use in every lesson from 2.3 onward.

---

## The Problem This Lesson Solves

Every time you want to run market research in Claude Code, you probably write something like this:

```
Research the legal AI market. Give me market size, key trends, competitive dynamics,
implications for us, and open questions. Format it with headers. Save the output as
a markdown file. Make sure to include a CAGR estimate and a competitor table...
```

That's 40 words of output structure definition before you even get to the actual research topic. And you write it again next week for a different market. And again the week after.

**Skills fix this.** You define the output structure once — in a `.md` file. From then on, you just type:

```
/market-research legal AI contract review platforms
```

Claude receives the full structure prompt automatically, replaces your topic in the right place, and runs. You never write the output format again.

This is the lesson: **encode your PM workflows once, run them with a single skill forever.**

---

## What Skills Are

A skill is a `.md` file stored in a specific folder. The filename becomes the skill name. The file content becomes the prompt Claude receives when you run it — with `$ARGUMENTS` replaced by whatever you type after the skill name.

| File | Skill | How you run it |
|------|-------|----------------|
| `~/.claude/commands/market-research.md` | `/market-research` | `/market-research legal AI platforms` |
| `~/.claude/commands/user-research.md` | `/user-research` | `/user-research enterprise onboarding` |
| `~/.claude/commands/prd.md` | `/prd` | `/prd AI-powered contract review` |

The key: `$ARGUMENTS` in the file gets replaced by whatever you type after the skill name. The rest — output structure, file naming, formatting rules — is fixed and automatic.

---

## Two Places to Store Skills

Skills live in a folder called `commands/` — that's just the folder name on disk. What matters is what you call them: **skills**.

| Location | Available | Use for |
|----------|-----------|---------|
| `~/.claude/commands/` | Everywhere — all projects, all sessions | Your personal PM toolkit |
| `./.claude/commands/` | This project folder only | Team workflows — commit to git so everyone gets them |

---

## How to Create a Skill

### Step 1 — Create the skill file using Claude Code Desktop

You don't write the file manually. Paste this into Claude Code Desktop and let it create the skill for you:

```
Create the file ~/.claude/commands/market-research.md with the following content:

Conduct a thorough market research report on: $ARGUMENTS

Structure the output EXACTLY as follows:

## Market Research: $ARGUMENTS

### 1. Market Size
- Current market size (TAM, SAM, SOM if applicable)
- Growth rate (CAGR)
- Key data sources / estimates

### 2. Key Trends
- Top 3–5 trends shaping the market right now
- Any emerging shifts (technology, regulation, behavior)

### 3. Competitive Dynamics
- Major players and their positioning
- Market concentration (fragmented vs. consolidated)
- Differentiation strategies in play

### 4. Implications for Us
- Opportunities worth pursuing
- Threats to watch
- Strategic angles based on the data

### 5. What We Still Don't Know
- Data gaps
- Assumptions made
- Areas needing primary research

---

**Open Questions**
- List 3–5 unresolved questions that should inform next steps

---

After completing the research, save the full report as a markdown file in the current working directory with the filename: market-research-<topic-slug>-<YYYY-MM-DD>.md
```

![images](./images/chatone.png)

Claude Code will create the file automatically. No manual editing needed.

> **Why this works:** Claude Code has direct access to your filesystem. You describe what you want — it writes the file to the right location.

![images](./images/etst.png)

---

### Step 2 — Run the skill

![images](./images/testing.png)

```
/market-research legal AI contract review platforms
```

Claude receives the full content of `market-research.md` with `$ARGUMENTS` replaced by `legal AI contract review platforms` — and runs the full structured research automatically.

![images](./images/res.png)

Notice what you did NOT type: output format, file naming rules, section headers, open questions instruction. All of that is already in the skill. You typed the topic. Claude handled the rest.

---

## Create Skills for User Research and PRD

Use the same approach to install two more skills you'll use throughout this bootcamp.

---

**User Research Skill** — paste into Claude Code Desktop:

```
Create the file ~/.claude/commands/user-research.md with the following content:

Conduct a structured user research report on: $ARGUMENTS

Structure the output EXACTLY as follows:

## User Research: $ARGUMENTS

### 1. Research Objective
- What question are we trying to answer?
- Decision this research will inform

### 2. User Persona
- Who was studied (segment, role, context)
- Recruitment criteria

### 3. Jobs to Be Done
- Primary job (functional)
- Secondary jobs (emotional, social)
- Current workarounds / solutions in use

### 4. Key Findings
- Top 3–5 insights from the research
- Direct quotes or evidence for each

### 5. Pain Points & Unmet Needs
- Ranked by frequency and severity
- Gap between current solution and ideal

### 6. Implications for Product
- Features or bets suggested by the findings
- What to build, change, or drop

---

**Open Questions**
- List 3–5 follow-up questions that need more research

---

After completing the report, save it as a markdown file in the current working directory with the filename: user-research-<topic-slug>-<YYYY-MM-DD>.md

Replace spaces with hyphens in the topic slug and use today's date.
```

---

**PRD Skill** — paste into Claude Code Desktop:

```
Create the file ~/.claude/commands/prd.md with the following content:

Write a Product Requirements Document for: $ARGUMENTS

Structure the output EXACTLY as follows:

## PRD: $ARGUMENTS

### 1. Problem Statement
- What problem are we solving and for whom?
- Why does it matter now?

### 2. User Persona
- Primary user segment
- Their context, goals, and constraints

### 3. Jobs to Be Done
- Functional job
- Emotional and social jobs

### 4. Success Metrics
- Primary metric (what moves the needle)
- Secondary metrics (guardrails)
- How we measure and by when

### 5. Requirements

**Must Have (P0)**
- [ ] Requirement 1
- [ ] Requirement 2

**Should Have (P1)**
- [ ] Requirement 3

**Nice to Have (P2)**
- [ ] Requirement 4

### 6. Out of Scope
- Explicitly list what this does NOT cover

### 7. Open Questions
- List 3–5 unresolved decisions that need answers before build

---

After completing the PRD, save it as a markdown file in the current working directory with the filename: prd-<topic-slug>-<YYYY-MM-DD>.md

Replace spaces with hyphens in the topic slug and use today's date.
```

---

Once all three are installed, use them like this:

```
/market-research legal AI contract review platforms
/user-research enterprise onboarding drop-off
/prd AI-powered contract review feature
```

---

## What Happens Behind the Scenes

![images](./images/diagramsystem.png)

**1. You type `/market-research legal AI contract review platforms`**
Claude Code intercepts `/market-research` and finds `~/.claude/commands/market-research.md`.

**2. `$ARGUMENTS` gets replaced**
Every instance of `$ARGUMENTS` in the file is replaced with `legal AI contract review platforms`. The file becomes a fully resolved prompt — your topic dropped into a complete structure.

**3. Your CLAUDE.md is already loaded**
Every session starts by loading your CLAUDE.md. By the time you run any skill, Claude already knows your company, personas, metrics, and working style. The skill output is automatically grounded in your context — no extra briefing needed.

**4. Output is saved automatically**
The skill instructs Claude to save the result as a dated markdown file. No copy-paste, no manual saving. The file lands in your workspace, ready to `@` reference in the next prompt.

---

## Things to Keep in Mind

- **`$ARGUMENTS` is optional.** Skills with no variable run the same way every time — useful for recurring workflows like a weekly standup summary or sprint retrospective.
- **You can use `@` inside skill files.** If a skill references `@company-context/competitive-landscape.md`, that file loads automatically every time the skill runs. Your skills can carry context built into them.
- **Filenames are case-sensitive on Mac and Linux.** Keep all skill filenames lowercase with hyphens: `market-research`, not `MarketResearch`.
- **Skills are just files.** Edit them any time by opening the `.md` file and changing the prompt. No reinstall, no config update needed.

---

## What You've Learned

### The Core Insight
> When you do research in Claude Code, you should never be writing output structure in your prompt. That belongs in a skill file — defined once, applied every time. Your prompt should contain only the topic.

### Key Concepts

**Skills are just `.md` files**
The filename becomes the skill name. The file content becomes the prompt. There is no syntax to learn, no config to edit — just a markdown file in the right folder.

**`$ARGUMENTS` is what makes skills flexible**
Whatever you type after the skill name gets substituted into every `$ARGUMENTS` placeholder in the file. One skill, infinite topics. The structure stays fixed; only the subject changes.

**Two storage locations, two use cases**
- `~/.claude/commands/` — global personal skills, available in every project and session
- `./.claude/commands/` — project-scoped skills, committable to git, shared with your team

**Skills and CLAUDE.md work as a system**
Skills encode *how* to structure output. CLAUDE.md encodes *who you are* and *what your company is*. Every time a skill runs, both are active — the output is automatically structured AND grounded in your specific product, personas, and market context. You don't have to brief Claude before each run.

**You built three PM skills**
- `/market-research [topic]` — full structured market research, saved as a dated file
- `/user-research [topic]` — structured user research with JTBD, findings, and product implications
- `/prd [feature]` — full PRD with requirements, metrics, and open questions

Each one encodes what used to be 30–50 words of prompt boilerplate into a single skill you never have to think about again.

**Skills are just files — edit them any time**
No reinstall. No config refresh. Open the `.md` file, change the prompt, save. The next time you run the skill, it uses the updated version.

---

*Next: [Lesson 2.3 — Market Research: Chaining Prompts](./Lesson2.3-Chaining-Research-Prompts.md)*
