# Lesson — Creating Claude Code Agents

![images](./images/banner.png)

---

As projects grow, Claude starts doing very different kinds of work.

One task might require turning a PRD into an engineering plan. Another might require reviewing that plan for missing requirements. Later, Claude may need to create implementation specs or test whether the application matches those specs.

You *could* keep giving one Claude session a different role every time.

But that creates a problem: every task starts with new instructions, responsibilities get mixed together, and the same Claude that created something may also be the one deciding whether its own work is correct.

A better approach is to create **specialized agents**.

Each agent gets one clear job, its own instructions, and its own project memory.

In this lesson, you'll create the agents that will be used throughout the next stages of the project.

You will **only create them here**. You will not run them yet.

---

## Where You Are in the Process

You've already prepared the project files that Claude will work from.

Now you're setting up the engineering team that will use those files later.

```
Idea
↓
Research
↓
PRD  ✓
↓
Claude Code Agents  ← YOU ARE HERE
↓
Engineering Document  
↓
Implementation Specs
↓
Build
↓
Memory Layer
↓
Deployment
↓
Iteration
```

By the end of this lesson, your project will contain reusable Claude Code agents ready for later labs.

---

## What Is a Claude Code Agent?

A **Claude Code subagent** is a specialized Claude with a specific responsibility.

Think about a real software team.

A senior engineer may design the system. Another engineer reviews the design. Someone else turns the design into implementation tasks. A QA engineer tests what was built.

They are all engineers — but they do different jobs.

Claude Code agents work the same way.

Instead of giving one Claude every responsibility, you create focused roles such as:

```text
engineering-planner
engineering-reviewer
spec-generator
testing-agent
```

Each agent knows what it is responsible for when you invoke it later.

---

## Agent vs Workflow

An **agent** and a **workflow** are related, but they are not the same thing.

An agent is the worker.

A workflow is the sequence of work.

For example:

```text
engineering-planner
```

is an agent.

But:

```text
engineering-planner

↓

engineering-reviewer

↓

spec-generator

↓

testing-agent
```

is a workflow.

| Concept | Meaning | Example |
|---|---|---|
| **Agent** | A specialized AI worker | `engineering-reviewer` |
| **Workflow** | The order in which work happens | Plan → Review → Spec → Test |

The simplest way to remember it:

```text
Agent = WHO does the work

Workflow = HOW the work moves
```

In this lesson, we're creating the **agents**.

You'll use them as part of workflows in later lessons.

---

## The Agents We Are Building

Our future engineering process will look like this:

```text
PRD
 ↓
engineering-planner
 ↓
Engineering Document
 ↓
engineering-reviewer
 ↓
Approved Engineering Document
 ↓
implementation-spec-planner
 ↓
implementation-spec-reviewer
 ↓
Implementation Specs
 ↓
Build
 ↓
testing-agent
 ↓
Test Results
```

Today, we're only preparing the agents.

No engineering document, specs, or tests should be generated in this lesson.

---

## Why Separate the Planner and Reviewer?

Imagine asking someone:

> Write this architecture document, then tell me whether your architecture document is correct.

They may miss the same thing twice.

Instead, we'll use two responsibilities:

```text
engineering-planner
        ↓
      creates

engineering-reviewer
        ↓
      checks
```

The planner's job is to create a complete engineering document.

The reviewer's job is to independently compare that document with the original PRD.

This is similar to how real engineering teams use design reviews: one person creates the proposal and another person checks it for missing requirements, incorrect assumptions, or technical gaps.

---

## What Is Agent Memory?

Agents may be used many times throughout a project.

Without memory, useful decisions from previous runs can be lost.

We'll configure the agents with:

```text
memory: project
```

This gives each agent persistent project-level memory.

For example, the reviewer may later remember that:

```text
- retention requirements need explicit validation
- privacy rules must be checked during review
- a previous review found a missing edge case
```

The planner can remember planning decisions.

The testing agent can remember important test findings.

This keeps useful context attached to the agent that needs it.

---

## Step 1 — Open the Project in VS Code

Open VS Code.

Go to **File > Open Folder** and select your project folder.

You should see project files such as:

```text
CLAUDE.md

docs/
└── ContractIQ_PRD.md

skills/
└── engineering-planner/
    └── SKILL.md
```


---

## Step 2 — Open a New Terminal

In VS Code, go to **Terminal > New Terminal**.

A terminal panel will open at the bottom of the screen.

![images](./images/1.png)

---

## Step 3 — Launch Claude Code

In the terminal, run:

```bash
claude
```

Press **Enter**.

Claude Code will start inside your current project.

![images](./images/3.png)

---

## Step 4 — Create the Engineering Agents

The first two agents work together during engineering planning:

