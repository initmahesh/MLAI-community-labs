[← Lesson 2 — Building the Application](../02-building-the-application-lesson/README.md) | [Lesson 4 — Azure AI Integration →](../04-integration-of-your-app-with-azure-ai/README.md)

---

# Lesson 3 — Security & Deployment

This is the **"make it safe to ship"** lesson. Your app already works on `http://localhost:3000` — that's the easy part. This lesson covers everything that has to happen *after* local development before real users can touch it: scanning for the security mistakes every fast-moving build accumulates, then pushing the code to GitHub and deploying it live.

> **Prerequisite:** You need a working ContractIQ app running locally with Supabase connected. That comes from [Lesson 2 — Building the Application](../02-building-the-application-lesson/README.md). If `npm run dev` doesn't give you a working app at `localhost:3000`, finish Lesson 2 first.

**Workflow note:** the security lesson runs entirely from Claude Code Desktop's terminal — same pattern as the previous two lessons. The deployment lesson moves between three places: your terminal (for git commands), the GitHub website, and the Netlify website.

---

## Lessons in This Part

| # | Lesson | What You Do |
|---|---|---|
| 1 | [Security Foundation](./01-security-foundation-lesson/readme.md) | Run the `security-foundation` skill to scan the codebase and automatically fix hardcoded secrets, missing auth checks, leaky errors, and other common vulnerabilities |
| 2 | [Deployment](./02-deployment-lesson/readme.md) | Push your code to GitHub and deploy the live app to Netlify, with environment variables configured correctly |

---

## What You Will Walk Away With

- A codebase with no hardcoded secrets, protected API routes, safe error handling, and security headers in place
- Your code pushed to your GitHub fork
- A live, publicly accessible app at `https://your-app-name.netlify.app`
- Automatic redeployment on every future `git push` to `main`

---

## Up Next

Start with [Lesson 1 — Security Foundation](./01-security-foundation-lesson/readme.md).
