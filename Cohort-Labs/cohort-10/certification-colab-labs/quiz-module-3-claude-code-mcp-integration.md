# Module 3 Quiz — Claude Code, MCP & Integration

15 multiple-choice questions. Pick one answer per question, then check the answer key at the bottom.
Pairs with: `claude-code-mcp-integration-colab.ipynb`

---

**1. What does `plan` permission mode do?**

- A. Auto-approves all edits and commands after showing a plan
- B. Denies every tool call that is not on an allow list
- C. Skips the explore phase and goes straight to coding
- D. Holds Claude Code in read-only exploration: no edits or shell commands until you approve a plan

**2. What does `acceptEdits` auto-approve?**

- A. Everything, with a classifier reviewing each action
- B. Reads, file edits and common filesystem commands inside the working directory; other shell commands and protected paths still prompt
- C. Only reads
- D. All tool calls, with no safety checks

**3. A developer wants fewer prompts and switches to `bypassPermissions` on a workstation. What is the correct assessment?**

- A. Only appropriate in an isolated, disposable container or VM; it removes every prompt including the protected-path guard, so use deny rules first, or `auto` for fewer prompts with a safety net
- B. Fine, as long as the task feels routine
- C. Acceptable on any machine if the repo is backed up
- D. It still prompts for all shell scripts

**4. An allow rule at project level and a deny rule at enterprise level conflict. What happens?**

- A. The project allow wins because it is more specific
- B. The deny wins; a deny rule always beats an allow rule, and enterprise managed settings can't be overridden by users or projects
- C. The most recently edited file wins
- D. Claude asks the user to choose

**5. How do you decide where a human review gate belongs?**

- A. Ask what the worst outcome is if this action runs unchecked: let reversible low-cost actions through, gate hard-to-undo or sensitive-path actions, and never let the agent be the only gate on code your team marked sensitive
- B. Gate every action equally
- C. Gate only actions that take a long time
- D. Gate only shell commands

**6. How should you treat an AI code reviewer's findings?**

- A. As a verdict to apply directly
- B. Trust claims about runtime behavior and other systems, but verify missing null checks
- C. Trust what is provable from the diff (and confirm it on the cited lines); treat claims about runtime behavior or other systems as hypotheses to test; keep a human gate where a finding becomes an irreversible action
- D. Ignore all of it

**7. Your CLAUDE.md has grown to 800+ lines and the agent edited a directory it was told not to touch. What is the best fix?**

- A. Add the rule again, in capital letters
- B. Increase the context window
- C. Move everything into a subagent
- D. Trim CLAUDE.md to the rules that change behavior, move path-specific guidance to scoped rules files (`paths:` frontmatter), move reference material elsewhere, and enforce the can't-fail rule with a hook

**8. Which statement about hooks is correct?**

- A. A `PostToolUse` hook can block the tool call that just ran
- B. A `PreToolUse` hook can block a call by exiting with code 2 and writing the reason to stderr; this enforces a guardrail regardless of permission mode, unlike an instruction in CLAUDE.md
- C. Hooks add their full source to the context window on every turn
- D. Hooks only run in `bypassPermissions` mode

**9. You delegate a task to the built-in Explore subagent and your project's CLAUDE.md rules are not followed. Why?**

- A. Subagents are never able to read files
- B. CLAUDE.md only loads in `plan` mode
- C. Explore and Plan skip CLAUDE.md and git status for speed; use the general-purpose subagent or a custom subagent when project rules must apply (and list any skills it needs in its frontmatter)
- D. The subagent inherited an outdated CLAUDE.md

**10. A skill worked in Claude Code but does nothing in a headless Agent SDK job. What is the most likely cause?**

- A. `settingSources` was never set, so filesystem settings and skills never loaded; set it explicitly
- B. Skills only run in the terminal
- C. The SDK doesn't support Markdown
- D. The skill needs the Messages API beta headers

**11. A plugin installs successfully for every teammate but its skill fails for all of them except the author. The skill calls `/Users/alex/projects/deploy-utils/validate.sh`. What is the fix?**

