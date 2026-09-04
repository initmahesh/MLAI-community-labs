[← Back to Lab 1 Overview](../readme.md)

[← Lesson 1](../01-project-foundation/readme.md) | **Lesson 2** | [Lesson 3 →](../03-engineering-planning/readme.md)

---

# Lesson 2 — Skills and the Design System

![images](./images/banner.png)

---

## The Problem With Starting From Scratch Every Session

In Lesson 1, you saw the file structure — `CLAUDE.md`, a `docs/` folder, a `skills/` directory with five subfolders.

But there's still a gap between seeing those files and knowing what happens when you actually put them to work.

Here's the problem they solve.

Every time you open a new Claude Code session, it starts completely blank. No memory of the product you're building. No idea what color scheme you chose. No awareness of the coding conventions you established last week.

You could paste in context at the start of every session. But that doesn't scale. What if a teammate opens the project? What if you return three weeks from now? What if you want Claude to follow the exact same process every time — not a slightly different version depending on how well you remembered to explain it?

Real engineering teams face the same challenge with human engineers. They solve it the same way: they write things down.

A **runbook** tells an engineer exactly how to deploy the application — the same steps every time, for every person. A **style guide** tells a designer which colors and fonts to use — no guessing. A **architecture decision record** explains why a technical choice was made, so the next engineer doesn't accidentally undo it.

Skills and the design system are the AI-native version of these documents.

---

## Where You Are in the Process

```
Idea
↓
Research
↓
PRD  ✓
↓
Claude Code Agents  ✓
↓
Engineering Document  ← (we get here in Lesson 4)
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

Today you're not building anything yet. You're understanding the tools before you use them — so that when Lesson 3 starts, you know exactly what's happening and why.

---

## Step 1 — Open a Skill File and Read It

In VS Code, open the file at `skills/engineering-planner/SKILL.md`.

![images](./images/1.png)

Read through it. You're not running anything yet — just reading the plain text inside.

---

**What you're looking at is Claude's job description.**

A skill is a saved set of instructions stored in your project. When you type `/engineering-planner` into Claude Code, Claude finds the `SKILL.md` file inside that folder and follows its instructions exactly — every time, for every session, for every teammate who opens this project.

Think of it like a recipe card. Instead of explaining the dish from scratch every time, you write the recipe once and anyone can cook it consistently. The recipe lives in the project, not in someone's head.

Every `SKILL.md` file follows the same four-section structure:

```
## Purpose
What does this skill do and when should someone run it?

## Inputs
Which files should Claude read before starting? List them by path.

## Instructions
What should Claude do, step by step? Be specific.

