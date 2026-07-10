# Schema — Company Second Brain

This file explains what this wiki is, where it comes from, and how to extend it.
Read this first, then `index.md`, before answering questions from this wiki.

## 1. Business description

MLAI Community is a cohort-based education business. It sells a paid, live AI
Product Management program (variously referred to as the "Agentic AI PM
Certification" and the "AI PM course") delivered on **Maven**, taught by founder
**Mahesh**, supported by a mentor team. Cohorts run roughly six weeks; Cohort 9
completed on 2026-07-05.

The curriculum blends conceptual AI/ML foundations (models, MCP, RAG, evals,
pricing) with hands-on labs, including a Snowflake + Claude "second brain" data
pipeline lab. Students are predominantly mid-to-senior Product Managers,
Program Managers, and data leaders transitioning into AI roles.

Demand is generated through two owned channels — a **YouTube** channel (~8.7K
subscribers) and a **LinkedIn** page (~5.9K followers) — and converts into paid
Maven cohort enrollments. The business competes against four other Maven-hosted
AI PM courses.

## 2. Source artifact types

All pages are built from `CUSTOMER_INTELLIGENCE_DB.SOURCE_DATA` in Snowflake.

| Table | Rows | Column shape |
|---|---|---|
| `YOUTUBE_CHANNEL_ANALYTICS` | 30 | `row_id, report_date, views, watch_hours, avg_view_duration_sec, likes, comments, subscribers_gained, subscribers_total` |
| `YOUTUBE_COMMENTS` | 8 | `comment_id, video_title, channel_name, commenter_name, comment_text, like_count, posted_date` |
| `LINKEDIN_PAGE_ANALYTICS` | 30 | `row_id, report_date, impressions, unique_views, clicks, engagements, followers_gained, followers_total` |
| `LINKEDIN_POSTS` | 5 | `post_id, author_name, author_title, post_text, reactions, comments_count, posted_date` |
| `MAVEN_FEEDBACK` | 11 | `feedback_id, student_name, student_title, student_company, rating, public_review, private_note, submitted_date` |
| `COMPETITORS` | 4 | `competitor_id, company_name, course_name, instructor_name, platform, youtube_handle, notes` |
| `COMPETITOR_YOUTUBE_ANALYTICS` | 120 | `row_id, competitor_id, report_date, views, subscribers_gained, subscribers_total, engagement_rate_pct` |
| `COMPETITOR_MAVEN_FEEDBACK` | 8 | `feedback_id, competitor_id, reviewer_title, rating, public_review, submitted_date` |

Both analytics tables cover **2026-06-11 → 2026-07-10** (30 days), which is the
canonical "period covered" for every analytics page in this wiki.

## 3. Wiki page types

**Entity pages** (`clients/`, `competitors/`, `concepts/`, `projects/`) use:

```markdown
# [Entity Name]
## Summary          — 2-3 sentences: what this is, why it matters
## Key Facts        — concrete facts, each attributed to a source table/row
## Open Questions   — unresolved gaps
## Related Pages    — [[wiki-links]]
## Source           — e.g. "MAVEN_FEEDBACK rows 7, 12; LINKEDIN_POSTS row 3"
```

Competitor pages additionally fold into Key Facts: instructor/course/platform
and positioning from `COMPETITORS`; subscriber trend (start → end, total gained)
from `COMPETITOR_YOUTUBE_ANALYTICS`; and a paraphrased sentiment summary
(average rating, common praise and criticism themes) from
`COMPETITOR_MAVEN_FEEDBACK`.

**Analytics pages** (`analytics/`) use:

```markdown
## Summary       — one paragraph, plain language, on the trend
## Key Metrics   — table: starting vs ending totals, total gained, peak day, daily average
## Notable Days  — spikes/drops, with a one-line hypothesis where inferable
## Related Pages
## Source
```

`competitive-landscape.md` instead uses: Summary / Key Metrics (us + all four
competitors) / Where We're Ahead / Where We're Behind / Related Pages / Source.

## 4. Naming conventions

- File names are the kebab-case of the entity name: `Bank OZK` → `bank-ozk.md`.
- Links are `[[kebab-case-name]]`, matching the file name without `.md`.
- Companies keep their common name, not their feedback-row spelling: a row
  reading `ex Microsoft` becomes `[[microsoft]]`, with the "ex-" relationship
  captured on the page body.

## 5. Ingest workflow

Future updates re-run the `company-second-brain-wiki` skill. It must:

1. Read `schema.md`, `index.md`, and `log.md` **before** writing anything.
2. Re-query the eight Snowflake tables above.
3. **Add or update** pages only. Never wipe or recreate the tree.
4. Leave `schema.md` untouched unless the source schema itself changed.
5. Append one entry to `log.md`.
6. Regenerate the `index.md` table to include any new pages.

Loose notes dropped into `inbox/` are unprocessed input; a future run should
fold them into the relevant entity page and then clear them.

## 6. index.md format

A single table listing every page:

```markdown
| Page | Type | Last Updated | Summary |
|---|---|---|---|
```

## 7. log.md format

Append-only, newest entry at the bottom:

```markdown
## [YYYY-MM-DD HH:MM] — Wiki build/update
- Source: Snowflake CUSTOMER_INTELLIGENCE_DB.SOURCE_DATA
- Tables processed: [list]
- Pages created: [list]
- Pages updated: [list]
- Notes: [anything skipped or worth flagging]
```

## 8. Cross-linking rules

Link an entity **every time it is named** on another page. If a competitor is
mentioned in a YouTube comment, the concept page covering that comment links to
the competitor page. If a student's employer appears in feedback, the concept
page links to the client page. Unresolved links (a `[[name]]` with no file yet)
are acceptable — they mark a page worth creating on the next run.

## 9. Standing rules

- **Never delete pages.** Only add or update them.
- **Always paraphrase feedback.** Never reproduce a review or private note
  verbatim at length. Short phrases (<10 words) that carry specific meaning are
  acceptable, in quotes.
- **Private notes are internal.** `MAVEN_FEEDBACK.private_note` content may
  inform pages but must be paraphrased and marked as sourced from a private
  note, never quoted.
- **Always cite the source table and row** for every factual claim.
- Analytics figures are computed over the full 30-day window unless stated.
