# Cohort 9

## Summary
Cohort 9 is the most recent completed run of the AI PM program, wrapping on or
about 2026-07-05. Its completion post is the highest-performing piece of content
in the entire dataset. It is also the anchor for a cluster of reviews and alumni
posts that landed in the first week of July 2026, and — indirectly — for our
best subscriber-conversion day on YouTube.

## Key Facts
- Announced complete by **Mahesh (Instructor)**, Founder, MLAI Community, on
  2026-07-05: PMs went from asking what an agent is to shipping working
  prototypes in **six weeks** (`LINKEDIN_POSTS` row 1, paraphrased).
- The post drew **312 reactions and 24 comments** — the highest reach of any post
  in `LINKEDIN_POSTS`, ahead of the next-best alumni testimonial at 187.
- Program length is therefore **six weeks**, the only place in the data this is
  stated (`LINKEDIN_POSTS` row 1).
- Stated outcome is a **shipped working prototype**, not a certificate. This
  matches [[stanford]]'s advice to arrive at lesson one with an idea you want to
  push to production (`MAVEN_FEEDBACK` row 4).
- On the same day, 2026-07-05, the YouTube channel recorded **33 subscribers
  gained on only 913 views** — the best conversion ratio and the lowest view
  count of the 30-day window (`YOUTUBE_CHANNEL_ANALYTICS` row 25). Cross-channel
  referral from the LinkedIn announcement is the plausible explanation. See
  [[youtube-performance]].
- Four days later, 2026-07-09 produced LinkedIn's strongest engagement day of the
  window — 448 engagements, 197 clicks (`LINKEDIN_PAGE_ANALYTICS` row 29) —
  consistent with sustained comment activity on the wrap-up and alumni posts.

## Reviews Plausibly Attributable
`MAVEN_FEEDBACK` has **no cohort column**, so none of this can be confirmed. But
five reviews were submitted between 2026-06-30 and 2026-07-08, bracketing the
wrap date:
- [[fermat-commerce]] — Sravya Siravuru, 2026-06-30
- [[stanford]] — Anja Lee, 2026-07-02
- [[loblaw-companies]] — Venkat krishnan Chellappa, 2026-07-04
- [[e3-global]] — Praneetha, 2026-07-06
- [[unaffiliated-students]] — Sidharth Sharma, 2026-07-08

Anja Lee's private note about labs changing mid-flight may therefore describe
Cohort 9 specifically — or may not. See [[course-logistics-friction]].

## Alumni Advocacy Generated
- [[t-mobile]] — Sunil Gangavarapu posted his certification completion
  2026-07-04, one day before the wrap (`LINKEDIN_POSTS` row 2, 187 reactions).
- [[microsoft]] — Kartiki Saraf posted about the Snowflake + Claude lab
  2026-06-25 (`LINKEDIN_POSTS` row 4, 156 reactions). See
  [[snowflake-claude-second-brain-lab]].

Together, the founder's post and two alumni posts generated 655 reactions in
under two weeks, against 94 for the [[ai-pm-academy]] advertisement.

## Open Questions
- **How many students were in Cohort 9?** No enrollment or cohort-size data
  exists anywhere in `SOURCE_DATA`.
- **What was the completion rate?** [[microsoft]]'s Kartiki Saraf was still
  working through homework when she submitted feedback.
- Which of the eleven reviews are actually Cohort 9? Without a cohort column in
  `MAVEN_FEEDBACK` this is guesswork based on submission dates.
- Cohort 9 implies eight prior cohorts. No historical data exists for them,
  so no trend in ratings, size, or outcomes can be computed.
- When does Cohort 10 open? Nothing in the data indicates a next-cohort date,
  which is the obvious moment to convert the 312-reaction post into enrollments.

## Related Pages
- [[agentic-ai-pm-certification]]
- [[snowflake-claude-second-brain-lab]]
- [[instructor-teaching-style]]
- [[course-logistics-friction]]
- [[career-transition-into-ai-pm]]
- [[linkedin-performance]]
- [[youtube-performance]]
- [[t-mobile]]
- [[microsoft]]
- [[stanford]]

## Source
`LINKEDIN_POSTS` rows 1, 2, 4 (and row 3 for contrast);
`YOUTUBE_CHANNEL_ANALYTICS` row 25; `LINKEDIN_PAGE_ANALYTICS` row 29;
`MAVEN_FEEDBACK` rows 1, 2, 3, 4, 5 (by submission date, unconfirmed attribution).
