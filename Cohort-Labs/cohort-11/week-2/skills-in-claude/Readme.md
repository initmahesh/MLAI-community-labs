# Skills in Claude — Week 2 Lab

This lab covers how to build and use **skills** — reusable instruction sets that tell Claude how to behave for a specific task. Instead of typing long instructions every time, you invoke a skill by name and Claude follows its built-in playbook.

---

## What is a Skill?

A skill is a Markdown file with a YAML frontmatter block (`name`, `description`, `version`) followed by detailed behavioral instructions. When you invoke it with `/skill-name`, Claude loads those instructions and follows them instead of its defaults.

Skills let you encode expertise, enforce structure, and get consistent output across sessions — without repeating yourself.

---


## How to Install a Skill

Not sure how to upload a skill into Claude? Watch this video:
[How to Upload a Skill in Claude - Click Here](https://maven.com/mahesh-yadav/genaipm/10/syllabus/modules/72e67d/eva3x7q8lc)

---

## Skills in This Lab

### `/prd` — PRD Writer

Writes modern, crisp Product Requirements Documents.

**When to use it:** Any time you need to write, draft, or spec out a product feature — from a quick speclet to a full launch-ready PRD.

**What it does:**
- Asks 3–5 clarifying questions before writing anything (who has the problem, what data exists, what stage this is at)
- Determines which of 6 PRD stages applies — from early team kickoff all the way to post-launch impact review
- Generates a structured PRD: hypothesis, problem with evidence, strategic fit, solution with user flows, non-goals, success metrics with baselines and targets, rollout plan, and open questions
- Runs a stage-appropriate checklist after generating and flags gaps
- Offers to tighten it into a 1-pager or review it from an engineer/designer/skeptic perspective

**Key principles it enforces:** No fabricated data, specific numbers over vague language, non-goals before scope creep sets in, customer evidence required.

---

### `/project-eval` — Project Evaluator

Scores an AI product concept against a structured PM checklist and gives honest, direct feedback.

**When to use it:** When you want to know if a product idea is ready for stakeholder review, or to get structured feedback before presenting to leadership.

**What it does:**
- Collects required inputs: product name, target persona, why agentic AI (not rule-based), and your MOAT
- Runs web research on competitors, market trends, and known failure patterns before scoring
- Evaluates 17 checks across 4 sections — Problem Definition (2x weight), Solution Definition, Core Metrics (2x weight), and Risks & Assumptions
- Calculates a weighted score out of 27 and maps it to a readiness tier (Early Stage → Developing → Strong)
- Outputs a full evaluation report written as prose — what's working, what needs work, detailed per-check feedback, top 3 priorities to fix, and quick wins you can add in under 30 minutes

**Key principles it enforces:** Feedback sounds like a senior PM colleague, not a rubric. Real competitor names, real market data, concrete next steps — no generic advice.

### `/idea-eval` — Idea Evaluator

Evaluates whether a product idea is a strong candidate for Agentic AI — calibrated on 200+ AI product pitches.

**When to use it:** When you have a product idea and want to know if it's a good fit for agentic AI, how complex it is to build, and what the risks are before investing more time.

**What it does:**
- Collects four required inputs upfront in one message: product name, target persona and their pain, why agentic AI (not rule-based logic), and your MOAT
- Runs market research on competitors, recent launches, and relevant data before scoring
- Scores the idea across 5 weighted sections: Problem Fit (20%), Agentic AI Fit (25%), MOAT Strength (20%), Monetization (15%), and GTM/Acquisition (20%)
- Adjusts scoring for stage — napkin ideas are not penalized for missing user research or kill criteria
- Outputs a concise **Complexity · Pros · Cons · Suggestion** evaluation with a single framing sentence, specific MVP scope, and a win condition

**Key principles it enforces:** Direct and specific — names real competitors, flags missing monetization or GTM as explicit cons, always ends with a concrete recommendation on what to build and what to defer.

---

## How to Invoke a Skill

Type the skill name as a slash command in Claude Code:

```
/prd
/project-eval
/idea-eval
```

Claude will load the skill's instructions and prompt you for any missing inputs before proceeding.
