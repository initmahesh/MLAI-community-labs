[← Back to Lab 1 Overview](../readme.md)

[← Lesson 2](../02-skills-and-design-system/readme.md) | **Lesson 3**

---

# Lesson 3 — Engineering Planning

![images](./images/banner.png)

## Where We Are

By this point you have:

- **Lesson 1** — Forked the `dev-os` starter repo, cloned it to your machine, and opened it in VS Code. You read the PRD and understood the project structure.
- **Lesson 2** — Learned what Claude Code skills are, explored the five skills in the project, and reviewed the design system in `docs/design.md`.

Now you are going to use the AI to turn that PRD into a concrete engineering plan. Before a single line of application code is written, you need a document that answers: *What are we building, how is it structured, and in what order does it get built?*

This lesson introduces **Plan Mode** — one of the most powerful features in Claude Code — and walks you through running the `/plan` command to produce the engineering documents that all of Lab 2 (Building the Application) depends on.

---

## What Is Plan Mode?

![images](./images/plan.png)

Plan Mode is a special state in Claude Code where the AI is allowed to **read and reason, but not write or change anything**.

When you prefix a prompt with `/plan`, Claude:

1. Reads every file you reference
2. Thinks through the full problem
3. Produces a structured plan as output
4. **Waits for your approval before doing anything**

No files are created. No code is touched. You see the complete plan first and decide whether to approve it or send Claude back to revise.

This matters because AI coding tools are most dangerous when they act before they think. Plan Mode forces a checkpoint. You stay in control of the direction before any work begins.

---

## When to Use Plan Mode

Use `/plan` whenever you are about to start something non-trivial and want to align on the approach before implementation begins.

| Situation | Use `/plan`? |
|---|---|
| Writing a single small function | No — just do it |
| Building a new feature with multiple files | Yes |
| Translating a PRD into architecture documents | Yes |
| Refactoring a module that touches shared state | Yes |
| Fixing a one-line bug | No |
| Starting a new application from scratch | Yes |

The rule of thumb: if reviewing the approach *before* the work would save you time, use Plan Mode.

---

## How Plan Mode Works in Practice

When Claude finishes generating a plan, you will see a structured breakdown — sections, decisions, trade-offs — displayed in the terminal. Claude then pauses and asks whether you want to proceed.

- If the plan looks right, you approve it and Claude carries it out.
- If something is off, you type a correction and Claude revises the plan.
- If you want to start over, you reject it entirely.

Nothing is committed to your files until you say yes.

---

## Step 1 — Open the Project in VS Code

Open VS Code. Go to **File > Open Folder** and select the `dev-os` folder you cloned in Lesson 1.

You should see the file tree on the left with `CLAUDE.md`, `docs/`, and `skills/` visible.

---

## Step 2 — Open a New Terminal

