# Lesson 3.3 — Skills and Hooks In Claude Code: Automating Your PM Workflow

---

## Where You Are

Across Module 2 and Lessons 3.1–3.2 you built:
- Custom slash commands for market research, user research, and PRDs
- A clickable prototype deployed to GitHub Pages
- Job assistants connected to external tools via MCP

Now you go to the next level: **Skills** (reusable prompt packages that Claude loads automatically) and **Hooks** (actions that fire automatically based on what Claude does — without you having to type anything).

This is where Claude Code stops feeling like a chat tool and starts feeling like a configured PM workflow system.

---

## Part 1 — Skills

### What Is a Skill?

A skill is a prompt file that Claude Code loads automatically in specific situations — triggered by what you're doing, not by a command you type.

The difference from a slash command:
- **Slash command** → you trigger it: `/market-research`
- **Skill** → Claude triggers it: you're writing a PRD and Claude automatically applies your PRD standards without being asked

Skills live in `~/.claude/skills/` (global) or `.claude/skills/` (project-level).

---

### PM Use Case: The PRD Review Skill

**The problem:** Every time you finish a PRD draft, you have to manually ask Claude to review it for completeness. You forget sometimes. The review is inconsistent.

**The skill:** Every time Claude writes or edits a file that looks like a PRD, it automatically checks it against your PRD standards — without you asking.

**Step 1 — Create the skill file**

Open Claude Code Desktop and run:

```
Create the file ~/.claude/skills/prd-reviewer.md with the following content:

---
name: PRD Reviewer
description: Automatically review any PRD draft for completeness and quality against LegalGraph standards
triggers:
  - Writing or editing a file named prd-*.md
  - Writing or editing a file in the outputs/ folder that contains "## Problem Statement"
---

When triggered, review the PRD against these standards:

**Completeness check — flag any missing section:**
- [ ] Problem Statement (one paragraph — pain, persona, why now)
- [ ] User Persona (primary user AND primary buyer identified separately)
- [ ] Jobs to Be Done (at least one JTBD in "When / I want to / So I can" format)
- [ ] Success Metrics (primary metric with baseline, target, and timeframe)
- [ ] Requirements (P0 list — each written as a testable acceptance criterion)
- [ ] Out of Scope (at least 3 explicit exclusions)
- [ ] Open Questions (at least 3, each with an owner)

**Quality check — flag if any of these are true:**
- Success metrics are vague (e.g., "improve satisfaction" with no number)
- Requirements are vague (e.g., "user can view reports" with no acceptance criteria)
- Out of Scope is empty or has fewer than 3 items
- Personas are job titles, not specific people with specific goals

**Output format:**
- List what's complete (✓)
- List what's missing or weak (✗) with a one-line fix suggestion
- End with: "Confidence to hand to eng: High / Medium / Low" with a one-line rationale
```

![alt text](./images/skill.png)

---

![alt text](./images/skilla1.png)

**Step 2 — Test it**

Open your PRD from Lesson 2.5:

```
@outputs/prd-lease-compliance-<date>.md

Review this PRD using your PRD review skill.
```

![alt text](./images/skills3.png)

Claude applies the skill standards and gives you a structured completeness report — without you having to explain what to look for.

![alt text](./images/skills33.png)

---

### Second PM Skill: The Research Quality Checker

> **Try It On Your Own**

You've seen how the PRD Reviewer skill works. Now build one yourself.

**The goal:** Create a skill that automatically scans any research output for vague claims and missing citations before you present it to stakeholders.

**What it should do:**
- Trigger on any file named `market-research-*.md` or `user-research-*.md`
- Flag red flags: unsourced claims, superlatives without data, estimated numbers presented as facts, competitor claims without evidence
- For each red flag: quote the phrase, explain why it's a problem, suggest the fix
- End with a count of red flags found

**Your task:**
1. Create the skill file at `~/.claude/skills/research-quality.md` following the same structure as the PRD Reviewer above
2. Test it against your market research from Lesson 2.3: `@outputs/market-research-lease-compliance-<date>.md`
3. Count how many red flags come back — aim for zero before presenting to your GC

> **Hint:** Follow the exact same file structure as the PRD Reviewer skill — `name`, `description`, `triggers`, then the instructions. The only thing that changes is what you're checking for.

