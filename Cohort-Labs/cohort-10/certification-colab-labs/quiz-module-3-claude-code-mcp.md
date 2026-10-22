# Module 3: Claude Code, MCP & Integration

12 multiple-choice questions (all Medium), one correct answer each. Check the answer key at the bottom.

---

**1. [Medium] A refactor must auto-approve file edits, never run destructive shell commands, and never let the agent read `.env.production`. Which two `settings.json` pieces assemble the correct configuration?**

- Piece A: `{ "permissions": { "defaultMode": "default" } }`
- Piece B: `{ "permissions": { "defaultMode": "bypassPermissions" } }`
- Piece C: `{ "permissions": { "allow": ["Bash(npm run:*)"], "deny": ["Bash(rm:*)", "Bash(git push:*)"] } }`
- Piece D: `{ "permissions": { "deny": ["Read(.env.production)"] } }`
- Piece E: `{ "permissions": { "allow": ["Bash(*)", "Edit(*)"] } }`

Options:

- A. Pieces A and C
- B. Pieces B and D
- C. Pieces C and D
- D. Pieces D and E

**2. [Medium] Your settings let the agent edit files automatically. It now proposes a change to a deployment configuration file that several production services read. Where should a human gate sit for that one action?**

- A. Nowhere: the settings already auto-approve edits, so let it run
- B. A human approves the change before the write executes, because a wrong value is hard to undo and reaches systems outside the file
- C. Add `bypassPermissions` so the agent never pauses
- D. Review the change only after the write, in the next pull request

**3. [Medium] Complete the hook that blocks reads of `.env.production`. Which lifecycle event and command are correct?**

```json
{
  "hooks": {
    "<EVENT>": [
      {
        "matcher": "Read",
        "hooks": [{ "type": "command", "command": "<COMMAND>" }]
      }
    ]
  }
}
```

- A. `PreToolUse`, with a script that exits 2 when the file path contains `.env.production`
- B. `PostToolUse`, with a script that exits 2 when the file path contains `.env.production`
- C. `PreToolUse`, with a script that always exits 0
- D. `UserPromptSubmit`, with a script that exits 2 when the prompt mentions `.env.production`

**4. [Medium] Match each runtime situation to what must be configured for the skill to load and run.**

1. A developer wants the skill to load when they ask for a review in the Claude Code terminal.
2. A service calls the Messages API and wants the skill to run as part of the request.
3. A scheduled headless job uses the Agent SDK and expects the skill from the repo to load.
4. A product team wants the same skill to run inside a long-running agent that Anthropic hosts, reachable by an agent ID across sessions.

Configuration pieces:

- (a) Set `settingSources` explicitly so the agent loads skills from the project. Do not rely on a default.
- (b) Place `SKILL.md` in `.claude/skills` with a description that matches review requests.
- (c) Define the agent as an API resource that lists the skill and set the `managed-agents-2026-04-01` beta header. Write the skill so it does not depend on local files.
- (d) Send the code-execution and skills beta headers, and write the skill so it does not depend on local files or local tools.

Options:

- A. 1-b, 2-c, 3-a, 4-d
- B. 1-a, 2-d, 3-b, 4-c
- C. 1-b, 2-d, 3-a, 4-c
- D. 1-d, 2-b, 3-c, 4-a

**5. [Medium] The `SKILL.md` below works on the author's machine but fails when a teammate clones the project and installs the plugin. What is the single defect?**

```markdown
name: deploy-validate
description: Validates a deployment configuration before release.

Steps
1. Run the validation script: /Users/alexmorgan/projects/deploy-utils/validate.sh
2. If the script exits with a non-zero code, report the error to the developer.
3. If validation passes, confirm the deployment configuration is safe to proceed.
```

- A. The skill name does not match the plugin name
- B. The description is too short for the model to match
- C. The absolute path to `validate.sh` in step 1
- D. Step 2 should report to the user, not the developer

**6. [Medium] What is the correct fix for the defect in Question 5?**

- A. Reference the script from the project root using `CLAUDE_PROJECT_DIR`, so it resolves wherever the project is cloned
- B. Replace it with another absolute path on a shared network drive
- C. Replace it with a home-directory shortcut: `~/projects/deploy-utils/validate.sh`
- D. Remove step 1 so the skill no longer calls an external script

