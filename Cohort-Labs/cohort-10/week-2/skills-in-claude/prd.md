---
name: prd
description: Use this skill whenever a user asks to write a PRD, create a PRD, draft a PRD, spec out a feature, or create a one-pager. Triggers include: "write a PRD", "create a PRD", "draft a PRD", "PRD for [feature]", "spec out [feature]", "one pager for [feature]", or any request to document a product requirement.
version: 1.0.0
argument-hint: <feature or product description>
---

# PRD Writer

## Trigger
Activate on "write a PRD", "create a PRD", "draft a PRD", "PRD for [feature]", "spec out [feature]", or "one pager for [feature]".

## Context

The PRD isn't dead. The bad PRD is dead. AI killed the 10-page PRD — no one read those. The modern PRD is lighter, sharper, and example-heavy.

Core philosophy:
- **Think crisp, not complete.** Teammates hate AI-generated bloat and crave human-written clarity. 2-3 pages max.
- **PRDs are for alignment, not dictation.** They drive discussion and decisions. They're what you discuss, debate, refer to, and sync on.
- **A PRD engineers actually want to read nails the "why" and the "what," not the "how."**
- **You don't write a PRD once. You write it over time.** The PRD is a living document reflecting the team's current thinking at each stage.

## Behavior

### Step 1: Clarify Before Writing

Before generating anything, ask 3-5 clarifying questions. Tailor to what's missing. Common gaps:

- Who specifically has this problem? (Not "users" — which users? Job title, company size, situation)
- What data do we have that this is worth solving? (Usage data, support tickets, revenue impact, customer quotes)
- What's the scope? (MVP vs full vision — and what stage is this PRD at?)
- Are there technical constraints the engineering team has flagged?
- What's the timeline and why?

Do NOT proceed until the user answers. A PRD without clear answers to these is vague and useless.

If the user is early-stage or exploring, generate a "speclet" (Stage 1) — just enough for the team to explore further. Never force a full PRD on an idea that needs discovery first.

### Step 2: Determine the PRD Stage

The PRD evolves through stages. Ask or infer which stage the user is at:

| Stage | What It Is | What the PRD Looks Like |
|-------|-----------|------------------------|
| **1. Team Kickoff** | Exploring the problem with design + eng | A "speclet" — title, problem hypothesis, 2-3 open questions. Maybe just a paragraph. |
| **2. Planning Review** | Presenting to leadership for prioritization | A 1-pager: problem, strategic fit, initial data, potential approach. Audience: VP, CEO. |
| **3. XFN Kickoff** | Bringing in sales, support, marketing, legal, QA | Expanded doc with cross-functional input needed. Compelling problem + initial solution direction. |
| **4. Solution Review** | Staking a position on the solution | Full PRD with solution details, flows, edge cases. May be presented to senior leadership. |
| **5. Launch Readiness** | Engineering handoff | Concrete specs: edge cases, metrics, user flows. Engineers comment heavily on this version. |
| **6. Impact Review** | Post-launch learning | Add results link at top. What worked, what didn't, rollback notes. Closes the build-test-learn loop. |

Default to Stage 4 (Solution Review) unless the user specifies otherwise. This is the most common PRD request.

### Step 3: Generate the PRD

Every section earns its place. If a section doesn't drive a decision or prevent a mistake, cut it.

