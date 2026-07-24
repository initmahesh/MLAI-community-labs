# Creating Your Wiki

![image](./images/banner.png)

---

## The Idea Behind a Wiki

Now that your data is being collected and stored in Snowflake, the next step is simple: make it useful.

Andrej Karpathy — one of the founding members of OpenAI and former AI lead at Tesla — talks about a concept he calls the personal knowledge OS.

The idea is simple but powerful. Most people keep knowledge in their heads, in scattered notes, or in conversations that disappear. The problem is not that the knowledge does not exist. The problem is that it is not organized anywhere you can actually use it.

Karpathy's point is that the highest-leverage thing a knowledge worker can build is an external system that:

1. Captures everything — every meeting, every data point, every insight, automatically
2. Connects the dots — links companies to their data, posts to their engagement, and calls to their outcomes
3. Stays current — updates itself when new information arrives, not when you remember to update it
4. Becomes queryable — so instead of saying, “I think I remember something about that company,” you can simply ask

That is what a wiki becomes in this context. Not just a document. Not just a spreadsheet. A living knowledge base that pulls from your data lake and keeps itself up to date.

```text
Snowflake (data lake)
     ↓
Claude reads new data
     ↓
Wiki updates automatically
     ↓
You always have a current picture of every company, channel, and project
```

The companies you are tracking, the YouTube channels you are following, and the LinkedIn profiles you care about all turn into a structured, searchable wiki that you do not have to maintain manually.

---

## How It Works: The build-wiki Skill

Just like the Snowflake push used a skill file, the wiki has one too.

The skill lives here:

```text
second-brain/assets/build-wiki.md
```

It contains the instructions Claude needs to structure the wiki — what pages to create, how to format company profiles, how to link data across sources, and where to save everything.

When you reference it in a prompt with `@second-brain/assets/build-wiki.md`, Claude reads those instructions and applies them to the data you point it at. The result is a consistent wiki instead of a one-off document.

---

## Build Your Wiki

The skill is fully self-contained. It discovers your data, builds the pages, and saves its own tracking state. You simply invoke it:

```text
run @second-brain/assets/build-wiki.md
```

![image](./images/1.png)

That is the whole prompt. The skill handles the rest — from reading Snowflake data to writing the final cross-links.

---

## What Happens Behind the Scenes

Karpathy's framing is very clear: Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.

The skill does not just summarize your data. It compiles it — the same way a compiler takes source files and produces structured output. Here is the process in simple terms:

### Step 1 — Load the wiki context
The skill reads `skill/build-wiki-context.json`, which tracks every page it has written and a hash of the source data that built it. On the first run, that file does not exist yet, so the skill creates it. On later runs, it becomes the memory of what was already done.

### Step 2 — Discover the Snowflake SQL tool through Composio
Instead of hardcoding a tool name, the skill searches Composio for a tool that can run SQL against Snowflake. It finds it, loads its schema, and uses that tool for every query that follows. That keeps the workflow flexible.

### Step 3 — Fetch the data
The skill reads `skill/push-data-to-snowflake-context.json` to see which tables exist, then runs `SELECT *` against each one. Every row comes back as structured data that Claude can work with.

### Step 4 — Discover entities automatically
This is the key step. The skill does not look for company pages or YouTube pages by name. It scans every row across every table and classifies what it finds into five entity types:

| Entity type | Example | Wiki folder |
|-------------|---------|-------------|
| People | LinkedIn profile, channel owner | `wiki/people/` |
| Companies | allneurons, maven, legalgraph | `wiki/companies/` |
| Products | courses, tools, platforms | `wiki/products/` |
| Topics | "Agentic AI", "Product Management" | `wiki/topics/` |
| Content channels | YouTube channel, LinkedIn feed | `wiki/content/` |

New entity types get their own folder automatically. Nothing is hardcoded.

### Step 5 — Decide what to write vs. skip
For each entity, the skill hashes the source rows that feed its page and compares them with what is already stored in `build-wiki-context.json`. If the hash has not changed, the page is skipped. Only entities with new or changed data get recompiled. That is why the wiki stays fast on daily runs.