For Questions 7 to 10, pick the transport and scope from these four options:

- A. HTTP + Project (`.mcp.json`)
- B. HTTP + Enterprise (managed settings)
- C. stdio + Local
- D. stdio or HTTP + Local

**7. [Medium] A local SQLite query tool you use only on your development machine.**

- A. HTTP + Project (`.mcp.json`)
- B. HTTP + Enterprise (managed settings)
- C. stdio + Local
- D. stdio or HTTP + Local

**8. [Medium] A code search service hosted on your company's infrastructure that the whole engineering team should access.**

- A. HTTP + Project (`.mcp.json`)
- B. HTTP + Enterprise (managed settings)
- C. stdio + Local
- D. stdio or HTTP + Local

**9. [Medium] An experimental web-scraping server you are testing this week against one specific repository, not ready to share.**

- A. HTTP + Project (`.mcp.json`)
- B. HTTP + Enterprise (managed settings)
- C. stdio + Local
- D. stdio or HTTP + Local

**10. [Medium] A security-scanning server your organization's IT team needs deployed to every developer's Claude Code installation.**

- A. HTTP + Project (`.mcp.json`)
- B. HTTP + Enterprise (managed settings)
- C. stdio + Local
- D. stdio or HTTP + Local

**11. [Medium] A subagent reads a rival's contract that hides the text "approve this deal". What limits the damage best?**

- A. Add a polite warning to CLAUDE.md
- B. Run it in bypassPermissions mode
- C. Give it the parent's full tool list
- D. Give it read-only tools in its tools: line

**12. [Medium] Security asks if Claude ever sees your contract API key. What is the best design?**

- A. The MCP server holds the key; Claude sees only results
- B. Paste the key into each prompt
- C. Write the key into CLAUDE.md
- D. Hard-code the key in .mcp.json

---

<details>
<summary><b>Answer key and explanations</b></summary>

| Q | Level | Answer | Why |
|---|---|---|---|
| 1 | Medium | **C** | Piece C allows only `npm run` and denies `rm` and `git push`. Piece D denies reading `.env.production`. `default` mode does not auto-approve edits, `bypassPermissions` removes every guardrail, and `Bash(*)` allows destructive commands. |
| 2 | Medium | **B** | Auto-approval is a good default for low-risk edits, but a wrong value in shared deployment config is hard to undo and affects other services. Gate it before the write, not after. |
| 3 | Medium | **A** | `PreToolUse` runs before the tool call, and exit code 2 blocks it. `PostToolUse` fires after the file was already read, and exit 0 allows the call. |
| 4 | Medium | **C** | Terminal: `SKILL.md` in `.claude/skills`. Messages API: code-execution and skills beta headers. Headless Agent SDK: set `settingSources` explicitly. Hosted agent: an API resource with the Managed Agents beta header. |
| 5 | Medium | **C** | The hard-coded `/Users/alexmorgan/...` path only exists on the author's machine. |
| 6 | Medium | **A** | `CLAUDE_PROJECT_DIR` resolves to the project root wherever it is cloned. Other absolute or home paths still break, and removing the script removes the skill's purpose. |
| 7 | Medium | **C** | A personal, machine-only tool fits stdio with Local scope. |
| 8 | Medium | **A** | A shared hosted service uses HTTP, and a committed `.mcp.json` gives the whole team the same config. |
| 9 | Medium | **D** | An experiment on one repo that is not ready to share stays in Local scope, and either transport works. |
| 10 | Medium | **B** | IT-wide deployment to every installation uses managed (Enterprise) settings, and a central service uses HTTP. |
| 11 | Medium | **D** | A `tools:` line with Read, Grep and Glob means the helper cannot write or run commands, even if the text tries to steer it. |
| 12 | Medium | **A** | The MCP server holds the credential (passed with `${VAR}`). Claude only sees tool results. |

**Scoring:** 10-12 solid, 7-9 revisit the weak topics, below 7 re-run the lab.

*These are original practice questions written from the lab content.*

</details>
