# Feature Gaps and Requests

## Summary
Four distinct asks appear in the data — three from prospects on YouTube, one
from a student in a private note. None is recorded as answered. They are small
in number because the dataset is small, but they are unusually specific, and two
of them point at content that would directly serve the career-transition motive
that drives most enrollments.

## The Requests

**1. Evaluations and testing for agentic workflows** — content gap
- Commenter `ai_curious_dev` asked for a follow-up video on evaluations and
  testing agentic workflows (`YOUTUBE_COMMENTS` row 2, 18 likes, on *Building AI
  Agents with Claude Code*, 2026-07-07).
- Evals are named as a curriculum element by [[tibco]]'s Hiren Shah
  (`MAVEN_FEEDBACK` row 11) and [[t-mobile]]'s Sunil Gangavarapu
  (`MAVEN_FEEDBACK` row 10), so the course covers them — **the gap is in the free
  content funnel, not the paid product.**
- Independently, the fintech hiring manager named evals as one of three things
  he needs AI PMs to actually understand (`LINKEDIN_POSTS` row 5).

**2. How to explain AI PM experience in interviews** — content gap
- Commenter `jordan_transitions` asked for this directly, saying he struggles
  with it (`YOUTUBE_COMMENTS` row 5, 27 likes, on *From PM to AI PM: Real Talk*).
- This is the second-most-liked request in the comment table.
- It maps exactly onto [[career-transition-into-ai-pm]], the dominant student
  motive. Nothing in the data suggests the curriculum addresses it.

**3. More PM skills content, and more time on it** — curriculum request
- From [[stanford]]'s Anja Lee, in a private note (`MAVEN_FEEDBACK` row 4,
  paraphrased). She argues the PM mindset outlasts any model release and
  that not everyone in the cohort arrives as a PM.
- She is an instructor and coach herself. See [[pm-vs-engineering-balance]].

**4. A comparison against free vendor documentation** — positioning gap
- Commenter `competitor_watcher` asked how our content compares to the OpenAI
  cookbook courses (`YOUTUBE_COMMENTS` row 8, 6 likes — the least-liked comment).
- No recorded answer exists. See [[openai-cookbook-courses]].

## Signals of What Already Lands
Worth stating so the gaps are read in proportion. Two comments describe content
succeeding: MCP finally clicking thanks to clear examples (`YOUTUBE_COMMENTS`
row 1, 42 likes) and a self-described non-technical viewer finding Claude Code
approachable (`YOUTUBE_COMMENTS` row 7, 54 likes — the most-liked comment in the
table). A third credits the RAG section with converting her to enroll
(`YOUTUBE_COMMENTS` row 3).

## Interpretation
Requests 1 and 2 are the same shape: **the paid course covers the material, but
the free funnel doesn't demonstrate it.** Evals are taught but not shown;
interview narrative may not be taught at all. Both sit on the critical path from
"watching a video" to "believing this is worth the price" — see
[[pricing-objections]].

## Open Questions
- Is there any content pipeline or backlog? No table in `SOURCE_DATA` tracks
  planned videos or curriculum changes, so "unanswered" here means "not visible
  in the data", not "ignored".
- Only 8 YouTube comments exist across 30 days and 78,053 views. Is comment
  volume this low, or is the table a sample? This materially affects how much
  weight any single request should carry.
- Does the course teach interview positioning? Unknown, and it is the request
  most aligned with why students enroll.

## Related Pages
- [[career-transition-into-ai-pm]]
- [[pm-vs-engineering-balance]]
- [[pricing-objections]]
- [[hands-on-labs-praise]]
- [[openai-cookbook-courses]]
- [[youtube-performance]]
- [[stanford]]
- [[course-logistics-friction]]

## Source
`YOUTUBE_COMMENTS` rows 1, 2, 3, 5, 7, 8; `MAVEN_FEEDBACK` rows 4, 10, 11;
`LINKEDIN_POSTS` row 5.
