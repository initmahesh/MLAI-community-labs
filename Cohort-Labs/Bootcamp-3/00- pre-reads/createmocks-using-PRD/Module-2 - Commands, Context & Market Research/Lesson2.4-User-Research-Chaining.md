# Lesson 2.4 — User Research: Chaining Prompts to Understand Customer Pain Points

---

## Where You Are

In Lesson 2.3 you ran chained market research on the Lease Compliance feature and updated CLAUDE.md with market intelligence.

Now you use the `/user-research` command you built in Lesson 2.2 — same chaining pattern, different lens. Instead of market size and competitors, you're going deep on who your user is, what job they're trying to do, and where the current workflow breaks down.

---

## What You're Researching

**Feature:** Lease Compliance Reporting
**Research question:** Who actually does this work, what does their current workflow look like, and where is the pain severe enough to justify switching to a new tool?

---

## Pre-Flight Checklist

- [ ] Verify `/user-research` command exists: `ls ~/.claude/commands/` — you should see `user-research.md`. If not, go back to Lesson 2.2 Step 3
- [ ] Verify your market research file from Lesson 2.3 is saved — you'll `@` reference it for context
- [ ] Verify `outputs/` folder exists (create if not: `mkdir outputs`)
- [ ] CLAUDE.md is loaded with LegalGraph context and market intelligence from Lesson 2.3

---

## The Research Session

### Stage 1 — Run Your Baseline with `/user-research`

Start here. This gives you the structured baseline report using the template you built in Lesson 2.2.

> **Company context:** The prompt uses `@` to load your company context file. We're using LegalGraph as the bootcamp example. Swap the filename if using your own company.

**Using LegalGraph context (bootcamp default):**
```
@company-context.md
@outputs/market-research-lease-compliance-<date>.md

/user-research in-house legal and finance teams doing lease compliance and IFRS 16 reporting
```

**Using your own company context:**
```
@<your-company-context-file>.md
@outputs/<your-market-research-file>.md

/user-research <your research topic>
```

> Loading the market research from Lesson 2.3 means Claude knows the market size, competitive landscape, and strategic context before generating user personas and pain points. The user research stays grounded in the same opportunity — not a generic study of any compliance team.

This runs your full user research template — Research Objective, User Persona, Jobs to Be Done, Key Findings, Pain Points & Unmet Needs, Implications for Product, and Open Questions — and saves the output to your working directory.

**After Stage 1:**
- Read the output — check that personas are specific, not generic job titles
- Note any shallow sections — you'll go deeper in Stages 2 and 3
- The saved `.md` file is your baseline. You'll `@` reference it in all following stages

---

### Stage 2 — Workflow Deep-Dive

Run only after reviewing Stage 1. Replace `<your-stage1-filename>` with the actual filename saved in Stage 1.

```
@<your-stage1-filename>.md

Using the user research above, now go deep on the current lease compliance workflow for in-house legal and finance teams.

I need to understand the step-by-step process:
- What triggers the lease compliance workflow? (audit cycle, new lease signed, reporting deadline?)
- Who does each step — legal, finance, or both?
- What tools are they using today at each step? (Excel, ERP, CLM, manual review?)
- Where do handoffs happen between legal and finance — and where do those break down?
- How long does the full workflow take end-to-end?
- What does a mistake or missed deadline cost them? (audit finding, restatement, fine?)

Be specific. If you find survey data, forum posts, or analyst research on this workflow, cite it.

Update the same file @<your-stage1-filename>.md — append a new "## Current Workflow" section with these findings. Do not rewrite the existing sections.
```

> **If the session is getting long after Stage 2:** Use `/compact` before Stage 3. Do not use `/clear` — you'll lose the research chain.

---

### Stage 3 — Pain Point Prioritization

Replace `<your-stage1-filename>` with the same file from Stage 1.

```
@<your-stage1-filename>.md

Using the user research and workflow analysis in the file above, now prioritize the pain points by severity and frequency.

I need to understand:
- Which workflow steps cause the most pain — and why? (time, error rate, compliance risk?)
- Which pain points are shared across legal and finance teams vs. unique to one?
- What workarounds have teams built? What does it tell us about the real need?
- Which pain points are urgent (deadline-driven) vs. chronic (always there but tolerated)?
- What would "good enough" look like for each pain point — and what would "delightful" look like?

End with: a ranked list of the top 3 pain points LegalGraph should design for first, with a one-line rationale for each ranking.

Update the same file @<your-stage1-filename>.md — append a new "## Pain Point Prioritization" section. Do not rewrite the existing sections.
```

---

### Stage 4 — Full Synthesis

This ties everything together into a decision-ready user research report. Replace `<your-stage1-filename>` with your actual filename.

```
@<your-stage1-filename>.md
@company-context.md

Using the full user research, workflow analysis, and pain point prioritization in the file above:

1. Synthesize the complete picture — who the user is, what job they're doing, where the workflow breaks, and what they actually need
2. Identify the primary user vs. the primary buyer — these may not be the same person
3. Write 3 Jobs to Be Done statements in this format:
   "When [situation], I want to [motivation], so I can [outcome]"
4. Identify the top unmet need that LegalGraph is best positioned to solve — with evidence from the research
5. Flag any assumptions in this research that need validation with real users before building
6. End with Open Questions — what we still don't know, with a suggested research method for each

Structure the output using the same format as the Stage 1 baseline. Save the completed report to: outputs/user-research-lease-compliance-<today's date>.md
```

