# Setting Up Your Second Brain Folder Structure

---

Before we build anything, let's talk about where everything is going to live.

Think about the last time you started a new project. You probably had files scattered across your Desktop, a Downloads folder full of random things, maybe a few docs in Google Drive, and some notes somewhere you can't remember. By week two, half your time was spent finding things instead of building things.

Now imagine working alongside Claude every day on a growing data lake project. Claude can only help you as well as your workspace allows. If your files have no structure, Claude has no structure to work with.

This is why we set up a **Second Brain** before doing anything.

---

## Today's Concept: The Second Brain

The folder we're creating is called `second-brain`.

It's not just a catchy name. The idea comes from the personal knowledge management world — a "second brain" is a trusted external system where you store everything you're working on, so your actual brain doesn't have to hold it all.

For us, it means one folder that contains:

- A place for raw channel data as it comes in
- A place for structured company and project information
- A place for call and meeting transcripts
- A place for completed work worth keeping

Here's the structure we're building today:

```
second-brain/
  ├── raw/
  ├── projects/
  └── Archive/
```

Four folders. That's it. Let's build them.

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

Every time you pull data from LinkedIn, YouTube, or any other channel using Composio, it gets stored here first. Raw data is never modified — it's your source of truth. If something goes wrong downstream in a pipeline, you always have the original to fall back on.

```
second-brain/raw/
  ├── linkedin/
  ├── youtube/
  └── ...
```

Think of `raw` as the loading dock: data arrives here before it gets processed or analysed.

---

## Step 3: Create the `projects` Subfolder

```bash
mkdir second-brain/projects
```

This is where structured company and project information lives.

Once raw data has been processed, the outputs go here — organised by company or project. Company overviews, follower snapshots, engagement reports, competitor analyses — anything that has been shaped into something useful belongs in `projects`.

```
second-brain/projects/
  └── OngoingProjects/
      ├── allneurons/
      │   ├── company-overview.json
      │   ├── post-engagement.json
      │   ├── follower-snapshots.json
      │   └── page-stats.json
      ├── maven/
      │   ├── company-overview.json
      │   ├── post-engagement.json
      │   ├── follower-snapshots.json
      │   └── page-stats.json
      └── legalgraph/
          ├── company-overview.json
          ├── post-engagement.json
          ├── follower-snapshots.json
          └── page-stats.json
```

The rule: raw data lives in `raw`, processed and structured data lives in `projects`.

To create this structure run:

```bash
mkdir -p second-brain/projects/OngoingProjects/allneurons
mkdir -p second-brain/projects/OngoingProjects/maven
mkdir -p second-brain/projects/OngoingProjects/legalgraph
```

Each company folder follows the same pattern — one JSON file per data type. When you run the LinkedIn prompts from the previous lesson, point the save path to the matching company folder here.

For example, when Claude saves company data for allneurons, the path will be:
`second-brain/projects/OngoingProjects/allneurons/company-overview.json`

---

## Step 4: Create the `Calltranscript` Subfolder

```bash
mkdir second-brain/Calltranscript
```

This is where call and meeting transcripts live.

Sales calls, customer interviews, team meetings, demo recordings — any transcript that might feed into your pipeline or analysis goes here. Having a dedicated folder means Claude can reference transcripts directly when summarising, extracting insights, or building context for a project.

---

## Step 5: Create the `Archive` Subfolder

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
Archive  Calltranscript  projects  raw
```

That's your workspace. Clean, intentional, and ready for Claude to work inside.

---

## How Real Teams Think About This

Senior engineers don't skip this step.

In any serious engineering organization, workspace structure is a first-class decision — not an afterthought. Teams have conventions for where code lives, where documentation lives, where experiments go. New engineers get onboarded to the structure before they write anything.

What we just built follows the same logic:

| Folder | Purpose |
|--------|---------|
| `raw/` | Channel data straight from the source — LinkedIn, YouTube, and other platforms |
| `projects/` | Processed outputs organised by company — overviews, reports, competitor analyses |
| `Calltranscript/` | Call and meeting transcripts for analysis and context |
| `Archive/` | Completed work — out of the way but not gone |

The specific names don't matter as much as the habit: **every project gets a home before it gets code.**

---

[← Back to module index](../../README.md)
