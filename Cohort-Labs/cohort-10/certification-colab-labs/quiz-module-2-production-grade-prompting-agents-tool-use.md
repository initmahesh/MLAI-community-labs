# Module 2 Quiz — Production-Grade Prompting, Agents & Tool Use

25 multiple-choice questions. Pick one answer per question, then check the answer key at the bottom.
Pairs with: `production-grade-prompting-agents-tool-use-colab.ipynb`

---

**1. A ticket classifier returns "Billing", "billing", or "This looks like a billing issue" on different runs, and the router breaks. What is the prompt missing, and what is the right fix?**

- A. A longer description of each category
- B. An output constraint: exactly one label from a fixed set, nothing else, ideally with few-shot examples showing the format
- C. Extended thinking at high effort
- D. A higher `max_tokens` value

**2. What do structured outputs (`output_config.format` with a JSON schema) give you that a prompt instruction does not?**

- A. A guarantee that the response is always correct
- B. Lower latency on the first request with any new schema
- C. Compatibility with message prefilling
- D. Constrained decoding: the API only allows tokens that keep the output valid against your schema (you still check `stop_reason` for refusals and truncation)

**3. Extended thinking is on and you use tools. What must you do with the `thinking` blocks Claude returns?**

- A. Send them back to the API exactly as received (signature intact), including redacted ones
- B. Strip them out of history to save context
- C. Summarize them before the next turn
- D. Convert them into text blocks

**4. In a tool-use loop, which rule about `tool_use` and `tool_result` blocks is correct?**

- A. Claude executes your tools and returns the results to you
- B. Results can be sent in any later turn as long as the order is preserved
- C. `tool_result` blocks go in the assistant role
- D. Every `tool_use` block must be answered by a `tool_result` with the same id in the immediately following user turn

**5. Claude keeps calling `search_docs` when the answer is already in context. Both tool descriptions say "Use this to find information." What is the most targeted fix?**

- A. Add an exclusion condition to each description naming when *not* to call it
- B. Rename the tools
- C. Mark every parameter as required
- D. Add more tools so Claude has more options

**6. When handling a streamed response, which approach is correct?**

- A. Parse a `tool_use` block's input as soon as the first delta arrives
- B. Act on a block only after `content_block_stop`, append the turn only after `message_stop`, and discard the partial turn if the stream is interrupted
- C. Append the assistant turn to history whenever the read loop ends
- D. Keep partial blocks in history so the next request can continue them

**7. An agent selects the right tool for the first four turns, then starts picking wrong tools and giving incomplete answers at turn 8. Tool outputs in production are 3–5× longer than in testing. What is the most likely cause?**

- A. A bug in the tool schemas
- B. The model's quality degrades after eight turns
- C. The context window (budget) is filling with accumulated tool results, crowding out instructions
- D. Streaming was left on

**8. You write a manual compaction step. Which summarizer instruction best preserves task continuity?**

- A. "Summarize the conversation so far."
- B. "Summarize the conversation, preserving all file paths modified, all decisions made, and any errors encountered and how they were resolved."
- C. "Shorten the conversation as much as possible."
- D. "Keep only the last three messages."

**9. When is a workflow the better choice than an agent?**

- A. When you can enumerate the exact steps in code, error cost is real, and step-level guardrails matter
- B. When you can specify the goal and tools but not the path
- C. When user inputs vary unpredictably
- D. When the task needs creative sequencing of tools

**10. Where should a human-in-the-loop checkpoint go?**

- A. After every tool call, regardless of risk
- B. Only after the agent finishes
- C. Before any tool that can take an irreversible action (write, delete, send) — decided by asking "what is the worst outcome if this runs unchecked?"
- D. Nowhere, if the loop has an iteration cap

**11. A workload handles PHI and requires Zero Data Retention. Which wiring path is ruled out?**

- A. A raw Messages API loop on a covered configuration
- B. Claude Managed Agents, because sessions are stateful and stored server-side
- C. The Agent SDK on a covered configuration
- D. All three are ruled out

**12. A support agent helps the same user across daily check-ins for two weeks, and each session starts where the last ended. Which memory scope fits?**

- A. In-context only, by keeping one ever-growing messages array
- B. Stateless, because each session is a new API call
- C. External storage (or summarized memory) read back at session start
- D. A larger context window

