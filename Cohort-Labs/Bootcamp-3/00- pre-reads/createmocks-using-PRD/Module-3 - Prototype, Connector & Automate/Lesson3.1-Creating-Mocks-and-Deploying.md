# Lesson 3.1 — Creating Mocks with Claude Code and Deploying

---

## Where You Are

Here's the full chain you've built — all on the Lease Compliance Reporting feature:

| Lesson | What you did | Output file |
|--------|-------------|-------------|
| 2.3 | Market research — size, trends, competitors | `outputs/market-research-lease-compliance-<date>.md` |
| 2.4 | User research — personas, workflow, pain points | `outputs/user-research-lease-compliance-<date>.md` |
| 2.5 | PRD — requirements, success metrics, out of scope | `outputs/prd-lease-compliance-<date>.md` |
| **3.1** | **Mock — clickable prototype from the PRD** | `mocks/lease-compliance-prototype.html` |

Now you take the PRD and turn it into a working visual prototype — using Claude Code to generate the UI, and deploying it so your GC and eng lead can click through it before a single line of production code is written.

---

## Why Mocks Before Code

A clickable mock answers questions a PRD can't:
- Does the compliance report layout actually make sense to Rachel (the Compliance Lead)?
- Is the IFRS 16 data extraction output readable for an auditor?
- Where does the user get confused before you've spent eng time building the wrong thing?

Claude Code can generate a working prototype from your PRD in minutes. You validate the UX, get stakeholder sign-off, and hand eng a visual spec — not just a document.

---

## Pre-Flight Checklist

- [ ] Market research from Lesson 2.3 saved at `outputs/market-research-lease-compliance-<date>.md`
- [ ] User research from Lesson 2.4 saved at `outputs/user-research-lease-compliance-<date>.md`
- [ ] PRD from Lesson 2.5 saved at `outputs/prd-lease-compliance-<date>.md`
- [ ] CLAUDE.md loaded with LegalGraph context, market intelligence, user research, and PRD decisions

---

## Step 1 — Generate the Mock from Your PRD

Open Claude Code Desktop in your working project folder and run:

```
@company-context.md
@outputs/prd-lease-compliance-<date>.md

Read all files above. Build a clickable HTML prototype for the Lease Compliance Reporting feature.

Requirements for the prototype:
- Single HTML file (self-contained — CSS and JS inline, no external dependencies)
- Implement these screens based on the P0 requirements in the PRD:
  1. Dashboard — shows active leases with compliance status (IFRS 16 / ASC 842)
  2. Lease Detail — extracted lease terms, amendment history, key dates
  3. Compliance Report — formatted output ready for auditor review
- Use LegalGraph's persona context: Rachel (Compliance Lead) is the primary user — design for her workflow, not a generic user
- Navigation between screens must work (clickable buttons/links)
- Use a clean, professional UI — legal/finance tool aesthetic, not a startup landing page
- Add realistic placeholder data for a mid-market company with 12 active leases

Save the file as: mocks/lease-compliance-prototype.html
```

Claude will generate the full prototype and save it to `mocks/`. This typically takes 2–3 minutes.

![alt text](./images/mock.png)

![alt text](./images/interface.png)


---

## Step 2 — Iterate Until Stakeholder-Ready

Before deploying, run one validation prompt:

```
@mocks/lease-compliance-prototype.html
@outputs/user-research-lease-compliance-<date>.md

Review the prototype against the user research. For each of the top 3 pain points identified in the research:
1. Does the current prototype address it? If yes — how?
2. If no — what's missing?

Then make the changes needed so all 3 pain points are addressed in the UI.
```

This closes the loop between your user research and the actual design — before you put it in front of stakeholders.


![alt text](./images/interface12.png)

---

## Step 3 — Deploy with Tiiny.host

No account. No setup. 30 seconds.

