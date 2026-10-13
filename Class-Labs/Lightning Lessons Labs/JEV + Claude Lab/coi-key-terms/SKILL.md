---
name: coi-key-terms
description: Extract key insurance terms, coverage details, policy limits, and important conditions from Certificates of Insurance (COIs). Use when the user requests COI key-term extraction; do not use for checklist compliance evaluation.
---

# COI Key-Term Extraction

## Objective
Extract document-supported insurance key terms from one or more Certificates of Insurance. This skill extracts facts, not checklist compliance results or legal advice.

## Inputs
- COI PDFs supplied by the user, or PDF files in `coi-documents/` if that folder exists.
- If several COIs are supplied, process each independently and identify it by filename.
- Do not send document contents to external services without authorization.

## Process
1. Read each COI completely, including tables, remarks, and endorsements when available. If text is unreadable, say so rather than guessing.
2. Locate and extract applicable terms in these groups:
   - **Certificate:** named insured, certificate holder, producer, insurer(s), certificate date.
   - **Policy:** policy number, effective date, expiry date, type of insurance.
   - **Coverage:** commercial general liability, automobile liability (including hired/non-owned), workers' compensation/employers' liability, umbrella/excess, property, equipment breakdown, business interruption, flood/earthquake, and other explicitly listed coverage.
   - **Limits and conditions:** each occurrence, general aggregate, products/completed operations, personal/advertising injury, deductibles, currency, additional insured, waiver of subrogation, cancellation notice, exclusions, and special conditions.
3. Preserve exact amounts, units, dates, and qualifiers. Do not treat a checkbox or certificate description as proof of an endorsement unless the document supports that conclusion.
4. Include a supporting page, section, or short evidence excerpt for each extracted value. Mark absent fields `Not Found` and ambiguous fields `Unclear` with an explanation.
5. Do not infer coverage from a blank field or assume a policy is currently active merely because a certificate was issued.

## Output
For each document, produce:

### [COI filename]

| Category | Key term | Extracted value | Evidence (page/section or brief excerpt) |
|---|---|---|---|
| Certificate | Named insured | ... | ... |
| Policy | Policy number | ... | ... |
| Coverage | General liability limit | ... | ... |

Include all relevant terms found, followed by:
- **Terms found:** number of populated terms.
- **Missing or unclear:** key fields not found or ambiguous.
- **Notes:** meaningful document limitations or caveats.

At the end, state total COIs processed and a concise factual summary. Avoid checklist-based compliance verdicts unless the user explicitly requests that separately.

## When Called by `skill-router`
- Follow the selected extraction instructions regardless of whether the router used `claude` or `jev` mode.
- Keep routing and extraction stages separate.
- Report actual extraction latency, token usage, and cost only if available from instrumentation; otherwise use `N/A`.
- Do not fabricate metrics or modify source COIs.