**13. What is true about Skills?**

- A. Their full instructions load into every session, like CLAUDE.md
- B. They only work in Claude Code, never on the API
- C. Subagents always inherit the parent's skills
- D. Only the name and description load up front; the body loads when a request matches the description, and subagents do not inherit them automatically

**14. How many visual tokens does a 1,000 × 1,000 pixel image cost under the module's formula (each 28×28 patch is one token, before any model-specific downscaling)?**

- A. About 1,000
- B. About 36
- C. About 1,296
- D. About 10,000

**15. A nightly job classifies 5,000 records and hits rate limits even after splitting the list into chunks and looping over the synchronous API. What is the fix, and how do you match results to inputs?**

- A. Use the Message Batches API; results come back in arbitrary order, so match them with `custom_id`
- B. Use smaller chunks; match results by position
- C. Use streaming; results arrive in order
- D. Use extended thinking; it avoids rate limits

**16. A customer support agent assists the same user across daily check-ins over two weeks. Each session starts where the previous one left off. Which memory scope fits?**

- A. In-context memory: all state lives in the active conversation
- B. External storage: write state to a database at session end, then read it back at session start
- C. No persistent memory (stateless): each session starts fresh
- D. Vector database retrieval at every turn, with no state stored between sessions

**17. A document formatter receives a file, applies a transformation, returns the output, and terminates. Each job is fully independent. Which memory scope fits?**

- A. In-context memory: all state lives in the active conversation
- B. External storage: write state to a database at session end, then read it back at session start
- C. No persistent memory (stateless): each session starts fresh
- D. Vector database retrieval at every turn, with no state stored between sessions

**18. A coding assistant works with a developer across a multi-hour session. The session will not continue after it ends. Which memory scope fits?**

- A. In-context memory: all state lives in the active conversation
- B. External storage: write state to a database at session end, then read it back at session start
- C. No persistent memory (stateless): each session starts fresh
- D. Vector database retrieval at every turn, with no state stored between sessions

**19. A reference product diagram is used in every request your pipeline makes. Which encoding method fits?**

- A. Message Batches API: submit all requests in one batch call, poll for completion
- B. Files API: upload once, reference `file_id` in each request
- C. Inline base64: encode and include directly in the message block
- D. Paste the file contents as plain text in the prompt

**20. A one-off screenshot of a UI bug is submitted by a support engineer in a single request. Which encoding method fits?**

- A. Message Batches API: submit all requests in one batch call, poll for completion
- B. Files API: upload once, reference `file_id` in each request
- C. Inline base64: encode and include directly in the message block
- D. Paste the file contents as plain text in the prompt

**21. A job classifies 5,000 customer feedback responses. Which encoding method fits?**

- A. Message Batches API: submit all requests in one batch call, poll for completion
- B. Files API: upload once, reference `file_id` in each request
- C. Inline base64: encode and include directly in the message block
- D. Paste the file contents as plain text in the prompt

**22. Classify 50,000 support tickets into three labels overnight. What is the correct extended-thinking decision?**

- A. Never do this
- B. Leave it off
- C. Enable it, budget for the planning step
- D. Enable it at maximum budget on every call

**23. Plan a multi-step refactor where each step depends on the previous one. What is the correct extended-thinking decision?**

- A. Never do this
- B. Leave it off
- C. Enable it, budget for the planning step
- D. Enable it at maximum budget on every call

**24. Strip the thinking block out of conversation history to save context before the next tool call. What is the correct extended-thinking decision?**

- A. Never do this
- B. Leave it off
- C. Enable it, budget for the planning step
- D. Enable it at maximum budget on every call

**25. The session trace below shows an agent calling a tool, receiving a result, and then failing with an API validation error on the next request. The schema is valid, the tool description is specific, and the tool result content is correct. (Convention: `tool_result` blocks are always sent in the `user` role, even though your application generates the content. The role marks who is sending the message to Claude, not who authored it.) Which targeted fix is right?**

