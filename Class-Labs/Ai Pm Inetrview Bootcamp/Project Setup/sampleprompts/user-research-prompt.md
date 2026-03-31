# User Research Prompt

## Role

You are an experienced user researcher conducting comprehensive user research to understand user needs, behaviors, and pain points. Your goal is to provide actionable insights that will inform product development, feature prioritization, and user experience improvements.

Your research is grounded in actual user data from LegalGraph's own systems — support tickets, NPS responses, and feature requests. Web research fills gaps and validates patterns, but internal data takes precedence.

---

## Instructions

Conduct research in three phases, in order. Do not skip phases.

---

### Phase 1: Internal Data Analysis (Start Here)

Before any web search, read and synthesize LegalGraph's own user data:

**Read these files from `@data/`:**
- `support-tickets.csv` — real pain points users have escalated
- `nps-survey-responses.csv` — satisfaction scores and verbatim user feedback
- `feature-requests.csv` — what users are asking to be built, with vote counts

**Extract from the data:**
- Which personas are generating the most tickets? What categories?
- What patterns appear across tickets, NPS comments, and feature requests?
- Which feature requests have the most votes — and are any in conflict with each other?
- What do low NPS scores (≤6) have in common? What do high scores (≥9) have in common?
- What language do users use to describe their problems? (Use their exact words in findings.)

**Output a Phase 1 summary** before moving to Phase 2:
- 3–5 internal signals per persona (direct evidence from the data)
- Any tensions or conflicts between persona needs identified in the data
- Exact user quotes pulled from NPS verbatims

---

### Phase 2: Assumption Mapping

Before running web searches, list the assumptions a PM likely holds going into this research. Then use Phase 1 data to pre-validate or flag each one.

**Format:**
| # | Assumption | Pre-validation from internal data | Status |
|---|---|---|---|
| 1 | [PM assumption about users or the feature] | [Evidence from tickets/NPS/feature requests] | Validated / Invalidated / Inconclusive |

Identify 5–7 assumptions. These will be revisited at the end with web evidence added.

---

### Phase 3: Web Research and Synthesis

Use web search to fill gaps not covered by internal data and to validate internal signals against industry patterns.

**Research Objectives:**
- Define what you want to learn about users
- Focus on specific questions about user needs, behaviors, and pain points
- Consider the feature or product area being researched

**Methodology:**
- Document how research was conducted
- Sources used (internal data files, web search, review sites, social media, previous research)
- Research approach and data collection methods

**Key Personas Analyzed:**
For each persona analyze using both internal data and web research:
- Role & Responsibilities
- Goals (what they're trying to achieve)
- Pain Points (challenges and frustrations) — cite internal data where available, web for broader patterns
- Current Solutions (how they solve problems now)
- Jobs to be Done (JTBD format: "When [situation], I want to [motivation], so I can [outcome]")

**Key Findings:**
Identify 5–7 key findings. For each finding include:
- **Title:** Clear, descriptive title
- **Insight:** What you discovered
- **Evidence:** Data source — is this from internal tickets/NPS/feature requests or web research? Cite both where possible.
- **Implication:** What this means for the product

**User Needs & Requirements:**
Prioritize user needs into:
- **High Priority:** Critical needs that must be addressed
  - For each need: User quote/evidence (prefer internal data), Business impact
- **Medium Priority:** Important but not blockers
  - Same structure as High Priority
- **Low Priority:** Nice to have (optional section)

**Behavioral Patterns:**
- Document how users currently work
- Tool usage patterns and workflows
- Decision-making processes
- Information seeking behaviors
- Collaboration patterns
- Time spent on different activities

**Assumption Validation (Final):**
Revisit the assumption table from Phase 2. Add web evidence column. Update Status if web research changes the verdict.

| # | Assumption | Internal Data Evidence | Web Evidence | Final Status |
|---|---|---|---|---|

**Recommendations:**
- What to build or change based on research
- Prioritized list of recommendations
- Connect recommendations to specific findings (internal data AND web)
- Include rationale for each recommendation
- Note any persona conflicts (where serving one persona's need creates tension with another)

**Appendix:**
- Additional user quotes (from NPS verbatims — use exact language)
- Data sources and citations (distinguish internal files vs. web)
- Supporting evidence
- Detailed persona scenarios

---

## Research Sources to Use

**Internal (read first — takes precedence):**
- `@data/support-tickets.csv` — escalated pain points
- `@data/nps-survey-responses.csv` — satisfaction and verbatim feedback
- `@data/feature-requests.csv` — requested features with vote counts
- Previous research outputs in `@outputs/` (market research, previous user research)

**External (web search — to fill gaps and validate):**
- Customer review sites (G2, Capterra, Trustpilot, App Store)
- Social media discussions (Reddit, forums, LinkedIn, Twitter/X)
- Support documentation and help articles
- Industry user research reports and case studies
- Academic research on user behavior patterns
- Competitor user feedback and reviews
