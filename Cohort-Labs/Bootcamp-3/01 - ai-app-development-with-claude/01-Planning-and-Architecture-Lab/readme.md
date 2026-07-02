# Lab 1 — Planning & Architecture

**Part 1 of 3** in the ContractIQ build path: [Lab 1: Planning](./readme.md) → [Lab 2: Building the Application](../02-Building-the-Application-Lab/readme.md) → [Lab 3: Security & Deployment](../03-Security-and-Deployment-Lab/readme.md)

---

This is the **"think before you build"** lab. No application code gets written here. By the end of this lab you will have forked a starter repository, understood the problem you're solving, learned how Claude Code's reusable instruction sets ("skills") and design system work, defined your tech stack, and turned a product idea into a concrete, file-by-file engineering plan.

If you skip this lab and go straight to coding, you end up improvising the database schema halfway through building a screen, or discovering a missing feature three files deep into implementation. This lab exists so that doesn't happen.

No prior AI development or software engineering experience is required. Every step is written assuming this is the first time you've done it.

---

## Lessons in This Lab

| # | Lesson | What You Do |
|---|---|---|
| 1 | [Project Foundation](./01-project-foundation/readme.md) | Understand the problem you're solving, fork the starter repo, clone it, and open it in VS Code |
| 2 | [Skills and the Design System](./02-skills-and-design-system/readme.md) | Learn how Claude Code skills work and review the design system that will govern the app's UI |
| 3 | [Engineering Planning](./03-engineering-planning/readme.md) | Use Plan Mode to turn the product requirements into an architecture document and file-by-file implementation specs |

---

## What You Will Build Toward

Across this lab you will plan **ContractIQ** — a web app where a user uploads a contract PDF and gets back a structured, page-cited breakdown of every clause that matters, plus a chat interface to ask follow-up questions about the document.

You won't write a line of frontend or backend code in this lab. What you *will* produce by the end:

- A local clone of the starter repository, open and ready in VS Code
- A clear mental model of the product, its users, and what "done" looks like
- An understanding of the five Claude Code skills that drive the rest of the build
- The design system (`docs/design.md`) that every screen will follow
- `docs/engineering/engineering-doc.md` — the architecture plan
- `docs/engineering/implementation-specs.md` — the file-by-file build blueprint

These last two documents are what Lab 2 is built from. Nothing in Lab 2 makes sense without them.

---

## Tech Stack Decided in This Lab

| Layer | Technology | Why |
|---|---|---|
| Frontend | Next.js 14, TypeScript, Tailwind CSS | Full-stack React framework, type safety, utility-first styling that maps cleanly to a design system |
| Database & Auth | Supabase (PostgreSQL + Auth) | Hosted Postgres with built-in auth and Row Level Security, generous free tier |
| AI | Claude API (Anthropic) / OpenAI | Powers the contract analysis and chat features |
| Planning & Build Tool | Claude Code | Plans, writes, secures, and helps ship the application |

This stack is fixed in the starter repo you fork in Lesson 1 — you are not choosing it from scratch, but you should understand *why* each piece is there before you build on top of it.

---

## Where to Drop Screenshots

Every lesson folder in this lab has its own `images/` subfolder, and the existing screenshots from the original walkthrough have already been copied in and are wired up — you don't need to add anything to follow along. If you want to **recapture your own screenshots** (recommended if any tool's UI has changed since this was written), drop the new image into the matching lesson's `images/` folder using the **same filename** that's already there (e.g. replace `01-project-foundation/images/3.png` with your own screenshot of the same step) — the lesson's `readme.md` already points at that filename, so nothing else needs to change.

---

## Up Next

Start with [Lesson 1 — Project Foundation](./01-project-foundation/readme.md).

When all three lessons are complete, continue to **[Lab 2 — Building the Application](../02-Building-the-Application-Lab/readme.md)**.
