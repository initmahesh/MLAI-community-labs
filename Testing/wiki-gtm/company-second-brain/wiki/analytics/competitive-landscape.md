# Competitive Landscape

## Summary
Across the same 30-day window (2026-06-11 → 2026-07-10), MLAI Community grew its
YouTube subscriber base faster in percentage terms than all four tracked
competitors — 6.1% against a competitor range of 2.3% to 3.0% — and posted the
highest engagement rate in the set at 5.34%, roughly a full point above the
competitor average of 4.56%. That is the good news, and it is real. The
qualifier is scale: we are the second-smallest channel here. Product Manager
Accelerator holds 121,605 subscribers to our 8,708, meaning their 3.0% growth
added 3,554 subscribers in the window while our faster 6.1% added 497. We are
winning the rate and losing the absolute. On reviews, our 11 Maven ratings
average a perfect 5.0 against a competitor average of 4.375, but our sample is
public reviews only from recent cohorts, while competitor 1 has run roughly 100
cohorts — the comparison flatters us and should not be read as a durable
quality lead.

## Key Metrics

| Channel | Start subs | End subs | Gained | % growth | Avg daily views | Avg engagement |
|---|---|---|---|---|---|---|
| **MLAI Community (us)** | 8,211 | 8,708 | +497 | **+6.05%** | 2,602 | **5.34%** |
| [[ai-product-academy]] (Marily Nika) | 14,214 | 14,546 | +332 | +2.34% | 5,576 | 4.79% |
| [[product-manager-accelerator]] (Nancy Li) | 118,051 | 121,605 | +3,554 | +3.01% | **12,615** | 4.11% |
| [[product-faculty]] (Varma & Shi) | 6,103 | 6,254 | +151 | +2.47% | 1,832 | 4.82% |
| [[hardcore-agentic-engineering]] (Godhuli Chatterjee) | 3,402 | 3,485 | +83 | +2.44% | 1,101 | 4.53% |

Our engagement rate is computed as (likes + comments) ÷ views from
`YOUTUBE_CHANNEL_ANALYTICS`; competitor rates are the pre-computed
`engagement_rate_pct` column averaged across 30 days. **These are not
guaranteed to be the same formula** — treat the comparison as directional. See
Open Questions.

| Course | Avg Maven rating | n reviews |
|---|---|---|
| **MLAI Community (us)** | **5.00** | 11 |
| [[ai-product-academy]] | 4.5 | 2 |
| [[product-manager-accelerator]] | 4.5 | 2 |
| [[product-faculty]] | 4.5 | 2 |
| [[hardcore-agentic-engineering]] | 4.0 | 2 |

## Where We're Ahead

- **Subscriber growth rate.** 6.05% versus a 2.34%–3.01% competitor band — we
  are growing at roughly twice the rate of the fastest competitor.
- **Audience engagement.** 5.34% beats every tracked competitor; the closest is
  Product Faculty at 4.82%.
- **Hands-on depth.** The most common praise in our reviews is practical labs
  (`MAVEN_FEEDBACK` rows 1, 6, 11). The most common *criticism* of competitor 1
  is that it is theory-heavy and light on coding practice
  (`COMPETITOR_MAVEN_FEEDBACK` rows 1, 2). This is a direct, exploitable gap.
  See [[hands-on-labs-praise]].
- **Review sentiment.** Every one of our 11 Maven reviews is 5 stars.
- **Instructor advocacy.** Alumni post unprompted testimonials to LinkedIn with
  strong reach (187 and 156 reactions, `LINKEDIN_POSTS` rows 2, 4). No
  competitor advocacy appears in the data — only a paid-style advertisement
  from [[ai-pm-academy]] at 94 reactions.

## Where We're Behind

- **Absolute scale.** Product Manager Accelerator has ~14× our subscribers and
  ~4.8× our daily views. Their slower growth rate still nets them 7× the
  subscribers we add per month.
- **Distribution reach.** At 2,602 average daily views we sit third of five,
  behind Product Manager Accelerator (12,615) and AI Product Academy (5,576).
- **Instructor brand credentials.** Competitors lead with hard credentials —
  ex-Google/Meta with an ML PhD (competitor 1), first PM at Cursor and an
  Anthropic MTS (competitor 3), 18 years at Amazon/Google/Microsoft
  (competitor 4). Our positioning rests on teaching quality, which reviews
  confirm but which is harder to signal cold. See [[instructor-teaching-style]].
- **Price perception.** A prospect publicly asked whether our pricing is
  justified against other AI PM bootcamps (`YOUTUBE_COMMENTS` row 4). Only
  competitor 3 draws a comparable pricing complaint
  (`COMPETITOR_MAVEN_FEEDBACK` row 6). See [[pricing-objections]].
- **Cohort maturity.** Competitor 1 has run ~100 cohorts; we completed Cohort 9.

## Open Questions
- Does `COMPETITOR_YOUTUBE_ANALYTICS.engagement_rate_pct` use the same
  (likes + comments) ÷ views definition we compute for ourselves? If it includes
  shares or subscribes, our 5.34% lead may be an artifact.
- Competitor review samples are 2 rows each — far too small to support the
  rating comparison above. Treat the ratings table as indicative only.
- No pricing data exists in any table. Every pricing conclusion in this wiki is
  inferred from prospect and reviewer language, not from actual price points.
- `COMPETITOR_YOUTUBE_ANALYTICS` subscriber totals do not reconcile exactly with
  summed `subscribers_gained` (e.g. competitor 1: +332 net vs 346 gained),
  implying unsubscribes are not captured. Net figures are used above.

## Related Pages
- [[ai-product-academy]]
- [[product-manager-accelerator]]
- [[product-faculty]]
- [[hardcore-agentic-engineering]]
- [[ai-pm-academy]]
- [[openai-cookbook-courses]]
- [[youtube-performance]]
- [[linkedin-performance]]
- [[pricing-objections]]
- [[hands-on-labs-praise]]

## Source
`YOUTUBE_CHANNEL_ANALYTICS` rows 1–30; `COMPETITOR_YOUTUBE_ANALYTICS` rows 1–120
(all four competitors × 30 days); `COMPETITORS` rows 1–4;
`COMPETITOR_MAVEN_FEEDBACK` rows 1–8; `MAVEN_FEEDBACK` rows 1–11;
`YOUTUBE_COMMENTS` row 4; `LINKEDIN_POSTS` rows 2, 3, 4.
