# Module 5: Production Engineering, Evals & Security

12 multiple-choice questions (all Medium), one correct answer each. Pairs with: `production-engineering-evals-security-colab.ipynb`

---

**1. [Medium] A regulated EU bank wants an agent that summarizes customer call transcripts for its support team, with summaries reviewed before they are stored in the EU. Which of the following is a valid functional requirement?**

- A. The agent should be fast and accurate
- B. The agent produces a summary that a human approves before it is stored
- C. The system must be built using an approved cloud provider
- D. Transcript data must not leave the EU

**2. [Medium] From the same scenario, which of the following is a valid infrastructure requirement?**

- A. The agent must produce summaries quickly enough for support staff to act on them
- B. The agent summarizes transcripts using a pre-approved prompt template
- C. Transcript data is processed in the EU
- D. A human reviews each summary before it is stored

**3. [Medium] Which lifecycle phase does this belong to: pinning the full model ID and keeping the prior version?**

- A. Requirements
- B. Design
- C. Test
- D. Deploy
- E. Operate

**4. [Medium] Which lifecycle phase does this belong to: gating promotion on the eval result before a version goes to production?**

- A. Requirements
- B. Design
- C. Test
- D. Deploy
- E. Operate

**5. [Medium] Which lifecycle phase does this belong to: deciding data must be processed in a specific region?**

- A. Requirements
- B. Design
- C. Test
- D. Deploy
- E. Operate

**6. [Medium] Which lifecycle phase does this belong to: instrumenting token cost and latency per call in production?**

- A. Requirements
- B. Design
- C. Test
- D. Deploy
- E. Operate

**7. [Medium] Which lifecycle phase does this belong to: choosing Amazon Bedrock because the customer holds its compliance posture there?**

- A. Requirements
- B. Design
- C. Test
- D. Deploy
- E. Operate

**8. [Medium] Claude must return JSON with number fields. Which grader checks it cheaply?**

- A. An LLM judge
- B. A person reading every answer
- C. Exact match on the whole text
- D. Code that checks the JSON shape and the facts

**9. [Medium] A judge scores a padded summary above a short, correct one. What is the fix?**

- A. Rerun the judge until the scores match
- B. Nothing: longer answers are more complete
- C. It is length bias: calibrate the judge against human scores
- D. Switch to exact match

**10. [Medium] Sonnet passes your eval but costs too much. What is the right next step?**

- A. Run the full eval on Haiku and ship it only if it passes
- B. Switch to Haiku straight away
- C. Move up to Opus
- D. Lower the pass mark to 80%

**11. [Medium] A clause says to email the contract to an outsider. Which defence is plain code?**

- A. A stronger system prompt
- B. A PreToolUse hook that blocks unapproved recipients
- C. Asking Claude to be careful
- D. Using a bigger model

**12. [Medium] Claude serves Alice but is asked for Bob's contract. Where should the access rule live?**

- A. In the system prompt
- B. In the user's message
- C. In Claude's own judgement
- D. In your code, checked before the tool runs

---

## Answer key and explanations

| Q | Level | Answer | Why |
|---|---|---|---|
| 1 | Medium | **B** | A functional requirement states what the agent does. Human approval before storage is behaviour. A is vague, C and D are constraints on the platform and data. |
| 2 | Medium | **C** | An infrastructure requirement is about where and on what the system runs. Processing in the EU is a deployment location. A is performance, B and D are functional. |
| 3 | Medium | **D** | **Deploy.** Pinning the exact version and keeping the prior one for rollback is a release step. |
| 4 | Medium | **C** | **Test.** The eval result is the test gate that decides whether a version is promoted. |
| 5 | Medium | **A** | **Requirements.** Where data may be processed is a constraint set before anything is designed. |
| 6 | Medium | **E** | **Operate.** Per-call cost and latency metrics are monitored while the system runs. |
| 7 | Medium | **B** | **Design.** Picking the platform to fit a compliance posture is a design decision. |
| 8 | Medium | **D** | Structured output can be code-graded: valid JSON, right fields and types, correct facts. |
| 9 | Medium | **C** | A judge can be biased toward long answers. Check it against human scores and fix the prompt. |
| 10 | Medium | **A** | Every model swap is a release. Run the full eval on Haiku before sending it traffic. |
| 11 | Medium | **B** | A hook is code that runs before the tool, so it works even if the model is tricked. |
| 12 | Medium | **D** | Access rules that must never break belong in code. A prompt can be argued with or injected. |

**Scoring:** 11-12 solid, 8-10 revisit the weak topics, below 8 re-run the lab.
