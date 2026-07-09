# Lab 1 — Planning & Architecture

**Part 1 of 3** → [Lab 1: Planning](./readme.md) · [Lab 2: Building](../02-Building-the-Application-Lab/readme.md) · [Lab 3: Security & Deployment](../03-Security-and-Deployment-Lab/readme.md)

---

Most developers who start an AI project with Claude make the same mistake.

They open a blank file, type a prompt like *"build me a contract review app"*, and let Claude write. Something appears. It looks promising. They keep going.

Three hours later the database schema doesn't match the frontend. There's a feature in the UI that has no backend. The chat interface works but forgets everything on refresh. The code is technically there — it just doesn't hold together.

The problem wasn't Claude. The problem was that nobody told Claude what it was actually building.

---

## What This Lab Is About

This is the **"think before you build"** lab.

No application code gets written here. What you're doing instead is more important: you're building the foundation that makes every future prompt produce something coherent.

By the end of this lab, Claude will know:

- What ContractIQ is, who it's for, and what "done" looks like
- The complete database schema, API design, and architecture
- Which files need to be built and in what order
- The visual rules every screen must follow
- The constraints and edge cases that matter for a legal tool

When Lab 2 starts, Claude won't be improvising. It will be executing a plan.

---

## The Problem You Are Solving

Picture a founder at a 20-person SaaS company. A potential enterprise client sends over a 30-page Master Service Agreement. She needs to sign it by end of week. She has no in-house lawyer, so she either spends 90 minutes reading every clause herself — or pays $400 for legal time to get a summary she barely understands.

She does this ten times a month.

You are building **your idea(ContractIQ)** — a web app where a user uploads a contract PDF and within 30 seconds sees a structured breakdown of every clause that matters: what it says, where it appears in the document, and how confident the AI is in its reading. If something looks off, the user can click through to the exact sentence it came from. And when they have a specific question, they can ask it in plain English and get an answer grounded in the actual document.

The tool doesn't replace a lawyer. It gives people enough understanding to know when they need one.

---

## What You Will Produce

You won't write a single line of frontend or backend code in this lab. What you *will* produce:

- A clear mental model of the product, its users, and what "done" looks like
- An understanding of the five Claude Code skills that drive the rest of the build
- The design system (`docs/design.md`) that every screen will follow
- `docs/engineering/engineering-doc.md` — the full architecture plan
- `docs/engineering/implementation-specs.md` — the file-by-file build blueprint

These last two documents are what Lab 2 is built from. Nothing in Lab 2 makes sense without them.

---

## Lessons in This Lab

| # | Lesson | What You Do |
|---|---|---|
| 1 | [Project Foundation](./01-project-foundation/readme.md) | Understand the problem you're solving, fork the starter repo, clone it, and open it in VS Code |
| 2 | [Skills and the Design System](./02-skills-and-design-system/readme.md) | Learn how Claude Code skills work and review the design system that will govern the app's UI |
| 3 | [Engineering Planning](./03-engineering-planning/readme.md) | Use Plan Mode to turn the product requirements into an architecture document and implementation specs |

---

## The Tech Stack

Every technology choice in this project was made for a reason. You're not choosing the stack from scratch — it's fixed in the starter repo — but you should understand *why* each piece is there before you build on top of it.

| Layer | Technology | Why |
|---|---|---|
| **Frontend** | Next.js 14, TypeScript, Tailwind CSS | Full-stack React framework with server components, type safety, and utility-first styling that maps cleanly to a design system |
| **Database & Auth** | Supabase (PostgreSQL + Auth) | Hosted Postgres with built-in authentication and Row Level Security — one user's contracts are never visible to another |
| **AI** | Openai API | Powers the contract analysis and chat features — the same model you're using to build the app |
| **Build Tool** | Claude Code | Plans, writes, secures, and helps ship the application |

---

## How to Navigate the Screenshots

Every lesson folder has its own `images/` subfolder. Existing screenshots are already wired up — you don't need to add anything to follow along.

If a tool's UI has changed since this was written, drop your own screenshot into the matching `images/` folder using the **same filename** already there (e.g. replace `01-project-foundation/images/3.png` with your version of the same step). The lesson files already point at those filenames — nothing else needs to change.

---

## Ready?

Start with **[Lesson 1 — Project Foundation](./01-project-foundation/readme.md)**.

When all three lessons are complete, continue to **[Lab 2 — Building the Application](../02-Building-the-Application-Lab/readme.md)**.
