---
name: job-strategy-doc-builder
description: >
  Builds a personalized Job Strategy Document from a user's resume,
  background, and career goals. Use for AI career planning, resume
  optimization, job search strategy, career transitions, and interview
  preparation.
---

# Job Strategy Doc Builder

Turns a scattered "I want an AI job" goal into a structured strategy document, modeled on a
diagnosis → guiding policy → objectives → action plan → roadmap → risk framework (the same
shape strategy consultants use for corporate strategy, applied to one person's career). The
point isn't to produce generic career advice — it's to force specific, personal answers out of
the user via targeted questions, then organize those answers into something they'll actually
reread and act on.

Two deliverables come out of every run:
1. A Markdown strategy doc (their reference copy, easy to edit later)
2. A self-contained HTML artifact (a visual version — sections as cards, a milestone timeline,
   a KPI tracker) they can open in a browser and glance at without wading through prose

After the doc is built, offer interview-prep follow-ups — see "Follow-up menu" below.

## Step 1 — Get the resume (and check for an existing strategy doc)

Before asking anything else, check whether the user already attached a resume/CV in this
conversation or uploaded one previously. If yes, read it — it's your best source for the
Diagnosis section (experience, domain, project history) and you should pull from it rather
than re-asking things it already answers.

If no resume is present, ask for one before proceeding — the strategy doc is much weaker
without it. Use AskUserQuestion:

- Question: "I'll build your strategy doc around your background. Do you have a resume handy?"
- Options: "I'll upload it now" / "Use my LinkedIn profile instead (I'll paste the URL/text)" /
  "I don't have one ready — build from what I tell you"

If they choose the third option, proceed, but lean harder on the interview questions in Step 2
to fill the gaps a resume would normally cover.

Also check if a strategy doc from this skill already exists earlier in the conversation
(look for a prior `*-job-strategy.md` file or a completed workshop). If one exists and the
user's current request is really about interview prep (not building a new strategy), skip
straight to "Follow-up menu" below and use that existing doc + resume as context.

## Step 2 — Run the workshop (AskUserQuestion, in batches)

This is the core of the skill: don't silently invent the user's answers. The whole value of
this exercise is forcing them to commit to specifics they'd otherwise leave vague. Use
`AskUserQuestion` in three batches (max 4 questions per call). Give each question 3-4 concrete
preset options plus room for "Other" — presets make it fast to answer, "Other" keeps it honest
when none of the presets fit.

**Batch A — Diagnosis** (current state, challenges, opportunities):
1. Experience level / current domain (options spanning junior/adjacent → senior/leadership,
   grounded in what the resume shows if you have one)
2. Employment status right now (employed full-time / between roles / student or new grad /
   freelance)
3. Biggest challenge to landing this role (location constraints / employment gap or irrelevant
   experience / skills-domain gap / limited time)
4. Biggest edge or unique asset (deep domain expertise / engineering-technical background /
   strong network / a specific project or body of work)

**Batch B — Guiding Policy & Objectives:**
1. Overall approach they want to take (domain-expertise-first / portfolio-and-build-in-public /
   certifications-and-network / direct outreach and referrals)
2. Non-negotiables — multiSelect (compensation must increase / location is fixed / must be
   people-management track / must be fully remote)
3. Where they want to be in ~3 years (senior/staff AI PM at a large company / founder running
   their own AI venture / director/head-of-AI track / deep technical specialist)
4. Timeframe they're working with (under 3 months / 3-6 months / 6-12 months / 12+ months,
   still exploring)

**Batch C — Action Plan, Roadmap, Risk:**
1. Initiatives already underway or planned — multiSelect (certification/course / a side project
   or startup / applying at scale / building a LinkedIn/content presence)
2. Resources they can put behind this (mostly their own time / savings or budget to invest /
   collaborators or a small team / a mentor or community)
3. Biggest risk to the plan (runway/savings running out / burnout or losing motivation / market
   conditions worsening / skills gap not closing fast enough)
4. Realistic weekly time commitment (under 5 hrs / 5-15 hrs / 15-30 hrs / 30+ hrs, treating it
   like a second job)

