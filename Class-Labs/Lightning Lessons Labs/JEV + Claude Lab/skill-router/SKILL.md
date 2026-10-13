---
name: skill-router
description: Route document tasks to existing Claude Code skills using either Claude-only or Jev-based selection, execute the selected skill, and report separately measured routing and extraction performance. Use when the user requests /skill-router with mode=claude or mode=jev.
---

# Skill Router — Claude vs Jev

## Usage

Invoke with one of:

- `/skill-router mode=claude Extract key terms from the attached COIs.`
- `/skill-router mode=jev Extract key terms from the same COIs.`

If no mode is supplied, ask for `claude` or `jev` before routing. Do not silently switch modes.

## 1. Discover available skills

Read the names, descriptions, and relevant instructions of skills available to the current Claude Code session (including project and user skills). Exclude `skill-router` itself. Use the available skill catalog as the allowed route IDs; do not invent skills.

In particular, distinguish:

- **`coi-key-terms`**: extract insurance terms, named insured, insurers, policy dates, coverages, limits, exclusions and conditions from COIs, with document evidence. This is **extraction**, not compliance scoring.
- **`coi-benchmark`** (if installed): compare COIs against a checklist or requirements, determine compliance, gaps, or pass/fail findings.
- **Other installed skills**: route only when their descriptions and task requirements fit better.
- **`no_match`**: use when none of the available skills fits; explain briefly and do not execute a specialist skill.

Do not automatically select `coi-key-terms` merely because the file is a COI. Decide using **both the user's requested task and document type**. If the user asks for key-term extraction from a COI, prefer `coi-key-terms`; if they ask for checklist validation/compliance, prefer the installed checklist/evaluation skill. If both tasks are requested, clarify which is primary or explicitly report the needed stages rather than pretending one skill covers both.

## 2. Keep the two runs comparable

Use the same user task, approved documents, list of candidate skills, and routing criteria in both modes. When possible use the same concise routing input: the user task, document filename/type, safe high-level summary, and candidate skill ID/description pairs. A mode must not change the specialist extraction instructions.

The router **only chooses** a skill. Skill execution is a separately timed stage.

## 3. Routing modes

### `mode=claude`

Have Claude choose exactly one allowed skill ID (or `no_match`) from the discovered catalog using the routing input. Do not perform term extraction during routing. Record a brief reason grounded in the task and document. Do not bias the answer using a presumed expected route.

### `mode=jev`

Use the *actually configured* Jev/Typesafe integration to route among the **same allowed skill IDs**, using its documented choice/classification capability if exposed by the installed integration. Do not assume or invent a Jev endpoint, tool name, schema, or credentials; inspect the real connected tool or integration documentation.

- Before sending any PDF text or document-derived content externally, check permission. If not authorized, send only an approved non-sensitive routing summary (if permitted), or stop Jev routing and report the limitation.
- Validate the returned ID against the allowed skill IDs; record Jev's returned reason if available (otherwise state `Reason not provided by Jev`).
- If Jev is unavailable, unauthorized, fails, or returns an invalid ID, show **Jev routing failed** with the reason. Do not secretly fall back to Claude and label it Jev.
- Do not let Claude override Jev's valid selection during the Jev-mode routing stage.

## 4. Required routing output (before execution)

Show clearly:

```text
Mode: claude | jev
Selected skill: <installed skill ID or no_match>
Reason: <brief explanation>
Routing latency: <measured duration or N/A>
```

If `no_match` or routing failure, stop before execution.

## 5. Execute the selected skill

After showing the routing decision, read and **execute** the selected skill's original `SKILL.md` on the provided document(s). Keep its expected outputs and evidence requirements unchanged. In particular, `coi-key-terms` must extract terms with supporting evidence, preserve values/qualifiers, and mark missing values `Not Found` rather than inventing coverage. Jev selects; **Claude executes** the specialist skill in both modes.

Never count a correct skill ID alone as completed extraction.

## 6. Performance instrumentation

Capture timestamps at the following boundaries using an actual available timer/instrumentation; do not rely on estimates disguised as measurements:

1. `routing_start`: immediately before the routing decision call/processing.
2. `routing_end`: when a valid skill ID is returned.
3. `extraction_start`: immediately before specialist skill execution.
4. `extraction_end`: after the extraction output is complete.

Report:

- **Routing latency** = routing_end − routing_start.
- **Extraction latency** = extraction_end − extraction_start.
- **Total elapsed time** = measured from beginning of this workflow to completion, including any overhead; do not automatically claim it equals routing + extraction.
- **Throughput** = documents processed ÷ total elapsed seconds × 60, in documents/minute, only when elapsed time is measured and boundaries are comparable.
- **Routing and extraction tokens/cost** only when the provider or runtime exposes them for those particular stages. Show `N/A` otherwise. `/usage` or other session-level totals are **not per-run costs**.

If Claude Code has no accessible wall-clock or model timing instrumentation, label measurements `N/A` and explain why; do not fabricate them. Any manually timed or estimated figure must be labeled with its method. Jev API network time and Claude-only selection time must have equivalent start/end boundaries for a meaningful comparison.

## 7. Results and visual comparison

For each run display routing decision, extraction output, and a compact metrics table. If a results directory already exists, save a run summary there only when the user asks or the current workflow already uses it; do not create extra project scaffolding.

Once both modes have been run on the same documents and task, render a simple visual comparison of **routing latency**, **extraction latency**, and **total latency** using measured data. If an actual charting tool or display isn't available, use a text table or a small proportional ASCII bar chart. Mark missing metrics `N/A` instead of drawing fictional bars.

Discuss potential routing cost/throughput benefits only as hypotheses until measurements support them. Do not reuse historical COI benchmark times as measured skill-routing latency.

## Non-negotiable rules

- Don't change other skills, PDFs, or checklists.
- Don't create ZIPs, manifests, additional agents, or a testing framework.
- Don't perform extraction in the routing stage.
- Don't claim Jev was used unless its integration was actually invoked successfully.
- Don't send document content to external APIs without authorization.
- Don't invent any latency, token, throughput, or cost figures.
