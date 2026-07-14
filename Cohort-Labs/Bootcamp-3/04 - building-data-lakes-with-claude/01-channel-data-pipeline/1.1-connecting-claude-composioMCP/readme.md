# Connecting Claude to Composio via MCP

---

## What Is MCP?

Before we do anything, let's make sure the concept lands.

MCP stands for **Model Context Protocol**. It's the standard language Claude uses to say: *"I want to use this tool — here's my request, here's what I need back."*

Without MCP, Claude is limited to what you type into the chat. With MCP, Claude can reach out to real systems — write to a database, pull from an API, trigger an action in an external tool — all within a single conversation.

Composio acts as the MCP server. It's the endpoint Claude will call every time it needs to interact with Snowflake, YouTube, or LinkedIn or diff chanels.

```
Claude
  ↓  (MCP)
Composio Server
  ├── Snowflake
  ├── YouTube
  └── LinkedIn
```

Once we wire this up, that entire stack becomes available to Claude on demand.

---

## Step 1: Generate the MCP URL

Go to this page:

```
https://composio.dev/toolkits/snowflake/framework/claude-code
```

Click **Generate MCP URL** and copy the URL that appears.

![Generate MCP URL](./images/1.png)

Keep that URL handy — you'll use it in the next step.

---

## Step 2: Tell Claude About Composio

Open the Claude desktop app and start a new chat.

Paste this prompt, replacing the placeholder with the URL you just copied:

```
Run the following command in the terminal and add the Composio MCP server:

<paste your MCP URL here>
```

Claude will run the command and register Composio as a connected tool.

![Claude running the MCP command](./images/2.png)

Once it does, Claude knows where Composio lives. From this point on, Claude can reach out to Composio any time it needs to interact with your connected tools.

---

> **What just happened?**
>
> Claude ran a terminal command that registered Composio's MCP endpoint in its tool configuration. This is a one-time setup step — you don't need to repeat it in future sessions. Claude will remember this connection.

---

## Step 3: Authenticate the Connection

The last step is giving Claude permission to actually use the connection.

After the command runs, Claude will open a browser window asking you to authorize it. Follow the prompts and approve the access.



Once you approve, the connection is live.

![Claude running the MCP command](./images/3.png)

That's it. Claude now has a live, authorized connection to Composio.

---

## What You've Actually Built

Let's take stock of where we are.

You haven't written a pipeline yet. You haven't queried a database. But you've done the hard part — you've connected three systems together:

```
Claude
  ↓  (MCP)
Composio
```

This is the backbone of everything we're about to build.

Claude can now reach Composio on demand. Composio already holds your authenticated connection. That means Claude can push data into your database, query it, and retrieve results — all from within a single conversation and also pull the data, without you doing anything manually.

This is exactly what a data engineering team sets up before they write a single line of pipeline code. Authentication first. Integration layer second. Logic third.

-
## Summary

You've done three things that matter:

1. Generated a unique MCP URL that identifies your Composio setup to Claude
2. Registered that URL with Claude so it knows where Composio lives
3. Authorized the connection so Claude has permission to use it

Claude is no longer in a closed room. It now has a direct line to Composio — and through Composio, to every tool you've connected.

---

## Pull Your First Data

The connection is live. Let's actually use it.

Below are ready-to-run prompts you can paste directly into Claude. Each one tells Claude exactly what to fetch and how to structure the output. Try them one at a time — watch Claude reach out through Composio and come back with real data from your accounts.

---

### YouTube Analytics

**Channel Overview**
```
Using Composio, pull my YouTube channel analytics and give me:
- Total subscribers
- Total views (all time)
- Watch time (last 28 days)
- Top 5 videos by view count with their titles, views, and like counts

Then:
1. Get my YouTube channel name
2. If a folder doesn't already exist at second-brain/projects/<channel-name>/, create it
3. Save the full analytics data as a JSON file at:
   second-brain/projects/<channel-name>/channel-overview.json
```

**Video Engagement Report**
```
Using Composio, fetch my last 10 YouTube videos and for each one collect:
- Title
- Published date
- View count
- Like count
- Comment count
- Engagement rate (likes + comments / views)

Sort by engagement rate, highest first.

Then:
1. Get my YouTube channel name
2. If a folder doesn't already exist at second-brain/projects/<channel-name>/, create it
3. Save the full results as a JSON file at:
   second-brain/projects/<channel-name>/video-engagement.json
```

