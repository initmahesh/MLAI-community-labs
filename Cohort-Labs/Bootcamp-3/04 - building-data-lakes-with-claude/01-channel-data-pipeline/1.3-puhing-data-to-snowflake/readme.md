# Pushing Data to Snowflake

---

You've pulled data from YouTube and LinkedIn. It's sitting in your `second-brain/raw/` folder — structured, date-stamped, ready.

Now it's time to make it permanent.

Right now that data only exists on your local machine. It can't be queried across time. It can't be shared with a teammate. It can't power a report next month. To do any of that, it needs to live in Snowflake.

This lesson is about pushing everything — raw channel data and processed project data — into your Snowflake data lake in one prompt.

---

## What We're Pushing

By this point your `second-brain` folder has two types of data worth storing:

```
second-brain/
  ├── raw/                          ← channel data straight from the source
  │   ├── youtube/
  │   │   ├── competitors/
  │   │   │   └── MaheshAIPMCommunity.json
  │   │   └── daily/
  │   │       └── YYYY-MM-DD.json
  │   └── linkedin/
  │       ├── my-profile/
  │       │   └── full-research.json
  │       └── daily/
  │           └── YYYY-MM-DD.json
  └── projects/                     ← processed company and project data
      └── OngoingProjects/
          ├── allneurons/
          ├── maven/
          └── legalgraph/
```

Both folders go to Snowflake. The difference is what happens after:

| Folder | After push |
|--------|-----------|
| `raw/` | Moves to `Archive/` — the push is complete, the original is preserved |
| `projects/` | Stays in place — this is live working data that continues to be updated |

---

## How This Works: The Skill File

Instead of writing out every Snowflake table and insert command by hand, we use a **skill file**.

A skill file is a reusable set of instructions stored in your `second-brain` folder. Claude reads it at the start of the prompt and knows exactly what to do — which tables to create, how to structure the data, what to log, and what to do when the push is complete.

The skill we're using lives at:

```
second-brain/skill/push-data-to-snowflake.md
```

When you reference it in a prompt with `@second-brain/skill/push-data-to-snowflake.md`, Claude loads those instructions and executes them against your current data. You don't need to explain the schema every time — the skill handles it.

---

## Push Your Data to Snowflake

Paste this prompt into Claude:

```
@second-brain/skill/push-data-to-snowflake.md

Push all data from the second-brain folder to Snowflake using the Composio MCP server.

Step 1 — Push Raw Data
Scan everything inside second-brain/raw/ and push each JSON file to the corresponding Snowflake table.
For each file:
- Detect the source (youtube or linkedin) and the data type (competitors, daily, my-profile)
- Create the table in Snowflake if it does not exist
- Insert the data as a new row with a timestamp of when the push ran
- Log the file path and row count after each successful insert

Step 2 — Push Project Data
Scan everything inside second-brain/projects/OngoingProjects/ and push each JSON file to Snowflake.
For each company folder (allneurons, maven, legalgraph):
- Push company-overview.json, post-engagement.json, follower-snapshots.json, and page-stats.json
- Create the table if it does not exist
- Insert the data with the company name and a timestamp
- Log each successful insert

Step 3 — Archive Raw Data
Once all raw files have been pushed successfully:
- Move everything from second-brain/raw/ to second-brain/Archive/raw/
- Preserve the original folder structure inside Archive
- Do not move or delete anything from second-brain/projects/

Step 4 — Summary
After everything is complete, tell me:
- How many files were pushed total
- Which Snowflake tables were created or updated
- Which files were archived
- If any file failed to push, list it with the reason
```

---

> **Why move raw to Archive after pushing?**
>
> Once data is in Snowflake, keeping it in `raw/` creates noise. The next pipeline run will generate a new file with today's date — and you don't want last week's file sitting alongside it pretending to be current. Moving it to `Archive/` means your `raw/` folder always contains only unprocessed data. Clean input. No ambiguity.

---

## What Snowflake Looks Like After the Push

Once Claude finishes, open your Snowflake account and go to **Data → Databases**. You should see tables created for each data type:

| Table | Source |
|-------|--------|
| `YOUTUBE_COMPETITORS` | `raw/youtube/competitors/` |
| `YOUTUBE_DAILY` | `raw/youtube/daily/` |
| `LINKEDIN_MY_PROFILE` | `raw/linkedin/my-profile/` |
| `LINKEDIN_DAILY` | `raw/linkedin/daily/` |
| `PROJECTS_COMPANY_OVERVIEW` | `projects/OngoingProjects/*/company-overview.json` |
| `PROJECTS_POST_ENGAGEMENT` | `projects/OngoingProjects/*/post-engagement.json` |
| `PROJECTS_FOLLOWER_SNAPSHOTS` | `projects/OngoingProjects/*/follower-snapshots.json` |
| `PROJECTS_PAGE_STATS` | `projects/OngoingProjects/*/page-stats.json` |

