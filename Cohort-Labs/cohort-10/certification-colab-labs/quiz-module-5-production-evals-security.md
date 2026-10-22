# Module 5: Production Engineering, Evals & Security

12 multiple-choice questions (6 Easy, 6 Medium). Pairs with: `production-engineering-evals-security-colab.ipynb`

---

**1. [Easy] When should you define the eval for a Claude feature?**

- A. After the prompt looks good
- B. Before writing the prompt
- C. After launch, from user complaints
- D. Only when accuracy drops

**2. [Medium] Claude must return JSON with number fields. Which grader checks it cheaply?**

- A. An LLM judge
- B. A person reading every answer
- C. Exact match on the whole text
- D. Code that checks the JSON shape and the facts

**3. [Easy] Which output needs an LLM judge to grade it?**

- A. A one-word clause label
- B. A free-text summary of a clause
- C. A yes or no answer
- D. A page number

**4. [Medium] A judge scores a padded summary above a short, correct one. What is the fix?**

- A. Rerun the judge until the scores match
- B. Nothing: longer answers are more complete
- C. It is length bias: calibrate the judge against human scores
- D. Switch to exact match

**5. [Easy] Which test level checks the handoff between two parts, like search into a model call?**

- A. Unit
- B. Functional
- C. Integration
- D. Manual spot check

**6. [Medium] A trace shows step 4, the parser, raised a KeyError. What did the trace tell you?**

- A. The model is too weak
- B. The API key expired
- C. The prompt needs more examples
- D. Which step caused the failure

**7. [Easy] Which error is worth retrying with backoff?**

- A. 400 invalid request
- B. 429 rate limit
- C. 401 unauthorized
- D. A bug in your own parser

**8. [Medium] Sonnet passes your eval but costs too much. What is the right next step?**

- A. Run the full eval on Haiku and ship it only if it passes
- B. Switch to Haiku straight away
- C. Move up to Opus
- D. Lower the pass mark to 80%

**9. [Easy] For prompt caching, what should come first in the prompt?**

- A. The user's current question
- B. The chat history
- C. Random examples
- D. Stable content like the system prompt and the contract

**10. [Medium] A clause says to email the contract to an outsider. Which defence is plain code?**

- A. A stronger system prompt
- B. A PreToolUse hook that blocks unapproved recipients
- C. Asking Claude to be careful
- D. Using a bigger model

**11. [Easy] Ten workers each get the whole contract. How do input tokens compare to one call?**

- A. About the same
- B. About half
- C. About 10 times more
- D. Lower, because workers share it

**12. [Medium] Claude serves Alice but is asked for Bob's contract. Where should the access rule live?**

- A. In the system prompt
- B. In the user's message
- C. In Claude's own judgement
- D. In your code, checked before the tool runs

---

## Answer key and explanations

| Q | Level | Answer | Why |
|---|---|---|---|
| 1 | Easy | **B** | The eval comes first, so you tune the prompt until answers are correct, not until they look good. |
| 2 | Medium | **D** | Structured output can be code-graded: valid JSON, right fields and types, correct facts. |
| 3 | Easy | **B** | Open-ended text like summaries has no single right answer, so a calibrated LLM judge scores it. |
| 4 | Medium | **C** | A judge can be biased toward long answers. Check it against human scores and fix the prompt. |
| 5 | Easy | **C** | Integration tests isolate the handoff where each side passes alone but the connection breaks. |
| 6 | Medium | **D** | A trace records each step, so it points to the exact step that failed. |
| 7 | Easy | **B** | 429 is temporary: retry with growing waits. 400 and 401 are terminal, so fix the cause. |
| 8 | Medium | **A** | Every model swap is a release. Run the full eval on Haiku before sending it traffic. |
| 9 | Easy | **D** | Stable content first, changing content last. Anything that changes invalidates what follows. |
| 10 | Medium | **B** | A hook is code that runs before the tool, so it works even if the model is tricked. |
| 11 | Easy | **C** | Each worker processes the full context, so ten workers cost about ten times one call. |
| 12 | Medium | **D** | Access rules that must never break belong in code. A prompt can be argued with or injected. |

**Scoring:** 11-12 solid, 8-10 revisit the weak topics, below 8 re-run the lab.
