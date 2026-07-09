# Lab 4: Competitor Monitoring

## How World-Class Product Teams Build Automated Intelligence Systems

--

Picture this.

You're a Product Manager at LegalGraph.

You've just walked into a quarterly review with your Head of Sales.

She pulls up a lost deal report.

*"We lost three mid-market deals this month to Harvey AI. Prospects keep saying Harvey does contract drafting natively inside their existing legal workflow. Did we know they shipped that?"*

You open your laptop. You search. Harvey AI announced it six weeks ago.

Six weeks.

You had no idea.

---

That feeling? It's not a one-time thing.

Legal tech is moving fast. Harvey AI raised $300M. Ironclad is pushing into mid-market. Spellbook is shipping AI redlining features every two weeks. Luminance just added a compliance module that overlaps directly with your COI Agent.

Today, you're going to build a system that makes sure LegalGraph is never blindsided again.

Here's what you'll have by the end of this lab:

```
Prompt 1 — Build company context + register in Claude's memory

Prompt 2 — Find top 10 legal tech competitors ranked by threat

Prompt 3 — Hook: auto-analyze whenever anyone drops competitor research

Prompt 4 — Scheduler: every Monday, search + send report to Slack
```

Let's build it step by step.

---

## Step 1 — Give Claude Your LegalGraph Context

Before we run a single query, let's think about something.

If you hired a brilliant analyst on their first day and immediately asked them *"which legal tech companies threaten us most?"* — what would they come back with?

A generic list. The obvious names. Ironclad because it's well known. Harvey AI because it raised a lot. No sense of whether your specific differentiators — on-premise deployment, zero data training, COI automation, mid-market focus — make certain competitors more or less dangerous for *you specifically*.

Claude has the exact same problem out of the box.

It knows the legal tech landscape broadly. But it doesn't know that your customers are mid-market enterprises who care deeply about data privacy. It doesn't know your strongest differentiator is private cloud deployment. It doesn't know your COI Agent is unique or that your lease analysis competes directly with Evisort.

So before we ask Claude anything about competitors, we need to give it a proper briefing on LegalGraph first.

---

### Prompt 1 — Build Context and Register It in Claude's Memory

One prompt. Claude creates the file and registers it in CLAUDE.md so it's always referenced going forward.

