# Lesson 2.5 — PRD: Turning Research into a Product Requirements Document

---

## Where You Are

Here's the chain you've built so far — all on the same feature:

| Lesson | What you did | Output file |
|--------|-------------|-------------|
| 2.3 | Market research — lease compliance market size, trends, competitors | `outputs/market-research-lease-compliance-<date>.md` |
| 2.4 | User research — who does this work, their workflow, ranked pain points | `outputs/user-research-lease-compliance-<date>.md` |
| **2.5** | **PRD — turning both into requirements** | `outputs/prd-lease-compliance-<date>.md` |

Now you use the `/prd` command you built in Lesson 2.2. You pass both research files as context — Claude uses the market findings to write the Problem Statement and competitive positioning, and the user research to write the personas, JTBD, and P0 requirements. You're not starting from scratch — you're synthesising research you already ran.

---

## What You're Building

**Feature:** Lease Compliance Reporting
**Goal:** A PRD your GC can review, your eng lead can scope, and your team can align on — built from the research you ran in 2.3 and 2.4, not from assumptions.

---

## Pre-Flight Checklist

- [ ] Verify `/prd` command exists: `ls ~/.claude/commands/` — you should see `prd.md`. If not, go back to Lesson 2.2 Step 3
- [ ] Verify your market research output from Lesson 2.3 is saved in `outputs/`
- [ ] Verify your user research output from Lesson 2.4 is saved in `outputs/`
- [ ] CLAUDE.md is loaded with LegalGraph context, market intelligence, and user research intelligence from Lessons 2.3 and 2.4

---

## The PRD Session

### Stage 1 — Run Your Baseline with `/prd`

Start here. This generates the structured PRD using the template you built in Lesson 2.2 — pre-loaded with everything Claude already knows from your research.

> **Company context:** The prompt uses `@` to load your company context and both research outputs. Claude uses all three to generate a grounded PRD, not a generic one.

**Using LegalGraph context (bootcamp default):**
```
@company-context.md
@outputs/market-research-lease-compliance-<date>.md
@outputs/user-research-lease-compliance-<date>.md

/prd Lease Compliance Reporting feature for LegalGraph
```

**Using your own company context:**
```
@<your-company-context-file>.md
@outputs/<your-market-research-file>.md
@outputs/<your-user-research-file>.md

/prd <your feature name>
```

> Claude reads all three files before generating the PRD — company context, market findings, and user research all feed directly into the requirements and success metrics.

This runs your full PRD template — Problem Statement, User Persona, Jobs to Be Done, Success Metrics, Requirements (P0/P1/P2), Out of Scope, and Open Questions — and saves the output to your working directory.

**After Stage 1:**
- Read the output — check that requirements trace back to real pain points from your research
- Check that success metrics are specific and measurable, not vanity metrics
- Note any sections that feel thin — you'll sharpen them in Stages 2 and 3

---

### Stage 2 — Requirements Deep-Dive

Run only after reviewing Stage 1. Replace `<your-stage1-filename>` with the actual PRD filename saved in Stage 1.

```
@<your-stage1-filename>.md
@outputs/user-research-lease-compliance-<date>.md

Using the PRD draft and user research above, now stress-test the requirements.

For each P0 requirement:
- Which specific user pain point does it address? (reference the user research directly)
- What does "done" look like — how will we know this requirement is met?
- What's the simplest version we could ship that still solves the pain?
- What are we explicitly NOT building in V1 — and why?

For success metrics:
- Are these metrics Claude or LegalGraph can actually measure?
- What's the baseline today (before the feature)?
- What's the target — and what's the timeframe?

End with: a revised P0 list — trimmed to only what must ship for the feature to be useful to Rachel (Compliance Lead).

Update the same file @<your-stage1-filename>.md — append a new "## Requirements Review" section with these findings. Do not rewrite the existing sections.
```

---

### Stage 3 — Edge Cases & Open Questions

Replace `<your-stage1-filename>` with the same PRD file from Stage 1.

```
@<your-stage1-filename>.md
@outputs/market-research-lease-compliance-<date>.md

Using the PRD and market research above, now surface the hard questions we haven't answered yet.

I need to understand:
- What happens when a lease has multiple amendments — how does extraction handle version history?
- IFRS 16 vs. ASC 842 — are we supporting both in V1 or one first? What's the implication for the addressable market?
- Who signs off on the compliance report output — legal, finance, or both? Does that change the format requirements?
- What's the audit trail requirement — do auditors need to see the source clause that generated each line item?
- Are there any competitors shipping this today that we missed in the market research? Any that just launched?

End with: a ranked list of the top 5 open questions that must be answered before we start building, and who owns answering each one.

Update the same file @<your-stage1-filename>.md — append a new "## Open Questions — Pre-Build" section. Do not rewrite the existing sections.
```

---

### Stage 4 — Final PRD

This produces the clean, final PRD ready to share with your GC and eng lead. Replace filenames with your actual filenames.

```
@<your-stage1-filename>.md
@company-context.md

Using the full PRD draft, requirements review, and open questions in the file above:

1. Write the final, clean PRD — structured exactly according to the /prd template format
2. Problem Statement must be one crisp paragraph: the pain, the persona, why now
3. Success metrics must have a baseline, a target, and a timeframe
4. Requirements must be written as testable acceptance criteria, not vague descriptions
5. Out of Scope must be explicit — list at least 3 things we are NOT building in V1
6. Open Questions must include the owner and a deadline for each question
7. End with a "Confidence Level" section — rate our confidence in each major assumption (High / Medium / Low) with a one-line rationale

Save the final PRD to: outputs/prd-lease-compliance-<today's date>.md
```

