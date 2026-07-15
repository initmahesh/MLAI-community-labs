# Setting Up Your Second Brain Folder Structure

---

Before we build anything, let's talk about where everything is going to live.

Think about the last time you started a new project. You probably had files scattered across your Desktop, a Downloads folder full of random things, maybe a few docs in Google Drive, and some notes somewhere you can't remember. By week two, half your time was spent finding things instead of building things.

Now imagine working alongside Claude every day on a growing data lake project. Claude can only help you as well as your workspace allows. If your files have no structure, Claude has no structure to work with.

This is why we set up a **Second Brain** before doing anything.

---

## Download the Template

You can download a copy of the exact Second Brain folder structure used in this course and replace the company files with your own:

> **[Download Second Brain Template](#)** ← add your link here

Open it, swap out the company folders and files with your own projects, and you're ready to go.

---

## Today's Concept: The Second Brain

The folder we're creating is called `second-brain`.

It's not just a catchy name. The idea comes from the personal knowledge management world — a "second brain" is a trusted external system where you store everything you're working on, so your actual brain doesn't have to hold it all.

For us, it means one folder that contains:

- A place for raw channel data as it comes in — immutable, never modified
- A place for structured company and project documents you write and maintain
- A place for Claude skill files that power your pipeline
- A place for completed work worth keeping

Here's the structure we're building today:

```
second-brain/
  ├── raw/
  ├── projects/
  ├── skill/
  └── Archive/
```

> **What about `wiki/`?** The wiki folder is created automatically when you run the `build-wiki.md` skill in a later lesson. You don't create it manually — Claude builds it for you.

---

## The Full Structure

Here's what the complete Second Brain looks like once everything is in place:

```
second-brain/
│
├── raw/                          ← immutable source data (ingested by push skill)
│   ├── LinkedIn-initmahesh.json
│   ├── MaheshAIPMCommunity.json
│   └── MaheshAIPMCommunity-topics.json
│
├── projects/                     ← company and project knowledge docs
│   ├── allneurons/
│   │   ├── company-overview.md
│   │   ├── product.md
│   │   └── user-persona.md
│   ├── legalgraph/
│   │   ├── company-overview.md
│   │   ├── product.md
│   │   └── user-persona.md
│   └── maven/
│       ├── course-bootcamp.md
│       └── course-genaipm.md
│
├── skill/                        ← Claude skill files that power the pipeline
│   ├── push-data-to-snowflake.md ← pushes raw + projects → Snowflake
│   └── build-wiki.md             ← fetches Snowflake → compiles wiki pages
│
└── Archive/                      ← raw files move here automatically after being pushed
```

Replace `allneurons`, `legalgraph`, and `maven` with the companies or projects you're tracking. The files inside each folder are starting templates — add or remove based on what you know about each company.

---

## What Each Folder Does

| Folder | What it does |
|--------|-------------|
| `raw/` | Raw JSON files fetched from LinkedIn/YouTube — never touched after they land |
| `projects/` | Your own markdown docs about each company — overviews, products, personas |
| `skill/` | Claude instruction files — tells Claude how to push data and build the wiki |
| `Archive/` | Raw files move here automatically after they've been pushed to Snowflake |

---

## Step 1: Create the `second-brain` Folder

Open your terminal and run:

```bash
mkdir second-brain
```

This is the root of your workspace. Everything we build in this module will live inside here.

---

## Step 2: Create the `raw` Subfolder

```bash
mkdir second-brain/raw
```

This is where your channel data lands — straight from the source, untouched.

Every time you pull data from LinkedIn, YouTube, or any other channel using Composio, it gets stored here first. Raw data is **never modified** — it's your source of truth. If something goes wrong downstream in a pipeline, you always have the original to fall back on.

Think of `raw` as the loading dock: data arrives here before it gets processed or pushed to Snowflake.

---

## Step 3: Create the `projects` Subfolder

```bash
mkdir -p second-brain/projects/allneurons
mkdir -p second-brain/projects/legalgraph
mkdir -p second-brain/projects/maven
```

This is where your structured company and project knowledge lives.

Unlike `raw/`, which holds JSON data fetched from APIs, `projects/` holds **documents you write and maintain** — company overviews, product notes, user personas, course descriptions. These are the context files Claude reads when it needs to understand what a company is about.

Replace `allneurons`, `legalgraph`, and `maven` with your own companies. The structure inside each folder is up to you — use whatever documents make sense for that company.

---

## Step 4: Create the `skill` Subfolder

```bash
mkdir second-brain/skill
```

This is where your Claude skill files live.

A skill file is a plain markdown file containing a set of reusable instructions for Claude. When you reference a skill in a prompt with `@second-brain/skill/filename.md`, Claude reads those instructions and follows them — consistently, every time.

Two skills power this entire pipeline:

| Skill file | What it does |
|------------|-------------|
| `push-data-to-snowflake.md` | Reads `raw/` and `projects/`, pushes everything to Snowflake, archives raw files |
| `build-wiki.md` | Connects to Snowflake, discovers entities in your data, compiles wiki pages automatically |

You'll download and add these skill files in later lessons. For now, create the folder so the structure is ready.

---

## Step 5: Create the `Archive` Subfolder

```bash
mkdir second-brain/Archive
```

This is where things go when they're done.

Not deleted. Not forgotten. Just moved out of the active workspace so they don't create noise.

When the push skill runs successfully, raw files move here automatically. Claude won't confuse archived files with current work, but you can always go back and find them.

---

## Your Structure Is Ready

Run this to confirm everything looks right:

```bash
ls second-brain
```

You should see:

```
Archive  projects  raw  skill
```

That's your workspace. Clean, intentional, and ready for Claude to work inside.

---

## How Real Teams Think About This

Senior engineers don't skip this step.

In any serious engineering organization, workspace structure is a first-class decision — not an afterthought. Teams have conventions for where code lives, where documentation lives, where experiments go. New engineers get onboarded to the structure before they write anything.

What we just built follows the same logic. The specific names don't matter as much as the habit: **every project gets a home before it gets code.**

---

[← Back to module index](../../README.md)
