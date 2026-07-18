# Creating Your Weekly Business Review (WBR)

![image](./images/banner.png)

---

## Why This Lesson Matters

By now, you have already built the system that collects data and turns it into a usable wiki.

That is a great foundation. But a wiki alone is not the full story. A wiki tells you what exists. A WBR tells you what changed.

This is where the habit becomes useful in real life.

Every Monday morning, instead of opening five tabs and trying to remember what happened last week, you open one report that gives you the answer in a clean, repeatable format. It shows you:

1. What happened this week
2. What changed from last week
3. What is working well
4. What deserves your attention

That is the purpose of a Weekly Business Review.

It is not just a report. It is a weekly briefing that helps you make better decisions without wasting time gathering context.

---

## What a WBR Actually Is

A WBR is a simple weekly summary of your business signals.

Think of it as your normal Monday morning check-in, but automated.

Instead of manually pulling numbers from YouTube, LinkedIn, Snowflake, and your company pages, the system compiles everything into one structured document. The result is a weekly snapshot that is easy to read and easy to compare.

A good WBR answers four questions:

- What happened this week?
- What changed from last week?
- What is performing well?
- What needs attention?

That is the difference between reacting to noise and making decisions from a clear view of the data.

---

## How It Works: The Build-WBR Skill

The WBR is powered by a assets file in your second-brain folder:

```text
run @second-brain/assets/build-wbr.md
```

This skill connects to Snowflake through Composio, pulls the last 7 days of data, compares it with the previous 7 days, and writes a markdown report for you.

It saves the output into your wiki folder with a date-based filename, so your reports build into a real archive over time.

```text
second-brain/wiki/wbr/
  ├── 2026-07-07.md
  ├── 2026-07-14.md   ← this week
  └── ...
```

You do not need to write the WBR by hand. You run the skill, and Claude creates the review for you.

---

## Build Your First WBR

Open a Claude session with your second-brain folder added, then run:

```text
run @second-brain/assets/build-wbr.md
```

That is the full prompt.

The skill will:

- connect to Snowflake
- pull this week's and last week's data
- calculate changes
- write the report
- save it into your WBR folder

![image](./images/1.png)

---

## What the WBR Contains

Each weekly report is built in a consistent format so you can scan it quickly.

### 1. Week Summary
A short plain-English summary of what happened this week.

### 2. Channel Performance
A table with the main numbers for your channels, such as subscribers, views, connections, and reactions.

| Metric | This week | Last week | Change |
|--------|-----------|-----------|--------|
| YouTube subscribers | — | — | — |
| YouTube total views | — | — | — |
| LinkedIn connections | — | — | — |
| LinkedIn post reactions | — | — | — |

### 3. Top Content This Week
The best-performing YouTube video and LinkedIn post from the last 7 days, along with why they did well.

### 4. Company Pulse
A quick view of the companies in your projects folder — what changed, what was added, and what may need attention.

### 5. What Needs Attention
The sections that are underperforming or falling behind, such as:

- metrics that dropped by more than 10%
- companies that have not been updated in 14+ days
- tables in Snowflake with no new data this week

### 6. One Recommendation
A single action for next week based on the patterns in the data.

> The WBR becomes more useful once you have a few weeks of history in Snowflake. If you are still early in the setup, run it after a week or two so the week-over-week comparisons actually mean something. In the meantime, you can also use the same structure to create an Executive Business Review, which is a one-time snapshot of everything in one place.

---

## What Happens Behind the Scenes

When you run the skill, Claude does a few important things in order:

1. Connects to Snowflake through Composio
2. Pulls data from the last 7 days
3. Pulls the previous 7 days for comparison
4. Writes the report in markdown
5. Saves it to a dated file in the WBR folder

That means every week you get a fresh report without needing to rebuild it from scratch.

---

## Automate It: Weekly WBR Every Monday at 8am

Once this is set up, you do not have to remember it.

Use Claude Code's scheduler to run the WBR every Monday at 8:00 AM.

```text
Using Claude Code's built-in scheduler, set up a weekly job that runs every Monday at 8:00 AM.

When the job runs, execute:
run @second-brain/skill/build-wbr.md

The skill handles everything automatically:
- Connects to Snowflake via Composio MCP
- Queries this week's and last week's data
- Calculates week-over-week changes
- Writes the WBR report
- Saves it to second-brain/wiki/wbr/YYYY-MM-DD.md

If no data is found for the current week, log: "No data for this week — WBR skipped."

Schedule this as a recurring job that runs automatically every Monday at 8:00 AM.
```

> Why Monday at 8am? Because your weekly data fetch usually happens later in the morning. Scheduling the WBR earlier gives you a clean review of the previous week before the new cycle begins.

---

## Your WBR Archive Over Time

After a few weeks and months, your WBR folder becomes one of the most valuable parts of your second brain.

```text
second-brain/wiki/wbr/
  ├── 2026-06-01.md
  ├── 2026-06-08.md
  ├── 2026-06-15.md
  ├── 2026-06-22.md
  ├── 2026-06-29.md
  ├── 2026-07-07.md
  └── 2026-07-14.md
```

Each file is a snapshot in time. Over time, you can ask Claude to read across multiple WBRs and spot trends that would be hard to notice from week to week.

---

## Why This Pattern Matters

Amazon is famous for its WBR process because it creates one shared source of truth.

Everyone looks at the same numbers. Everyone reads the same summary. Everyone starts from the same context.

That is exactly what you are building here.

The value is not in writing the report. The value is in making sure you always have a clear and consistent view of what changed.

---

## What You Have Learned

- Why a WBR is useful as a weekly decision-making tool
- How the build-wbr skill pulls data from Snowflake and compiles a report
- How to structure a weekly review around summary, performance, attention areas, and recommendations
- How to automate the report so it runs every week without manual effort

---

## What's Next

[← Back to module index](../README.md)
