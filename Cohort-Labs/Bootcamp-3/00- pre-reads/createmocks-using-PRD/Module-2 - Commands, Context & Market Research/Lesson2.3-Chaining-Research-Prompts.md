# Lesson 2.3 — Chaining Research Prompts: Deep Market Research on the Lease Compliance Feature

---

## Where You Are

In Lesson 2.2 you built three custom slash commands:
- `/market-research` — structured market research with your exact format baked in
- `/user-research` — structured user research output
- `/prd` — Product Requirements Document

The format, structure, and quality standards are already inside those command files. You don't need a separate `sampleprompts/` or `templates/` folder — the command IS the template.

Now you use `/market-research` as your baseline, then chain deeper focused prompts on top of it — on a real feature request from your GC.

---

## What Is Prompt Chaining?

Prompt chaining is running a series of connected prompts where each one builds on the output of the last.

Instead of one big prompt like "research the lease compliance market" (which produces shallow, generic output), you break the research into focused stages:

```
Stage 1: Run /market-research → baseline report saved to file
    ↓ (output becomes context for)
Stage 2: Competitive landscape deep-dive
    ↓ (output becomes context for)
Stage 3: Customer segments and pain points
    ↓ (all of the above becomes input for)
Stage 4: Full synthesis → final decision-ready report saved to outputs/
```

Each stage is narrow. Claude goes deep on one question at a time. The final output is richer than anything a single prompt produces.

---

## Why This Matters for Complex Features

The Lease Compliance Reporting feature touches multiple markets:
- Legal AI and CLM software
- Financial accounting software (IFRS 16 / ASC 842 compliance)
- Audit and compliance tooling

One prompt won't cover this adequately. Chaining will.

---

## The Feature Brief

Your GC wants to add a feature that:
- Extracts lease terms and history automatically from contracts
- Generates compliance reports (IFRS 16 accounting standards, audit reports)
- Provides formatted outputs for accountants and auditors

The research question: **Is this a strong market opportunity for LegalGraph — and if so, how should we position it?**

---

## Pre-Flight Checklist

> Run through this before starting any research session. Skipping this is the most common reason research outputs are mediocre.

- [ ] Verify `/market-research` command exists: `ls ~/.claude/commands/` — you should see `market-research.md`. If not, go back to Lesson 2.2 Step 3
- [ ] Verify `outputs/` folder exists in your working directory (create if not: `mkdir outputs`)
- [ ] Your project folder is added to the Claude Code chat
- [ ] CLAUDE.md is loaded — your LegalGraph context (personas, product details) is active

---

## The Research Session

### Stage 1 — Run Your Baseline with `/market-research`

Start here. This gives you the structured baseline report using the template you built in Lesson 2.2.

> **Company context:** The prompt below uses `@` to load your company context file directly into the prompt. Claude reads it automatically — no copy-pasting needed. We're using LegalGraph as the bootcamp example. If you're using your own company, swap the filename for your own context file.

**Using LegalGraph context (bootcamp default):**
```
@company-context.md

/market-research AI-powered lease compliance and contract review platforms
```


![images](./images/lesson2.31.png)

**Using your own company context:**
```
@<your-company-context-file>.md

/market-research <your research topic>
```

> The `@` loads your company file into the session before the command runs — Claude uses it to make the Implications and Open Questions sections specific to your product and market position, not generic.

This runs your full market research template — Market Size, Key Trends, Competitive Dynamics, Implications, What We Still Don't Know, and Open Questions — and saves the output to your working directory.

**After Stage 1:**
- Read the output file — check that numbers have sources and sections are specific, not generic
- Note shallow areas — you'll go deeper on those in Stages 2 and 3
- The saved `.md` file is your baseline. You'll `@` reference it in Stage 4
  
![images](./images/mr-1.png)
---

### Stage 2 — Competitive Landscape Deep-Dive

Run only after reviewing the Stage 1 output. Replace `<your-stage1-filename>` with the actual filename saved in Stage 1.

![images](./images/mr23.png)