---

## Part 2 — Hooks

### What Is a Hook?

A hook is a shell command that Claude Code runs automatically at specific points — before or after tool use, when a session starts, before compacting, etc.

You configure hooks in your settings file. Claude Code executes them — you don't have to remember to run them.

**PM use cases:**

| Hook | Trigger | What it does |
|------|---------|--------------|
| Format reminder | Before every session | Reminds Claude to always use your PRD template format |
| Research tone guard | Before Claude writes any file | Tells Claude to flag vague claims before saving |
| Session greeter | When a session starts | Claude summarises your current project priorities from CLAUDE.md |
| PRD review prompt | After Claude writes a PRD file | Claude automatically runs a completeness check on what it just wrote |

---

### Hook Demo 1 — Session Greeter

Every time you open Claude Code in your project, this hook automatically briefs you on your current priorities — without you having to ask.

**Step 1 — Check your current `~/.claude/settings.json`**

Before adding any hooks, open the file. It should look like this — just a WebSearch permission from earlier setup:

```json
{
  "permissions": {
    "allow": [
      "WebSearch"
    ]
  }
}
```

**Step 2 — Add the hook in Claude Code Desktop:**

```
Add a SessionStart hook to ~/.claude/settings.json.

When a session starts, Claude should:
- Read @./CLAUDE.md
- Print a short brief: current feature focus, top open question, and one thing to do today
- Keep it under 5 lines
```

![alt text](./images/hook23.png)

**Your `~/.claude/settings.json` — After:**

![alt text](./images/hookiop.png)

> Claude uses the `update-config` skill to write hooks — that's why `Skill(update-config)` and `Skill(update-config:*)` appear in your permissions automatically after it runs.

**What you see every morning when you open Claude Code:**

```
Current focus: Lease Compliance Reporting — PRD under GC review
Top open question: IFRS 16 vs ASC 842 — decision needed by April 5 (Jennifer)
Today: Follow up with Rachel on discount rate assumption
```

No more context-switching cost at the start of every session.

---

### Hook Demo 2 — Auto PRD Review

Every time Claude finishes writing a PRD file, this hook automatically runs a completeness check on it — without you having to ask.




**Step 2 — Add the hook in Claude Code Desktop:**

```
Add a PostToolUse hook to ~/.claude/settings.json.

After Claude writes any file matching prd-*.md, Claude should automatically:
- Check the file for missing sections (Problem Statement, Success Metrics, Out of Scope, Open Questions)
- Flag any section that is empty or under 2 bullet points
- Print a one-line summary: "PRD check: X sections complete, Y need attention"
```



> **Note:** Permissions don't change this time — `Skill(update-config)` is already there from Demo 1. Claude just merges the new `PostToolUse` block into your existing `hooks` object.

**What happens after every PRD save:**

```
PRD check: 6 sections complete, 1 needs attention
→ Out of Scope has only 1 item — add at least 2 more before sharing with eng
```

You catch gaps immediately — before your GC sees them.

---

### Hook Demo 3 — Research Tone Reminder

Before Claude writes any research file, this hook reminds it to cite sources and flag estimates — so you never get a research output full of vague claims.


**Step 2 — Add the hook in Claude Code Desktop:**

```
Add a PreToolUse hook to ~/.claude/settings.json that triggers before any Write tool call on files matching market-research-*.md or user-research-*.md.

Before writing, Claude should remind itself:
- Every market size number must have a source or be flagged as estimated
- No superlatives without data (avoid "most companies", "widely adopted")
- Each competitor claim needs evidence
- Flag any section where data is missing rather than filling it with assumptions
```
```



```

> This is your fully configured `settings.json` after all three demos. Three hooks, three event types — all active, all running automatically.

This runs silently before every research file is saved — keeping your outputs citation-clean without any extra prompting.

---

## What Happens Behind the Scenes

**Skills:**

**1. Skills load on match, not on command**
Claude Code watches what tools are being used. When a skill's trigger pattern matches — a file being written that matches `prd-*.md` — Claude loads the skill prompt into context automatically. You didn't type `/prd-review`. It happened because you were working on a PRD.

