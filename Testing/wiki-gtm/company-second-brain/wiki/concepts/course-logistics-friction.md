# Course Logistics Friction

## Summary
One student recorded an operational defect: labs were being modified while
students were working through them. It is the only negative observation about
the product anywhere in eleven reviews, it was filed in a private note behind a
5-star public rating, and it came from the most qualified person in the cohort
to notice it. That combination is why this page exists despite n=1.

## Key Facts
- Source: [[stanford]]'s **Anja Lee**, Data PM, coach and instructor
  (`MAVEN_FEEDBACK` row 4).
- Her public rating: **5 stars**. Her public review is entirely positive.
- Her private note records three things (paraphrased, internal — not for
  external use):
  - Logistics could be a little better.
  - **The labs were changing while students were doing them, which was
    confusing.**
  - She wanted more PM skills content and more time on it (covered separately in
    [[pm-vs-engineering-balance]]).
- The word "intense" appears from two other students describing the experience
  positively: [[microsoft]]'s Kartiki Saraf (more intense than expected, in a
  good way) and [[loblaw-companies]]' Venkat krishnan Chellappa (a wonderful and
  intense experience) (`MAVEN_FEEDBACK` rows 9, 3, `private_note`, paraphrased).
- Kartiki also noted she was **still working through the homework** when she
  submitted her feedback (`MAVEN_FEEDBACK` row 9, `private_note`).

## The Structural Finding
Look at where criticism lives. All eleven public reviews are 5 stars. All
recorded criticism sits in `private_note` — a field prospects never see.

| | Public review | Private note |
|---|---|---|
| Anja Lee ([[stanford]]) | Glowing, no criticism | Lab churn, logistics, wants more PM content |
| Avinendra Chauhan ([[bank-ozk]]) | Glowing | Job searching, not a PM by background |
| Kartiki Saraf ([[microsoft]]) | Four words | Intense, homework incomplete, seeking re-entry |

The 5.0 average cited in [[competitive-landscape]] is therefore not a clean
quality measurement. It measures what students are willing to say in public,
which is a different quantity — goodwill toward an instructor they like. The
real product feedback is in the private channel, and it is thin because only
five of eleven students wrote one.

## Interpretation
Lab churn is a fixable process problem, and it sits directly on our single
strongest asset. Labs are the most-praised element of the course
([[hands-on-labs-praise]], six of eleven reviewers) and they are also the only
thing anyone complained about. Editing them in flight risks the differentiator.

That said: **one person said this.** Whether it was a one-cohort artifact of
rapid iteration or a standing practice is not answerable from this data, and
this page should not be treated as established fact until a second cohort
confirms it.

## Open Questions
- Were labs mid-revision during Anja's cohort specifically, or is in-flight
  editing standard practice? **This is the question that determines whether
  anything needs to change.**
- Which cohort was she in? `MAVEN_FEEDBACK` has no cohort column, so her
  feedback cannot be tied to [[cohort-9]] or any other run.
- Six of eleven students left no private note. Is their silence satisfaction, or
  is the private-note field simply easy to skip?
- Does an operational cadence exist for freezing lab content before a cohort
  starts? Nothing in the data indicates one.

## Related Pages
- [[hands-on-labs-praise]]
- [[pm-vs-engineering-balance]]
- [[feature-gaps-and-requests]]
- [[instructor-teaching-style]]
- [[cohort-9]]
- [[snowflake-claude-second-brain-lab]]
- [[stanford]]
- [[microsoft]]
- [[competitive-landscape]]

## Source
`MAVEN_FEEDBACK` row 4 (`private_note`, primary); supporting rows 3, 9
(`private_note`); rows 1–11 for the public/private rating pattern.
