# Build Data Pipelines with Claude Code

![image](./imaged/1.png)

An end-to-end AI pipeline that collects customer intelligence from multiple sources, analyzes it with Claude, generates an interactive dashboard, and publishes results to Snowflake — all triggered by a single slash command.

---

## What You Will Build

By the end of this series you will have a fully working pipeline where:

1. Claude scrapes **LinkedIn** and **YouTube** live using Apify
2. Claude parses your **customer feedback files** and **meeting notes**
3. Claude generates an **interactive HTML dashboard** with a health score, pain points, feature requests, and cross-source insights
4. All data is published to a **Snowflake data warehouse** for ongoing querying and analysis

---

## Modules

| # | Module | What you set up |
|---|--------|----------------|
| [00](./00-setup-snowflake/Readme.md) | **Snowflake Setup** | Provision a free Snowflake trial account and prepare it for the pipeline |
| [01](./01-setup-composio/readme.md) | **Composio + Snowflake** | Connect Snowflake to Claude via Composio's MCP server |
| [02](./02-setup-apify/readme.md) | **Apify Connector** | Add Apify to Claude so it can scrape live web data |
| [03](./03-data-ingestion-pipeline/readme.md) | **Data Ingestion Pipeline** | Install the Customer Intelligence Hub skill and run the full pipeline |

Work through the modules in order — each one builds on the previous.

---

## Prerequisites

- A Google account (for Apify and Snowflake sign-up)
- Claude desktop app installed
- No coding experience required