```
@<your-stage1-filename>.md

Using the market research above, now research the competitive landscape for AI-powered contract review tools that include or are building toward lease compliance and IFRS reporting features.

Analyze these competitors:
- Ironclad
- Kira Systems
- LawGeex
- Evisort
- LinkSquares
- Robin AI
- ThoughtRiver

For each:
- Core product focus (what are they primarily known for?)
- Do they have lease extraction or IFRS compliance features? If yes — how mature?
- Pricing model (if publicly available)
- Target customer: SMB, mid-market, or enterprise?
- One clear strength
- One clear weakness

End with three things:
1. Where LegalGraph has a clear opening in this space
2. Where LegalGraph is most vulnerable right now
3. The one competitor we should watch most closely — and why

Update the same file @<your-stage1-filename>.md — append a new "## Competitive Landscape" section with these findings. Do not rewrite the existing sections.
```

> **If the session is getting long after Stage 2:** Use `/compact` before Stage 3. Claude preserves a summary and you continue with a fresh context budget. Do not use `/clear` — you'll lose the research chain.

![images](./images/mr4.png)

---

### Stage 3 — Customer Segments & Pain Points

Replace `<your-stage1-filename>` with the same file from Stage 1.

![images](./images/op.png)

```
@<your-stage1-filename>.md

Using the market research and competitive analysis in the file above, research the specific customer pain points around lease compliance and IFRS 16 / ASC 842 reporting in legal and finance teams.

I need to understand:
- Who in the org actually owns lease compliance? (Legal? Finance? Both? Does it depend on company size?)
- What does the current workflow look like without AI tooling — step by step, not just "it's manual"
- Which specific steps are most painful and why
- What compliance requirements are creating urgency right now (IFRS 16, ASC 842, audit trail requirements, SOX)
- What do accountants and auditors specifically need that in-house legal teams typically don't provide well
- Any survey data, analyst reports, or first-hand accounts of this workflow (Reddit, LinkedIn, industry forums)

End with: which of LegalGraph's three personas — Jennifer (GC), David (Senior Associate), or Rachel (Compliance Lead) — is the primary buyer for this feature, and why? Who is the user vs. the buyer?

Update the same file @<your-stage1-filename>.md — append a new "## Customer Segments & Pain Points" section with these findings. Do not rewrite the existing sections.
```
![images](./images/90.png)
---

### Stage 4 — Full Synthesis

This ties everything together. It uses your CLAUDE.md context, the Stage 1 baseline file, and all the research from Stages 2 and 3 to produce a structured, decision-ready report.

Replace `<your-stage1-filename>` with the actual filename saved in Stage 1.

```
Do market research for the Lease Compliance Reporting feature.

Our GC wants to add a feature that:
- Extracts lease terms and history automatically
- Generates compliance reports (IFRS 16 accounting standards, audit reports)
- Provides formatted outputs for accountants and auditors

Research steps:
1. Read @<your-stage1-filename>.md — this is the baseline market research from our session. Use it as primary input, not a starting point to redo
2. Use the competitive analysis and customer pain points from our conversation above as additional input
3. Supplement with web search only where data is still missing:
   - Legal AI and CLM market size and growth (2025–2030)
   - IFRS 16 / ASC 842 compliance tooling market updates
   - AI/ML capability trends in legal tech (accuracy benchmarks, LLM adoption)
4. Structure the full output using the same format as the Stage 1 baseline — every section, in order, with Key Implications
5. Include specific data points and citations — flag estimated vs. verified
6. Tie strategic recommendations to LegalGraph's north star metrics: activation rate and AI extraction accuracy
7. Identify the primary buyer persona for this feature with evidence
8. End with Open Questions — what we still don't know, with a suggested method to answer each

Save the completed report to: <mentioned your workspace and file name>
```

---

## What Happens Behind the Scenes

![images](./images/mrs.png)

Understanding what Claude is actually doing at each stage helps you debug when output is shallow and push when it's not good enough.

**1. You run `/market-research` in Stage 1**
Claude Code intercepts `/market-research`, loads `~/.claude/commands/market-research.md`, replaces `$ARGUMENTS` with your topic, and runs the full structured prompt. The `@company-context.md` file is read first — so your company, personas, and metrics are active context before the research starts.

**2. The output saves to a `.md` file**
Claude writes the structured report directly to your working directory. That file is now a permanent artifact — not just a chat message that disappears. Every future stage `@` references it.

**3. `@filename` in Stages 2, 3, and 4**
When you prefix a prompt with `@<filename>.md`, Claude reads the full file contents before processing your instructions. It's not relying on conversation memory — it's reading the actual saved research. This is why chaining works across long sessions: the file is the chain, not the chat history.