**Comment Sentiment Snapshot**
```
Using Composio, pull the 20 most recent comments from my top-performing YouTube video.
Summarize the overall sentiment, highlight the top 3 themes people are discussing,
and flag any negative feedback worth responding to.

Then:
1. Get my YouTube channel name
2. If a folder doesn't already exist at second-brain/projects/<channel-name>/, create it
3. Save the raw comments plus the sentiment summary as a JSON file at:
   second-brain/projects/<channel-name>/comment-sentiment.json
```

---

### LinkedIn Analytics

**Profile & Page Performance**
```
Using Composio, pull my LinkedIn page analytics and give me:
- Follower count
- Follower growth over the last 30 days
- Top 5 posts by impressions with their content preview and engagement numbers

Then:
1. Get my LinkedIn page or profile name
2. If a folder doesn't already exist at second-brain/projects/<page-name>/, create it
3. Save the full analytics data as a JSON file at:
   second-brain/projects/<page-name>/page-performance.json
```

**Post Engagement Report**
```
Using Composio, fetch my last 10 LinkedIn posts and for each one collect:
- Post preview (first 100 characters)
- Published date
- Impressions
- Reactions
- Comments
- Shares
- Engagement rate

Sort by engagement rate, highest first.

Then:
1. Get my LinkedIn page or profile name
2. If a folder doesn't already exist at second-brain/projects/<page-name>/, create it
3. Save the full results as a JSON file at:
   second-brain/projects/<page-name>/post-engagement.json
```

**Audience Demographics Snapshot**
```
Using Composio, pull my LinkedIn follower demographics:
- Top 5 industries my followers work in
- Top 5 job functions
- Top 5 locations

Then tell me: based on this audience, what type of content would likely
perform best on my page?

Finally:
1. Get my LinkedIn page or profile name
2. If a folder doesn't already exist at second-brain/projects/<page-name>/, create it
3. Save the demographics data plus the content recommendation as a JSON file at:
   second-brain/projects/<page-name>/audience-demographics.json
```

---

### Combined Cross-Channel Report

Once both channels are pulling data, try this:

```
Using Composio, pull the last 30 days of analytics from both my YouTube channel
and my LinkedIn page. Then give me:

1. A side-by-side comparison of total reach (views vs impressions)
2. Which platform had higher engagement rate
3. My top-performing piece of content on each platform
4. One recommendation for where to focus more effort this month, and why

Then:
1. Get both the YouTube channel name and LinkedIn page name
2. Create a shared folder at second-brain/projects/cross-channel/ if it doesn't exist
3. Save the full combined report as a JSON file at:
   second-brain/projects/cross-channel/30-day-report.json
```

This is the kind of query that used to require a business analyst, a spreadsheet, and two hours of manual data pulling. Now it's one prompt — and the results are automatically saved to your project folder, ready for the next pipeline step.

---

> **What's happening under the hood?**
>
> When you run any of these prompts, Claude is calling Composio's MCP tools in real time. Composio authenticates with YouTube and LinkedIn using the OAuth tokens you set up, fetches the requested data, and returns it to Claude — all within seconds. You're not seeing cached data. You're seeing live numbers from your accounts right now.

---

## What's Next

You've connected Claude to Composio, and you've seen it pull live data from YouTube and LinkedIn with a single prompt.

In the next lesson, we'll take this further — building a proper data pipeline that runs these queries automatically, structures the output, and loads everything into your Snowflake data lake for long-term storage and analysis.

---

## Claude Concepts Covered in This Lesson

| Concept | Where it appeared | Learn more |
|---------|-------------------|------------|
| **MCP (Model Context Protocol)** | **What Is MCP?** — *"MCP stands for Model Context Protocol. It's the standard language Claude uses to say: 'I want to use this tool — here's my request, here's what I need back.'"* | [MCP Documentation →](https://docs.anthropic.com/en/docs/claude-code/mcp) |
| **MCP Server** | **What Is MCP?** — *"Composio acts as the MCP server. It's the endpoint Claude will call every time it needs to interact with Snowflake, YouTube, or LinkedIn."* | [Claude Code Overview →](https://docs.anthropic.com/en/docs/claude-code) |
| **Tool Connections** | **Pull Your First Data** — *"When you run any of these prompts, Claude is calling Composio's MCP tools in real time."* | [Claude Code Integrations →](https://docs.anthropic.com/en/docs/claude-code) |

---

[← Back to module index](../README.md)