In VS Code, go to **Terminal > New Terminal** (or press `` Ctrl+` ``).

A terminal panel will open at the bottom of the screen, already pointed at your project folder. You will run all commands from here.

![images](./images/4.png)

---

## Step 3 — Launch Claude Code

In the terminal, type:

```bash
claude
```

Claude Code will start and show its interactive prompt. You are now in a Claude Code session scoped to your project. Claude can read all files in the folder and will follow the rules defined in `CLAUDE.md`.


![images](./images/3.png)

---

## Step 4 — Run the Engineering Planning Prompt

Copy and paste the following prompt into the Claude Code terminal:

```
/plan Create an end-to-end engineering document based on the provided @docs/ContractIQ_PRD.md. Your task is to meticulously extract all features and specifications from the PRD and translate them into detailed engineering design elements. Use the @skills/engineering-planner/SKILL.md for creating the doc.
```

Press **Enter**.

![images](./images/4.png)


> **Note:** Claude may ask a few clarifying questions before proceeding — go with the recommended option unless you have a specific reason to change it.

![images](./images/5.png)

---

> **Note:** This step can take 10–15 minutes. Let Claude finish without interrupting — in the meantime, let's discuss the `@` symbol in Claude.

![images](./images/meme.png)


# The `@` File Reference Syntax

The `@` symbol is how you point Claude at a specific file or folder in your project. Instead of copying and pasting content into your prompt, you reference the path — Claude reads it directly.

```
@docs/ContractIQ_PRD.md       → reads a single file
@skills/engineering-planner/  → reads every file inside that folder
```

You can use `@` anywhere in a prompt and chain as many references as you need:

```
Example :

/plan Review @docs/ContractIQ_PRD.md and apply the rules in @skills/engineering-planner/SKILL.md
```

Claude reads each referenced file at the start of the task before it generates any output. This means your prompt stays short, but Claude has the full context of every document you care about.

Use `@` whenever you want Claude to work from your actual project files rather than its own general knowledge. For a task like engineering planning, this is essential — the plan should be grounded in your specific PRD, not a generic template.

---

## What This Prompt Does

There are three parts to this prompt worth understanding:

**`/plan`**
Activates Plan Mode. Claude will read, reason, and show you a plan — but will not write any files until you approve.

**`@docs/ContractIQ_PRD.md`**
Points Claude at the product requirements document. Claude reads every feature, constraint, and data requirement in that file before producing any output — the plan is grounded in what the PRD actually says.

**`@skills/engineering-planner/SKILL.md`**
Points Claude at the engineering-planner skill. Claude reads its instructions for how the output should be structured — what sections to include, what level of detail to capture, and where to save the resulting documents.

---

## What Claude Will Produce

After Claude processes the PRD through the engineering-planner skill, it will generate a plan covering:

- **Architecture Overview** — The system components and how they connect: Next.js frontend, Supabase database, Claude AI API, and file storage.
- **Data Models** — Every database table, its columns, types, relationships, and the Row Level Security rules that control access.
- **API Design** — The server-side routes the application needs, what each one accepts, and what it returns.
- **Feature Breakdown** — Each PRD feature mapped to the specific components, database tables, and API routes required to build it.
- **Build Sequence** — The order in which features should be built so each stage produces something working before the next one starts.

These documents are saved to `docs/engineering/` and become the input for Lab 2, where you run `/implementation-specs` to break each engineering decision into file-by-file build instructions.

![images](./images/6.png)

---

## Reviewing and Approving the Plan

When Claude finishes generating the plan, read through it carefully before approving.

Ask yourself:

- Does the data model capture everything described in the PRD?
- Can every action a user takes in the app — uploading a file, asking a question, viewing results — actually be handled? If a feature exists in the PRD but has no corresponding backend step in the plan, it will silently break later.
- Does the build sequence make sense — does each stage produce something you could actually open in a browser and use, rather than a half-built piece that only works once the next stage is also done?
- Is anything missing that is clearly required by the PRD?

If the plan looks correct, type `yes` or `proceed` to approve it. Claude will then write the engineering documents to `docs/engineering/`.

If you want to adjust something, describe the change and Claude will revise the plan before asking again.

---

## What Gets Saved

Once approved, you will find new files under `docs/engineering/`:

```
docs/
└── engineering
```

These files are the technical foundation for everything that follows. Every future skill — `/implementation-specs`, `/security-foundation`, `/frontend-setup` — reads these documents to understand what has already been decided.

![images](./images/6.png)

---

## The Stage-Gated Principle

Each lesson in this lab — and the two labs that follow it — follows the same pattern:

1. You run a command
2. Claude produces output for your review
3. You approve before anything is committed
4. The output becomes the input for the next stage

This is intentional. Real software projects fail when decisions are made without visibility. By making the plan explicit and reviewable at each stage, you stay in control of what is being built — even when the AI is doing most of the writing.

---

## What You Learned

- **Plan Mode as a safety checkpoint** — `/plan` puts Claude into a read-and-reason-only state; no files are created or changed until you explicitly approve, giving you full visibility into the direction before any work begins.
- **`@` file references in practice** — pointing a prompt at `@docs/ContractIQ_PRD.md` and `@skills/engineering-planner/SKILL.md` grounds Claude's output in your specific documents rather than generic templates.
- **What a complete engineering plan contains** — architecture overview, data models, API design, feature-to-component mapping, and a build sequence that produces something usable at each stage.
- **How to review a plan before approving** — checking that every PRD feature has a corresponding backend step, that the data model captures all the information the app needs to store, and that the build order is logically sequenced.
- **The stage-gated principle in action** — the engineering documents saved to `docs/engineering/` become the direct input for Lab 2's implementation prompts; each stage depends on the previous one being correct.
- **Why catching gaps at the plan stage matters** — a missing table or a circular dependency in the build order is trivial to fix in a document and very expensive to fix after several lessons of code have been written on top of it.

---

## This Lab Is Complete

You now have everything Lab 2 needs:

- A local clone of `dev-os`, open in VS Code
- An understanding of the five skills and the design system
- `docs/engineering/engineering-doc.md` and `docs/engineering/implementation-specs.md`

Continue to **[Lab 2 — Building the Application](../../02-Building-the-Application-Lab/readme.md)**, where you'll scaffold the Next.js app, set up Supabase, and implement everything end to end.

---

[← Back to Lab 1 Overview](../readme.md)

[← Lesson 2](../02-skills-and-design-system/readme.md) | **Lesson 3** | [Continue to Lab 2 →](../../02-Building-the-Application-Lab/readme.md)