Every push adds a new row — so over time you'll have a full historical record of how your channels and projects have changed.

---

## Auto-Sync Scheduler: Push New Files to Snowflake Every Morning

Running the push manually works — but the real power is when it happens automatically.

The scheduler below runs every morning at 6:00 AM using Claude Code's built-in scheduler. It scans both folders, detects any files added since the last run, pushes only the new ones to Snowflake, and archives raw files once they're safely stored. Nothing runs if there's nothing new.

**Set Up Daily Snowflake Sync at 6am**
```
Using Claude Code's built-in scheduler, set up a daily job that runs every morning at 6:00 AM. Use the Composio MCP server to push any new data to Snowflake.

Step 1 — Scan for New Files
Check both folders for files that have been added since the last successful push:
- second-brain/raw/ (all subfolders)
- second-brain/projects/OngoingProjects/ (all company subfolders)

A file is considered new if it has not already been pushed to Snowflake in a previous run.
Skip any file that was already pushed — do not create duplicate rows.

Step 2 — Push New Raw Files
For each new file found in second-brain/raw/:
- Detect the source (youtube or linkedin) and data type (competitors, daily, my-profile)
- Create the Snowflake table if it does not exist
- Insert the data as a new row with a timestamp of when the push ran
- Log the file name, table name, and row count

Step 3 — Push New Project Files
For each new file found in second-brain/projects/OngoingProjects/:
- Detect the company name and file type (company-overview, post-engagement, follower-snapshots, page-stats)
- Create the Snowflake table if it does not exist
- Insert the data with the company name and a timestamp
- Log each successful insert

Step 4 — Archive Pushed Raw Files
Once all new raw files have been successfully pushed:
- Move them from second-brain/raw/ to second-brain/Archive/raw/
- Preserve the original subfolder structure inside Archive
- Do not touch second-brain/projects/

Step 5 — Summary Log
After the run completes, print:
- Date and time the job ran
- How many new files were found
- How many were pushed successfully
- Which Snowflake tables were updated
- Any files that failed, with the reason
- If no new files were found, log: "No new files — nothing to push."

Schedule this as a recurring cron job that runs automatically every day at 6:00 AM.
```

> **Why 6am?** The daily data fetch (set up in lesson 1.1) runs at 10am. By running the Snowflake sync at 6am, you're pushing any files that landed the previous day before the new day's fetch kicks off — keeping the pipeline clean and in sequence.

---

## How Real Teams Think About This

In production data pipelines, there's a pattern called **ELT — Extract, Load, Transform**.

- **Extract** — pull the data from its source (you did this with YouTube and LinkedIn via Composio)
- **Load** — push it into the warehouse as-is (that's what this lesson does)
- **Transform** — reshape and analyze it inside the warehouse (that comes later)

Most teams separate these stages deliberately. Loading raw data first means you always have the original if a transform goes wrong. You can re-run the transform without re-fetching from the source API.

What you've built here follows that same logic: raw data lands in `raw/`, gets pushed to Snowflake unmodified, then moves to `Archive/`. The warehouse becomes the source of truth. Everything downstream queries Snowflake — nothing queries a local file.

---

## What's Next

Your data is in Snowflake. Now it can be queried, compared across time, and shared across your team.

In the next lesson, we'll write SQL queries directly from Claude to start pulling insights out of what you've built — trends, comparisons, and reports that would have taken hours to produce manually.

---

## Claude Concepts Covered in This Lesson

| Concept | Where it appeared | Learn more |
|---------|-------------------|------------|
| **Skill files** | **How This Works** — *"A skill file is a reusable set of instructions stored in your second-brain folder."* | [Claude Code slash commands](https://docs.anthropic.com/en/docs/claude-code/slash-commands) |
| **MCP Tool Use** | **Push Your Data** — *"Push all data from the second-brain folder to Snowflake using the Composio MCP server."* | [MCP Documentation](https://docs.anthropic.com/en/docs/claude-code/mcp) |
| **File References** | **How This Works** — *"When you reference it in a prompt with @second-brain/skill/push-data-to-snowflake.md"* | [Claude Code Overview](https://docs.anthropic.com/en/docs/claude-code) |

---

[← Back to module index](../README.md)
