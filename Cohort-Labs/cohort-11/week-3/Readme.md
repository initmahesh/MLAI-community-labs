# Week 3: Prove Your App Actually Works

Welcome to Week 3 of the AI PM Certification.

Your agent has been ingesting contracts and answering questions since Week 2 — but "it runs" and "it's good" are two different claims. This week you build the tooling to back up the second claim with evidence: a feedback form that captures what real users think, a code reviewer that checks how the app was built, and a scoring system that proves — with real numbers, not guesswork — which AI model actually gives better answers.

Each lab builds directly on the last. Work through them in order.

---

## The Labs

### [Lab 3.1 — Connect Your App to Supabase Using Claude's Connectors](./3.1-connectors-feedback-form/Readme.md)

Your app works, but you have no way to know if users are satisfied — and the moment you refresh, your chat is gone with nowhere to keep feedback. You'll build a feedback form and, along the way, learn what a **connector** is by using one to wire your app to a real **Supabase** database, so chats and feedback are saved instead of disappearing.

---

### [Lab 3.2 — Review Your App Using Claude's Sub Agent](./3.2-code-review-subagent/Readme.md)

Your app now collects real feedback, but a working demo and well-built code are two different things — nobody's actually looked at the code underneath and asked whether it's handling errors properly, whether anything's a security risk, or whether it's more complicated than it needs to be. You'll install the **Superpowers** plugin and, along the way, learn what a **subagent** is by turning its code-review skill into a standing `code-reviewer` agent you can point at your own project any time.

---

### [Lab 3.3 — Evaluate Your Agent's Answers with Azure AI Foundry](./3.3-microsoft-foundry-eval-plugin/Readme.md)

A feedback form tells you how people *feel* about an answer — not whether it was actually correct. This lab closes that gap. You'll add a **Download Responses** feature to your app that exports real question-and-answer pairs from your live agent, reformat them into a dataset **Azure AI Foundry** can read, and run a structured evaluation that scores every answer across five dimensions: relevance, groundedness, coherence, similarity, and fluency. Then you'll re-run the same evaluation with a stronger judge model (GPT-5 instead of GPT-4o) and compare the two reports, to see how much the judge you pick shapes the score. The result is a scored report — not guesswork — that tells you exactly where your agent is strong and where it falls short.

---