1. Go to **tiiny.host** : https://tiiny.host
![alt text](./images/host.png)
2. Drag and drop `mocks/lease-compliance-prototype.html` — this file is created inside the workspace folder you added to Claude Code. Open your project folder in Finder (Mac) or File Explorer (Windows), navigate to the `mocks/` subfolder, and drag the file directly onto the Tiiny.host page
3. You get a live link instantly — e.g. `https://lease-compliance.tiiny.site`

![alt text](./images/livelink.png)

---

![alt text](./images/livelink122.png)

Share that link with your GC, eng lead, or any stakeholder. They click it, the prototype opens in their browser — no file attachment, no login, no setup on their end.

---

## What Happens Behind the Scenes

![alt text](./images/sop.png)

**1. Claude reads the PRD before generating any UI**
The `@outputs/prd-lease-compliance-<date>.md` loads your full PRD — P0 requirements, personas, success metrics — into context. Claude isn't guessing what screens to build. It's building directly from your documented requirements.

**2. The prototype is a single self-contained file**
No build tools, no npm install, no dependencies. One `.html` file with inline CSS and JS. Anyone can open it in a browser. This is intentional — the goal is fast stakeholder feedback, not production-ready code.

**3. Iteration is just a prompt**
When you ask Claude to fix a screen, it reads the existing file and edits it directly. You're not starting over — you're refining. The file gets better with each prompt.

**4. Deployment takes 5 minutes**
GitHub Pages turns any static file into a public URL instantly. No server, no DevOps, no cost. The link you share with your GC looks and behaves exactly like the file on your machine.

**5. The mock becomes a spec**
Once stakeholders approve the prototype, you hand it to eng as a visual spec. The HTML is inspectable — eng can see exactly what layout, data structure, and interactions are expected. It reduces ambiguity before a line of production code is written.

```
PRD from Lesson 2.5 → @reference in Claude Code
    ↓
Claude generates HTML prototype (single file)
    ↓
Local preview → iterate with targeted prompts
    ↓
Validate against user research pain points
    ↓
Deploy to GitHub Pages → shareable link
    ↓
Stakeholder feedback → one more iteration → eng handoff
```

---

## Things to Keep in Mind

- **The mock is for validation, not production.** Don't let anyone mistake it for real software. Add a "PROTOTYPE — NOT FOR PRODUCTION USE" banner if needed.
- **One file = one source of truth.** Keep everything in `mocks/lease-compliance-prototype.html`. Don't create multiple versions — iterate on the same file and use git to track history.
- **Specific feedback > vague feedback.** When your GC reviews it, ask: "Which screen doesn't match how Rachel actually works?" Not "what do you think?"
- **The user research is your design spec.** If a design decision isn't grounded in a pain point from Lesson 2.4 — question it before building it.

---

## What You've Learned

- **A PRD is the complete spec for a prototype** — Claude generates the mock directly from your `prd-lease-compliance.md`. Every screen, flow, and interaction traces back to a requirement. No blank-page design work needed.
- **Validation closes the research loop** — running the validation prompt against your user research output checks whether the prototype actually solves the pain points you identified in Lesson 2.4. It surfaces gaps before a stakeholder sees them.
- **Mocks get async feedback faster than docs** — sharing a clickable link gets faster, more concrete feedback than sharing a PRD. Stakeholders react to what they can click; they abstract over what they read.
- **Tiiny.host deploys in one step** — drag the HTML file, get a shareable link. No servers, no config. The prototype is live for stakeholder review the moment you deploy it.
- **The full research → PRD → prototype chain** — the prototype is not an isolated artifact. It is the final output of a chain that started with market research in Lesson 2.3. Every screen reflects a user need you identified and a requirement you wrote.

---

*Next: [Lesson 3.2 — CoWork: Creating a Job Assistant and Understanding Connectors](./Lesson3.2-CoWork:%20Creating-a-Job-Assistant-and-Understanding-Connectors.md)*
