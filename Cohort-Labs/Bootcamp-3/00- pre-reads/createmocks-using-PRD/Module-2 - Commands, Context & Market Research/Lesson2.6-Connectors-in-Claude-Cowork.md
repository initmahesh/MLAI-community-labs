# Lesson 2.6 — Connectors in Claude Cowork: Close the Loop with Slack and Other Tools

---

![images](../Module-3%20-%20Prototype%2C%20Connector%20%26%20Automate/images/banner.png)

---

## Where You Are

In Lessons 2.3 through 2.5 you ran a full chained research workflow — market research, user research, and a PRD — all on the same feature. Each stage took time: searching, synthesising, generating structured output. You had to stay close to the session to know when it was done.

That changes now. This lesson adds connectors to your workflow so Claude can notify you in Slack the moment a task finishes — and you can step away while it runs.

---

## What This Lesson Is About

You've built commands that run research and generate documents. But long tasks still require you to watch them. Connectors fix that.

**Connectors** are the answer. A connector links Claude Cowork to an external tool — Slack, Gmail, Google Calendar, and more — so Claude can take actions in those tools as part of any workflow. The most practical use: send yourself a Slack message when a long-running task finishes.

This lesson shows you exactly how to add the Slack connector and wire it into a prompt, so Claude closes the loop for you automatically.

---

## What Is a Connector?

A connector is an authorized integration between Claude Cowork and an external service. Once connected, Claude can call that service as a tool — the same way it calls web search or the file system.

| Connector | What Claude can do with it |
|-----------|---------------------------|
| **Slack** | Send messages to users or channels |
| **Gmail** | Read emails, draft and send replies |
| **Google Calendar** | Read events, create or update meetings |
| **Browser** | Open URLs, fill forms, click buttons |

Connectors make Claude's output actionable in the tools you already live in. Instead of checking whether a task is done, Claude tells you.

---

## Why This Matters for PMs

As a PM, you'll run Claude Cowork tasks that take time — market research sweeps, competitive analysis, PRD drafts from raw notes. You don't want to sit watching a progress bar.

Connectors let you:
- **Start a task and walk away** — Claude runs it, then pings you in Slack when it's done
- **Keep your workflow in one place** — the output lands in your file system and the confirmation lands in Slack; you never need to check Claude manually
- **Chain tasks with notifications** — run task A, get notified, review the output, trigger task B

The pattern is: **prompt Claude → Claude works → Claude notifies you → you review and act.**

---

## How to Add the Slack Connector

### Step 1 — Open Connections

In Claude Cowork, go to **Connection** → **Manage connector**.

![images](../Module-3%20-%20Prototype%2C%20Connector%20%26%20Automate/images/10.png)

---

### Step 2 — Browse Available Connectors

Click **Browser connector** to see the full list of available integrations.

![images](../Module-3%20-%20Prototype%2C%20Connector%20%26%20Automate/images/11.png)

---

### Step 3 — Find Slack

Search for **Slack** in the connector list.

![images](../Module-3%20-%20Prototype%2C%20Connector%20%26%20Automate/images/12.png)

---

### Step 4 — Authorize the Connection

Click **Connect** and then **Allow** when prompted. Claude Cowork will request permission to access your Slack workspace. Once authorized, the Slack connector is active.

![images](../Module-3%20-%20Prototype%2C%20Connector%20%26%20Automate/images/13.png)

You're connected. Claude can now send Slack messages as part of any workflow you run.

---

## Now Let's Try It

Before wiring connectors into complex workflows, start simple — just send a message to Slack directly from Claude Cowork.

Once your Slack connector is active, type this in Claude Cowork:

```
Send a message on Slack to [Your Name]: "Hello from Claude Cowork — connector is working."
```

> Replace `[Your Name]` with your own Slack display name or a channel (e.g. `#general`).

That's it. Claude will look up the recipient in your connected workspace and send the message. No task, no files, no setup — just a direct Slack message to confirm the connector works end to end.

Once you've confirmed it works, you're ready to attach the connector to any real workflow.

---

## The Connector Pattern — Reuse It Anywhere

The Slack notification pattern is not specific to one task. You can add it to the end of any Claude Cowork prompt:

| Task | Add this at the end |
|------|---------------------|
| Market research sweep | `Once done, send a Slack message to [me]: "Market research complete. File saved to outputs/."` |
| Competitive analysis | `When finished, message [channel] in Slack: "Competitive analysis ready for review."` |
| PRD draft | `After saving the PRD, send a Slack message to [teammate]: "First draft ready — please review."` |
| Data cleanup | `Once the CSV is cleaned, notify [me] on Slack: "Data is ready."` |

One connector. Infinite workflows. You write the task; Claude closes the loop.

---

## Things to Keep in Mind

- **Connectors can lose session state after a restart.** If Slack stops working after you reopen the app, go to Manage Connectors, toggle Slack off, and reconnect.
- **Claude searches by display name.** Make sure the name in your prompt matches the Slack display name exactly, or use a channel name (e.g. `#general`).
- **The app must stay open.** If Claude Desktop closes or your computer sleeps mid-task, the connector action won't fire.
- **Connectors are scoped to your workspace.** Claude can only message users and channels in the Slack workspace you authorized. It cannot message external Slack workspaces.

---

## What You've Learned

### What Connectors Are
Connectors are authorized integrations that let Claude Cowork act inside external tools — Slack, Gmail, Calendar — as part of any workflow. They are called as tools, the same way Claude calls web search or the file system.

### The Core Pattern
> Write your task prompt as normal → add the Slack (or other connector) instruction at the end → Claude runs the task and notifies you when it's done.

You don't need a second prompt or a separate step. The connector fires automatically when Claude reaches that instruction.

### Why It Matters for PM Work
Long-running tasks (research, synthesis, document generation) don't require you to watch them. Set the task, step away, and get notified in the tool you're already in. The output is waiting when you come back.

### The Reusable Pattern
Any Claude Cowork task can close the loop with a notification. The structure is always the same: task instructions first, connector instruction last. Swap the task, keep the pattern.

### How This Connects to the Agentic Loop
The Slack notification is the final step of the five-stage agentic loop: **gather context → plan → confirm → act → report back.** The connector is how Claude reports back to you in your world, not just inside the Claude interface.

---

*Next: [Module 3 — Prototype, Connector & Automate](../Module-3%20-%20Prototype%2C%20Connector%20%26%20Automate/Lesson3.1-Creating-Mocks-and-Deploying.md)*
