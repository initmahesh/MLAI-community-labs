# Week 3: Prove Your App Actually Works

Welcome to Week 3 of the AI PM Certification.

Your agent has been ingesting contracts and answering questions since Week 2 — but "it runs" and "it's good" are two different claims. This week you build the tooling to back up the second claim with evidence: a code reviewer that checks how the app was built, a feedback form that captures what real users think, and a scoring system that proves — with real numbers, not guesswork — which AI model actually gives better answers.

Each lab builds directly on the last. Work through them in order.

---

## The Labs

### [Lab 3.1 — Give Your Contract Review App a Code Reviewer](./3.1-code-review-plugin-agent/Readme.md)

Your app works end to end — upload, ingest, ask, answer — but nobody's actually looked at the code underneath and asked whether it's handling errors properly, whether anything's a security risk, or whether it's more complicated than it needs to be. You'll install the **Superpowers** plugin, turn its code-review skill into a standing `code-reviewer` agent, and point it at your own project to surface real issues. Then you'll add a feedback form wired to a real **Supabase** database, so users can start telling you how the app is doing.

---

### [Lab 3.2 — Evaluate Your Agent's Answers with Azure AI Foundry](./3.2-microsoft-foundry-eval-plugin/Readme.md)

A feedback form tells you how people *feel* about an answer — not whether it was actually correct. This lab closes that gap. You'll add a Download Responses feature to your app that exports real question-and-answer pairs from your live agent, reformat them into a dataset Azure AI Foundry can read, and run a structured evaluation that scores every answer across five dimensions: **Relevance, Groundedness, Coherence, Similarity, and Fluency**. The result is a scored report — not guesswork — that tells you exactly where your agent is strong and where it falls short.

---

> If you get stuck in any lab, each one has troubleshooting guidance built in. Read the error carefully — most issues in these labs have a one-line fix.
