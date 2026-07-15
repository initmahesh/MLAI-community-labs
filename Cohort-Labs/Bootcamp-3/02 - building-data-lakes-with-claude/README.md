# Building Data Lakes with Claude

---

## What We're Building

By the end of this module, you'll have a fully automated data pipeline that runs itself.

Every day, Claude pulls fresh data from your YouTube channel and LinkedIn profile. It pushes that data into a Snowflake data lake. It compiles everything into a structured wiki that stays current without any manual work. And every Monday morning, a Weekly Business Review lands automatically — showing you exactly what changed, what's working, and what needs attention.

You don't write pipeline code. You don't manage credentials. You don't manually update documents. You set it up once and it runs.

```
YouTube + LinkedIn
       ↓  (Composio MCP — 10am daily)
    Claude pulls channel data
       ↓
    second-brain/raw/
       ↓  (push skill — 6am daily)
    Snowflake (SECOND_BRAIN database)
       ↓  (wiki skill — 12pm daily)
    second-brain/wiki/
       ↓  (WBR skill — 8am Monday)
    second-brain/wiki/wbr/YYYY-MM-DD.md
```

---

## What You'll Learn

- How to use **MCP (Model Context Protocol)** to connect Claude to real external systems
- How to use **Composio** as the integration hub between Claude and your tools
- How to build a **Snowflake data lake** that accumulates a historical record of your channels
- How to write **skill files** — reusable Claude instructions that act like pipeline scripts
- How to use **Claude's built-in scheduler** to run jobs automatically at set times
- How to compile a **living wiki** from your data lake using Karpathy's personal knowledge OS pattern
- How to generate a **Weekly Business Review** automatically, with week-over-week comparisons

---

## What You'll Need

| Tool | What it's for | Cost |
|------|--------------|------|
| **Claude Code** | The AI that runs your pipeline | Paid subscription |
| **Composio** | Integration hub connecting Claude to external tools | Free tier available |
| **Snowflake** | Cloud data warehouse — your data lake | Free 30-day trial |
| **Obsidian** | Desktop app for reading your wiki | Free |
| **YouTube account** | The channel you want to track | Free |
| **LinkedIn account** | The profile you want to track | Free |

---

## Module Structure

### Foundation — Set Up Your Workspace

| Lesson | What you'll do |
|--------|---------------|
| [0.1 — Create Your Second Brain Folder](./00-foundation/0.1-creating-folderstructure/readme.md) | Download and set up the folder structure Claude will read and write to |
| [0.2 — Create Your Composio Account](./00-foundation/0.2-creating-composioaccount/readme.md) | Set up the integration hub that connects Claude to YouTube, LinkedIn, and Snowflake |
| [0.3 — Set Up Snowflake](./00-foundation/0.3-creating-snowflake-account/Readme.md) | Create your free cloud data warehouse — the permanent destination for all your data |

### Channel Data Pipeline — Connect and Automate

| Lesson | What you'll do |
|--------|---------------|
| [1.0 — Enable Channels in Composio](./01-channel-data-pipeline/1.0-enabling-channels%20-in-composio/readme.md) | Authenticate YouTube and LinkedIn in Composio so Claude can access both |
| [1.1 — Connect Claude to Composio via MCP](./01-channel-data-pipeline/1.1-connecting-claude-composioMCP/readme.md) | Register Composio as an MCP server in Claude and pull your first live data |
| [1.2 — Connect Snowflake to Composio](./01-channel-data-pipeline/1.2-connecting-snowflake-composio/Readme.md) | Authorize Composio to write to your Snowflake account via OAuth |
| [1.3 — Push Data to Snowflake](./01-channel-data-pipeline/1.3-puhing-data-to-snowflake/readme.md) | Use a skill file to push all your data into Snowflake and set up daily auto-sync |

### Building Your Wiki — Knowledge That Maintains Itself

| Lesson | What you'll do |
|--------|---------------|
| [2.0 — Create Your Wiki](./02-building-wiki/2.0-personal-knowledge-os/readme.md) | Compile your Snowflake data into a structured, cross-linked wiki using the build-wiki skill |
| [2.1 — Create Your Weekly Business Review](./02-building-wiki/2.1-creating-WBR/readme.md) | Automate a weekly report that shows week-over-week performance every Monday at 8am |

---

## How the Timing Works

Once everything is set up, here's what runs automatically every day:

| Time | What runs | What it does |
|------|-----------|-------------|
| **10:00 AM** | Daily data fetch | Pulls fresh YouTube and LinkedIn data into `raw/` |
| **6:00 AM** (next day) | Snowflake push | Detects new files in `raw/` and `projects/`, pushes to Snowflake, archives raw files |
| **12:00 PM** | Wiki sync | Queries Snowflake for new data, updates only affected wiki pages |
| **8:00 AM Monday** | Weekly WBR | Compiles the previous week's data into a full business review |

You set each of these up once. After that, they run without you.

---

## Start Here

**[→ Lesson 0.1: Set Up Your Second Brain Folder](./00-foundation/0.1-creating-folderstructure/readme.md)**
