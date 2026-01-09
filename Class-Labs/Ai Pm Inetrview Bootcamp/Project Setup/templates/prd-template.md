# Product Requirements Document: [Feature Name]

**Status**: Draft | In Review | Approved
**Author**: [Name]
**Date**: [Date]
**Last Updated**: [Date]

## Executive Summary
[One paragraph overview]

## Problem Statement
### User Problem
[What problem are we solving?]

### Business Problem
[Why does this matter to the business?]

### Supporting Evidence
- Market research: [Link to research doc]
- User research: [Link to research doc]
- Data: [Relevant metrics]

## Goals & Success Metrics
### User Goals
1. [Goal] - measured by [metric]

### Business Goals
1. [Goal] - measured by [metric]

## User Stories & Use Cases
### Primary Use Case
**Actor**: [Persona]
**Goal**: [What they want to accomplish]
**Steps**:
1. [Step]
2. [Step]

[Repeat for 3-5 use cases]

## Requirements

### Must Have (P0)
1. **[Requirement]**
   - User story: As a [persona], I want to [action] so that [benefit]
   - Acceptance criteria:
     - [ ] [Criterion]
     - [ ] [Criterion]

### Should Have (P1)
[Same structure]

### Nice to Have (P2)
[Same structure]

## Design & User Experience
[Wireframes, mockups, flow diagrams]

## Technical Considerations
### Architecture
[High-level technical approach]

### Dependencies
[What this depends on]

### Security & Compliance
[Relevant requirements]

## Out of Scope
[What we're explicitly NOT doing]

## Launch Plan
### Phase 1: [Name]
- Timeline: [Dates]
- Features: [List]
- Success criteria: [Metrics]

## Risks & Mitigations
| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| [Risk] | High/Med/Low | High/Med/Low | [Strategy] |

## Open Questions
1. [Question] - Owner: [Name] - Due: [Date]

## Appendix
### Research References
- [Link to market research]
- [Link to user research]

### Change Log
| Date | Author | Change |
|------|--------|--------|
| [Date] | [Name] | [Description] |
```

### Module 7: Sample Queries & Expected Outputs

#### Sample Query Set 1: Market Research
```
Query: "Conduct market research for AI legal contract review platforms. Focus on enterprise segment."

Expected Claude Actions:
1. Read company-context/company-overview.md
2. Read company-context/competitive-landscape.md
3. Read templates/market-research-format.md
4. Execute web searches:
   - "legal tech market size 2026"
   - "AI contract review platforms comparison"
   - "enterprise legal software trends"
5. Structure output per template
6. Save to outputs/market-research-[date].md
```

#### Sample Query Set 2: User Research
```
Query: "Research user needs for contract risk assessment features targeting legal ops managers."

Expected Claude Actions:
1. Read company-context/user-personas.md (focus on legal ops persona)
2. Read templates/user-research-format.md
3. Execute web searches:
   - "legal operations manager workflow"
   - "contract risk management best practices"
   - "legal ops technology adoption"
4. Structure findings per template
5. Save to outputs/user-research-[date].md
```

#### Sample Query Set 3: PRD Writing
```
Query: "Write a PRD for automated clause extraction feature. Use all previous research."

Expected Claude Actions:
1. Read outputs/market-research-[date].md
2. Read outputs/user-research-[date].md
3. Read company-context/* (all files)
4. Read templates/prd-template.md
5. Write comprehensive PRD following template
6. Include references to research
7. Save to outputs/prd-clause-extraction.md