- `engineering-planner`
- `engineering-reviewer`

Copy and paste this prompt into Claude Code:

```text
Create two project-level Claude Code subagents with `memory: project`. Only create the agents; do not run them.

**1. engineering-planner**

* Run only when explicitly invoked.
* Read `docs/ContractIQ_PRD.md` fully and strictly follow `skills/engineering-planner/SKILL.md`.
* Generate **only** `docs/engineering/engineering-doc.md`. Do not create implementation specs or other documents.
* Extract every PRD requirement into an internal checklist, including functional, technical, data, security, privacy, retention, user-flow, edge-case, constraint, and acceptance requirements.
* Write the engineering doc, then compare it against the PRD requirement-by-requirement.
* If ANY requirement is missing, vague, incorrect, conflicting, or not technically addressed, fix the document and check again.
* Repeat this self-review → fix cycle until every PRD requirement is fully covered.
* Only after reaching zero gaps, invoke `engineering-reviewer`.
* Store important decisions and run history in project memory.

**2. engineering-reviewer**

* Independently compare `docs/ContractIQ_PRD.md` with `docs/engineering/engineering-doc.md` requirement-by-requirement.
* Return `👍 😊 APPROVED` only when there are zero gaps; otherwise return `❌ NEEDS REVISION` with exact issues.
* If revision is needed, send all issues to `engineering-planner`, which must fix them and invoke the reviewer again.
* Repeat until `👍 😊 APPROVED`.
* Store review history in project memory.

Create both agents under `.claude/agents/` and stop. **Do not generate any document until `engineering-planner` is explicitly invoked.**
```

Press **Enter**.


---

## What Claude Just Created

Claude should create:

```text
.claude/
└── agents/
    ├── engineering-planner.md
    └── engineering-reviewer.md
```

![images](./images/2.png)

Notice what **didn't** happen.

Claude did not create:

```text
docs/engineering/engineering-doc.md
```

That's intentional.

You have created the workers, but you haven't given them work yet.

Think of it like hiring an engineer and writing their job description. Hiring them does not automatically mean they start building the application.

---

## What Is Inside an Agent File?

Open:

```text
.claude/agents/engineering-planner.md
```

You'll see configuration describing the agent and instructions describing its responsibility.

One important setting is:

```text
memory: project
```

The rest of the file acts like the agent's **job description**.

It explains what the agent should read, what it should produce, and what rules it must follow when invoked.

![images](./images/4.png)

Now open:

```text
.claude/agents/engineering-reviewer.md
```

Notice that it has a different responsibility.

The planner creates.

The reviewer checks.

They are separate agents because they have separate jobs.

---

## Step 5 — Create the Implementation Spec Agents

Later, after the engineering document has been reviewed and approved, we'll need to convert it into implementation-ready specs.

For that, we'll create two agents: one creates the spec and one independently reviews it.

Paste:

```text
Create two project-level Claude Code subagents with `memory: project`. Only create the agents; do not run them.

**1. implementation-spec-planner**

* Run only when explicitly invoked.
* Read `docs/ContractIQ_PRD.md` and `docs/engineering/engineering-doc.md`.
* Strictly follow `skills/implementation-specs/SKILL.md`.
* Generate only the implementation specification under `docs/implementation/`.
* Cover every feature, workflow, technical requirement, API, database change, frontend/backend detail, edge case, and acceptance criterion from both the PRD and engineering doc.
* Before finishing, compare the spec against both source documents requirement-by-requirement.
* If anything is missing, vague, conflicting, or incomplete, fix it and check again.
* Repeat this self-review → fix loop until there are zero gaps.
* Only then invoke `implementation-spec-reviewer`.
* Store important decisions and run history in project memory.

**2. implementation-spec-reviewer**

* Independently compare the generated implementation spec against both `docs/ContractIQ_PRD.md` and `docs/engineering/engineering-doc.md`.
* Return `👍 😊 APPROVED` only if everything is fully and correctly covered.
* Otherwise return `❌ NEEDS REVISION` with exact gaps.
* If revision is needed, send all issues back to `implementation-spec-planner` and repeat until approved.
* Store review history in project memory.

Create both agents under `.claude/agents/` and stop. Do not generate the implementation spec until `implementation-spec-planner` is explicitly invoked.
```

Press **Enter**.


Your agents folder should now contain:

```text
.claude/
└── agents/
    ├── engineering-planner.md
    ├── engineering-reviewer.md
    ├── implementation-spec-planner.md
    └── implementation-spec-reviewer.md
```

---

## Step 6 — Create the Testing Agent

The final agent will be used after features have been implemented.

Its responsibility will be to verify that the implementation matches what was planned.

Paste:

