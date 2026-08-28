# PRD Checklist — 20-Point Quality Standard

Use this checklist before finalizing any PRD. Every item should be answered with a clear "yes" backed by evidence in the document. If any item is "no" or "unclear", the PRD is not ready for review.

---

## Problem & Context

- [ ] **1. Problem Statement is crisp** — The core user/business pain is stated in one or two sentences without solution language.
- [ ] **2. Problem is validated** — Evidence cited: user research, support tickets, sales feedback, data, or equivalent. Not assumed.
- [ ] **3. Scope is bounded** — What is explicitly OUT of scope is stated. No scope creep risk.
- [ ] **4. Strategic alignment** — The problem connects to a company or team-level OKR or strategic bet.

---

## Users & Jobs to Be Done

- [ ] **5. Primary persona defined** — Name, role, context, and technical literacy level are described.
- [ ] **6. Secondary personas identified** — Stakeholders or adjacent users who are affected but not the primary target.
- [ ] **7. Jobs to Be Done (JTBD) articulated** — Written in "When I __, I want to __, so I can __" format for each persona.
- [ ] **8. Pain points ranked** — User pain points are prioritized, not just listed. Highest severity pains drive requirements.

---

## Success Metrics

- [ ] **9. Primary success metric defined** — One north-star metric with a target value and measurement window.
- [ ] **10. Guardrail metrics defined** — Metrics that must NOT degrade (e.g., latency, error rate, churn).
- [ ] **11. Leading indicators identified** — Early proxy metrics to detect success/failure before primary metric moves.
- [ ] **12. Baseline established** — Current state of each metric is documented so delta is measurable.

---

## Requirements

- [ ] **13. Functional requirements are complete** — Every user-facing behavior is described, including edge cases.
- [ ] **14. Non-functional requirements stated** — Performance, scalability, availability, and compliance thresholds specified.
- [ ] **15. Requirements are prioritized (MoSCoW or equivalent)** — Must-have, Should-have, Could-have clearly labeled.
- [ ] **16. Acceptance criteria written** — Each requirement has a testable pass/fail condition. No ambiguous "should work well."

---

## Risks & Dependencies

- [ ] **17. Dependencies mapped** — All upstream and downstream system, team, and data dependencies are listed with owners.
- [ ] **18. Risks identified with mitigations** — Top 3–5 risks called out; each has a mitigation or contingency plan.
- [ ] **19. Regulatory / legal / compliance flags** — Any data privacy, security, or industry-specific compliance requirements are noted.

---

## Launch & Rollout

- [ ] **20. Go-to-market and rollout plan outlined** — Phased rollout strategy, feature flags, pilot users, and comms plan are described or referenced.

---

> **Pass threshold:** All 20 items checked before entering engineering scoping.
