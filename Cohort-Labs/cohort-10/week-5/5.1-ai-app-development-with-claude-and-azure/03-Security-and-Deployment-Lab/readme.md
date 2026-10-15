# Lab 3 — Security & Deployment

**Part 3 of 3** in the ContractIQ build path: [Lab 1: Planning](../01-Planning-and-Architecture-Lab/readme.md) → [Lab 2: Building](../02-Building-the-Application-Lab/readme.md) → [Lab 3: Security & Deployment](./readme.md)

---

This is the **"make it safe to ship"** lab. Your app already works on `http://localhost:3000` — that's the easy part. This lab covers everything that has to happen *after* local development before real users can touch it: scanning for the security mistakes every fast-moving build accumulates, then pushing the code to GitHub and deploying it live.

> **Prerequisite:** You need a working ContractIQ app running locally with Supabase connected. That comes from [Lab 2 — Building the Application](../02-Building-the-Application-Lab/readme.md). If `npm run dev` doesn't give you a working app at `localhost:3000`, finish Lab 2 first.

**Workflow note:** the security lesson runs entirely from the Claude Code CLI inside VS Code's terminal — same pattern as the previous two labs (`Terminal > New Terminal`, then `claude`). The deployment lesson moves between three places: your terminal (for git commands), the GitHub website, and the Netlify website.

---

## Lessons in This Lab

| # | Lesson | What You Do |
|---|---|---|
| 1 | [Security Foundation](./01-security-foundation/readme.md) | Run the `security-fix` skill to scan the codebase and automatically fix hardcoded secrets, missing auth checks, leaky errors, and other common vulnerabilities |
| 2 | [Deployment](./02-deployment/readme.md) | Push your code to GitHub and deploy the live app to Netlify, with environment variables configured correctly |

---

## What You Will Walk Away With

- A codebase with no hardcoded secrets, protected API routes, safe error handling, and security headers in place
- Your code pushed to your GitHub fork
- A live, publicly accessible app at `https://your-app-name.netlify.app`
- Automatic redeployment on every future `git push` to `main`

---

## Where to Drop Screenshots

The **Deployment** lesson's `images/` folder already has the original Netlify walkthrough screenshots copied in. The **Security Foundation** lesson has no screenshots in the original walkthrough — the entire lesson happens inside the Claude Code terminal, so there's nothing visual to capture except the terminal output itself. If you want to add screenshots there for your own reference, drop them into `01-security-foundation/images/` as `1.png`, `2.png`, etc., and reference them in that lesson's `readme.md` with `![images](./images/1.png)`.

---

## Up Next

Start with [Lesson 1 — Security Foundation](./01-security-foundation/readme.md).
