# Lab 2 — Building the Application

**Part 2 of 3** in the ContractIQ build path: [Lab 1: Planning](../01-Planning-and-Architecture-Lab/readme.md) → [Lab 2: Building](./readme.md) → [Lab 3: Security & Deployment](../03-Security-and-Deployment-Lab/readme.md)

---

This is the **"make it real"** lab. You take the engineering plan from Lab 1 and turn it into a running application: a Next.js frontend, a Supabase database with authentication, an AI-powered backend, and a chat interface that actually remembers what was said five minutes ago.

> **Prerequisite:** You need `docs/engineering/engineering-doc.md` and `docs/engineering/implementation-specs.md` in your project before starting this lab. These come from [Lab 1, Lesson 3 — Engineering Planning](../01-Planning-and-Architecture-Lab/03-engineering-planning/readme.md). If you don't have them yet, go back and run that lesson first — everything in this lab reads from those two files.

**Workflow note:** every prompt in this lab is run the same way — open your project in **VS Code**, open the built-in terminal (**Terminal > New Terminal**, or `` Ctrl+` ``), type `claude` to launch the **Claude Code CLI**, and paste the prompt. You stay inside that one terminal session for both lessons.

---

## Lessons in This Lab

| # | Lesson | What You Do |
|---|---|---|
| 1 | [Building the Application](./01-building-the-application/readme.md) | Set up a live Supabase database, scaffold the Next.js app, implement the frontend and backend from your engineering docs, generate the SQL schema, and run the app in your browser |
| 2 | [Memory Layer](./02-memory-layer/readme.md) | Give the chat assistant persistent memory so it can answer follow-up questions within a session and across page refreshes |

---

## What You Will Build in This Lab

- A Next.js 14 application with a complete, production-style folder structure
- A live Supabase project: PostgreSQL database, authentication, Row Level Security
- The full ContractIQ feature set: PDF upload, AI-powered clause extraction, page-cited results
- A chat interface with persistent, multi-turn conversation memory
- An app running and fully testable at `http://localhost:3000`

By the end of this lab, ContractIQ works. It is not yet secure for production and it is not yet on the internet — that's Lab 3.

---

## Where to Drop Screenshots

Each lesson's `images/` folder already has the original walkthrough screenshots copied in and wired up by filename — you don't need to add anything to follow along. If your local UI looks different (Supabase or Netlify redesigns their dashboard fairly often), recapture that one screenshot and save it over the existing file using the **same filename** so the `readme.md` doesn't need any edits. The two places most likely to drift over time are the **Supabase project creation screens** (Lesson 1, images `1.png`–`7.png`) and the **Supabase SQL Editor** (Lesson 1, image `19.png`).

---

## Up Next

Start with [Lesson 1 — Building the Application](./01-building-the-application/readme.md).

When both lessons are complete, continue to **[Lab 3 — Security & Deployment](../03-Security-and-Deployment-Lab/readme.md)**.