- A. Switch to a home shortcut such as `~/projects/deploy-utils/validate.sh`
- B. Put the script on a shared network drive and use that absolute path
- C. Reference scripts with `$CLAUDE_PROJECT_DIR` (project) or `${CLAUDE_PLUGIN_ROOT}` (bundled in the plugin), bundle or share every dependency, and test on a clean machine
- D. Remove the validation step

**12. A code-search service hosted on your company's infrastructure must be available to the whole engineering team through the repo. Which transport and scope fit?**

- A. stdio + local scope
- B. SSE + user scope
- C. stdio + project scope, because stdio is the most secure
- D. HTTP (streamable) + project scope (`.mcp.json` committed to the repo)

**13. An API key was committed inline in `.mcp.json`. The developer replaces it with `${WAREHOUSE_MCP_TOKEN}` in a new commit. Is the problem solved?**

- A. No; the key is still in git history and must be treated as compromised and rotated. Configs should only ever hold variable references (back the convention with a PreToolUse hook)
- B. Yes, the file no longer contains the key
- C. Yes, as long as the repository is private
- D. No, but rotating is unnecessary if you force-push

**14. Which MCP primitive is read-only data the client fetches by URI and places directly into context, rather than the model calling an action?**

- A. Tool
- B. Resource
- C. Prompt
- D. Transport

**15. An OAuth-authenticated MCP integration works in staging but every production sign-in fails with a redirect URI mismatch. What is the cause and the fix?**

- A. A code defect in the MCP server; rewrite the sign-in flow
- B. The token expired; refresh it
- C. Redirect URIs are registered per host (and often per environment); register the production host's redirect URI, and check whether separate OAuth app registrations per environment are required
- D. OAuth can't be used in production; switch to a hard-coded API key

---

<details>
<summary><b>Answer key and explanations</b></summary>

| Q | Answer | Why |
|---|---|---|
| 1 | **D** | `plan` keeps Claude Code in explore (read-only) until you approve a plan. |
| 2 | **B** | `acceptEdits` covers edits and common filesystem commands inside the working directory; everything else still prompts. |
| 3 | **A** | Bypass removes all checks including the protected-path guard. Use only in disposable environments; use deny rules or `auto` instead. |
| 4 | **B** | Deny always beats allow, and managed (enterprise) settings can't be overridden. |
| 5 | **A** | The worst-case-cost question places the gate; agent output is an input to a human decision for sensitive code. |
| 6 | **C** | Verify what is provable from the diff, test runtime claims, and gate irreversible actions. |
| 7 | **D** | CLAUDE.md dilutes with size. Scoped rules files, separate reference docs, and a hook for the critical rule. |
| 8 | **B** | `PreToolUse` + exit code 2 blocks; `PostToolUse` can't block (the call already happened). Hooks are guardrails; CLAUDE.md lines are conventions. |
| 9 | **C** | Explore and Plan skip CLAUDE.md and git status. Custom subagents also don't inherit skills automatically. |
| 10 | **A** | Under the Agent SDK, whether CLAUDE.md and skills load is controlled by `settingSources`; set it explicitly. |
| 11 | **C** | Install copies files; execution resolves paths on the running machine. Use `$CLAUDE_PROJECT_DIR` / `${CLAUDE_PLUGIN_ROOT}`. |
| 12 | **D** | Shared remote servers use HTTP; project scope commits `.mcp.json` so the config travels with the repo. A stdio server runs only on each machine; SSE is legacy. |
| 13 | **A** | Overwriting doesn't remove history. Rotate, and keep only `${VAR}` references in config. |
| 14 | **B** | Resources are read-only data addressed by URI; tools are actions; prompts are instruction templates. |
| 15 | **C** | Redirect URIs are per host. Add the production URI, and verify whether separate app registrations per environment are required. |

**Scoring:** 13–15 solid · 10–12 revisit the weak topics · below 10 re-run the lab.

*These are original practice questions written from the module content, not the course's own checkpoint items.*

</details>
