# AI App Development with Claude Code

---

## What This Course Teaches

This is a **three-lab hands-on path** that teaches you how world-class engineering teams build AI products — not just how to prompt.

You will build **ContractIQ**: a full-stack AI application where users upload a contract PDF and get a structured breakdown of every clause that matters, with multi-turn chat, persistent memory, row-level database security, and automatic deployment.

But the application is the vehicle, not the destination.

What you're really learning is **a repeatable process**:

```
Plan before you build
↓
Build with precise context
↓
Add memory intentionally
↓
Secure before you ship
↓
Deploy with confidence
```

Every Claude prompt you write in this course follows that sequence. By the end, you won't just have a deployed app — you'll have a mental model for building AI products that hold together.

---

## The Three Labs

| Lab | What You Do | Lessons |
|---|---|---|
| **[Lab 1 — Planning & Architecture](./01-Planning-and-Architecture-Lab/readme.md)** | Build the foundation that makes every future prompt coherent — the product spec, design system, engineering document, and implementation blueprint | 3 |
| **[Lab 2 — Building the Application](./02-Building-the-Application-Lab/readme.md)** | Use Claude Code to scaffold the app, implement every feature, and add a persistent memory layer to the chat assistant | 2 |
| **[Lab 3 — Security & Deployment](./03-Security-and-Deployment-Lab/readme.md)** | Scan and fix every security vulnerability, then push to GitHub and deploy live on Netlify | 2 |

Work through them **in order**. Each lab builds directly on what the previous one produced — the engineering documents from Lab 1 drive every build prompt in Lab 2, and you cannot harden and deploy something that doesn't exist yet.

```
Lab 1: Planning        →   Lab 2: Building        →   Lab 3: Ship It
(no app code yet)          (app runs on localhost)     (app is live on the internet)
```

---

## What You Will Build

**Your IDEA (ContractIQ)** — a production-ready AI application with:

- PDF upload and AI-powered contract analysis
- Structured clause breakdown with page citations
- Multi-turn chat with persistent conversation memory
- Supabase database with Row Level Security
- Authentication with protected routes
- Security-hardened codebase ready for production
- Deployment via Netlify — every `git push` redeploys

---

## The Tech Stack

Every choice here was made deliberately. You're not picking the stack — it's fixed in the starter repo — but understanding *why* each piece is there helps you use it correctly.

| Layer | Technology | Why |
|---|---|---|
| **Frontend** | Next.js 14, TypeScript, Tailwind CSS | Full-stack React framework with server components, type safety, and utility-first styling that maps cleanly to a design system |
| **Database & Auth** | Supabase (PostgreSQL + Auth) | Hosted Postgres with built-in authentication and Row Level Security — one user's contracts are never visible to another |
| **AI** | Claude API (Anthropic) | Powers the contract analysis and chat — the same model you're using as your build tool |
| **Deployment** | Netlify | Zero-config deployment from GitHub with encrypted environment variables and automatic redeploys |
| **Build tool** | Claude Code CLI | Plans, writes, secures, and debugs the application — run from the VS Code integrated terminal |

---

## Claude Concepts in This Course

These are the Claude-specific concepts you will encounter and use across all three labs. Each one is explained in context when it first appears — this table is here so you can go deeper on any concept that interests you.

| Concept | First appears | Learn more |
|---------|--------------|------------|
| **Claude Code CLI** | Lab 1, Lesson 1 — the build tool used throughout every lab to plan, write, debug, and ship | [Claude Code →](https://docs.anthropic.com/en/docs/claude-code) |
| **CLAUDE.md** | Lab 1, Lesson 1 — a project-level file Claude reads at the start of every session to understand context, rules, and current stage | [Memory →](https://docs.anthropic.com/en/docs/claude-code/memory) |
| **Skills / slash commands** | Lab 1, Lesson 2 — reusable `SKILL.md` files that define exactly how Claude should approach a task, invoked with `/skill-name` | [Skills guide →](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf) |
| **Plan Mode** | Lab 1, Lesson 3 — Claude reads and reasons but writes nothing until you approve; catches architecture gaps before any code is written | [Claude Code →](https://docs.anthropic.com/en/docs/claude-code) |
| **`@` file references** | Lab 1, Lesson 3 — point Claude directly at a file path instead of pasting content; Claude reads it in context | [Prompt engineering →](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) |
| **Stateless Claude API** | Lab 2, Lesson 2 — each API call starts fresh with no memory of prior calls; conversation history must be explicitly loaded | [Messages API →](https://docs.anthropic.com/en/api/messages) |
| **Context windows** | Lab 2, Lesson 2 — the messages[] array Claude sees on each call; short-term memory lives here | [Context windows →](https://docs.anthropic.com/en/docs/build-with-claude/context-windows) |
| **Prompt engineering** | Throughout — how you structure prompts determines what Claude builds; specificity and context are the levers | [Prompt engineering →](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) |

---

## Start Here

Begin with **[Lab 1 — Planning & Architecture](./01-Planning-and-Architecture-Lab/readme.md)**.
