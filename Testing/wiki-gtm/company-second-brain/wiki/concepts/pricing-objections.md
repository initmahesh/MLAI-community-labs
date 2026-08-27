# Pricing Objections

## Summary
Price resistance appears exactly once in our own data — a single YouTube comment
— and never in a review. That thinness is itself the finding: we have no pricing
data, no competitor price points, and no evidence about whether the objection is
widespread or isolated. What we can say is that the one prospect who raised it
had not yet bought, and that every student who *did* buy rated the course 5
stars.

## Key Facts
- The sole direct objection: commenter `skeptical_sam` asked, on *AI Product
  Manager Roadmap 2026*, whether the pricing is worth it given it seems steep
  against other AI PM bootcamps (`YOUTUBE_COMMENTS` row 4, posted 2026-07-03).
- The comment drew **9 likes** — low, but not zero. Compare 42 and 54 likes on
  the two most-liked comments (`YOUTUBE_COMMENTS` rows 1, 7).
- On the **same video and same day**, commenter `priya_builds` said she signed up
  for the cohort after watching, with the RAG section being decisive
  (31 likes, `YOUTUBE_COMMENTS` row 3). Price objection and conversion coexist
  on one video.
- That day, 2026-07-03, produced 3,686 views but only **4 subscribers gained** —
  the lowest subscriber conversion of the 30-day window
  (`YOUTUBE_CHANNEL_ANALYTICS` row 23). Causation is not established.
- **Zero pricing complaints appear in `MAVEN_FEEDBACK`.** All 11 reviews are
  5 stars, and no public review or private note mentions cost.
- Among competitors, only [[product-faculty]] draws a pricing complaint — a
  reviewer called it pricier than alternatives, while noting the team-cohort
  option positively (`COMPETITOR_MAVEN_FEEDBACK` row 6, 4 stars).
- A free substitute was raised separately: the OpenAI cookbook courses
  (`YOUTUBE_COMMENTS` row 8). See [[openai-cookbook-courses]].

## Interpretation
The pattern is a **pre-purchase objection that post-purchase students do not
share.** Nobody who paid complained about price; one person who hadn't paid did.
That is the normal shape of a value-communication problem rather than a
price-level problem — but with n=1, it could equally be noise.

The asset we have for answering it is unusually strong: alumni publicly
attribute concrete outcomes to the program, including building a working data
pipeline as a PM ([[microsoft]], `LINKEDIN_POSTS` row 4) and bridging the PM-to-AI
gap better than alternatives they tried ([[t-mobile]], `LINKEDIN_POSTS` row 2).
Neither of those claims is on the pricing page, because we do not have pricing
page data at all.

## Open Questions
- **What do we actually charge, and what do competitors charge?** No table in
  `SOURCE_DATA` contains a price. Every statement above is inferred from
  language. This is the single largest data gap in the wiki.
- Is one objecting comment in a 30-day window a signal or noise? We have no
  historical baseline.
- Did `skeptical_sam` ever convert? No table links commenters to enrollments.
- Does the 2026-07-03 conversion dip relate to the pricing comment, or to the
  video's own top-of-funnel nature? Unresolvable with current data.

## Related Pages
- [[competitive-landscape]]
- [[product-faculty]]
- [[product-manager-accelerator]]
- [[openai-cookbook-courses]]
- [[hands-on-labs-praise]]
- [[youtube-performance]]
- [[t-mobile]]
- [[microsoft]]

## Source
`YOUTUBE_COMMENTS` rows 3, 4, 8; `YOUTUBE_CHANNEL_ANALYTICS` row 23;
`COMPETITOR_MAVEN_FEEDBACK` row 6; `MAVEN_FEEDBACK` rows 1–11 (absence of
pricing complaints); `LINKEDIN_POSTS` rows 2, 4.