## Output
What files should exist when the skill finishes?
```

This gives the skill a clear contract. **Purpose** says what it does. **Inputs** say what it reads. **Instructions** say how it works. **Output** says what proof you have that it finished correctly.

> **Learn more:** [The Complete Guide to Building Skills for Claude →](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf)

---

## Step 2 — Walk Through the 5 Skills in Order

![images](./images/skills.png)

These five skills form a pipeline — the output of each one becomes the input to the next. Understanding that sequence is what makes the whole build make sense.

---

**`/engineering-planner`** — *Run in Lesson 3*

Reads the PRD and turns it into an organized build plan. It figures out which features are essential for launch, maps out all the data the product needs to store and how it connects, and breaks the build into stages so you can ship something working early.

Saves everything to `docs/engineering/` for the next skill to read.

---

**`/implementation-specs`** — *Run in Lab 2, Lesson 1*

Takes the engineering plan and turns it into a detailed blueprint — a room-by-room guide before construction begins. It breaks the build into clear sections, describes exactly what needs to be built in each section and in what order, and flags every place two features have to work together so nothing gets discovered by accident.

Saves everything to `specs/`.

---

**`/frontend-setup`** — *Run in Lab 2, Lesson 1*

Builds the empty shell of the application with the design system already baked in. It reads `docs/design.md` first so brand colors and fonts are built in from day one, creates the folder structure so every future file has a logical home, and sets up the connection to the database.

---

**`/design-system`** — *Used throughout Lab 2*

The skill you'll use most. Every time Claude builds a new screen, this skill makes sure it matches everything else. It reads `docs/design.md` at the start of every session — never works from memory — and uses named colors and spacing values from the design system rather than inventing new ones.

---

**`/security-foundation`** — *Run in Lab 3*

Reviews the plan for security issues before anything ships — like a safety inspector walking through blueprints before construction begins. It checks that private data can only be accessed by the person it belongs to, verifies that uploaded files are validated before being processed, and makes sure secret keys are stored safely.

---

**You might be wondering — why run them in this exact order?**

Because each skill depends on what the previous one produced.

`/engineering-planner` needs the PRD to exist. `/implementation-specs` needs the engineering plan. `/frontend-setup` needs the implementation specs. `/design-system` needs the design file. Skip a step or run them out of order and the later skill has nothing meaningful to read.

Think of it like an assembly line — each station feeds directly into the next. The line only works if every station runs in sequence.

---

## Step 3 — Open the Design System File

Open `docs/design.md` in VS Code.

![images](./images/design.png)

Scroll through it. You'll see colors defined by name, font choices, spacing scales, button shapes, animation rules, and component patterns — all written down before a single page of the app exists.

![images](./images/2.png)

---

**This file is what keeps the entire app visually consistent.**

Without it, here's what happens.

Each page you build drifts slightly from the last. One button is a shade darker than the previous screen. A heading uses a slightly different font weight. Nothing looks broken. Nothing looks *finished* either. The app feels assembled rather than designed.

A design system is a set of visual decisions you make once — colors, fonts, spacing, button shapes — written down so every new screen follows the same rules automatically. In this project, `docs/design.md` is the single source of truth for everything visual.

When Claude builds any screen in Lab 2, it reads this file first so every element matches everything else — without you having to describe your visual style on every prompt.

The `design.md` file is already included in the repository you cloned. If you want to swap it out for your own visual style — using a screenshot, a website URL, or a Figma file — the instructions are here: [How to Create Your Own Design System →](../00-resources/create-design-system.md)

> **Learn more:** [Design systems and Claude →](https://docs.anthropic.com/en/docs/claude-code)

---

## Bonus — Build Your Own Skill

You don't need to build a skill from scratch for this course — the five that ship with the project are everything you need. But if you ever want to create one for a different job, here's how.

**1. Pick one clear job.** One skill, one purpose. If you can't describe what it does in a single sentence, it's not ready.

**2. Create the folder and file.**
```
skills/your-skill-name/
└── SKILL.md
```
The folder name becomes the slash command.

**3. Write the four sections:** Purpose, Inputs, Instructions, Output.

**4. Name your files explicitly.** Don't say "read the design document" — say "read `docs/design.md`". Vague references produce inconsistent results.

**5. Test and refine.** Run the command, review the output, and tighten any instruction that produced something unexpected. Treat `SKILL.md` like code — update it, commit it, iterate.

---

### Let Claude Write the Skill for You

You don't have to write the `SKILL.md` yourself. Copy the prompt below, fill in the blanks, and paste it into Claude Code:

```
I want to create a new Claude Code skill.

Skill name: [what you want to type as a slash command, e.g. brand-voice]

Job: [one sentence — what should this skill do?]
Example: "Review any new page I build and make sure the writing matches our brand tone document."

Reference files: [any files Claude should read before running the skill]
Example: docs/brand.md, docs/PRD.md

Output: [what should exist when the skill finishes?]
Example: A revised version of the page with tone corrections applied.

Please create the folder skills/[skill-name]/ and write a SKILL.md file inside it
with Purpose, Inputs, Instructions, and Output sections.
```

---

## What You Accomplished

You came into this lesson having seen the project structure but not really understanding it.

You're leaving with something more useful: a mental model of exactly how the build pipeline works before a single command has been run.

You know what each skill does and when it runs. You know why the design system exists as a file rather than a set of instructions you paste in every session. You know why the skills run in order and what breaks if they don't.

---

## What's Next

All five skills are loaded. The design system is in place. But nothing has run yet.

`docs/engineering/` doesn't exist. There's no architecture plan, no database schema, no list of files to build. Without those documents, there's no foundation for the code that comes in Lab 2.

In Lesson 3, you'll run `/engineering-planner` for the first time — and watch it translate the PRD into a concrete technical blueprint in a single session. That document is what everything else is built from.

---

## Claude Concepts Covered in This Lesson

| Concept | Where it appeared | Learn more |
|---------|-------------------|------------|
| **Skills / slash commands** | **Step 1** — "When you type `/engineering-planner` into Claude Code, Claude finds the `SKILL.md` file inside that folder and follows its instructions exactly — every time, for every session, for every teammate who opens this project." | [Skills guide →](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf) |
| **SKILL.md structure** | **Step 1** — "Purpose says what it does. Inputs say what it reads. Instructions say how it works. Output says what proof you have it finished." | [Skills guide →](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf) |
| **Stage-gated pipeline** | **Step 2** — "Each skill depends on what the previous one produced. Skip a step or run them out of order and the later skill has nothing meaningful to read." | [Claude Code docs →](https://docs.anthropic.com/en/docs/claude-code) |
| **Design system as persistent visual context** | **Step 3** — "When Claude builds any screen in Lab 2, it reads this file first so every element matches everything else — without you having to describe your brand on every prompt." | [Claude Code docs →](https://docs.anthropic.com/en/docs/claude-code) |

---

[← Back to Lab 1 Overview](../readme.md)

[← Lesson 1](../01-project-foundation/readme.md) | **Lesson 2** | [Lesson 3 →](../03-engineering-planning/readme.md)