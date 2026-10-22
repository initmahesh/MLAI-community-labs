# Lab 4 Kahoot: Claude Code, MCP & Integration (Simple)

12 multiple-choice questions for `claude-code-mcp-integration-simple-colab.ipynb`. 6 Easy and 6 Medium, one correct answer each, 20 seconds per question.

---

**1. (Easy) In 3.1, which mode let Claude save the report file with no prompt?**

- A. plan
- B. acceptEdits
- C. dontAsk with only Read allowed
- D. All three modes saved it

**2. (Easy) Which settings layer can never be overridden by project or session flags?**

- A. User global
- B. Project
- C. Enterprise policy
- D. Local session

**3. (Medium) reports.md has a `paths:` line for reports/. When does Claude load it?**

- A. Only when working on matching report files
- B. At the start of every session, for every folder
- C. Only when plan mode is on
- D. Never, rules files need a hook to load

**4. (Easy) A PreToolUse hook script ends with exit code 2. What happens?**

- A. The tool call is allowed
- B. Claude Code restarts
- C. The hook is skipped
- D. The tool call is blocked

**5. (Medium) CLAUDE.md was hidden, yet the hook still blocked the edit. What does this show?**

- A. CLAUDE.md is never read in headless mode
- B. acceptEdits mode blocks every edit
- C. A hook is enforced, a CLAUDE.md rule is only a request
- D. SHA-256 stopped the edit

**6. (Easy) Which transport did the lab's MCP server use on the same machine?**

- A. stdio
- B. Streamable HTTP
- C. SSE
- D. WebSocket

**7. (Medium) clause-auditor has `tools: Read, Grep, Glob`. Why is that safer?**

- A. It runs faster than other subagents
- B. It cannot write files or run commands, even if tricked
- C. It skips CLAUDE.md
- D. It can safely search the internet

**8. (Easy) Which MCP primitive is `contract://main`, the full contract text?**

- A. Tool
- B. Prompt
- C. Hook
- D. Resource

**9. (Medium) You said "review the contract" with no steps pasted, and the skill ran. Why?**

- A. Skills are loaded in every session like CLAUDE.md
- B. A PreToolUse hook started it
- C. Claude matched your request to the skill's description
- D. The --permission-mode flag picked it

**10. (Easy) What does a SHA-256 fingerprint of a file show in the hook test?**

- A. Whether the file changed, even by one character
- B. Who edited the file
- C. How many pages the file has
- D. Whether the file is a PDF

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
| 1 | Easy | **B** | `acceptEdits` allows file writes; `plan` wrote nothing and `dontAsk` with only Read denied the write. |
| 2 | Easy | **C** | Enterprise policy is set by an admin and always has the final word. |
| 3 | Medium | **A** | A rule with `paths:` loads only for matching files; a rule with no `paths:` applies everywhere. |
| 4 | Easy | **D** | Exit code 2 blocks the tool call; exit code 0 allows it. |
| 5 | Medium | **C** | The edit was blocked with the written rule hidden, so the hook enforces it and CLAUDE.md only asks. |
| 6 | Easy | **A** | The server runs on the same machine, so `stdio` is the simplest choice. |
| 7 | Medium | **B** | The `tools:` line limits it to read and search, which limits the damage from hidden instructions. |
| 8 | Easy | **D** | A resource is read-only data addressed by a URI; `find_clause` is the tool and `review` is the prompt. |
| 9 | Medium | **C** | A skill loads only when the request matches its description; CLAUDE.md is always loaded. |
| 10 | Easy | **A** | Any change to a file, even one character, gives a different hash, so matching hashes prove no edit. |
| 11 | Medium | **B** | The config holds only the `${VAR}` reference, so the secret stays out of Git. |
| 12 | Medium | **D** | The lab's check finds the quote on another page and reports a wrong page; a human reviews anything that fails. |

**Scoring:** 11-12 solid · 8-10 revisit the weak topics · below 8 re-run the lab.
