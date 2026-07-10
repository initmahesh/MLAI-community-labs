# AI PM Academy

## Summary
AI PM Academy is a competitor that appears in our LinkedIn data but is **not
present in the `COMPETITORS` table**. It surfaced by sweeping `LINKEDIN_POSTS`
for named competitors. It advertises an *Applied AI Product Management* cohort
positioned on live case studies with no coding required — a direct
counter-position to our hands-on, build-it-yourself curriculum.

## Key Facts
- Identified in the data only as "Competitor Account: AI PM Academy", with the
  author title "Course Provider" (`LINKEDIN_POSTS` row 3).
- Course: *Applied AI Product Management* cohort (`LINKEDIN_POSTS` row 3).
- Positioning, taken from their own post: live case studies, **no coding
  required** (`LINKEDIN_POSTS` row 3).
- The post is enrollment-driven, using closing-soon urgency framing
  (`LINKEDIN_POSTS` row 3, posted 2026-07-01).
- Reach: 94 reactions, 11 comments. This is the **lowest-performing** of the
  three substantive posts in the table, well behind our alumni testimonials at
  187 and 156 reactions (`LINKEDIN_POSTS` rows 2, 4).
- **No YouTube analytics, no review data, and no instructor name exist for this
  competitor** — they are absent from `COMPETITORS`,
  `COMPETITOR_YOUTUBE_ANALYTICS`, and `COMPETITOR_MAVEN_FEEDBACK`.

## Competitive Read
"No coding required" is the cleanest articulation of the opposite strategy to
ours, and it is a real market. Note the tension with the hiring-manager post in
the same table: a Head of Product at a fintech startup asked where to find AI
PMs who genuinely understand RAG, evals, and agent architecture rather than
buzzwords (`LINKEDIN_POSTS` row 5). A no-coding course does not produce that
person. That contrast is the strongest positioning argument available to us in
this entire dataset, and it comes from a buyer, not from us. See
[[career-transition-into-ai-pm]].

Their paid advertisement underperforming our organic alumni advocacy on the same
platform is worth tracking as a leading indicator, though a single post is not
evidence of a pattern.

## Open Questions
- Is this the same entity as [[ai-product-academy]] (Dr. Marily Nika) under a
  different name, or a genuinely separate provider? The names are close enough
  to warrant confirmation before either page is acted upon. **This is the most
  important open question on this page.**
- Should AI PM Academy be added to the `COMPETITORS` table and tracked in
  `COMPETITOR_YOUTUBE_ANALYTICS` going forward?
- Who is the instructor, and what is the price point?

## Related Pages
- [[ai-product-academy]]
- [[competitive-landscape]]
- [[linkedin-performance]]
- [[career-transition-into-ai-pm]]
- [[pm-vs-engineering-balance]]

## Source
`LINKEDIN_POSTS` row 3 (sole source); contrast drawn from `LINKEDIN_POSTS`
rows 2, 4, 5. Not present in `COMPETITORS`.
