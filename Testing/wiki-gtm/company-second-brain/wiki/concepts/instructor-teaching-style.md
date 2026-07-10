# Instructor Teaching Style

## Summary
Mahesh's teaching is named as the reason the course works in seven of eleven
reviews, and it is the only asset in this dataset that no competitor is credited
with. Two words recur: **energy** and **practical**. The strategic problem is
that teaching quality is invisible to a prospect who has not yet enrolled, while
our competitors lead with credentials that are legible in one line.

## Key Facts

**Reviewers crediting teaching style directly:**
- [[bank-ozk]] — Avinendra Chauhan: a natural, practical teaching style that
  makes complex concepts easy to absorb and apply. In a private note he compared
  Mahesh to the engineering coaching tutors of his hometown, Kota, Rajasthan
  (`MAVEN_FEEDBACK` row 8, review and `private_note`, paraphrased).
- [[stanford]] — Anja Lee: as an instructor herself, she judges that Mahesh
  genuinely *likes* to teach and consistently goes beyond in answering
  questions. She rates him a seasoned practitioner in both AI engineering and AI
  product (`MAVEN_FEEDBACK` row 4, paraphrased). This is peer assessment, not
  customer satisfaction.
- [[unaffiliated-students]] — Sidharth Sharma: interactive sessions, energy and
  passion described as infectious (`MAVEN_FEEDBACK` row 1, paraphrased).
- [[unaffiliated-students]] — Shankar Ranganathan: notes in private that Mahesh
  brings a lot of energy to the course (`MAVEN_FEEDBACK` row 7, `private_note`,
  paraphrased).
- [[tibco]] — Hiren Shah: credits Mahesh with covering the concepts needed for a
  strong foundation (`MAVEN_FEEDBACK` row 11).
- [[loblaw-companies]] — Venkat krishnan Chellappa: credits the
  build-on-your-learning approach with aiding retention (`MAVEN_FEEDBACK` row 3).
- [[fermat-commerce]] — Sravya Siravuru: technical concepts are very well
  explained (`MAVEN_FEEDBACK` row 5).

**The mentor team is credited separately:**
- [[stanford]] — Anja Lee: mentors bend over backwards to help students through
  final projects (`MAVEN_FEEDBACK` row 4, paraphrased).
- [[unaffiliated-students]] — Sidharth Sharma thanks Mahesh **and the mentors**
  (`MAVEN_FEEDBACK` row 1, `private_note`).

**Nothing comparable exists on the competitor side.** Across all eight rows of
`COMPETITOR_MAVEN_FEEDBACK`, no reviewer praises teaching style, energy, or
responsiveness. Competitor praise attaches to *credentials* ("great credentials
from the instructor", competitor 1), *narrative* (an inspiring personal story,
competitor 2), and *credibility* (the builder angle, competitor 3).

## The Asymmetry
Our competitors' instructors are legible before purchase: a PhD in ML from
ex-Google/Meta ([[ai-product-academy]]), the first PM at Cursor and an Anthropic
MTS ([[product-faculty]]), 18 years at Amazon/Google/Microsoft
([[hardcore-agentic-engineering]]), a LinkedIn Top Voice with 100K+ followers
([[product-manager-accelerator]]) — all from `COMPETITORS` rows 1–4.

Ours is legible only after. Teaching quality is a *post-purchase* discovery, and
it is generating exactly the artifact that could carry it pre-purchase: unpaid
alumni advocacy, at 187 and 156 LinkedIn reactions, outperforming a competitor's
own advertisement at 94 (`LINKEDIN_POSTS` rows 2, 3, 4).

## Open Questions
- What are Mahesh's own credentials? Nothing in `SOURCE_DATA` records them,
  though [[stanford]]'s Anja Lee — qualified to judge — calls him a seasoned
  practitioner in both AI engineering and AI product.
- Does teaching quality scale? It is a person, and it is our differentiator.
  Cohort 9 is complete; there is no data on cohort size or on whether mentor
  quality holds as cohorts grow. See [[cohort-9]].
- Is alumni advocacy prompted or organic? It matters entirely for whether it is
  a repeatable channel.

## Related Pages
- [[hands-on-labs-praise]]
- [[cohort-9]]
- [[competitive-landscape]]
- [[course-logistics-friction]]
- [[linkedin-performance]]
- [[stanford]]
- [[bank-ozk]]
- [[unaffiliated-students]]
- [[product-faculty]]
- [[ai-product-academy]]

## Source
`MAVEN_FEEDBACK` rows 1, 3, 4, 5, 7, 8, 11 (public reviews and private notes);
`COMPETITOR_MAVEN_FEEDBACK` rows 1–8; `COMPETITORS` rows 1–4;
`LINKEDIN_POSTS` rows 2, 3, 4.