**Title:** [Feature Name]
**Author:** [User's name if known]
**Date:** [Today's date]
**Status:** Draft — [Stage name]

---

**1. Hypothesis**
One sentence. Testable. Prevents wasted development cycles.
Format: "We believe [action] will [outcome] for [users], measured by [metric]."

Example: "We believe one-click checkout for returning users will increase conversion rates by 15% by reducing friction in the buying process."

**2. Problem**
- Who has this problem (specific user segment, not "everyone")
- How bad is it (frequency, severity, with data)
- How are they solving it today (workarounds = strong signal)
- What happens if we don't solve it
- Customer evidence: quotes, support tickets, research findings. A PRD without customer evidence is a PRD built on assumptions.

**3. Strategic Fit**
- Why this problem, why now
- How it connects to current OKRs
- Why this approach vs alternatives we considered (explain controversial decisions explicitly — this is where alignment happens)
- Competitive context if relevant (name competitors, don't just say "the market")

**4. Solution**
- Specific description of what we're building (not vague)
- User flow (step by step)
- Key interactions and states
- Include wireframe descriptions or ASCII mockups where helpful
- For AI features: 15-25 example input/output pairs showing expected behavior, edge-case inputs, rejection criteria, and how the system handles unexpected or malformed inputs

**5. Non-Goals**
State these early. Best defense against scope creep.
- What we're explicitly NOT doing in this version (be specific: "We are NOT building Outlook sync in V1")
- Features we considered and cut, with one-line reasoning for each
- Intentional trade-offs the team should understand

**6. Success Metrics**
- Primary metric with target number and timeframe
- Secondary metrics (2-3)
- Guardrail metrics (what should NOT get worse — with current baselines and acceptable ranges)
- For experiments: passing criteria to graduate the A/B test

**7. Rollout Plan**
- A/B test or full rollout? Gradual or big bang?
- If gradual: rollout percentage stages (1% → 10% → 50% → 100%) with go/no-go criteria at each stage
- Rollback plan: how to undo this if it goes wrong

**8. Open Questions**
- Flag unresolved items with `[NEED: data from X]` placeholders
- Include owner and deadline for each question
- Don't hide unknowns — surface them

---

### Step 4: Stage-Appropriate Checklist

After generating, verify the PRD against the checklist for its stage. Flag gaps to the user.

**Planning Stage Checklist:**
- [ ] Problem clearly defined with user segment?
- [ ] Current state documented (how problem goes unaddressed today)?
- [ ] Business metrics that will move identified?
- [ ] Qualitative evidence included (not just assumptions)?
- [ ] Knowledge gaps identified with owners and timelines?
- [ ] Competitive landscape surveyed?

**Solution Review Checklist:**
- [ ] Edge cases identified?
- [ ] Rollout plan determined (experiment vs. gradual)?
- [ ] Cross-functional requirements specified (legal, marketing, support)?
- [ ] Tracking and analytics events defined?
- [ ] Risks and mitigations documented?

**Launch Readiness Checklist:**
- [ ] Engineering concerns addressed?
- [ ] Design complete?
- [ ] Tasks estimated and created?
- [ ] GTM enablement complete (sales, support, docs)?
- [ ] Hypothesis and impact sizing documented?
- [ ] All edge cases resolved?
- [ ] QA test plan prepared?

### Step 5: Review

After generating, offer:
- "Want me to review this as an engineer, designer, or skeptic?"
- "Want me to tighten this into a 1-pager for executive review?"
- "Want me to add an AI behavior spec with input/output examples?"

---

## Good vs. Bad PRD Sections

### Bad Hypothesis (vague, untestable)
```
We believe improving the onboarding experience will lead to better user engagement.
```
No specific action, no target user, no metric, no number. "Better" and "improving" mean nothing.

### Good Hypothesis (specific, testable)
```
We believe that replacing the 7-step onboarding wizard with a single-screen
setup for mid-market teams (50-200 employees) will increase 7-day activation
from 23% to 35%, because 67% of users currently abandon at step 4 (the
integrations screen) according to our June cohort analysis.
```

### Bad Problem Section (no evidence)
```
Users find the current experience confusing and would benefit from improvements.
Many users have expressed interest in a better solution.
```
No specifics, no data, no customer quotes, no evidence of workarounds. This could describe any feature at any company.

### Good Problem Section (evidence-rich)
```
Who: Mid-market project teams (50-200 people) using our tool for task management.

How bad: In our latest user survey (n=340), 67% of respondents said they use a
separate calendar tool to track project deadlines. Support tickets related to
"missed deadlines" increased 23% QoQ. Exit interviews cite "no calendar view"
as the #3 reason for churn.

Current workarounds: Users export tasks to CSV, manually add deadlines to Google
Calendar, or use Zapier integrations that break frequently. The fact that they
build workarounds proves the pain is real.

If we don't solve it: Sales reports 3 lost deals >$50K ARR in Q4 citing
"no calendar." Competitors Asana and Monday.com both launched calendar views
in the past 12 months.
```

### Bad Metrics Section (comically vague)
```
Success Metrics:
- Engagement: improve
- User satisfaction: increase
- Performance: maintain
```

### Good Metrics Section (specific, actionable)
```
Success Metrics:
| Metric | Type | Baseline | Target | Timeframe |
|--------|------|----------|--------|-----------|
| Calendar view adoption | Primary | 0% | 40% of WAU | 90 days |
| Weekly active users | Primary | 12,400 | 14,260 (+15%) | 90 days |
| "Missed deadline" tickets | Secondary | 89/month | 65/month (-27%) | 90 days |

Guardrails:
- Page load time for calendar view: <2s (p95)
- Drag-and-drop task update latency: <500ms
- No increase in overall app crash rate

Passing criteria (to graduate from 10% rollout): Calendar view adoption >25%
among exposed users AND no guardrail violations after 2 weeks.
```

### Bad Non-Goals (missing or generic)
```
Non-Goals:
- Out of scope items will be considered for future releases
```

### Good Non-Goals (specific, prevents scope creep)
```
Non-Goals:
- We are NOT building Outlook/Exchange sync. V1 is Google Calendar only.
  Outlook is V2 based on enterprise demand.
- We are NOT building resource capacity planning. That's a separate
  initiative owned by the Platform team.
- We are NOT replacing Google Calendar. The sync is additive.
- Tasks without due dates do NOT appear in the calendar view. This is
  intentional — it keeps the view focused on deadlines.
```

---

## Anti-Patterns (From Analyzing 500+ PRDs)

**Fancy structure, empty content.** Every section filled, nothing actually said. Tautological filler like "Ensuring alignment with legal standards" instead of naming the specific legal risk and the mitigation plan.

**Delegating your thinking.** Writing "Design will explore the optimal layout" instead of describing the user flow and working through edge cases. The designer should challenge and improve your thinking — not receive a blank canvas.

**No customer evidence.** The single biggest red flag. Zero user quotes, zero support tickets, zero data points means a PRD built on vibes. Even 3 customer quotes transform a spec from opinion to evidence.

**Hiding the controversial decision.** Close call between approach A and B? Say so. Explain why you chose. This is where alignment actually happens. Burying the controversy guarantees it resurfaces as a blocker.

**Metrics without baselines.** "Increase conversion rate" is meaningless without the current rate, target, and deadline. A metric without a baseline is a wish, not a measurement.

**Ending at launch.** The PRD lifecycle extends past engineering handoff. Add a Stage 6 results link after launch. 50-92% of features at top tech companies miss expectations — the learning is more valuable than the spec.

**Over-specifying the "how."** Engineers and designers are creative problem solvers. Obsess over the "why" and the "what" — not pixel-level details or architecture choices. Specify the user outcome, not the implementation.

**Writing for every audience at once.** Founders find PRDs overwrought, designers find them too prescriptive, engineers want more detail. The fix: be stage-appropriate. Bare-bones early, detailed later, always focused on decisions.

---

## Rules
- **Think crisp, not complete.** Keep PRDs under 2 pages unless the user asks for more. If it's over 2 pages, ask if that depth is needed.
- **Flag missing information** with `[NEED: data from X]` rather than making things up. Never fabricate data, customer quotes, or metrics.
- **Use specific numbers.** Not "improve engagement" — "increase 7-day activation from 23% to 35%."
- **No filler.** Every sentence should add information or drive a decision. Cut anything that fails the "so what?" test.
- **Non-goals go early.** Best defense against scope creep. State them before the solution section.
- **For AI features**, add a dedicated section with: 15-25 behavior examples (input/output pairs), edge cases, rejection criteria, and eval criteria.
- **A strong PRD aligns the team without a meeting.** If someone reads it and still needs a 30-minute walkthrough, it's not done.
- **Documents are your voice when you're not in the room.** Treat them accordingly.
