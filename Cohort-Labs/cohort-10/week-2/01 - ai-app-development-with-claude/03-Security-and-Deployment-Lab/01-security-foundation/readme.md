[← Back to Lab 3 Overview](../readme.md)

**Lesson 1** | [Lesson 2 →](../02-deployment/readme.md)

---

# Lesson 1 — Security Foundation

![images](./images/banner.png)

---

## Why Security Breaks Happen

Here's the uncomfortable truth about building quickly with AI.

Claude writes code that does what you describe. If you say *"build a chat API route"*, Claude builds a chat API route — functional, well-structured, exactly as requested. It doesn't add authentication unless you ask for it. It doesn't scrub secrets from error messages unless that's in the spec. It doesn't add browser security headers because those weren't in the prompt.

None of this is Claude's fault. It built what you asked for.

The problem is that security requirements are easy to forget when you're focused on features. And unlike a missing feature — which is immediately obvious — a security gap is invisible in the browser. Everything looks fine. It just isn't.

The vulnerabilities aren't random, either. They're predictable. The same issues appear in almost every AI-built application:

| Vulnerability | What it means | Why it matters |
|---|---|---|
| Hardcoded secrets in source code | API keys written directly into files | One `git push` to a public repo exposes them to everyone |
| Secrets with `NEXT_PUBLIC_` prefix | Secret keys that ship to every browser | Visible in the page source — anyone can read them |
| API routes without auth checks | Backend endpoints callable without logging in | Anyone on the internet can call your API directly |
| Stack traces in error responses | Full error details returned to the client | Attackers learn your file paths, library versions, and database structure |
| Missing security headers | No browser-side protections configured | Enables clickjacking, MIME sniffing, and reflected XSS attacks |
| `console.log` printing sensitive data | Credentials written to server logs | Logs that others can read become a credentials dump |
| Unsafe `eval` or `innerHTML` | Unsanitized user content executed as code | A user can run arbitrary JavaScript in other users' browsers |
| `.env.local` not in `.gitignore` | Environment file not ignored by git | One `git add .` commits every secret in the project |

None of these are hypothetical. They are the most common vulnerabilities found in production AI applications — and every one of them is invisible from the browser.

---

## Where You Are in the Process

```
Idea
↓
Research
↓
PRD  ✓
↓
Claude Code Agents  ✓
↓
Engineering Document  ✓
↓
Implementation Specs  ✓
↓
Build  ✓
↓
Memory Layer  ✓
↓
Security Foundation  ← YOU ARE HERE
↓
Deployment
↓
Iteration
```

You have a working app. Now you make it safe to ship.

---

## What the Skill Does

The `security-fix` skill scans the entire codebase and fixes every vulnerability it finds — automatically, in one pass.

It works through eight checks in order. For each issue found, it applies the fix before moving to the next check:

| # | Check | What gets fixed |
|---|---|---|
| 1 | **Hardcoded secrets** | Replaced with `process.env.YOUR_VAR_NAME`; variable added to `.env.example` |
| 2 | **Secrets in `console.log`** | Statements printing sensitive data removed or scrubbed |
| 3 | **Secrets exposed to client** | `NEXT_PUBLIC_` prefix removed from secret vars; reads moved server-side |
| 4 | **API routes missing auth** | `getUser()` check inserted at the top of each unprotected handler |
| 5 | **Stack traces in error responses** | Generic `"Internal server error"` returned to client; full error kept in server log |
| 6 | **Missing security headers** | `X-Frame-Options`, `X-Content-Type-Options`, `X-XSS-Protection`, `Referrer-Policy`, `Permissions-Policy` added to `next.config.js` |
| 7 | **Unsafe `eval` / `innerHTML`** | `eval()` and `new Function()` removed; `dangerouslySetInnerHTML` wrapped with `DOMPurify.sanitize()` |
| 8 | **`.gitignore` missing env files** | `.env`, `.env.local`, `.env*.local` entries added |

At the end, the skill produces a summary table showing the status and changed files for every check — plus a **Manual Actions Required** list for anything it found but couldn't fix automatically.

---

## Step 1 — Open Claude Code

