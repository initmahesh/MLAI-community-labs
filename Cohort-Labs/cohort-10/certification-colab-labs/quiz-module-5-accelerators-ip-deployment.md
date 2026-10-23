# Module 5: Accelerators, IP & Deployment

12 multiple-choice questions (all Medium), one correct answer each. Pairs with: `accelerators-ip-deployment.md`. Check the answer key at the bottom.

---

**1. [Medium] A team ships a working contract reviewer as loose scripts, with customer-specific values scattered through the code. What goes wrong, and what is the fix?**

- A. The next team copies the scripts and diverges; package it as an agent template where customer-specific values become settings with documented defaults
- B. The scripts cannot run on another machine; add a Dockerfile
- C. The scripts run too slowly; rewrite them in a faster language
- D. Nothing: loose scripts that run are already reusable

**2. [Medium] A full multi-component application is sent to the Claude Cookbook and is never reviewed. What is the most likely reason?**

- A. The application had too many tests
- B. The Cookbook only accepts code written by Anthropic staff
- C. The README was too short
- D. It is a channel mismatch: the Cookbook holds focused, self-contained reference implementations, and reviewers check one focused pattern

**3. [Medium] A contribution is technically ready. Which check must be cleared before the technical review?**

- A. A benchmark showing it beats existing tools
- B. Approval from the customer's sales team
- C. Licensing and attribution: confirm you have the right to contribute it and credit anything you built on
- D. A second example in another language

**4. [Medium] A regulated EU bank wants an agent that summarizes customer call transcripts for its support team, with summaries reviewed before they are stored in the EU. Which of the following is a valid functional requirement?**

- A. The agent should be fast and accurate
- B. The agent produces a summary that a human approves before it is stored
- C. The system must be built using an approved cloud provider
- D. Transcript data must not leave the EU

**5. [Medium] From the same scenario, which of the following is a valid infrastructure requirement?**

- A. The agent must produce summaries quickly enough for support staff to act on them
- B. The agent summarizes transcripts using a pre-approved prompt template
- C. Transcript data is processed in the EU
- D. A human reviews each summary before it is stored

For Questions 6 to 10, place each activity in the lifecycle phase it belongs to: Requirements, Design, Test, Deploy or Operate.

**6. [Medium] Pinning the full model ID and keeping the prior version.**

- A. Requirements
- B. Design
- C. Test
- D. Deploy
- E. Operate

**7. [Medium] Gating promotion on the eval result before a version goes to production.**

- A. Requirements
- B. Design
- C. Test
- D. Deploy
- E. Operate

**8. [Medium] Deciding data must be processed in a specific region.**

- A. Requirements
- B. Design
- C. Test
- D. Deploy
- E. Operate

**9. [Medium] Instrumenting token cost and latency per call in production.**

- A. Requirements
- B. Design
- C. Test
- D. Deploy
- E. Operate

**10. [Medium] Choosing Amazon Bedrock because the customer holds its compliance posture there.**

- A. Requirements
- B. Design
- C. Test
- D. Deploy
- E. Operate

**11. [Medium] A customer is already certified on one cloud and treats EU data residency as pass or fail. How should you handle the platform comparison?**

- A. Measure speed, compliance and cost equally before deciding
- B. Choose the platform with the lowest token price
- C. Choose the first-party API because it gets new features first
- D. Skip the full comparison: compliance is already pass or fail, so it decides the platform alone

**12. [Medium] A Claude Code task fetches content and then calls an MCP server that holds broad system access, because each part worked fine alone. Which principle does this break?**

- A. Every connection is a trust boundary: trust does not carry over from the component that sent the data, and each part should hold only the least privilege its job needs
- B. Components should share one credential so access is easier to audit
- C. A component is safe once it passes its own tests
- D. Content fetched by one component can be trusted by the next, because it already passed one check

---

## Answer key and explanations

| Q | Level | Answer | Why |
|---|---|---|---|
| 1 | Medium | **A** | Loose scripts run, so they look reusable, but customer-specific values are scattered and the next team copies and diverges them. Keep the reusable core and turn customer-specific parts into settings with documented defaults. |
| 2 | Medium | **D** | Each channel fits one kind of contribution. Sending a full multi-component application to the Cookbook is a mismatch, and one of the most common reasons a contribution is never reviewed. |
| 3 | Medium | **C** | Licensing and attribution decide whether a contribution can be accepted at all, so they come before technical review. |
| 4 | Medium | **B** | A functional requirement states what the agent does. Human approval before storage is behaviour. A is vague, C and D are constraints on the platform and data. |
| 5 | Medium | **C** | An infrastructure requirement is about where and on what the system runs. Processing in the EU is a deployment location. A is performance, B and D are functional. |
| 6 | Medium | **D** | **Deploy.** Pinning the exact version and keeping the prior one for rollback is a release step. |
| 7 | Medium | **C** | **Test.** The eval result is the test gate that decides whether a version is promoted. |
| 8 | Medium | **A** | **Requirements.** Where data may be processed is a constraint set before anything is designed. |
| 9 | Medium | **E** | **Operate.** Per-call cost and latency metrics are monitored while the system runs. |
| 10 | Medium | **B** | **Design.** Picking the platform to fit a compliance posture is a design decision. |
| 11 | Medium | **D** | Compliance often ends the debate: a customer certified on one cloud will not re-certify on another, and regulated customers treat residency as pass or fail. When it is already pass or fail, it decides the platform alone. |
| 12 | Medium | **A** | The whole application is only as safe as its most over-privileged part. Treat everything that crosses a boundary as data, never as instructions, and hand any seam that cannot be secured to a human owner. |

**Scoring:** 11-12 solid, 8-10 revisit the weak topics, below 8 re-read the lab.
