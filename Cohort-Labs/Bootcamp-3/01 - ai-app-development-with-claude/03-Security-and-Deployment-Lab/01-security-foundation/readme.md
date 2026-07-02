[← Back to Lab 3 Overview](../readme.md)

**Lesson 1** | [Lesson 2 →](../02-deployment/readme.md)

---

# Lesson 1 — Security Foundation

<!-- 📸 Add a banner screenshot here as ./images/banner.png and uncomment the line below.
     Suggested shot: the Claude Code terminal mid-way through a /security-fix run, showing
     the checklist of issues being found and fixed.
![images](./images/banner.png) -->

## Where We Are

By this point you have completed **Lab 1 — Planning & Architecture** and **Lab 2 — Building the Application**:

- Forked the `dev-os` starter repo, explored the skills and design system, and produced the engineering documents in `docs/engineering/`.
- Scaffolded the Next.js project, implemented the application, ran the database schema in Supabase, and added a memory layer so the assistant can recall conversation history within and across sessions.

You now have a fully working application. The next question is: **is it safe to ship?**

This lesson runs the `security-fix` skill, which scans every file in the codebase, identifies the most common security vulnerabilities, and fixes each one automatically — before any real user touches the app.

---

## The Problem — A Working App Is Not a Secure App

When you build quickly, security gaps appear naturally. None of them are obvious from the browser — the app looks fine. But underneath, several things are likely wrong:

| Problem | What Can Go Wrong |
|---|---|
| Hardcoded secrets in source code | Secrets get committed to GitHub and are exposed publicly |
| Sensitive data printed to `console.log` | API keys and user data appear in server logs that may be accessible to others |
| Secrets with a `NEXT_PUBLIC_` prefix | The key ships to every user's browser and is visible in the page source |
| API routes without auth checks | Anyone can call `/api/chat` directly from the terminal, without logging in |
| Error responses that include stack traces | An attacker learns your file paths, library versions, and database structure |
| Missing security headers | The browser has no instruction to block clickjacking, MIME sniffing, or XSS |
| Unsafe `eval` or unescaped `innerHTML` | User-supplied content can execute arbitrary code in the browser |
| `.env.local` not in `.gitignore` | A `git push` accidentally commits your API keys to a public repo |

None of these are hypothetical. They are the most common vulnerabilities in AI applications built under time pressure. This lesson fixes all of them in one pass.

---

## What the Skill Does

The `security-fix` skill works through eight checks in order. For every issue it finds, it applies the fix immediately before moving to the next check.

| # | Check | What Gets Fixed |
|---|---|---|
| 1 | **Hardcoded secrets** | Replaced with `process.env.YOUR_VAR_NAME`; var added to `.env.example` |
| 2 | **Secrets in `console.log`** | Statements printing sensitive data removed or scrubbed |
| 3 | **Secrets exposed to client** | `NEXT_PUBLIC_` prefix removed from secret vars; reads moved to API routes |
| 4 | **API routes missing auth** | `getUser()` check inserted at the top of each unprotected handler |
| 5 | **Stack traces in error responses** | Generic `"Internal server error"` returned to client; full error kept in server log |
| 6 | **Missing security headers** | `X-Frame-Options`, `X-Content-Type-Options`, `X-XSS-Protection`, `Referrer-Policy`, `Permissions-Policy` added to `next.config.js`; `poweredByHeader: false` set |
| 7 | **Unsafe `eval` / `innerHTML`** | `eval()` and `new Function()` removed; `dangerouslySetInnerHTML` wrapped with `DOMPurify.sanitize()` |
| 8 | **`.gitignore` missing env files** | `.env`, `.env.local`, `.env*.local` entries added |

At the end, the skill presents a summary table showing the status and changed files for every check.

---

## Step 1 — Open Claude Code in VS Code

