# Setting Up Your Second Brain Folder Structure

---

Before we build anything, let's talk about where everything is going to live.

Think about the last time you started a new project. You probably had files scattered across your Desktop, a Downloads folder full of random things, maybe a few docs in Google Drive, and some notes somewhere you can't remember. By week two, half your time was spent finding things instead of building things.

Now imagine working alongside Claude every day on a growing data lake project. Claude can only help you as well as your workspace allows. If your files have no structure, Claude has no structure to work with.

This is why we set up a **Second Brain** before doing anything.

---

## Today's Concept: The Second Brain

The folder we're creating is called `second-brain`.

It's not just a catchy name. The idea comes from the personal knowledge management world a "second brain" is a trusted external system where you store everything you're working on, so your actual brain doesn't have to hold it all.

For us, it means one folder that contains:

- Everything Claude needs to understand the current project
- A place for active work
- A place for things that are done but worth keeping

Here's the structure we're building today:

```
second-brain/
  ├── projects/
  ├── CLAUDE.md
  └── Archive/
```

Three things. That's it. Let's build them.

---

## Step 1: Create the `second-brain` Folder

Open your terminal and run:

```bash
mkdir second-brain
```

This is the root of your workspace. Everything we build in this module will live inside here.

---

## Step 2: Create the `projects` Subfolder

```bash
mkdir second-brain/projects
```

This is where active work lives. When we start building data pipelines, ingestion scripts, and analysis notebooks — they go here.

The rule is simple: if you're actively working on it, it's in `projects`.

---

## Step 3: Create the `CLAUDE.md` File

```bash
touch second-brain/CLAUDE.md
```

This file is how you talk to Claude at the project level.

`CLAUDE.md` is a special file that Claude reads automatically when you open a project. You can use it to tell Claude:

- What this project is about
- What conventions to follow
- What tools are available
- What to do and what to avoid

Right now it's empty. We'll fill it in as the course progresses. But creating it now means Claude will start looking for it from the very first session.

> **Why does this matter?** Without a `CLAUDE.md`, Claude starts every session with zero context about your project. With one, it walks in already briefed — like a team member who read the onboarding doc before their first day.

---

## Step 4: Create the `Archive` Subfolder

```bash
mkdir second-brain/Archive
```

This is where things go when they're done.

Not deleted. Not forgotten. Just moved out of the active workspace so they don't create noise.

Completed pipeline runs, old experiments, previous versions of documents — they go in Archive. Claude won't confuse them with current work, but you can always go back and find them.

---

## Your Structure Is Ready

Run this to confirm everything looks right:

```bash
ls -R second-brain
```

You should see:

```
second-brain/:
Archive  CLAUDE.md  projects
```

That's your workspace. Clean, intentional, and ready for Claude to work inside.

---

## How Real Teams Think About This

Senior engineers don't skip this step.

In any serious engineering organization, workspace structure is a first-class decision — not an afterthought. Teams have conventions for where code lives, where documentation lives, where experiments go. New engineers get onboarded to the structure before they write anything.

What we just built follows the same logic:

| Folder / File | Purpose |
|---------------|---------|
| `projects/` | Active work — what's being built right now |
| `CLAUDE.md` | Project-level instructions for Claude |
| `Archive/` | Completed work — out of the way but not gone |

The specific names don't matter as much as the habit: **every project gets a home before it gets code.**


---

[← Back to module index](../../README.md)