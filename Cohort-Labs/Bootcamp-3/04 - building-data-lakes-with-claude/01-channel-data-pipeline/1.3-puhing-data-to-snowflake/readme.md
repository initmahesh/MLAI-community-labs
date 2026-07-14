# Pushing Data to Snowflake

---

Look at your `projects` folder right now.

It has JSON files. YouTube analytics. LinkedIn posts. Maybe some engagement data. All collected, all structured, all sitting there.

But none of it is in Snowflake yet.

That data is one step away from becoming a real data lake — queryable, historical, permanent. The last step is pushing it in. And not just pushing it blindly — pushing it intelligently: creating the right tables, handling new data types automatically, and cleaning up the workspace when it's done.

That's what this lesson is about.

---

## The Problem With Just "Pushing Data"

Pushing data to a database sounds simple. In practice, it involves a lot of decisions:

- What database do we write to?
- Does the table already exist?
- If not, what should the schema look like?
- What if a new channel type appears — CSV, a new platform?
- How do we avoid duplicating rows we already inserted?
- What happens to the local files after we push them?

If you hand Claude a raw instruction like "push my data to Snowflake," it'll do its best — but it'll guess at all of these. Different answers every time. Tables with different column names. Duplicated records. Files left behind cluttering your workspace.

What we need is a **Skill** — a set of instructions Claude follows every time, consistently, so the pipeline behaves the same whether you run it today or six months from now.

---

## Skills as Pipeline Instructions

A Skill is a file that contains a complete, reusable set of instructions for Claude.

Think of it like handing a new team member a standard operating procedure. They read it once and they know exactly what to do — in what order, what to create, what to check, what to update. You don't have to explain it from scratch every time.

The Skill we're using today is called `dynamic-snowflake-ingestion`. Here's what it does every time you run it:

```
1. Check the projects/ folder for data files
      ↓
2. Connect to Snowflake, create database if it doesn't exist
      ↓
3. For each data type (YouTube, LinkedIn, CSV...)
   create the right table if it doesn't exist
      ↓
4. Insert the data — no duplicates
      ↓
5. Update the Skill file with schema info
   so next run it already knows the structure
      ↓
6. Move all processed files to Archive/
```

Notice step 5 — the Skill updates itself. After the first run, it knows your database name, your table names, your column schemas. The second run is faster and smarter than the first. That's a self-improving pipeline.

---

## Before You Start

Make sure you're working inside your `second-brain` folder. Everything in this lesson — skills, projects, archive — is relative to that folder.

If you're not sure where you are, ask Claude:

```
What is my current working directory?
```

It should show a path ending in `second-brain`.

---

## Step 1: Check Your Snowflake Connection

Before pushing anything, confirm that Claude can actually reach Snowflake through Composio.

Open Claude and run this prompt:

```
Check if I have an active Snowflake connection through Composio.
If yes, tell me which account it's connected to.
If no, tell me what's missing.
```

You should see confirmation that the connection is live. If not, go back to lesson 1.2 and re-check your Composio setup.

---

## Step 2: Create a `skills` Folder in Your Second Brain

We need a home for skills inside your workspace so create a new folder inside the second-brain with name skills

This is where all Claude Skills for this project will live. By keeping them inside `second-brain`, Claude can find and read them automatically when you reference them in a prompt.

Your workspace now looks like this:

```
second-brain/
  ├── projects/         ← your data files live here
  ├── skills/           ← skills live here  ← new
  ├── CLAUDE.md
  └── Archive/
```

---

## Step 3: Add the Skill File

Download the `dynamic-snowflake-ingestion` skill file and place it inside `second-brain/skills/`.

- [Download the skill →](https://pragyaallc-my.sharepoint.com/:u:/g/personal/sachin_parmar_legalgraph_ai/IQBDcdh8Vfx4TKiGFk_GjPtPAV7sruWexnM8tBsjQBx0OPI?e=A8WT5p)

Once it's there, your skills folder should look like this:

```
second-brain/skills/
  └── dynamic-snowflake-ingestion.md
```

---

> **What's inside this Skill file?**
>
> The Skill contains detailed instructions that tell Claude:
> - What database to use (`company-second-brain`)
> - How to detect the data type of each file (YouTube, LinkedIn, CSV)
> - What table schema to create for each type
> - How to check if a table already exists before creating it
> - How to update itself after the first run so schemas are remembered
> - How to move files to `Archive/` once they've been successfully pushed
>
> You don't need to edit it. Claude reads it and follows it.

---

## Step 4: Push the Data to Snowflake

Now open Claude, make sure you're in your `second-brain` folder, and run this prompt:

```
Use the projects folder to push data to Snowflake.
Use the skill @dynamic-snowflake-ingestion
```

Claude will:

1. Read the Skill file for instructions
2. Scan your `projects/` folder for all data files
3. Connect to Snowflake via Composio
4. Create the `company-second-brain` database if it doesn't exist
5. For each data file, determine the type and create the appropriate table if needed
6. Insert the data
7. Update the Skill file with any new schema information
8. Move all processed files from `projects/` to `Archive/`

When it's done, your `projects/` folder will be empty and your data will be in Snowflake.

---

## What Just Happened — Behind the Scenes

Let's break down what Claude actually did during that one prompt.

**Table creation logic:**

| Data type | Table created |
|-----------|--------------|
| YouTube channel analytics | `youtube_channel_overview` |
| YouTube video engagement | `youtube_video_engagement` |
| LinkedIn page performance | `linkedin_page_performance` |
| LinkedIn post engagement | `linkedin_post_engagement` |
| CSV file | Table named after the filename |

If a table already existed from a previous run, Claude skipped creation and went straight to inserting new rows.

**Self-updating behavior:**

After the first run, open `second-brain/skills/dynamic-snowflake-ingestion.md`. You'll see it now contains your database name and the schemas of the tables that were created. The next time you run the same prompt, Claude won't create anything from scratch — it'll use what it already knows.

**Archive cleanup:**

Every file that was in `projects/` is now in `Archive/`. Your workspace is clean and ready for the next pipeline run.

---

## Verify the Data in Snowflake

Log into your Snowflake account and go to **Data → Databases**.

You should see `COMPANY-SECOND-BRAIN` listed as a new database.

Open it and browse the tables. Click any table → **Data Preview** to confirm your records are there.

---

## How Real Teams Think About This

In a production data pipeline, data engineers obsess over three things:

**Idempotency** — running the pipeline twice shouldn't create duplicate data. Our Skill handles this by checking what already exists before inserting.

**Schema management** — as data sources evolve, tables need to evolve too. Our Skill updates itself with new schemas so future runs stay consistent.

**Observability** — after a run, you should be able to tell exactly what happened: what was inserted, what was skipped, what failed. Claude's response after running the Skill gives you that summary.

The `dynamic-snowflake-ingestion` Skill embodies all three. It's not just a push script — it's a self-maintaining pipeline component.

```

Your data is now in Snowflake. The pipeline is complete end to end.

---

## Summary

You did four things:

1. Created a `skills/` folder inside your second brain
2. Added the `dynamic-snowflake-ingestion` Skill
3. Ran a single prompt that pushed all your channel data into Snowflake
4. Watched the Skill clean up your workspace by moving files to Archive

That one prompt replaced what would otherwise be a custom ETL script, a schema migration tool, a deduplication check, and a file cleanup job.

---

