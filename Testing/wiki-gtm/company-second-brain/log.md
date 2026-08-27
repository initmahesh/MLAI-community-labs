# Build Log

Append-only. Newest entry at the bottom.

## [2026-07-10 12:05] — Wiki build/update
- Source: Snowflake CUSTOMER_INTELLIGENCE_DB.SOURCE_DATA (Composio, connection `snowflake_basic_barwal-lax`)
- Type: **first build** — no `company-second-brain/` existed in the working directory
- Tables processed (8 of 8, all present):
  - `YOUTUBE_CHANNEL_ANALYTICS` — 30 rows (2026-06-11 → 2026-07-10)
  - `YOUTUBE_COMMENTS` — 8 rows
  - `LINKEDIN_PAGE_ANALYTICS` — 30 rows (2026-06-11 → 2026-07-10)
  - `LINKEDIN_POSTS` — 5 rows
  - `MAVEN_FEEDBACK` — 11 rows
  - `COMPETITORS` — 4 rows
  - `COMPETITOR_YOUTUBE_ANALYTICS` — 120 rows (4 competitors × 30 days)
  - `COMPETITOR_MAVEN_FEEDBACK` — 8 rows
- Pages created (22):
  - clients: `tibco`, `t-mobile`, `microsoft`, `bank-ozk`, `datacrew`,
    `fermat-commerce`, `stanford`, `loblaw-companies`, `e3-global`,
    `unaffiliated-students`
  - competitors: `ai-product-academy`, `product-manager-accelerator`,
    `product-faculty`, `hardcore-agentic-engineering`, `ai-pm-academy`,
    `openai-cookbook-courses`
  - concepts: `pricing-objections`, `hands-on-labs-praise`,
    `pm-vs-engineering-balance`, `career-transition-into-ai-pm`,
    `feature-gaps-and-requests`, `instructor-teaching-style`,
    `course-logistics-friction`
  - projects: `cohort-9`, `agentic-ai-pm-certification`,
    `snowflake-claude-second-brain-lab`
  - analytics: `youtube-performance`, `linkedin-performance`,
    `competitive-landscape`
  - root: `schema.md`, `index.md`, `log.md`; empty `inbox/` created
- Pages updated: none (first build)
- Notes:
  - `MAVEN_FEEDBACK` returned **11 rows, not the 20** the skill documentation
    anticipated. Not an error — the table genuinely holds 11.
  - Two extra competitors were added beyond the `COMPETITORS` table by sweeping
    other tables for named rivals: **AI PM Academy** (`LINKEDIN_POSTS` row 3) and
    **OpenAI cookbook courses** (`YOUTUBE_COMMENTS` row 8). Neither has analytics
    or review data.
  - **Open naming collision:** "AI PM Academy" (LinkedIn) may or may not be the
    same entity as "AI Product Academy" (Dr. Marily Nika, `COMPETITORS` row 1).
    Flagged on both pages; needs human confirmation before either is acted on.
  - Two `MAVEN_FEEDBACK` rows have no usable employer ("N.A." row 1; "Currently
    between jobs" row 7). Rather than drop them, both are captured on a single
    `clients/unaffiliated-students` page.
  - `COMPETITOR_YOUTUBE_ANALYTICS` subscriber totals do not reconcile with summed
    `subscribers_gained` (competitor 1: +332 net vs 346 gained), implying
    unsubscribes are not captured. Net figures used throughout.
  - Our YouTube engagement rate (5.34%) is computed as (likes + comments) ÷ views;
    competitor rates come from a pre-computed `engagement_rate_pct` column whose
    formula is unknown. The comparison in `competitive-landscape` is directional
    only, and says so.
  - Competitor review samples are 2 rows each — too small to support the ratings
    comparison. Noted on every competitor page.
  - Four structural data gaps recorded at the foot of `index.md`: no pricing, no
    outcomes, no cohort attribution, no curriculum table.
