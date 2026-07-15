# Setting Up Your Second Brain Folder Structure

![image](./images/banner.png)

---

Before we build anything, let's talk about where everything is going to live.

Think about the last time you started a new project. You probably had files scattered across your Desktop, a Downloads folder full of random things, maybe a few docs in Google Drive, and some notes somewhere you can't remember. By week two, half your time was spent finding things instead of building things.

Now imagine working alongside Claude every day on a growing data lake project. Claude can only help you as well as your workspace allows. If your files have no structure, Claude has no structure to work with.

This is why we set up a **Second Brain** before doing anything.

---

## Today's Concept: The Second Brain

The folder we're creating is called `Second-Brain`.

A **Second Brain** is a trusted external system where you store everything you're working on — raw data, processed insights, and the skill files that power your pipeline. Your actual brain doesn't have to hold it all.

For this course we're using **Maven** as our real-world use case. Maven runs courses (like the AI PM Bootcamp and GenAI PM course) and markets them through LinkedIn and YouTube. Our job is to:

- Pull raw engagement data from **LinkedIn** (ads, campaigns) and **YouTube** (video performance)
- Push that data into Snowflake
- Build a structured **wiki** that Claude can read as context when generating reports and analyses

The `wiki/` folder is the heart of the Second Brain. It's where processed, structured knowledge lives — organized by courses and campaigns — so Claude always has the right context when you ask it questions.

---

## Step 1: Download the Template

Download the Second Brain folder structure used in this course:

> **[Download Second Brain Template](https://pragyaallc-my.sharepoint.com/:u:/g/personal/sachin_parmar_legalgraph_ai/IQA2txH3NdrqTruh-6z1qmgiATevR5uChgptEBnW8GCP3U4?e=EWIdSb)**

This gives you the exact folder layout with example files already in place. You don't need to create anything from scratch.

---

## The Full Structure

Here's what the complete Second Brain looks like:

```
Second-Brain/
│
├── raw/                              ← immutable source data (ingested by push skill)
│   ├── LinkedIn-ads.json
│   ├── LinkedIn-campaign.json
│   └── YouTube-channel.json
│
├── skill/                            ← Claude skill files that power the pipeline
│   ├── push-data-to-snowflake.md     ← pushes raw data → Snowflake
│   ├── build-wiki.md                 ← fetches Snowflake → compiles wiki pages
│   └── build-wbr.md                  ← builds weekly business review from wiki
│
├── wiki/                             ← structured knowledge Claude reads as context
│   ├── campaigns/
│   │   ├── README.md                 ← campaign overview across all channels
│   │   ├── linkedin-ads/
│   │   │   └── README.md             ← LinkedIn ad performance insights
│   │   ├── linkedin-campaign/
│   │   │   └── README.md             ← LinkedIn campaign-level breakdown
│   │   └── youtube/
│   │       └── README.md             ← YouTube video and channel metrics
│   └── courses/
│       ├── course-bootcamp.md        ← AI PM Bootcamp course details
│       └── course-genaipm.md         ← GenAI PM course details
│
└── Archive/                          ← raw files move here after being pushed
```

---

## What Each Folder Does

| Folder | What it does |
|--------|-------------|
| `raw/` | Raw JSON files pulled from LinkedIn and YouTube — never modified after they land |
| `skill/` | Claude instruction files — tells Claude how to push data, build the wiki, and generate reports |
| `wiki/` | Structured markdown knowledge base — courses and campaign data organized for Claude to read as context |
| `Archive/` | Raw files move here automatically after they've been pushed to Snowflake |

---

## Why `wiki/` Replaces `projects/`

In earlier versions of this course, a `projects/` folder held static company docs you wrote by hand. We've moved past that.

Now the **wiki is auto-generated**. Claude pulls live data from Snowflake, structures it into markdown pages, and writes them into `wiki/`. This means:

- Your context is always based on **real, up-to-date data** — not static notes
- LinkedIn and YouTube metrics flow directly into the wiki pages Claude references
- You never have to manually maintain context documents

The wiki is the living knowledge layer of your Second Brain.

---

## How Real Teams Think About This

Senior engineers don't skip this step.

In any serious engineering organization, workspace structure is a first-class decision — not an afterthought. Teams have conventions for where code lives, where documentation lives, where experiments go. New engineers get onboarded to the structure before they write anything.

What we just built follows the same logic. The specific names don't matter as much as the habit: **every project gets a home before it gets code.**

---

## What You've Learned

- The Second Brain folder structure and what each folder is for
- Why `raw/` is immutable and `wiki/` holds Claude's live context
- How skill files in `skill/` power the entire pipeline without writing code
- That `wiki/` is auto-generated from Snowflake data — you never maintain it manually
- How Maven's LinkedIn and YouTube data flows into structured wiki pages

---

## What's Next

**[Lesson 0.2 → Create Your Composio Account](../0.2-creating-composioaccount/readme.md)**

Composio is the integration hub that connects Claude to YouTube, LinkedIn, and Snowflake. In the next lesson you'll create your account and get familiar with the dashboard — the foundation every lesson after this depends on.

---

[← Back to module index](../../README.md)