Ask batch A first, then B, then C — don't front-load all twelve questions at once. Read each
answer before framing the next batch's options (e.g. if they said "between roles," don't offer
"employed full-time" as a challenge option later).

## Step 3 — Ground the Market Analysis in reality, not vibes

The template's "Market and Competitive Analysis" section asks the user to research trends and
competitor profiles manually. Don't leave that entirely on them — run a couple of WebSearch
queries on current AI hiring trends for their target role/domain (e.g. "AI product manager
hiring trends 2026", "[their domain] AI roles market demand") and fold real, dated findings
into that section alongside whatever anecdotal insight they gave you. Cite what you find.

## Step 4 — Write the Markdown strategy doc

Use the **"Markdown output template"** section near the bottom of this file as the structure —
sequential numbering 1-7 (the source template the user supplied had a numbering typo skipping
"3"; don't replicate that), and every heading and sub-heading from that template must appear in
the output, in that order. Copy its section layout and replace every `[bracketed]` placeholder
with this user's real content — don't leave a sub-bullet in as a stub if it doesn't apply,
delete it instead.

This needs to be a genuinely **detailed** document, not a condensed summary — the point of the
original template is that each section gets real thinking, the way the example template did
("Ai is must irrespective of time it takes | Money need to doubled | Location need to be CA" is
specific and opinionated, not a placeholder-length one-liner). Write multiple sentences or
several bullets per sub-section wherever the workshop answers support it — don't compress a
rich answer into a single clipped line just to keep things short. Write in the user's voice
where you can (pull phrasing from their actual answers rather than generic corporate language).
Every section should reflect a real answer they gave, not a filler placeholder. Save as
`[name]-job-strategy.md` in the outputs folder.

## Step 5 — Build the HTML artifact

Design this one at runtime rather than filling in a fixed template — see **"HTML artifact —
design it at runtime"** near the bottom of this file for the structural requirements and
non-negotiables (self-contained single file, every number traceable to something the user
actually said, etc.). The right layout depends on how much content this particular user has —
someone with 8 KPIs and someone with 2 shouldn't get the same rigid grid.

Before doing anything else, deliver both files — call `present_files` with the `.md` and the
`.html` together so the user has real, downloadable files in hand. This has to actually happen
(not just be described) before you move on to Step 6; "the doc is done" means they can open it,
not that you've described what it would contain.

## Step 6 — Offer the follow-up menu (plain chat, not AskUserQuestion)

Once both files are delivered, offer the interview-prep follow-ups as a normal chat message —
plain text, not the `AskUserQuestion` tool. This one's conversational by design: the user
should be able to just reply "do #1 and #3" or "let's do the salary one" in their own words
rather than clicking a multiple-choice widget. Something like:

> Your strategy doc and visual artifact are ready above. Want to keep going with any of these?
> 1. Five stories for your first-round interview (I'll need the job description)
> 2. Project discussion key points
> 3. STAR story bank
> 4. Mock interview Q&A prep
> 5. Salary negotiation script
> 6. Company & interviewer research brief

Full instructions for each — what to ask for, what to research, and the output format — are in
the **"Follow-up menu — full details"** section below. Read that section once the user picks
one (or more) rather than improvising the flow from scratch, since each has a specific required
input (e.g. #1 cannot proceed without a job description — don't skip that dependency). Within
each follow-up flow, AskUserQuestion is still fine for the flow's own inputs (e.g. #2's "which
project" question) — it's specifically the top-level "what do you want next" offer that should
stay conversational.

Users may come back to this skill later just for a follow-up (no new strategy doc needed) — in
that case skip Steps 1-5 and jump straight to the relevant flow below, using whatever
resume/strategy-doc context already exists in the conversation.

---

## Follow-up menu — full details

Read only the sub-section for what the user picked. Each one lists required inputs, what to
ask if those inputs are missing, and the expected output. All outputs should be saved as
Markdown files in the outputs folder (`[name]-<followup>.md`) — no need for an HTML artifact
for these, the strategy doc is the one deliverable that gets the visual treatment.

### 1. Five Stories for First-Round Interview

**Hard dependency: a job description.** This flow cannot produce good output without one —
don't generate generic stories and call it done. If the user hasn't already shared a JD in the
conversation, stop and ask for it (paste the text, a link, or the job title + company so you
can search for it) before doing anything else.

Once you have the JD:
1. Extract the 4-6 things it's clearly screening for (a mix of hard requirements and softer
   signals — e.g. "cross-functional influence," "ambiguity," "technical depth," "shipped 0→1").
2. Cross-reference against the resume to find the strongest real story for each. If two
   requirements point to the same story, that's fine — better a true, strong story reused than
   a thin invented one.
3. Write 5 stories in STAR format (Situation, Task, Action, Result), each explicitly tagged
   with which requirement from the JD it's aimed at, 150-250 words each. Close each with a
   one-line "why this matters for this role" note.

Output: `[name]-interview-stories.md`, with the JD requirements listed at the top so the
mapping is visible.

### 2. Project Discussion Key Points

**Uses the resume as the primary reference.** Before building this, ask (AskUserQuestion, one
batch):
1. Which project(s) to focus on — offer the 2-3 most substantial ones you see on the resume as
   options, plus "let me specify" via Other
2. What angle the interviewer is likely to probe — options: technical deep-dive (architecture,
   trade-offs, how it actually works) / business impact (metrics, stakeholders, why it
   mattered) / leadership & process (how decisions got made, conflict, what they'd do
   differently) / not sure, cover all three

For each selected project, produce talking points covering: context (problem, constraints),
your specific role and decisions, technical/product trade-offs you made and why, quantified
outcome, and one honest "what I'd do differently" reflection — interviewers notice when
candidates only tell the polished version.

Output: `[name]-project-discussion-points.md`.

### 3. STAR Story Bank

Broader and less JD-specific than #1 — a reusable bank rather than a targeted set. Pull from
the full resume and build one story per competency, for the competencies that actually show up
in the person's background (don't force a "conflict" story if nothing on the resume supports
one — flag the gap instead so they know to prep it separately). Typical set: leadership,
handling failure/setback, ambiguity, influence without authority, data-driven decision-making,
cross-functional conflict.

Each story: STAR format, 150-200 words, plus a one-line note on which competency it covers and
which other competencies it could stretch to cover if asked a follow-up.

Output: `[name]-star-story-bank.md`.

### 4. Mock Interview Q&A Prep

Ask (if not already known from context): the role/JD (if available) and interview stage
(recruiter screen / hiring manager / panel / technical). Then generate 8-12 likely questions
spanning product sense, technical depth, behavioral, and "why this role/company," each with a
short answer framework (not a scripted answer — a structure: what to lead with, what to
include, what to avoid). If a JD is available, weight questions toward what it emphasizes.

Output: `[name]-mock-qa-prep.md`.

### 5. Salary Negotiation Script

Ask (AskUserQuestion): target role/level and location, current compensation (optional — they
may not want to share; give a "prefer not to say, just use market range" option), and target
compensation or range if they have one in mind. If you don't have a market range from search
already, run a quick WebSearch for current comp benchmarks for that role/level/location and
cite what you find rather than guessing a number.

Produce: a short set of talking points for the comp conversation, a written script for
responding to "what are your salary expectations," and a script for countering a lowball
offer — grounded in the market data, not generic negotiation platitudes.

Output: `[name]-salary-negotiation.md`.

### 6. Company & Interviewer Research Brief

Ask for the company name and, if available, the interviewer's name/LinkedIn or role. Use
WebSearch to gather: what the company/team actually does, recent news (funding, product
launches, layoffs — anything materially relevant), and if an interviewer name was given, their
public background (prior companies, apparent focus area) to the extent it's findable. Don't
fabricate details you can't find — say what's unknown rather than guessing.

Produce a short brief (company/team snapshot, 2-3 recent developments worth knowing, likely
interviewer focus/lens if determinable) plus 3-4 smart questions the user could ask that show
they did the homework and aren't generic ("what's the culture like").

Output: `[name]-company-research-brief.md`.

---

## Markdown output template

Copy this structure, replace every `[bracketed]` placeholder with the real user's answers, and
delete any sub-bullet that doesn't apply rather than leaving it as a stub.

```markdown
# Job Strategy Document — [Name]
*Generated [date] · Target: [role/domain] · Timeframe: [e.g. 6-12 months]*

## 1. Diagnosis

### Current Situation Analysis
[1-2 lines stating where they stand today — domain, experience level, current role.]
[2-3 sentences drawing on resume/LinkedIn: relevant experience, domain depth, adjacent skills.]

### Challenges and Opportunities
**Challenges**
- [Location constraint, if any]
- [Employment status — gap, irrelevant experience, etc.]
- [Skills/domain gap]

**Opportunities**
- [Domain expertise or adjacent experience]
- [Unique background — engineering bent, curiosity, prior wins]
- [Network, portfolio, or other asset]

### Market and Competitive Analysis
[2-4 sentences of *real, dated* findings from search on hiring trends/demand for their target
role — cite what you found, don't speculate.]
[Any competitive-landscape insight the user gave you — cohort peers, recent LinkedIn "I got
the role" posts, etc.]

## 2. Guiding Policy

### Overall Approach
[1-3 sentences: the strategy they're committing to and why, given the diagnosis above.]

### Core Principles and Values
- [Non-negotiable 1]
- [Non-negotiable 2]
- [Non-negotiable 3]

## 3. Strategic Objectives

### Long-term Goals
[Where they want to be in ~3 years — one clear statement.]

### Short-term Objectives (SMART)
- [Specific, measurable, time-bound objective 1]
- [Specific, measurable, time-bound objective 2]
- [Specific, measurable, time-bound objective 3]

## 4. Action Plan

### Key Initiatives
- [Initiative 1]
- [Initiative 2]
- [Initiative 3]

### Resource Allocation
[What they're putting behind this — time budget, money, people — in their own terms.]

### Roles and Responsibilities
[Who's involved besides them, if anyone — mentors, collaborators, dev help, etc. Fine to state
"solo effort" if that's the reality.]

## 5. Implementation Roadmap

### Timeline
| Milestone | Target Date |
|---|---|
| [Milestone 1] | [date] |
| [Milestone 2] | [date] |
| [Milestone 3] | [date] |

### Key Performance Indicators
- [KPI: e.g. applications submitted] — target [n]
- [KPI: e.g. mock interviews completed] — target [n]
- [KPI: e.g. interview calls] — target [n]
- [KPI: e.g. LinkedIn posts / GitHub contributions] — target [n]

## 6. Risk Management

### Potential Risks
- [Risk 1]
- [Risk 2]

### Mitigation Plans
- [Mitigation for risk 1]
- [Mitigation for risk 2]

## 7. Appendices
[Any supporting detail worth keeping for reference — links, extra research, source notes for
the market analysis above.]
```

## HTML artifact — design it at runtime

Don't copy a fixed template here — design the HTML fresh each time, because a rigid template
either overflows (someone with 6 initiatives and 8 KPIs) or looks sparse (someone with a lean
2-milestone plan). You have the design judgment to do this well; use it. If the visualize
tool is available in this session, call `mcp__visualize__read_me` (module: `data_viz` or
`mockup`) first and follow its color/typography/layout guidance rather than inventing your own
palette from scratch — that keeps the output visually consistent with other artifacts in this
product.

What the artifact needs to contain, structurally:
- A header identifying whose strategy this is, the target role, and the timeframe
- All 7 sections from the Markdown doc, represented visually rather than as dense paragraphs —
  short summaries, pills/tags for challenges vs. opportunities, that kind of thing, not the
  full prose
- The roadmap milestones as a visual timeline (however many the user actually has)
- KPIs as a scannable list or table, sized to however many the user actually named
- Risks paired directly with their mitigations, not in two separate disconnected lists

Non-negotiables regardless of the specific design you choose:
- Single self-contained HTML file — inline CSS and JS only, no external fonts/scripts/
  stylesheets, so it opens standalone in any browser with no internet connection
- Every value in the artifact must trace back to something the user actually said in the
  workshop or the resume — no invented stats or filler numbers to make the header stat row
  look fuller
- Clean and readable over flashy — this is something they'll reopen to check progress, not a
  one-time impression piece

Save as `[name]-job-strategy.html` in the outputs folder. If `mcp__visualize__show_widget` is
available, also render it inline (after calling `read_me`) so the user sees it immediately in
the conversation, in addition to the saved file.