**4. "Append, don't rewrite" instruction**
Each stage tells Claude to append a new section to the same file rather than create a new one. By the end of Stage 3, your single research file has grown from the baseline into a document with Market Size, Key Trends, Competitive Landscape, and Customer Pain Points — all in one place for Stage 4 to synthesize.

**5. Stage 4 reads the full accumulated file**
Stage 4 `@` references the same file that now contains everything from Stages 1–3. Claude reads the full document, synthesizes across all sections, and produces the final report. This is why Stage 4 output is significantly richer than anything a single prompt produces.

**6. CLAUDE.md append in Step 5**
When you run Step 5, Claude reads both the research file and your existing CLAUDE.md. It extracts only what's decision-relevant and appends it as a new section — without touching what's already there. From the next session onward, that market intelligence loads automatically before you type a single word.

```
/market-research → saves file
    ↓
Stage 2: @file → research + append → same file grows
    ↓
Stage 3: @file → research + append → same file grows
    ↓
Stage 4: @file (full) → synthesize → final report saved
    ↓
Step 5: @final report + @CLAUDE.md → append intelligence → loads every session
```

---

## Debugging Workflow

![images](./images/mre.png)



---

## Things to Keep in Mind

**On data quality:**
- IFRS 16 is the international lease accounting standard (mandatory for public companies globally). ASC 842 is the US equivalent (FASB). Your GC will know the difference — make sure the research does too.
- If Claude cites a market size number that feels off, ask: "What's the source for that figure? Is it from an analyst report or derived?" Better to flag uncertainty than present it as fact.

**On context management:**
- Stage 4 is token-heavy. If Claude seems to lose earlier context, paste key findings in manually: "Here's the competitive analysis from Stage 2: [paste]. Now run Stage 4."
- Always use `/compact`, not `/clear`, during a chained research session. `/clear` wipes the chain.

**On saving intermediate work:**
- After Stage 2, save a snapshot: `Save the competitive analysis table from this session to outputs/competitive-landscape-draft.md`
- This gives you a recoverable snapshot if Stage 3 or 4 goes sideways.

---

## Step 5 — Update CLAUDE.md with Market Intelligence

Once Stage 4 is saved, run this prompt to update your project CLAUDE.md. Replace `<your-stage1-filename>` with the actual filename:

```
@<your-stage1-filename>.md
@./CLAUDE.md

Read the market research report and the current CLAUDE.md above.

Extract the findings that matter for ongoing LegalGraph roadmap and strategy work. Append a new "## Market Intelligence" section to ./CLAUDE.md.

The section must include:
- Top 3 market findings relevant to product decisions (with numbers where available)
- Key competitors most relevant to our current positioning
- Primary persona for this feature (buyer vs. user — be explicit)
- One market risk to keep visible in roadmap discussions
- One strategic opening LegalGraph should act on
- Research date: [today's date]

Rules:
- Do not modify anything already in CLAUDE.md — only append
- Keep the section under 15 bullet points total
- Write for speed — someone reading in 30 seconds should understand the market situation
- If a finding doesn't change a product decision, leave it out
```

> Run `/memory` after updating to confirm the new section loads in your next session.

---

## What You've Learned

- **What prompt chaining is** — breaking a complex research task into sequential stages where each output becomes input for the next. Each stage deepens the analysis rather than repeating it.
- **Why chaining beats a single prompt** — a single prompt produces surface-level output. Chaining forces Claude to deepen at each stage: baseline → competitors → customer segments → full synthesis. The final output is 4x richer than anything a single prompt produces.
- **The four-stage market research structure** — Stage 1: baseline market size and trends. Stage 2: competitive landscape deep-dive. Stage 3: customer segments and pain points. Stage 4: full synthesis with strategic implications.
- **When to use `/compact`** — after a long research stage when the context window is filling up. Compressing history keeps Claude focused on the task without losing the thread.
- **Why CLAUDE.md gets updated at the end** — market intelligence is only useful if it loads in every future session. Updating CLAUDE.md after research means every future prompt on this feature starts with that intelligence already loaded.

---

*Next: [Lesson 2.4 — User Research: Chaining Prompts](./Lesson2.4-User-Research-Chaining.md)*
