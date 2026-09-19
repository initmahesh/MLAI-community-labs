# Week 3: Prove Your App Actually Works

Welcome to Week 3 of the AI PM Certification.

Your agent has been ingesting contracts and answering questions since Week 2 — but "it runs" and "it's good" are two different claims. This week you build the tooling to back up the second claim with evidence: a code reviewer that checks how the app was built, a feedback form that captures what real users think, and a scoring system that proves — with real numbers, not guesswork — which AI model actually gives better answers.

Each lab builds directly on the last. Work through them in order.

---

## The Labs

### [Lab 3.1.1 — Give Your Contract Review App a Code Reviewer](./3.1-subagent-connectors/3.1.1-code-review-subagent/Readme.md)

A working demo and well-built code are two different things — nobody's actually looked at the code underneath and asked whether it's handling errors properly, whether anything's a security risk, or whether it's more complicated than it needs to be. You'll install the **Superpowers** plugin and, along the way, learn what a **subagent** is by turning its code-review skill into a standing `code-reviewer` agent you can point at your own project any time.

---

### [Lab 3.1.2 — Give Your Contract Review App a Feedback Form](./3.1-subagent-connectors/3.1.2-connectors-feedback-form/Readme.md)

Your app's code is in good shape now, but you still have no way to know if it's actually satisfying anyone. You'll build a feedback form and, along the way, learn what a **connector** is by using one to wire that form to a real **Supabase** database, so submissions land somewhere real instead of disappearing.

---

### [Lab 3.2 — Evaluate Your Agent's Answers with Azure AI Foundry](./3.2-microsoft-foundry-eval-plugin/Readme.md)

A feedback form tells you how people *feel* about an answer — not whether it was actually correct. This lab closes that gap. You'll add a Download Responses feature to your app that exports real question-and-answer pairs from your live agent, reformat them into a dataset Azure AI Foundry can read, and run a structured evaluation that scores every answer across five dimensions: **Relevance, Groundedness, Coherence, Similarity, and Fluency**. The result is a scored report — not guesswork — that tells you exactly where your agent is strong and where it falls short.

---