**2. Skills are context injections**
A skill doesn't run a separate process. It injects the skill's prompt content into Claude's active context, adding constraints and instructions that shape how Claude responds. The PRD Reviewer skill tells Claude "also check these things" every time a PRD is touched.

**Hooks:**

**3. Hooks are shell commands, not Claude prompts**
A hook is a bash command that Claude Code's harness executes at a lifecycle event. Claude doesn't "decide" to run a hook — the harness runs it automatically. This is why hooks are reliable: they're not subject to Claude forgetting or misunderstanding.

**4. Hooks receive JSON on stdin**
Every hook gets a JSON payload describing what just happened — the tool name, the file path, the content. Your hook command reads this JSON (via `jq`) to decide what to do. The backup hook reads the file path, checks if it's in `outputs/`, and copies it. Simple, deterministic, always fires.

**5. The harness is always running**
Claude Code's harness runs throughout your session. Every Write, Edit, or Bash tool call passes through it. Hooks are registered once in `settings.json` and fire for every matching event — you don't have to remember them after setup.

```
You type a prompt
    ↓
Claude decides to use a tool (Write, Edit, Bash)
    ↓
Harness checks: any PreToolUse hooks for this tool? → runs them
    ↓
Tool executes
    ↓
Harness checks: any PostToolUse hooks for this tool? → runs them
    ↓ (backup hook copies file, changelog hook appends entry)
Claude continues
```

---

## Skills vs. Hooks vs. Commands — When to Use What

| | Slash Command | Skill | Hook |
|-|--------------|-------|------|
| **Triggered by** | You typing `/name` | Pattern match on what Claude is doing | Lifecycle event (write, edit, session start) |
| **Use for** | On-demand workflows | Automatic quality checks | Automatic side effects |
| **PM example** | `/market-research` | PRD completeness check | Auto-backup outputs |
| **Requires user action** | Yes | No | No |
| **Lives in** | `~/.claude/commands/` | `~/.claude/skills/` | `settings.json` |

---

## Things to Keep in Mind

- **Skills are additive, not directive.** A skill adds constraints to Claude's existing behavior — it doesn't take over. If a skill conflicts with your prompt, your prompt wins.
- **Test hooks with safe side effects first.** The backup hook and session logger are safe — they only append or copy. The Notion sync hook writes to an external system — test it manually before automating.
- **One hook at a time.** Add one hook, verify it works, then add the next. A broken hook in `settings.json` silently fails and can disable all settings from that file.
- **`/compact` doesn't clear hooks.** Hooks survive compaction. Skills reload with the new context. Your automations continue running through long sessions.

---

## What You've Learned

- **Skills vs. hooks vs. commands — when to use each** — commands run when you type them; skills trigger on natural language phrases and run adaptive, multi-step logic; hooks run automatically in response to events (file saved, session started) without any trigger from you. Each fills a different gap.
- **Skills enforce quality standards** — the PRD Reviewer and Research Quality Checker skills act as automatic quality gates. They run the same review criteria every time, on any PRD or research file, without you having to remember to check.
- **Hooks automate what you'd otherwise forget** — the auto-backup hook saves versions silently; the PRD changelog hook logs every edit; the session logger records every session. These are housekeeping tasks that matter when something goes wrong, and skills ensure they happen.
- **The session greeter hook eliminates cold-start prompting** — instead of re-briefing Claude at the start of every session, the hook fires automatically and loads your standing context. Every session starts warm.
- **Your PM workflow is now a system** — CLAUDE.md loads context, commands run research, skills review output, hooks log and protect your work. You assembled this piece by piece across three modules. It runs without you thinking about it.

---

## Module 3 Complete

You've extended Claude Code from a research and writing tool into a configured PM workflow system.

**What you've shipped across Module 3:**
- `mocks/lease-compliance-prototype.html` — deployed clickable prototype on GitHub Pages
- `/standup` and `/competitive-intel` job assistants
- Notion MCP connector — research syncs directly to your workspace
- PRD Reviewer and Research Quality Checker skills — automatic quality gates
- Auto-backup, PRD changelog, and session logger hooks — your workflow logs itself

Combined with Module 2's research-to-PRD workflow and Module 1's CLAUDE.md context system, you now have a full PM operating system running on top of Claude Code.

---

*Next: Module 4 — [Coming Soon]*