---

## Step 5 — Update CLAUDE.md with PRD Intelligence

Once Stage 4 is saved, run this prompt. Replace `<date>` with your actual filename date:

```
@outputs/prd-lease-compliance-<date>.md
@./CLAUDE.md

Read the PRD and the current CLAUDE.md above.

Extract the decisions that matter for future LegalGraph product work. Append a new "## PRD Intelligence — Lease Compliance Reporting" section to ./CLAUDE.md.

The section must include:
- The feature's core problem statement (one sentence)
- P0 requirements (bullet list — what must ship in V1)
- Primary success metric with target and timeframe
- Top 3 open questions still unresolved
- Confidence level on the biggest assumption
- PRD date: [today's date]

Rules:
- Do not modify anything already in CLAUDE.md — only append
- Keep the section under 15 bullet points total
- Write for speed — a PM or engineer reading in 30 seconds should know what we're building, for whom, and what success looks like
- If a detail doesn't change a build or prioritization decision, leave it out
```

> Run `/memory` after updating to confirm the new section loads in your next session.

---

## What Happens Behind the Scenes

![images](./images/prd.png)

**1. You run `/prd` in Stage 1 with three `@` files**
Claude Code loads `~/.claude/commands/prd.md` and replaces `$ARGUMENTS` with your feature name. But before generating anything, it reads all three `@` files you passed — company context, market research, and user research. By the time the PRD template runs, Claude has your company goals, market sizing, competitive landscape, user personas, ranked pain points, and JTBD statements all active in context. The PRD it generates is grounded in your actual research, not generic best practices.

**2. Requirements trace back to real pain points**
Because the user research file is loaded, Claude can directly connect each P0 requirement to a specific pain point from Lesson 2.4. Stage 2 formalizes this — it stress-tests every requirement against the research and asks "which pain point does this solve?" Requirements that can't answer that question get cut or moved to P2.

**3. Stage 2 and 3 append to the same PRD file**
Just like Lessons 2.3 and 2.4, each stage appends a new section to the same file:
- After Stage 1: Full PRD draft (all sections)
- After Stage 2: + Requirements Review (stress-tested, trimmed P0 list)
- After Stage 3: + Open Questions — Pre-Build (edge cases, unresolved decisions)

By Stage 4, the file is a fully annotated PRD with a clean final version, a requirements review, and a pre-build open questions log.

**4. Stage 4 produces the presentation-ready PRD**
Stage 4 reads the full accumulated file and rewrites the PRD into final form — clean structure, testable acceptance criteria, explicit out of scope, confidence levels on key assumptions. This is the version you share with your GC and eng lead, not the draft from Stage 1.

**5. CLAUDE.md gets the PRD decisions, not the full document**
Step 5 extracts only what shapes future decisions — the problem statement, P0 requirements, primary metric, top open questions — and appends it to CLAUDE.md. When you open a new session to work on this feature next week, Claude already knows what you decided to build, for whom, and what success looks like.

```
/prd + @company-context + @market-research + @user-research → PRD draft saved
    ↓
Stage 2: @PRD file → requirements stress-test + append → file grows
    ↓
Stage 3: @PRD file + @market-research → edge cases + append → file grows
    ↓
Stage 4: @full PRD file → final clean PRD saved to outputs/
    ↓
Step 5: @final PRD + @CLAUDE.md → append decisions → loads every session
```

---

## Things to Keep in Mind

**On grounding requirements in research:**
- Every P0 requirement should trace back to a specific pain point from your Lesson 2.4 user research. If it doesn't — ask yourself why it's P0.
- Push Claude if a requirement is vague: "Rewrite this requirement as a testable acceptance criterion."

**On success metrics:**
- "Improve user satisfaction" is not a metric. "Rachel completes her quarterly IFRS 16 compliance report in under 2 hours (vs. current 6-hour manual process), measured by in-app time tracking, within 60 days of launch" is a metric.

**On out of scope:**
- Being explicit about what you're NOT building is as important as what you are. It prevents scope creep and sets eng expectations correctly.

**On open questions:**
- A PRD with zero open questions is either perfect or dishonest. Aim for 3–5 real unresolved decisions — with an owner and a deadline for each.

---

## What You've Learned

- **A PRD built on chained research is grounded by default** — because Stages 2.3 and 2.4 outputs load as context, every requirement in this PRD traces back to a market signal or a user pain point. You're not writing requirements from intuition.
- **The four-stage PRD structure** — Stage 1: baseline draft from the `/prd` command. Stage 2: stress-test requirements against user research (what do real users need vs. what did we assume?). Stage 3: edge cases and open questions before build. Stage 4: final clean PRD ready for stakeholder review.
- **Requirements stress-testing is its own stage** — comparing the draft PRD against user research at Stage 2 surfaces requirements that look right but don't match what users actually do. Catching that before build is the point.
- **Open questions belong in the PRD** — surfacing unresolved decisions before scoping begins gives engineers and stakeholders a chance to resolve them, not discover them mid-sprint.
- **CLAUDE.md now carries the full research-to-PRD chain** — market intelligence, user insights, and PRD decisions all load in every session. From this point forward, Claude has the context to help you make decisions on this feature without re-briefing.

---

*Next: [Lesson 2.6 — Connectors in Claude Cowork](./Lesson2.6-Connectors-in-Claude-Cowork.md)*