### Step 6 — Compile the pages
Each page is written by reading across all source rows for that entity and building a structured page from them. Specific numbers, dates, URLs, and proper nouns are preserved exactly. Every mention of another entity gets a `[[slug]]` cross-link so the wiki is fully navigable in Obsidian.

### Step 7 — Generate the master index
`wiki/index.md` is rebuilt from scratch so it always reflects the latest pages in the wiki.

### Step 8 — Save the context
`build-wiki-context.json` is updated with the new page hashes and entity map. That makes the next run incremental and efficient.

Every future run reads the context file first. No data gets compiled twice.

![images](./images/2.png)

---

> **Before you run the prompts below:** Open a new Claude session and add your `second-brain/wiki/` folder to the cowork. Claude will read directly from those wiki pages to answer your questions.

## Test Your Wiki: Three Strategic Questions

Once your wiki is built, the best way to test it is not by asking, “Does the data exist?” but by asking, “What should I do with this data?”

These three prompts use your `second-brain/wiki/` folder as the knowledge source. Each one surfaces a different kind of strategic insight.

---

### Question 1 — What Topics Is My Audience Hungry For?

> Find the recurring themes and questions your audience is actively engaging with — the signals that show unmet demand in your content.

```text
Read all files inside second-brain/wiki/

Look across the YouTube channel data, LinkedIn engagement data, and company pages. Identify the top content opportunities based on what my audience is already responding to.

Specifically:
- Which video topics or LinkedIn post themes are generating the most comments and reactions?
- Are there questions appearing repeatedly in comments or reactions that I have not covered yet?
- Which topics have high engagement relative to how often I post about them — suggesting the audience wants more?

Give me the top 5 underserved topics my audience is clearly asking for, ranked by engagement signal strength. For each one, include the data point that supports it.
```

![images](./images/3.png)

---

### Question 2 — What Is My Competition Completely Missing?

> Find the content gaps competitors have not touched — topics where you can build authority without fighting for space.

```text
Read all files inside second-brain/wiki/

Compare my YouTube channel data against the competitor channel data. Identify content gaps — topics or formats that my audience engages with but that competitors are not covering or are underserving.

Specifically:
- What themes appear in my top-performing content that are absent or thin in competitor content?
- Are there video formats such as Shorts, tutorials, or case studies that I am using but competitors are not?
- Are there industry topics relevant to AI PM and product management that neither of us has covered yet?

Give me the top 3 content gaps competitors are leaving open. For each one, explain why it is an opportunity and what content I could create to own that space.
```

---

### Question 3 — What Content Is Getting the Least Return on Effort?

> Find the content types and topics where the effort is not paying off — so you can stop doing what is not working.

```text
Read all files inside second-brain/wiki/

Look at engagement data across YouTube videos and LinkedIn posts. Identify content that is consistently underperforming — low reactions, low comments, and low watch signals relative to other content.

Specifically:
- Which content types such as text posts, image posts, long-form videos, or Shorts have the lowest average engagement?
- Are there topic areas I return to repeatedly that consistently underperform?
- Is there a posting cadence pattern such as day of week or frequency that correlates with lower performance?

Give me the bottom 3 content patterns that are not delivering value. For each one, show the data and give a recommendation: stop completely, repurpose differently, or test a format change.
```

---

> **Why these three questions?**
>
> They cover the three levers of any content strategy: demand you are not meeting, space competitors have not claimed, and effort you should redirect. Together they give you a clear action list — what to make more of, what to own first, and what to cut.

---

## Optional — View Your Wiki in Obsidian

Your wiki pages are plain markdown files, but the real power shows up when you open them in Obsidian.

Obsidian is a free note-taking app built specifically for connected knowledge. Unlike a regular text editor, it understands the `[[slug]]` cross-links your wiki uses and renders them as a navigable graph, so you can click between pages and explore your entire knowledge base visually.

### To set it up:

1. Download Obsidian at [https://obsidian.md/](https://obsidian.md/) and click **Get Obsidian for macOS**
2. Move it to your Applications folder after it downloads

![image](./images/6.png)

3. Open Obsidian and click **Open folder as vault**
4. Select your `second-brain/wiki/` folder

![image](./images/5.png)

Obsidian will index all your wiki pages instantly. You will be able to navigate between companies, topics, people, and channels by clicking the cross-links, and you can switch to the graph view to see how everything connects.

---

## Auto-Update Scheduler: Keep the Wiki Current at 12pm Daily

The wiki is only useful if it stays current. The scheduler below runs every day at 12pm using Claude Code's built-in scheduler. It reads `sync-log.json`, queries Snowflake for rows newer than the last processed timestamp, and updates only the wiki pages that have new data.

### Set Up Daily Wiki Sync at 12pm

```text
Using Claude Code's built-in scheduler, set up a daily job that runs every day at 12:00 PM.

When the job runs, execute:
@second-brain/skill/build-wiki.md

The skill handles everything automatically:
- It reads skill/build-wiki-context.json to know what was already processed
- It fetches only data that has changed since the last run
- It recompiles only the wiki pages affected by new data
- It updates the context file so the next run knows where this one left off

If skill/build-wiki-context.json does not exist, the skill runs a full build from scratch.

Schedule this as a recurring cron job that runs automatically every day at 12:00 PM.
```

![images](./images/4.png)

> **How the tracking prevents double-processing:**
> The skill hashes the source rows for each wiki page and stores those hashes in `skill/build-wiki-context.json`. On the next run, it recomputes the hashes from the current Snowflake data and compares them. If the hash matches, the page is skipped. Only pages whose underlying data changed get recompiled.

---

## Your Wiki Folder After the First Build

```text
second-brain/
  ├── skill/
  │   ├── build-wiki-context.json         ← tracks page hashes + entity map (auto-managed)
  │   └── push-data-to-snowflake-context.json
  └── wiki/
      ├── index.md                        ← master index, auto-generated
      ├── people/                         ← one page per real person
      ├── companies/                      ← one page per company or org
      │   ├── allneurons.md
      │   ├── maven.md
      │   └── legalgraph.md
      ├── products/                       ← one page per product, course, or tool
      ├── topics/                         ← concept pages: themes, frameworks, ideas
      └── content/                        ← one page per content channel or corpus
          ├── maheshaipmc-youtube.md
          └── linkedin-my-profile.md
```

Every page is plain markdown — Obsidian-compatible, readable in any editor, and queryable by Claude. Cross-links use `[[slug]]` syntax so the whole wiki is navigable as a graph.

---

## How Real Teams Think About This

What you have built is a pattern enterprise teams call a knowledge graph with incremental refresh.

The key insight is the separation between the data store (Snowflake) and the knowledge layer (the wiki). Most teams conflate the two — they dump raw data into a document and call it a wiki. The problem is that raw data and organized knowledge serve different purposes:

| Raw Data (Snowflake) | Knowledge Layer (Wiki) |
|----------------------|------------------------|
| Every row ever inserted | Only the current picture |
| Optimized for querying | Optimized for reading |
| Grows forever | Stays concise and gets updated in place |
| Source of truth | Derived from the source of truth |

The sync log is what keeps these two layers connected without duplicating work. It is a simple pattern, but it is the same mechanism production pipelines use to handle incremental loads at scale.

---

## What You Have Learned

- Karpathy's personal knowledge OS concept — and why compilation beats summarization
- How the `build-wiki.md` skill works: entity discovery, hash-based change detection, and incremental recompilation
- That a single prompt (`run @second-brain/skill/build-wiki.md`) builds your entire wiki automatically
- How `[[slug]]` cross-links make your wiki navigable as a graph in Obsidian
- How to set up a daily 12pm scheduler that updates only the pages with new data
- How to query your wiki with three strategic questions: audience demand, competitor gaps, and low-ROI content

---

## What's Next

**[Lesson 2.1 → Create Your Weekly Business Review](../2.1-creating-WBR/readme.md)**

Your wiki gives you a current picture of everything. The WBR zooms out to show you what changed week over week — automatically compiled every Monday morning before your week starts.
