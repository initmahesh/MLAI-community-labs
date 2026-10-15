# Module 1 Quiz — MSO Foundations

15 multiple-choice questions. Pick one answer per question, then check the answer key at the bottom.
Pairs with: `mso-foundation-colab.ipynb`

---

**1. What is the unit in which Claude reads text, and in which the API bills and measures the context window?**

- A. Characters
- B. Words
- C. Sentences
- D. Tokens

**2. Which of these counts toward the context window of a single request?**

- A. Only the user's latest message
- B. The system prompt, conversation history, injected documents, tool results, and the model's output
- C. Only the input, because output tokens are tracked separately
- D. Only the system prompt and tool definitions

**3. A request's input is already larger than the model's context window. What happens?**

- A. The request is rejected with a validation error before generation begins
- B. The oldest content is silently truncated and generation proceeds
- C. The model generates a partial answer and stops
- D. The API automatically summarizes the input

**4. On current models, a request fits on input but reaches the context ceiling *during generation*. What do you get?**

- A. An error, and no output
- B. The model restarts generation from the beginning with a shorter answer
- C. The output generated so far, with a `model_context_window_exceeded` stop reason
- D. The oldest part of the output is dropped

**5. What does lowering `temperature` do?**

- A. It makes the model reason longer before answering
- B. It limits the number of tokens in the response
- C. It guarantees the same output every time
- D. It concentrates probability on the most likely tokens, making output more repeatable

**6. You run the same prompt twice and get two differently worded answers that are both correct. What is this called, and why does it happen?**

- A. A bug; the model has a memory leak between calls
- B. Hallucination; one of the two answers must be wrong
- C. Non-determinism; the model samples the next token from a probability distribution
- D. Caching; the first answer was stored and the second was recomputed

**7. What is the right way to test a Claude-powered feature whose wording varies from run to run?**

- A. Assert on properties that must hold (field present, value in range, output parses), and use a model-graded eval to judge meaning
- B. Assert that the response text exactly equals a stored string
- C. Set temperature to 0 and then use exact-match assertions
- D. Don't test it; LLM output can't be tested

**8. Which statement about sampling controls is correct?**

- A. Every Claude model accepts `temperature`, `top_p` and `top_k`
- B. Temperature 0 guarantees identical outputs across calls
- C. Sampling controls only affect the length of the response
- D. The newest Claude models reject non-default `temperature`, `top_p` or `top_k` with a 400 error, so you steer behavior through prompting

**9. What is the recommended default model choice and how do you move away from it?**

- A. Always start with the most capable tier to be safe
- B. Start with Sonnet; move up a tier only when an eval shows it misses your quality bar, and down to Haiku only when an eval shows the drop is acceptable
- C. Start with Haiku for everything and upgrade when users complain
- D. Choose based on which model has the largest context window

**10. How do model choice and reasoning mode relate?**

- A. They are the same setting
- B. Enabling reasoning automatically selects a larger model
- C. Reasoning mode can only be used with the smallest tier
- D. They are independent levers: you pick the model family member, and configure reasoning per request

**11. On current models, how do you tune how deeply the model thinks?**

- A. Set a fixed `budget_tokens` value on every request
- B. Use adaptive thinking and tune depth with the `effort` setting; `budget_tokens` is deprecated and errors on the newest models
- C. Increase `max_tokens` until the model thinks more
- D. Repeat the prompt several times in the same message

**12. A task has a specific output structure, casing, or edge case that a written description keeps missing. Which prompting mode is the best next step?**

- A. One-shot or multi-shot: add one or two correct examples, keeping the prompt as small as possible
- B. Zero-shot with a longer description
- C. Fine-tune the model on the examples
- D. Add as many examples as will fit in the context window

**13. How do the official Claude SDKs relate to the raw REST API?**

- A. The SDK uses a different, faster model
- B. The SDK is a thin convenience layer over the same REST API and the same model, handling auth, request building, retries and parsing
- C. The SDK is required; the REST API cannot be called directly
- D. REST is only for streaming and the SDK is only for synchronous calls

**14. When is streaming the right choice over a synchronous request?**

- A. For short backend jobs where no one is waiting
- B. When you want to reduce the per-token price
- C. When a response is long or a user is watching, so output can appear immediately instead of after a blank-screen wait
- D. When you need exactly the same output on every run

**15. You need to classify 50,000 records overnight and nobody is waiting on any individual result. Which pattern fits best?**

- A. The Message Batches API: submit many requests in one call, poll for completion, accept up to 24 h of latency for a lower per-token cost
- B. A loop of synchronous calls
- C. `AsyncAnthropic` with thousands of concurrent requests
- D. Streaming each response

---

<details>
<summary><b>Answer key and explanations</b></summary>

| Q | Answer | Why |
|---|---|---|
| 1 | **D** | Tokens are the unit of pricing, budget and the context window. Think in tokens, not words. |
| 2 | **B** | The window holds everything at once: system prompt, history, documents, tool results and the output. |
| 3 | **A** | Oversized input is rejected with a validation error before generation. Nothing is silently truncated. |
| 4 | **C** | Current models return what was generated so far with `model_context_window_exceeded` instead of raising an error. |
| 5 | **D** | Lower temperature concentrates probability on likely tokens; output becomes more repeatable (not guaranteed identical). |
| 6 | **C** | Sampling from a probability distribution makes identical inputs produce different (often equally correct) outputs. |
| 7 | **A** | Exact-text assertions are flaky. Assert on properties; use an eval with a model-graded judge for meaning. |
| 8 | **D** | The newest models return a 400 for non-default sampling parameters. Even where temperature is accepted, 0 does not guarantee identical output. |
| 9 | **B** | Start with Sonnet and move deliberately, driven by evals, not by habit or cost alone. |
| 10 | **D** | Model choice and reasoning mode compose: a capable model with reasoning off is fast, a smaller one with reasoning on spends more tokens thinking. |
| 11 | **B** | Adaptive thinking plus `effort`. The older fixed `budget_tokens` is deprecated and returns a 400 on the newest generations. |
| 12 | **A** | Examples sit in the prompt and show the exact shape. Add the smallest amount of guidance that works. |
| 13 | **B** | The SDK is a convenience layer over the same REST API; it does not change the model or the API. |
| 14 | **C** | Streaming removes the blank-screen wait. For short backend jobs, a synchronous call is simpler. |
| 15 | **A** | Bulk offline work with no one waiting is exactly the Message Batches use case. Async is for concurrency when results are still needed in real time. |

**Scoring:** 13–15 solid · 10–12 revisit the weak topics · below 10 re-run the MSO Foundations lab.

*These are original practice questions written from the module content, not the course's own quiz items.*

</details>