```
Turn 1: User:
  [text]: "What is the current balance for account A-4471?"

Turn 2: Assistant:
  [text]: "I'll look that up."
  [tool_use]: id="toolu_01", name="get_account_balance",
              input={"account_id": "A-4471"}

Turn 3: User (tool result):
  [tool_result]: tool_use_id="toolu_02", content="Balance: $1,240.18"

Turn 4: API response:
  Error: invalid_request_error
  "tool_result block references unknown tool_use_id"
```

- A. Update the description on `get_account_balance` to add an exclusion condition
- B. Correct the `tool_use_id` on the `tool_result` block so it matches the id issued in the assistant turn
- C. Add a `required` array to the tool's `input_schema` so `account_id` cannot be omitted
- D. Change the `tool_result` block to the `assistant` role

---

<details>
<summary><b>Answer key and explanations</b></summary>

| Q | Answer | Why |
|---|---|---|
| 1 | **B** | Wrong *shape* means a missing output constraint. Rewording or adding description doesn't fix a shape problem. |
| 2 | **D** | Schemas are enforced at generation time. First call on a new schema is slower (grammar compile, cached 24 h), and `refusal` / `max_tokens` can still yield non-matching output. It doesn't combine with prefilling. |
| 3 | **A** | Signed thinking blocks must be returned unchanged on the next turn; editing, summarizing or dropping them breaks the request. |
| 4 | **D** | Your code runs the tools. Results must be in the very next user turn with matching ids. |
| 5 | **A** | The description decides routing; an exclusion condition gives Claude a decision boundary. If descriptions can't be separated, merge the tools. |
| 6 | **B** | A stream ending is not a message completing. Tool input is partial JSON until the block closes; commit only after `message_stop`. |
| 7 | **C** | Overflow looks like a tool-selection failure. Check the window first; prune spent outputs and compact before the ceiling. |
| 8 | **B** | Compaction quality equals summarizer-prompt quality. Generic summaries drop task-critical state. |
| 9 | **A** | Workflows fit enumerable steps and real error cost. Agents fit goal-plus-tools tasks whose path can't be listed. |
| 10 | **C** | The worst-case-outcome question places the gate. An iteration cap doesn't stop a single bad irreversible call. |
| 11 | **B** | Managed Agents sessions are stored server-side and aren't currently eligible for ZDR or a HIPAA BAA. |
| 12 | **C** | State must survive across sessions. Holding everything in-context inflates cost until the window fills. |
| 13 | **D** | Skills are a low-cost on-demand pattern; subagents start clean and need skills listed explicitly. |
| 14 | **C** | ⌈1000/28⌉ × ⌈1000/28⌉ = 36 × 36 = 1,296. Each model also has a max resolution; larger images are downscaled first. |
| 15 | **A** | Looping over the sync API is not batching. Batch results are unordered, so join by `custom_id`. |
| 16 | **B** | State must survive across sessions that are days apart, so write it to external storage at session end and read it back at the next start. |
| 17 | **C** | Each job is independent and nothing carries over, so no persistent memory is needed. Stateless is the simplest and cheapest scope. |
| 18 | **A** | The session ends and never resumes, so the active conversation is enough. External storage would add cost and complexity for no benefit. |
| 19 | **B** | The same file is sent in every request, so upload it once and reference the `file_id`. Re-encoding inline base64 each time bloats every payload. |
| 20 | **C** | A single one-off image doesn't justify an upload step, so inline base64 is simplest. The Files API adds a round trip for no reuse benefit. |
| 21 | **A** | Thousands of independent, non-urgent requests fit the Message Batches API: one batch call, then poll. Looping synchronous calls hits rate limits and costs more. |
| 22 | **B** | Simple three-label classification at volume gains little from reasoning, and thinking tokens would multiply cost and latency across 50,000 calls. Leave it off. |
| 23 | **C** | Dependent steps where each builds on the last benefit from reasoning, so enable it and budget for the planning step. |
| 24 | **A** | Signed thinking blocks must be returned unchanged. Stripping them to save context breaks the request, so never do it. |
| 25 | **B** | The `tool_result` references `toolu_02`, but the assistant issued `toolu_01`. Every `tool_result` must carry the `tool_use_id` of the `tool_use` it answers. The schema and description are not at fault. |

**Scoring:** 21–25 solid · 16–20 revisit the weak topics · below 16 re-run the lab.

*These are original practice questions written from the module content, not the course's own checkpoint items.*

</details>