---

## Step 5 — Update CLAUDE.md with User Research Intelligence

Once Stage 4 is saved, run this prompt. Replace `<your-stage1-filename>` with your actual filename:

```
@outputs/user-research-lease-compliance-<date>.md
@./CLAUDE.md

Read the user research report and the current CLAUDE.md above.

Extract the findings that matter for ongoing LegalGraph product decisions. Append a new "## User Research Intelligence" section to ./CLAUDE.md.

The section must include:
- Primary user and primary buyer for Lease Compliance Reporting (be explicit — they may differ)
- Top 3 pain points ranked by severity
- The most important Job to Be Done (the one that drives switching behavior)
- One key assumption that still needs validation
- Research date: [today's date]

Rules:
- Do not modify anything already in CLAUDE.md — only append
- Keep the section under 12 bullet points total
- Write for speed — a PM reading in 30 seconds should understand what to build and for whom
- If a finding doesn't change a product or design decision, leave it out
```

> Run `/memory` after updating to confirm the new section loads in your next session.

---

## What Happens Behind the Scenes

![images](./images/opiop.png)

**1. You run `/user-research` in Stage 1**
Claude Code loads `~/.claude/commands/user-research.md`, replaces `$ARGUMENTS` with your topic, and runs the full structured prompt. The `@company-context.md` file is read first — so Claude knows your personas, product context, and goals before it starts generating user profiles and pain points.

**2. The output saves to a `.md` file**
Claude writes the structured user research report to your working directory as a permanent file. It's not a chat message — it's a referenceable artifact that every following stage builds on.

**3. `@filename` pulls the file into every stage**
When you prefix Stage 2 or 3 with `@<your-stage1-filename>.md`, Claude reads the full saved file before processing your instructions. It's not relying on conversation memory — it's reading the actual document. This keeps the research grounded and consistent across a long session.

**4. The file grows section by section**
Each stage appends a new section to the same file instead of creating a new one:
- After Stage 1: Research Objective, Persona, JTBD, Key Findings, Pain Points
- After Stage 2: + Current Workflow (step-by-step)
- After Stage 3: + Pain Point Prioritization (ranked)

By the time Stage 4 runs, the single file contains the full picture.

**5. Stage 4 synthesizes the full accumulated file**
Stage 4 reads the entire file — all sections from Stages 1–3 — and produces a final, clean report with JTBD statements, primary user identification, and pre-build assumptions flagged. The output is richer than any single prompt because it's synthesizing structured depth, not surface-level breadth.

**6. CLAUDE.md append in Step 5**
Claude reads both your user research output and your existing CLAUDE.md. It extracts only what changes a product or design decision — primary user, ranked pain points, top JTBD, key assumption — and appends it without touching anything already in the file. Next session, that intelligence loads automatically alongside your market research from Lesson 2.3.

```
/user-research + @company-context → saves file
    ↓
Stage 2: @file → workflow deep-dive + append → file grows
    ↓
Stage 3: @file → pain point prioritization + append → file grows
    ↓
Stage 4: @file (full) → synthesize → final report saved
    ↓
Step 5: @final report + @CLAUDE.md → append intelligence → loads every session
```

---

## Things to Keep in Mind

**On user research vs. market research:**
- Market research tells you the size of the opportunity. User research tells you if you're solving the right problem. Both need to agree before you write a PRD.
- If your user research contradicts the market research from Lesson 2.3 — that's a signal, not a problem. Surface it in Open Questions.

**On specificity:**
- "Users find it time-consuming" is not a finding. "Finance teams spend 3–4 hours per lease per quarter reconciling Excel with ERP data" is a finding.
- Push Claude on vague outputs: "Give me a specific example of what this workflow looks like for a 500-person company with 40 active leases."

**On context management:**
- Always use `/compact`, not `/clear`, during a chained research session.
- If Claude loses track of earlier stages, paste the key findings manually before running Stage 4.

---

## What You've Learned

- **User research chaining uses the same pattern as market research** — four stages, each deepening the previous: baseline persona → workflow deep-dive → ranked pain points → full synthesis. The chain structure is reusable across any research type.
- **How market research context feeds user research** — Stage 1 loads the Lesson 2.3 output via `@` to ground the user research in the competitive and market reality you already established. Research compounds when outputs chain.
- **Jobs to Be Done as a PM framework** — functional job (what the user is trying to accomplish), emotional job (how they want to feel), social job (how they want to be seen). Claude applies this framework when you use the `/user-research` command.
- **Pain point prioritization produces PRD inputs** — Stage 3 ranks pain points by frequency and severity. This ranking directly informs the P0/P1/P2 requirements in the PRD you'll build in Lesson 2.5.
- **CLAUDE.md as a compounding research layer** — each lesson that updates CLAUDE.md adds a new intelligence layer. By now, Claude knows your market, your competitors, your users, and their pain points — all loading silently at the start of every session.

---

*Next: [Lesson 2.5 — PRD](./Lesson2.5-PRD.md)*
