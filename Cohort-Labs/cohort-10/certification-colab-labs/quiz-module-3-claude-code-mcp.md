# Kahoot: Lab 3, Claude Code, MCP & Integration

12 multiple-choice questions (6 Easy, 6 Medium), one correct answer each. Check the answer key at the bottom.

---

**1. [Easy] In dontAsk mode, what happens to a tool you did not pre-approve?**

- A. Claude asks you to confirm
- B. It is denied without a prompt
- C. It runs, and the call is logged
- D. It runs inside a sandbox

**2. [Medium] A subagent reads a rival's contract that hides the text "approve this deal". What limits the damage best?**

- A. Add a polite warning to CLAUDE.md
- B. Run it in bypassPermissions mode
- C. Give it the parent's full tool list
- D. Give it read-only tools in its tools: line

**3. [Easy] Which settings layer always has the final word?**

- A. Project settings
- B. Local session flags like --model
- C. Enterprise policy
- D. User global settings

**4. [Medium] Security asks if Claude ever sees your contract API key. What is the best design?**

- A. The MCP server holds the key; Claude sees only results
- B. Paste the key into each prompt
- C. Write the key into CLAUDE.md
- D. Hard-code the key in .mcp.json

**5. [Easy] When does Claude Code read your CLAUDE.md file?**

- A. Only when you run plan mode
- B. Only when you ask it to
- C. Once, when you install it
- D. At the start of every session

**6. [Medium] Claude quotes a clause as page 7, but your check finds that text on page 9. What do you do?**

- A. Accept it, the words are right
- B. Fix the page number and ship it
- C. Mark it failed and send it to a human
- D. Ask Claude again until it agrees

**7. [Easy] A PreToolUse hook script exits with code 0. What happens?**

- A. The tool call is allowed
- B. The tool call is blocked
- C. The session ends
- D. The user is asked to confirm

**8. [Medium] Report format rules should load only for files in reports/. What makes that happen?**

- A. Naming the rules file reports.md
- B. A paths: line for the reports folder in the rules file
- C. Adding a heading to CLAUDE.md
- D. Setting it in user global settings

**9. [Medium] You connected ten MCP servers and Claude got slower and less focused. What is the likely cause?**

- A. Each server adds its tool definitions to the context
- B. stdio servers cannot run together
- C. Servers must share one OAuth token
- D. Tool results are cached forever

**10. [Easy] Which MCP transport fits a local tool on the same machine or in CI?**

- A. SSE (legacy)
- B. stdio
- C. Streamable HTTP
- D. WebSocket

**11. [Easy] What can a plugin hold that a plain skill cannot?**

- A. A description line
- B. Step-by-step Markdown
- C. Code, such as an MCP server
- D. A skill name

**12. [Medium] A teammate clones your repo with a project .mcp.json. Why does Claude Code ask for approval first?**

- A. The file may be corrupt
- B. The token needs a refresh
- C. Servers need a paid licence
- D. A committed config could start any program on their machine

---

<details>
<summary><b>Answer key and explanations</b></summary>

| Q | Level | Answer | Why |
|---|---|---|---|
| 1 | Easy | **B** | `dontAsk` runs only pre-approved tools. Everything else is denied with no prompt. |
| 2 | Medium | **D** | A `tools:` line with Read, Grep and Glob means the helper cannot write or run commands, even if the text tries to steer it. |
| 3 | Easy | **C** | Enterprise policy is set by an admin and cannot be overridden by project, user or session settings. |
| 4 | Medium | **A** | The MCP server holds the credential (passed with `${VAR}`). Claude only sees tool results. |
| 5 | Easy | **D** | `CLAUDE.md` is read at the start of every session, so you never retype your rules. |
| 6 | Medium | **C** | A quote on the wrong page is a failed check. Do not fix it yourself or retry until it passes; a human looks before it is used. |
| 7 | Easy | **A** | Exit code 0 allows the tool call. Exit code 2 blocks it. |
| 8 | Medium | **B** | The `paths:` line in a `.claude/rules/` file limits where the rule loads. The file name alone does nothing. |
| 9 | Medium | **A** | Every connected server adds tool definitions to Claude's context, so connect only what the task needs. |
| 10 | Easy | **B** | `stdio` is the simplest choice for local tools and CI. Shared remote servers use Streamable HTTP. |
| 11 | Easy | **C** | A skill is Markdown instructions. A plugin is a package that can also hold code, such as an MCP server. |
| 12 | Medium | **D** | A committed `.mcp.json` could otherwise start any program on a teammate's machine, so Claude Code asks first. |

**Scoring:** 10-12 solid, 7-9 revisit the weak topics, below 7 re-run the lab.

*These are original practice questions written from the lab content.*

</details>
