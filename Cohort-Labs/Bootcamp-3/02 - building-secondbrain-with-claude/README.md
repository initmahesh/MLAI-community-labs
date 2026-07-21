# Build Your Second Brain with Claude

---

## Why This Is Worth Building

You are about to build something that feels more useful than a notebook, more practical than a dashboard, and more powerful than a pile of scattered notes.

This lab turns your online activity into a living system you can actually use. Claude pulls data from your YouTube channel, LinkedIn profile, and Zoom meetings. It stores that data in Snowflake. Then it turns the information into a searchable wiki and a weekly business review.

The goal is simple: stop letting important ideas, updates, and signals live in random places. Instead, build one system that keeps working for you.

If you have ever thought, “I wish I had a better way to organize all this,” this is the lesson for you.

---

## What You Will Build

By the end of this module, you will have a Second Brain that runs more like a real personal operating system than a manual workflow.

You will build a system that:

- collects fresh data from your channels and meetings
- stores it in a real data warehouse
- turns that data into a wiki you can explore
- generates a weekly review every Monday

It is not just a tutorial. It is a practical build you can actually use.

```text
YouTube + LinkedIn + Zoom
        ↓
     Claude pulls data
        ↓
   Snowflake stores it
        ↓
   Wiki updates itself
        ↓
   WBR shows what changed
```

---

## What You Will Learn

In this module, you will learn how to:

- connect Claude to real tools using MCP and Composio
- create a folder structure that Claude can read and write to
- move data into Snowflake as structured JSON and raw files
- use skill files to automate work
- build a wiki from your data
- generate a weekly business review automatically

This is a hands-on build, not just a theory lesson.

---

## What You Will Need

| Tool | What it's for | Cost |
|------|--------------|------|
| **Claude Code** | The AI that runs your Second Brain | Paid subscription |
| **Composio** | Integration hub connecting Claude to external tools | Free tier available |
| **Snowflake** | Cloud data warehouse — permanent storage for all your data | Free 30-day trial |
| **Obsidian** | Desktop app for reading your wiki | Free |
| **YouTube account** | The channel you want to track | Free |
| **LinkedIn account** | The profile you want to track | Free |
| **Zoom account** | Meeting transcripts (auto-fetch requires) | Free / Paid |

---

## How the Module Flows

This module is designed as a step-by-step build.

### Foundation — Set Up Your Workspace

| Lesson | What you'll do |
|--------|---------------|
| [0.1 — Create Your Second Brain Folder](./00-foundation/0.1-creating-folderstructure/readme.md) | Set up the folder structure Claude will read and write to |
| [0.2 — Create Your Composio Account](./00-foundation/0.2-creating-composioaccount/readme.md) | Connect the tools that will power your workflow |
| [0.3 — Set Up Apify](./00-foundation/0.3-setup-apify/readme.md) | Install the web data connector for LinkedIn scraping |
| [0.4 — Set Up Snowflake](./00-foundation/0.4-creating-snowflake-account/Readme.md) | Create the cloud storage layer for your data |

### Channel Data Pipeline — Connect and Automate

| Lesson | What you'll do |
|--------|---------------|
| [1.0 — Enable Channels in Composio](./01-channel-data-pipeline/1.0-enabling-channels%20-in-composio/readme.md) | Connect YouTube and LinkedIn so Claude can access them |
| [1.1 — Connect Claude to Composio via MCP](./01-channel-data-pipeline/1.2-connecting-claude-composioMCP/readme.md) | Register Composio as an MCP server and pull your first live data |
| [1.2 — Connect Snowflake to Composio](./01-channel-data-pipeline/1.1-connecting-snowflake-composio/Readme.md) | Authorize Composio to write to Snowflake |
| [1.3 — Push Data to Snowflake](./01-channel-data-pipeline/1.3-puhing-data-to-snowflake/readme.md) | Use a skill file to send your data into Snowflake and automate the sync |

### Building Your Wiki — Knowledge That Maintains Itself

| Lesson | What you'll do |
|--------|---------------|
| [2.0 — Create Your Wiki](./02-building-wiki/2.0-personal-knowledge-os/readme.md) | Turn your Snowflake data into a structured, linked wiki |
| [2.1 — Create Your Weekly Business Review](./02-building-wiki/2.1-creating-WBR/readme.md) | Automate a weekly report that shows what changed every Monday |

---

## How the Automation Works

Once everything is set up, this is what runs automatically:

| Time | What runs | What it does |
|------|-----------|-------------|
| **10:00 AM** | Daily data fetch | Pulls fresh YouTube, LinkedIn, and Zoom data into `raw/` |
| **6:00 AM** (next day) | Snowflake push | Detects new files in `raw/`, pushes JSON + transcripts to Snowflake, archives raw files |
| **12:00 PM** | Wiki sync | Queries Snowflake for new data and updates only affected wiki pages |
| **8:00 AM Monday** | Weekly WBR | Compiles the previous week's data into a full business review |

You set each of these up once. After that, they keep running without you.

---

## Start Here

**[→ Lesson 0.1: Set Up Your Second Brain Folder](./00-foundation/0.1-creating-folderstructure/readme.md)**