Open your project folder in **VS Code**, open the integrated terminal (**Terminal > New Terminal**, or `` Ctrl+` ``), and start the Claude Code CLI:

```bash
claude
```

---

## Step 2 — Run the Security Fix Skill

Copy and paste the following prompt into the same Claude Code terminal session:

```
Use @skills/security-fix/SKILL.md to scan the codebase and fix all security issues.
```

Press **Enter** and let the skill run.

> **Note:** The skill applies fixes automatically. Review each diff before approving. Pay attention to any items listed under **Manual Actions Required** at the end — these are issues the skill found but could not fix automatically.

<!-- 📸 Optional: capture the skill's final summary table as ./images/1.png and reference it
     here with ![Summary table](./images/1.png) -->

---

## What the Skill Changes

The skill modifies existing files only — it does not create new ones. The files most commonly changed are:

```
next.config.js         ← security headers added; poweredByHeader set to false
.gitignore             ← .env.local and .env*.local entries added
app/api/**/route.ts    ← auth checks inserted at the top of unprotected handlers
.env.example           ← any newly referenced env vars documented
```

Individual source files are updated wherever hardcoded secrets, unsafe console logs, or dangerous HTML patterns are found.

---

## Step 3 — Verify the Fixes

Start the development server if it is not already running:

```bash
npm run dev
```

Walk through this verification sequence:

| Test | How to Check | Expected Result |
|---|---|---|
| Security headers present | Open DevTools → Network → any request → Response Headers | `X-Frame-Options`, `X-Content-Type-Options`, `X-XSS-Protection` visible |
| Unauthorized API call | Call `/api/chat` in a new tab without being logged in | `401 Unauthorized` response |
| No secrets in page source | View page source in the browser and search for your API key value | Key is not present |
| `.gitignore` covers env files | Run `git status` — `.env.local` should not appear as untracked | File is ignored |

<!-- 📸 Optional: capture the DevTools Response Headers panel showing the new security
     headers as ./images/2.png and reference it here with ![Security headers](./images/2.png) -->

If any test fails, paste the description into the Claude Code terminal and it will diagnose and fix the specific issue.

---

## What You Have Built

At the end of this lesson your application has:

- **No hardcoded secrets** — every credential is read from environment variables
- **Protected API routes** — unauthenticated requests are rejected before reaching any business logic
- **Safe error handling** — internal details stay on the server; clients receive only a generic message
- **Security headers** — the browser is instructed to block clickjacking, MIME sniffing, and reflected XSS
- **A clean `.gitignore`** — environment files cannot be accidentally committed to version control

---

## What You Learned

- **Why a working app is not a secure app** — speed of development creates predictable security gaps; the most common ones (hardcoded secrets, missing auth on API routes, `NEXT_PUBLIC_` on secret vars) are invisible from the browser but exploitable from the terminal.
- **Scanning before shipping** — running a dedicated security scan as a step in the build process catches issues that code review misses, because reviewers focus on logic, not attack surfaces.
- **The principle of least privilege for environment variables** — `NEXT_PUBLIC_` means "ship this to every browser"; secrets like `OPENAI_API_KEY` must never carry that prefix and must only be read inside server-side API routes.
- **Security headers as browser-side controls** — `X-Frame-Options`, `X-XSS-Protection`, and `X-Content-Type-Options` are instructions to the browser; they do not protect the server but they block a class of client-side attacks that server code cannot see.
- **Generic error responses** — returning `"Internal server error"` to the client while logging the real error server-side is a deliberate trade-off: it keeps your infrastructure details out of an attacker's hands without losing the information you need to debug.
- **`.gitignore` as a last line of defence** — if `.env.local` is not ignored, one accidental `git add .` exposes every secret in the project to anyone with read access to the repository.

---

## Troubleshooting — Let Claude Fix It

If a security fix breaks something or a check did not apply correctly, paste the issue into the Claude Code terminal using one of the prompts below.

---

#### Security headers are not appearing in responses

```
The security headers (X-Frame-Options, X-Content-Type-Options, etc.) are not appearing in response headers. Check the headers() export in next.config.js and confirm the config is structured correctly. Fix whatever is preventing the headers from being applied.
```

---

#### An API route is still accessible without authentication

```
The route [paste the route path] is returning a 200 response when called without an auth token. The security-fix skill should have added a getUser() check at the top of the handler. Find out why the check is missing or not running and add it correctly.
```

---

#### A valid feature broke after the auth check was added

```
After the security-fix skill added an auth check to [route path], this feature stopped working: [describe the feature]. The error is: [paste the error]. The auth check should not block this flow — diagnose why it is and fix it without removing the check.
```

---

#### `.env.local` is still showing as untracked in git

```
Running git status shows .env.local as an untracked file even after the security-fix skill ran. Check .gitignore and add the correct entries so all env files are ignored.
```

---

#### The skill reported a Manual Action Required item you are not sure how to handle

```
The security-fix skill flagged this as a manual action required: [paste the item]. Explain what the issue is, why it could not be auto-fixed, and give me the exact steps or code changes needed to resolve it.
```

---

[← Back to Lab 3 Overview](../readme.md)

**Lesson 1** | [Lesson 2 →](../02-deployment/readme.md)