```text
Create a project-level Claude Code subagent named `testing-agent` with `memory: project`. Only create it; do not run it.

When invoked:
- Read the PRD, engineering doc, and implementation spec.
- Test the actual application against every requirement, including features, flows, APIs, DB, frontend/backend, edge cases, security, and acceptance criteria.
- Do not mark anything passed without evidence.
- Generate `docs/testing/testing-report.md` with a requirement checklist using `✅ PASS`, `❌ FAIL`, or `⚠️ PARTIAL`, including evidence/issues.
- Return `👍 😊 ALL REQUIREMENTS VERIFIED` only if everything passes; otherwise report the gaps.
- Store important findings and run history in project memory.

Create it under `.claude/agents/` and stop. Run only when explicitly invoked.
```

Press **Enter**.


---

## What Gets Saved

Once all agents are created, your project should contain:

```text
.claude/
└── agents/
    ├── engineering-planner.md
    ├── engineering-reviewer.md
    ├── implementation-spec-planner.md
    ├── implementation-spec-reviewer.md
    └── testing-agent.md
```


These files are reusable.

You don't need to rewrite all of these instructions every time you want Claude to perform one of these roles.

Later, you'll simply invoke the relevant agent.

---

## Agent vs Skill

There is one more distinction worth understanding.

The engineering planner will use:

```text
skills/engineering-planner/SKILL.md
```

But the skill and the agent are not the same thing.

A **skill** describes how a type of work should be done.

An **agent** is the specialized worker responsible for doing that work.

Think of it like this:

```text
Agent = Engineer

Skill = Playbook the engineer follows
```

For our planner:

```text
engineering-planner agent
          ↓
         uses
          ↓
engineering-planner skill
```

So:

```text
Skill    → HOW the work should be done

Agent    → WHO performs the work

Workflow → WHAT happens next
```

---

## How These Agents Will Be Used Later

We are not running the agents in this lesson.

But in later lessons, the workflow will become:

```text
engineering-planner
        ↓
engineering-doc.md
        ↓
engineering-reviewer
        ↓
   👍 APPROVED
        ↓
implementation-spec-planner
        ↓
implementation-spec-reviewer
        ↓
implementation specs
        ↓
      Build
        ↓
testing-agent
        ↓
   test results
```

The output of one stage becomes the input to the next.

This keeps each stage focused and reviewable.

---

## How Real Engineering Teams Do This

The agents you created roughly match responsibilities found on real engineering teams.

| Claude Agent | Similar Engineering Responsibility |
|---|---|
| `engineering-planner` | Tech Lead / Architect |
| `engineering-reviewer` | Technical Reviewer |
| `implementation-spec-planner` | Implementation Planning |
| `implementation-spec-reviewer` | Implementation Review |
| `testing-agent` | QA / Testing |

The goal isn't to perfectly reproduce an organization chart.

The goal is to give important work **clear ownership**.

Instead of asking one Claude to constantly switch roles, each agent has a specific responsibility and persistent project memory.

---

## The Stage-Gated Principle

The agents you created will eventually work in stages:

```text
Plan
 ↓
Review
 ↓
Spec
 ↓
Build
 ↓
Test
```

Each stage depends on the output of the stage before it.

This matters because mistakes become more expensive the further they travel.

A missing requirement found during engineering review may take a few lines to correct.

The same missing requirement found after the application is built may require changes to the database, APIs, frontend, and tests.

The agents help perform the work.

The workflow controls **when that work should happen**.

---

## Claude Concepts Covered in This Lesson

| Concept | Where it appeared | Learn more |
|---------|-------------------|------------|
| **Claude Code subagents** | **Step 4** — Creating `engineering-planner` and `engineering-reviewer` as separate, focused workers instead of one general-purpose Claude. | [Claude Code docs →](https://docs.anthropic.com/en/docs/claude-code) |
| **Project-level agent memory (`memory: project`)** | **What Is Agent Memory?** — Configuring each agent to persist decisions and run history across invocations. | [Claude Code docs →](https://docs.anthropic.com/en/docs/claude-code) |
| **Agent-to-agent delegation** | **Step 4** — `engineering-planner` invokes `engineering-reviewer`, and revision requests flow back from reviewer to planner. | [Claude Code docs →](https://docs.anthropic.com/en/docs/claude-code) |
| **Skills as agent instructions** | **Agent vs Skill** — The `engineering-planner` agent follows `skills/engineering-planner/SKILL.md` as its playbook. | [Claude Code docs →](https://docs.anthropic.com/en/docs/claude-code) |

---

[← Back to Lab 1 Overview](../readme.md)

[← Lesson 2](../02-skills-and-design-system/readme.md) | **Lesson 3** | [Lesson 4 →](../04-engineering-planning/readme.md)