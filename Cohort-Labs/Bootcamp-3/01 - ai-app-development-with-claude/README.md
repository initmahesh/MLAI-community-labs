# AI App Development with Claude Code

A hands-on, three-lab path that takes you from a blank idea to a deployed, production-ready AI application — using the **Claude Code CLI inside VS Code** to plan, build, secure, and ship every step of the way.

You will build **ContractIQ**: a full-stack web app where users upload contract PDFs and receive an AI-powered breakdown of every clause that matters — what it says, where it appears, and how confident the model is in its reading.

No prior AI development experience required. This is an **implement-first** course: you build the real thing first, and the "why" behind each step is explained as you go, not before.

---

## The Three Labs

| Lab | Focus | Lessons |
|---|---|---|
| **[Lab 1 — Planning & Architecture](./01-Planning-and-Architecture-Lab/readme.md)** | Everything that happens *before* you write application code: understanding the problem, the starter repo, Claude Code skills, the design system, and turning a product idea into a concrete engineering plan | 3 |
| **[Lab 2 — Building the Application](./02-Building-the-Application-Lab/readme.md)** | Everything that happens *while* you write application code: scaffolding Next.js, setting up Supabase, implementing the frontend and backend, and adding a persistent memory layer to the chat assistant | 2 |
| **[Lab 3 — Security & Deployment](./03-Security-and-Deployment-Lab/readme.md)** | Everything that happens *after* the app works on `localhost`: scanning and fixing security vulnerabilities, then pushing to GitHub and deploying live on Netlify | 2 |

Work through them **in order** — each lab assumes the previous one is finished and reads from files the previous lab produced. You cannot skip to Lab 2 without the engineering documents from Lab 1, and you cannot deploy in Lab 3 without a working app from Lab 2.

```
Lab 1: Planning  →  Lab 2: Building  →  Lab 3: Security & Deployment
(no code yet)       (app runs locally)   (app is live on the internet)
```

---

## What You Will Build

**ContractIQ** — a full-stack AI application with:

- PDF upload and AI-powered contract analysis
- Structured clause breakdown with page citations
- Multi-turn chat with persistent conversation memory
- Supabase database with Row Level Security
- Authentication with protected routes
- Security-hardened codebase
- Automatic CI/CD deployment via Netlify

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Next.js 14, TypeScript, Tailwind CSS |
| Database & Auth | Supabase (PostgreSQL + Auth) |
| AI | Claude API (Anthropic) / OpenAI |
| Deployment | Netlify |
| Planning & Build | Claude Code CLI (run from VS Code's integrated terminal) |

---

## How Each Lesson Is Structured

Every lesson folder across all three labs follows the same pattern, so once you've done one you know what to expect from the rest:

- **Where We Are** — a recap of what's been completed so far in the path
- **Step-by-step instructions** — including the exact prompts to paste into the Claude Code CLI
- **Screenshots** — in that lesson's own `images/` folder, referenced inline
- **What You Have Built / What You Learned** — a summary at the end
- **Troubleshooting** (where relevant) — ready-to-paste prompts for the most common failure modes

---

## Screenshots — Where to Put Them

Every lesson has its own `images/` folder sitting right next to its `readme.md`. The original walkthrough's screenshots have already been copied into the matching folders across all three labs and are wired up by filename — **you don't need to add anything to start.**

If you want to refresh a screenshot (UI redesigns happen — Supabase and Netlify both change their dashboards periodically):

1. Open the lesson's `readme.md` and find the `![...](./images/N.png)` reference for the step you want to update.
2. Save your new screenshot over the existing file at that exact path and filename (e.g. `02-Building-the-Application-Lab/01-building-the-application/images/6.png`).
3. That's it — no markdown edits needed, since the file is referenced by name, not content.

Two spots have **no screenshot yet** and are marked with an HTML comment in the source explaining what to capture:
- `03-Security-and-Deployment-Lab/01-security-foundation/` — the original course never captured screenshots for this lesson since it runs entirely in the terminal; add your own if you'd like a visual record of the `security-fix` skill's summary output.
- `03-Security-and-Deployment-Lab/02-deployment/` — the final "redeployed after updating NEXTAUTH_URL" screenshot was missing from the original course too.

---

## Start Here

Begin with **[Lab 1 — Planning & Architecture](./01-Planning-and-Architecture-Lab/readme.md)**.