Open your project folder in **VS Code**, open the integrated terminal (**Terminal > New Terminal**, or `` Ctrl+` ``), and start Claude Code:

```bash
claude
```

---

## Step 2 — Run the Security Skill

Paste the following prompt into the Claude Code terminal:

```
Use @skills/security-foundation/SKILL.md to scan the codebase and fix all security issues.
```

Press **Enter** and let the skill run completely.

> **Note:** The skill applies fixes automatically. Review each diff before approving. Pay close attention to any items listed under **Manual Actions Required** at the end — these are issues the skill found but could not fix without your input.

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

Start the development server:

```bash
npm run dev
```

Walk through this verification sequence:

| Test | How to check | Expected result |
|---|---|---|
| Security headers present | DevTools → Network → any request → Response Headers | `X-Frame-Options`, `X-Content-Type-Options`, `X-XSS-Protection` visible |
| Unauthorized API call | Call `/api/chat` in a new terminal without being logged in | `401 Unauthorized` response |
| No secrets in page source | View page source and search for your API key value | Key is not present anywhere in the source |
| `.gitignore` covers env files | Run `git status` — `.env.local` should not appear as untracked | File is ignored |

If any test fails, paste the description into the Claude Code terminal and it will diagnose and fix the specific issue.

---

## How Real Engineering Teams Think About Security

Here's a perspective worth carrying into every project you build.

Security is not a feature you add at the end. It's a property of the system — either present from the start or absent throughout.

The best engineering teams treat a security scan like a compiler check. You don't ship code that doesn't compile. You also don't ship code that hasn't been scanned. It's not an optional extra review — it's a gate in the process.

What the `security-fix` skill does is give you that gate without requiring a security engineering background. The checks it runs are the same checks a security engineer would run in a code review. The difference is it takes one prompt instead of several hours.

One thing worth internalizing: **`NEXT_PUBLIC_` means "ship to every browser."** That prefix is for things you genuinely want every user's browser to have — your public Supabase URL, for instance. Anything that must stay server-side — API keys, service role credentials, signing secrets — must never carry that prefix. This is not a rule that changes with context. It is always true.

---

## What You Built

Your application now has:

- **No hardcoded secrets** — every credential is read from environment variables
- **Protected API routes** — unauthenticated requests are rejected before reaching any business logic
- **Safe error handling** — internal error details stay on the server; clients receive only a generic message
- **Security headers** — the browser is instructed to block clickjacking, MIME sniffing, and reflected XSS
- **A clean `.gitignore`** — environment files cannot be accidentally committed to version control

---

## Troubleshooting — Let Claude Fix It

If a security fix breaks something or a check didn't apply correctly, paste the issue into the Claude Code terminal.

---

**Security headers are not appearing in responses**

```
The security headers (X-Frame-Options, X-Content-Type-Options, etc.) are not
appearing in response headers. Check the headers() export in next.config.js and
confirm the config is structured correctly. Fix whatever is preventing the headers
from being applied.
```

---

**An API route is still accessible without authentication**

```
The route [paste the route path] is returning a 200 response when called without
an auth token. The security-fix skill should have added a getUser() check at the
top of the handler. Find out why the check is missing or not running and add it
correctly.
```

---

**A valid feature broke after the auth check was added**

```
After the security-fix skill added an auth check to [route path], this feature
stopped working: [describe the feature]. The error is: [paste the error]. The auth
check should not block this flow — diagnose why it is and fix it without removing
the check.
```

---

**`.env.local` is still showing as untracked in git**

```
Running git status shows .env.local as an untracked file even after the security-fix
skill ran. Check .gitignore and add the correct entries so all env files are ignored.
```

---

**The skill reported a Manual Action Required item you're not sure how to handle**

```
The security-fix skill flagged this as a manual action required: [paste the item].
Explain what the issue is, why it could not be auto-fixed, and give me the exact
steps or code changes needed to resolve it.
```

---

## What's Next

The app is working and secure.

But it's still only running on your machine.

In the next lesson, you deploy it — taking everything from `localhost:3000` to a live URL anyone can open, with a production database, environment variables configured correctly, and automatic deployments wired up from GitHub.

---

## Claude Concepts Covered in This Lesson

| Concept | Where it appeared | Learn more |
|---------|-------------------|------------|
| **Skills for automated security scanning** | **Step 2 — Run the Security Skill** — "Use `@skills/security-fix/SKILL.md` to scan the codebase and fix all security issues automatically, in one pass." | [Skills guide →](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf) |
| **`NEXT_PUBLIC_` prefix rule** | **How Real Engineering Teams Think About Security** — "`NEXT_PUBLIC_` means 'ship to every browser.' Anything that must stay server-side must never carry that prefix. This is not a rule that changes with context. It is always true." | [Claude Code docs →](https://docs.anthropic.com/en/docs/claude-code) |
| **Claude Code for iterative debugging** | **Step 3 — Verify the Fixes** — "If any test fails, paste the description into the Claude Code terminal and it will diagnose and fix the specific issue." | [Claude Code →](https://docs.anthropic.com/en/docs/claude-code) |

---

[← Back to Lab 3 Overview](../readme.md)

**Lesson 1** | [Lesson 2 →](../02-deployment/readme.md)
