# Module 4: Claude Code, MCP & Integration (Simple)

12 multiple-choice questions for `claude-code-mcp-integration-colab.ipynb`. All Medium, one correct answer each. Check the answer key at the bottom.

---

**1. (Medium) A high-volume classification step labels millions of short messages per day. An eval shows Haiku holding the quality bar. Which choice is best?**

- A. Opus, the deciding constraint is reasoning depth on ambiguous messages
- B. Sonnet, the deciding constraint is balancing quality and speed across volume
- C. Haiku, the deciding constraint is cost-at-volume, since the eval confirms the quality bar still holds
- D. Opus, the deciding constraint is consistency across millions of requests

**2. (Medium) A multi-step agent plans a dependent refactor where a wrong early step is expensive. An eval shows Sonnet missing the bar on the hardest cases. Which choice is best?**

- A. Sonnet, the deciding constraint is cost efficiency on a long agent run
- B. Opus, the deciding constraint is quality on hard reasoning where the cost of a wrong answer is high
- C. Haiku, the deciding constraint is speed across many sequential steps
- D. Sonnet, the deciding constraint is latency on dependent steps

**3. (Medium) Mixed traffic: most requests are simple lookups, a few are complex synthesis. Which approach is best?**

- A. Opus for everything, the deciding constraint is guaranteeing quality on the complex requests
- B. Haiku for everything, the deciding constraint is minimizing cost across all traffic
- C. Sonnet for everything, the deciding constraint is a single balanced model for mixed needs
- D. Route: a Sonnet (or Haiku) default with an Opus override on the complex requests, the deciding constraint is that traffic is mixed

For Questions 4 to 7, pick the configuration snippet that best matches the scenario:

```
A  orchestrator_worker(lead=LARGE, workers=SMALL, n=5)    # lever: parallel split
B  single_agent(model=SMALL, batch=True, cache=True)      # lever: Message Batches API (~50% cost reduction) + prompt caching
C  single_agent(model=SMALL, retrieval="fetch_once")      # lever: model choice
D  single_agent(model=SMALL, stream=True)                 # lever: streaming
```

**4. (Medium) A single-fact lookup against a stable reference corpus.**

- A. Snippet A
- B. Snippet B
- C. Snippet C
- D. Snippet D

**5. (Medium) A broad research question that splits into independent parts explored at once.**

- A. Snippet A
- B. Snippet B
- C. Snippet C
- D. Snippet D

**6. (Medium) A user-facing request where the reply should feel instant.**

- A. Snippet A
- B. Snippet B
- C. Snippet C
- D. Snippet D

**7. (Medium) A cost-sensitive, non-urgent batch job.**

- A. Snippet A
- B. Snippet B
- C. Snippet C
- D. Snippet D

**8. (Medium) reports.md has a `paths:` line for reports/. When does Claude load it?**

- A. Only when working on matching report files
- B. At the start of every session, for every folder
- C. Only when plan mode is on
- D. Never, rules files need a hook to load

**9. (Medium) CLAUDE.md was hidden, yet the hook still blocked the edit. What does this show?**

- A. CLAUDE.md is never read in headless mode
- B. acceptEdits mode blocks every edit
- C. A hook is enforced, a CLAUDE.md rule is only a request
- D. SHA-256 stopped the edit

**10. (Medium) You said "review the contract" with no steps pasted, and the skill ran. Why?**

- A. Skills are loaded in every session like CLAUDE.md
- B. A PreToolUse hook started it
- C. Claude matched your request to the skill's description
- D. The --permission-mode flag picked it

**11. (Medium) A server needs an API key. What should `.mcp.json` hold?**

- A. The key itself, if the repo is private
- B. Only a ${API_KEY} reference, never the key
- C. The key, encoded in base64
- D. The key, hidden in a comment

**12. (Medium) Claude quotes a sentence and names page 4, but it is only on page 6. What does the check say?**

- A. Verified, because the quote is real
- B. Not found, a human must check it
- C. Nothing, it only checks JSON format
- D. Wrong page: the text is on page 6, not page 4

---

## Answer key

| Q | Level | Answer | Why |
|---|---|---|---|
| 1 | Medium | **C** | The eval shows Haiku meets the quality bar, so cost at volume decides. |
| 2 | Medium | **B** | Sonnet misses the bar on the hardest cases and a wrong early step is costly, so quality on hard reasoning decides. |
| 3 | Medium | **D** | Mixed traffic is best routed: a cheaper default with an Opus override for the complex requests. |
| 4 | Medium | **C** | A single fact in a stable corpus needs one small-model agent that fetches once. |
| 5 | Medium | **A** | Independent parts explored at once fit an orchestrator with parallel workers. |
| 6 | Medium | **D** | Streaming makes the reply feel instant to the user. |
| 7 | Medium | **B** | Non-urgent, cost-sensitive work fits the Message Batches API (~50% cost reduction) plus prompt caching. |
| 8 | Medium | **A** | A rule with `paths:` loads only for matching files; a rule with no `paths:` applies everywhere. |
| 9 | Medium | **C** | The edit was blocked with the written rule hidden, so the hook enforces it and CLAUDE.md only asks. |
| 10 | Medium | **C** | A skill loads only when the request matches its description; CLAUDE.md is always loaded. |
| 11 | Medium | **B** | The config holds only the `${VAR}` reference, so the secret stays out of Git. |
| 12 | Medium | **D** | The lab's check finds the quote on another page and reports a wrong page; a human reviews anything that fails. |

**Scoring:** 11-12 solid · 8-10 revisit the weak topics · below 8 re-run the lab.