> **Want to skip ahead?** Download the sample `context.md` for LegalGraph [here →](#). Create a `company/` folder, drop the file in, and add it to Claude — then jump straight to Prompt 2. Otherwise, use the prompt below to build your own.
> [Download it here →](#)
> Create a folder named `company/` in your project, drop the file in as `context.md`, and then add the folder to Claude before running Prompt 2.

```
Do two things:

1. Create a company context file with the following details.
   If the company/ folder does not exist, create it first.
   Save as company/context.md.

   Company: LegalGraph
   Product: AI-powered contract review, COI tracking, lease analysis,
   and compliance automation for mid-market enterprises.

   Target customer: Legal and compliance teams at mid-market companies
   (100–2000 employees) overwhelmed by manual contract workflows
   and unable to afford enterprise CLM solutions.

   Our top differentiators:
   - On-premise and private cloud deployment (Azure, GCP, AWS) —
     customer data never leaves their environment
   - Zero data used for model training — ever
   - COI Agent: automated Certificate of Insurance tracking with
     escalating reminders
   - Bulk contract review: analyze 10+ contracts simultaneously
     with side-by-side comparison
   - MS Word plugin available via Microsoft AppSource

   Our known gaps:
   - SOC 2 Type II still in progress (not yet certified)
   - No native contract drafting (review and analysis only)
   - No public pricing — enterprise sales motion only
   - Integration depth limited vs established CLM platforms

   Stage: Early growth, targeting mid-market enterprises

2. Add this to CLAUDE.md:

   ## LegalGraph Company Context
   Always reference @company/context.md when:
   - Analyzing legal tech competitors
   - Evaluating threats to our contract review or COI product lines
   - Assessing positioning in the mid-market CLM space
   - Generating competitive reports or threat assessments
```

Once this runs, open `company/context.md` and verify it looks right. The more accurate this file is, the sharper everything that follows will be.

From this point on, every competitive analysis Claude does is grounded in your actual company — not a generic view of the market.

---

### Prompt 2 — Find Your Top 10 Competitors

Now let's see what Claude can do with that context.

```
Using @company/context.md, identify our top 10 competitors
in the legal AI and contract management space.

Include companies competing in any of these areas:
- Contract review and redlining
- COI / Certificate of Insurance tracking
- Lease analysis and abstraction
- Compliance automation for mid-market

For each competitor, evaluate:
- Data privacy model (On-prem available / SaaS-only)
- AI contract features (score 1–10)
- Mid-market fit (score 1–10)
- Pricing model (Freemium / SMB / Mid-market / Enterprise-only)
- Direct overlap with our COI Agent or Lease Analysis product
- Recent momentum (funding, launches, hiring signals)

Rank by threat level to LegalGraph: High / Medium / Low
Output as a table.

If the competitor-notes/ folder does not exist, create it first.
Save the output to competitor-notes/top-competitors.md.
If the file already exists, overwrite it.
```

Run this and look at the output carefully.

Notice what's happening: because Claude knows your differentiators and gaps, it's ranking competitors relative to *your* specific position — not just by market size. A company with aggressive mid-market pricing and SOC 2 certification matters more to you right now than an enterprise-only player that never touches your ICP.

That's grounded competitive intelligence. Not generic market research.

---

> **Checkpoint**
> Review the table. Does the ranking feel right?
> Are there players missing — a niche COI tool, a regional CLM?
> Add anything missing to `company/context.md` under a "Known competitors" section.

---

## Step 2 — Hook: Auto-Extract Competitor Intelligence

Great. You now have a ranked competitor list grounded in LegalGraph's actual positioning.

But here's the thing — you ran that analysis once.

Next week, your sales engineer pastes a Spellbook feature breakdown into Slack. Your CEO forwards an Ironclad press release. Your CS team drops notes from a call where a prospect compared you to Evisort.

All of that intelligence lands in random places. To act on it, you'd have to manually collect it, read it, run a new prompt, and update your tracker. Every. Single. Time.

What if Claude just did that automatically the moment anyone dropped new research?

That's exactly what a hook does.

A hook is a trigger — *when something happens, Claude does something automatically.* You set up a hook that watches a folder. The moment a file lands in it — a competitor teardown, a sales rep's notes, a pricing screenshot — Claude wakes up, reads it, extracts the intelligence, compares it against your company context, and logs the findings.

Your team keeps doing what they already do. The analysis runs in the background without anyone asking.

**Here's how hooks actually work under the hood.**

When an event fires inside a Claude Code session, Claude passes a JSON context about that event to your hook handler. Your handler reads it, takes action, and optionally returns a decision back.

Here are the five events you'll use most often as a PM building automations:

| Event | When it fires |
|---|---|
| `FileChanged` | When a watched file changes on disk — you specify which filenames to watch |
| `PostToolUse` | After a tool call succeeds |
| `UserPromptSubmit` | When you submit a prompt, before Claude processes it |
| `PreToolUse` | Before a tool call executes — can block it |
| `Stop` | When Claude finishes responding |

For our competitor monitoring use case, we're using **`FileChanged`** — it watches the `competitor-notes/` folder and fires the moment a new research file lands in it.

**But how does Claude actually decide what to do when a hook fires?**

Let's walk through it using our exact example — your sales rep just dropped `harvey-ai-update.md` into `competitor-notes/`.

**1 — Event fires**
The `FileChanged` event fires. Claude Code packages the file details as JSON and sends it to your hook handler:
```json
{ "event": "FileChanged", "file": "competitor-notes/harvey-ai-update.md" }
```

**2 — Matcher checks**
Your hook has a matcher set to `"competitor-notes/*"`. It checks the file path — matches. The hook group activates. If you'd used `"*"`, it would activate on every file change across your entire project.

**3 — If condition checks**
The `if` condition checks that the file is a `.md` file inside `competitor-notes/`. It matches, so the handler runs. If your sales rep had dropped a `.png` screenshot instead, the `if` check would fail and the handler would be skipped — no wasted processing.

**4 — Hook handler runs**
The handler reads `harvey-ai-update.md`, extracts the intelligence, compares it against `@company/context.md`, and appends the findings to `summary.md`. It exits with code `0` — meaning the job is done, no further decision needed.

**5 — Claude Code acts**
Claude Code sees the clean exit, confirms the hook completed, and moves on. Your `competitor-notes/summary.md` now has a fresh entry with Harvey AI's update, threat level, and the implication for LegalGraph — without anyone running a single prompt.

> Want to go deeper on how hooks work? [Read the full hooks documentation →](https://code.claude.com/docs/en/hooks#hook-lifecycle)

---

### Prompt 3 — Set Up the Competitor Notes Hook

```
Set up a hook in my Claude Code settings:

Trigger: Whenever a new file is added to /competitor-notes

Action:
1. Read the file
2. Identify which competitor it's about
3. Extract:
   - New features or product capabilities
   - Pricing or packaging changes
   - Data privacy or security updates
   - Compliance certifications gained (SOC 2, ISO, etc.)
   - AI model or accuracy improvements
   - Mid-market or enterprise positioning shifts
4. Compare each finding against @company/context.md:
   - Does this competitor now match our on-premise deployment story?
   - Does this threaten our COI Agent's uniqueness?
   - Does this affect our mid-market positioning?
5. Flag threat level: High / Medium / Low
6. If competitor-notes/summary.md does not exist, create it.
   Append a structured summary with: date, source file,
   competitor name, findings, threat level.
```

---

Now test it.

Create a file in `competitor-notes/` with rough notes about any competitor you've observed recently — even three or four bullet points.

Watch what Claude does.

It reads the raw notes. Structures the intelligence. Compares it specifically against LegalGraph's positioning. Flags the threat level. Appends a clean summary to `summary.md`.

You didn't run a prompt. It just happened.

---

> **Checkpoint**
> Try two files:
>
> File 1: Notes about Harvey AI's contract drafting announcement
> File 2: Notes about Ironclad's new mid-market pricing tier
>
> Open `competitor-notes/summary.md` after each.
> Notice how Claude is evaluating each finding against LegalGraph's
> positioning — not generically.

---

## Step 3 — Scheduler: Proactive Weekly Intelligence

The hook is working. Every time someone drops a file, Claude analyzes it automatically.

But notice what the hook depends on — someone on your team actually dropping a file.

What about the week everyone is heads-down on a release? Nobody's sharing research. Meanwhile, Evisort quietly added a COI tracking feature that competes directly with your agent. Spellbook updated their pricing to go after your mid-market ICP. Neither made noise. Nobody on your team caught it.

Hooks are reactive. The biggest threats in legal tech often move quietly, without anyone on your team noticing.

You need something that goes looking on its own — a scheduled job.

Think of it like hiring a weekly analyst who shows up every Monday morning without you asking, searches for what moved in the legal tech market over the past seven days, writes up the threat assessment, and leaves it on your desk. A scheduled job in Claude Code does exactly that — it fires at a set time, every week, automatically, whether or not your team noticed anything.

**Here's how the scheduler lifecycle works — using our exact setup.**

A scheduled job in Claude Code has three parts: a schedule (when to fire), a task (what to run), and an optional output action (what to do with the result). Let's walk through what happens every Monday at 9am.

**1 — Schedule triggers**
The cron expression `0 9 * * 1` fires at 9:00 AM every Monday. Claude Code wakes up the scheduled task regardless of whether anyone is actively using it. No session needs to be open. No prompt needs to be run.

**2 — Task context is loaded**
Before running, Claude Code loads the task's registered context — in our case, `@company/context.md`. This is what makes the search grounded in LegalGraph's positioning rather than generic legal tech news.

**3 — Task executes**
Claude searches for updates from the past 7 days across the competitor list. For each competitor with notable activity, it generates:
- What changed
- How it affects LegalGraph specifically
- Threat level: High / Medium / Low
- Recommended action

```json
{
  "schedule": "0 9 * * 1",
  "context": ["company/context.md"],
  "task": "search legal tech competitors, assess threats, save report",
  "output": "competitor-notes/weekly-report-2025-01-13.md"
}
```

**4 — Output is saved**
The report is written to `competitor-notes/weekly-report-[date].md`. If the folder doesn't exist, the scheduler creates it. Each week gets its own file — nothing is overwritten.

**5 — Slack delivery runs**
After the file is saved, the scheduler triggers the Slack step. It formats the ranked report and posts it to `#competitor-intel`. Your team sees it before their Monday standup — without anyone asking for it.

> Want to go deeper on how scheduled jobs work? [Read the full scheduler documentation →](https://docs.anthropic.com/en/docs/claude-code)

---

### Prompt 4 — Set Up the Weekly Scheduler and Send to Slack

The scheduler runs the search. The Slack delivery is just part of what it does when it's done. One prompt handles both.

```
Create a weekly scheduled task:

Schedule: Every Monday at 9:00 AM

Task:
1. Search for updates from the past 7 days across these
   legal tech competitors: Ironclad, Harvey AI, Evisort,
   Spellbook, Luminance, DocuSign CLM, LinkSquares,
   Icertis, ContractPodAi, Clio.

   For each competitor with notable activity, generate:
   - What changed (1–2 sentences, specific)
   - How it affects LegalGraph based on @company/context.md
   - Threat level: High / Medium / Low
   - Recommended action for our product or go-to-market team

   Sort by threat level: High first.
   Save as competitor-notes/weekly-report-[date].md

2. Then send the report to Slack.
   Channel: #competitor-intel
   Format:
   - Header: "⚖️ LegalGraph Weekly Competitor Update — [Date]"
   - 🔴 High threat  🟡 Medium threat  🟢 Low threat
   - One bullet per competitor: what changed, implication, action
   - Footer: "Full report → competitor-notes/weekly-report-[date].md"
```

---

> **Checkpoint**
> Manually trigger the scheduler once to test it.
> Check `competitor-notes/` for the report file.
> Check `#competitor-intel` in Slack for the message.
> If both landed — your competitive intelligence system is fully live.

---

## The Full System

Step back and look at what you built.

```
Your Team Drops a Competitor Note
              ↓
         Hook Fires
              ↓
    Claude Reads the Raw Notes
    Compares Against LegalGraph's Differentiators
    Flags Threat Level
    Updates competitor-notes/summary.md

    ─────────────────────────────

    Every Monday 9:00 AM
              ↓
    Scheduler Fires Automatically
              ↓
    Claude Searches Legal Tech News (Past 7 Days)
    Generates Threat Assessment for LegalGraph
              ↓
    Sends Ranked Report to #competitor-intel
```

Three layers working together:

| Layer | Trigger | What it catches |
|---|---|---|
| Manual query | You run it | Deep landscape view — before a board meeting, pricing review, or roadmap planning |
| Hook | File dropped in folder | Anything your team surfaces — teardowns, sales notes, press releases |
| Scheduler + Slack | Every Monday 9am | Everything nobody noticed — quiet launches, pricing tweaks, certification updates |

---

## Summary

Here's what changed.

**Before this lab:**
- Competitive intelligence was manual, scattered, always three weeks behind
- Lost deal debriefs were the first time you heard about competitor features
- Research lived in one Slack thread nobody checked

**After this lab:**
- Claude knows LegalGraph's differentiators and gaps well enough to evaluate threats meaningfully
- Any research your team shares is automatically analyzed and logged
- Every Monday morning, your team wakes up to a proactive update in Slack — ranked by threat, with recommended actions
- You have a metrics-based view of your top 10 legal tech competitors grounded in your actual positioning

Four prompts. No code.

That's the shift.

---

## Claude Concepts Covered in This Lesson

| Concept | Where it appeared | Learn more |
|---------|-------------------|------------|
| **CLAUDE.md memory** | Step 1 — "tell Claude to always use this file when doing competitive analysis... every competitive analysis Claude does is grounded in your actual company" | [Memory & CLAUDE.md →](https://docs.anthropic.com/en/docs/claude-code/memory) |
| **Hooks** | Step 2 — "a hook is a trigger... the moment a file lands in that folder, Claude wakes up, reads it, extracts the intelligence, and logs the findings" | [Claude Code overview →](https://docs.anthropic.com/en/docs/claude-code) |
| **Scheduled tasks** | Step 3 — "a scheduled job fires at a specific time, automatically, on repeat... every Monday at 9am Claude wakes up, searches for legal tech competitor updates" | [Claude Code overview →](https://docs.anthropic.com/en/docs/claude-code) |
| **Context grounding** | Step 1 — "because Claude knows your differentiators and gaps, it's ranking competitors relative to your specific position — not just by market size" | [Prompt engineering →](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) |
| **System prompts** | Step 1 — "from this point on, every competitive analysis Claude does is grounded in your actual company — not a generic view of the market" | [System prompts →](https://docs.anthropic.com/en/docs/build-with-claude/system-prompts) |