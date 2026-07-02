# Module 2 — Commands, Context & Market Research

Build a reusable PM skills library and run a full research-to-PRD workflow — market research, user research, and a structured PRD — all on the same feature.

---

## Lessons

| # | Lesson | What You'll Do |
|---|--------|---------------|
| 2.1 | [Slash Commands in Claude Code](./Lesson2.1-Slash-Commands-in-Claude-Code.md) | Understand how built-in slash commands and skills work |
| 2.2 | [Skills](./Lesson2.2-Skills.md) | Build `/market-research`, `/user-research`, and `/prd` skills |
| 2.3 | [Market Research — Chaining Prompts](./Lesson2.3-Chaining-Research-Prompts.md) | Chain 4 research stages on the Lease Compliance feature, update CLAUDE.md |
| 2.4 | [User Research — Chaining Prompts](./Lesson2.4-User-Research-Chaining.md) | Chain user research on the same feature using market research as context |
| 2.5 | [PRD](./Lesson2.5-PRD.md) | Turn both research outputs into a structured PRD, update CLAUDE.md |
| 2.6 | [Connectors in Claude Cowork](./Lesson2.6-Connectors-in-Claude-Cowork.md) | Connect Claude to Slack and other tools so it notifies you when long-running tasks finish |

---

## The Chain

Every lesson builds on the same feature — Lease Compliance Reporting for LegalGraph:

```
2.3 → market-research-lease-compliance-<date>.md
2.4 → user-research-lease-compliance-<date>.md  (uses 2.3 as context)
2.5 → prd-lease-compliance-<date>.md            (uses 2.3 + 2.4 as context)
2.6 → Slack connector active — tasks notify you when done
```

---

## What You'll Have by the End

- Three reusable skills in your personal library (`/market-research`, `/user-research`, `/prd`)
- Three research output files saved in `outputs/`
- CLAUDE.md updated with market intelligence, user research, PRD decisions, and competitive context
- Slack connector configured — Claude notifies you when any long-running task completes

---

*Previous: [Module 1 — Claude Foundation](../Module-1%20-%20ClaudeFoundation/README.md)*
*Next: [Module 3 — Prototype, Connector & Automate](../Module-3%20-%20Prototype%2C%20Connector%20%26%20Automate/README.md)*
