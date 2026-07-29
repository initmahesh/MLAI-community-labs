# Week 3 — Building Your AI Agent

---

## What This Week Is About

By now you have a working web application and a solid understanding of how AI works. This week, you take the next big step — you are going to build your own AI agent and connect it directly to your app.

Think of an AI agent as a smart assistant that does not just answer questions, but actually takes actions. It reads documents, remembers past conversations, searches for information, and makes decisions — all on its own. By the end of this week, your app will have one of these agents running inside it, and you will be able to watch it work in real time.

This week has two labs. They build on each other, so complete them in order.

---

## Quick Links

| Lab | What You Will Do |
|---|---|
| [Lab 01 — Build Your Agent in Azure AI Foundry](./01-azureaifoundary-agent/Readme.md) | Create, configure, test, and publish your AI agent |
| [Lab 02 — Connect Your Agent to Your App](./02-integration-of-azureagent-with-your-app/Readme.md) | Integrate the agent into your web application |

---

## Lab 01 — Build Your Agent in Azure AI Foundry

**[→ Go to Lab 01](./01-azureaifoundary-agent/Readme.md)**

In this lab, you will use **Azure AI Foundry** — Microsoft's platform for building and managing AI agents — to create a Contract Review Agent from scratch. No coding required.

You will walk through 12 parts, from creating the agent to publishing it inside Microsoft Teams so your whole team can use it.

**What you will build:** A smart contract-review agent that reads uploaded legal documents, flags risky clauses, answers follow-up questions, and remembers past conversations.

**What you will learn:**
- How to create and configure an AI agent with custom instructions
- How to give the agent tools — like the ability to read documents and search the web
- How to add memory so the agent remembers things between conversations
- How to set safety guardrails to keep the agent on-task
- How to publish the agent to Microsoft Teams and Microsoft 365 Copilot
- How to monitor usage, cost, and response quality in real time

**Time to complete:** Approximately 60–90 minutes

---

## Lab 02 — Connect Your Agent to Your App

**[→ Go to Lab 02](./02-integration-of-azureagent-with-your-app/Readme.md)**

In this lab, you will connect the Azure AI agent you built in Lab 01 to the web application you built in Week 1. This is where your two worlds — your app and your agent — come together.

You will use a Claude skill to automatically update your codebase, then configure your environment and database to work with the new agent.

**What you will build:** A fully integrated web application that talks to your Azure AI agent and logs every conversation in Azure AI Foundry's Traces dashboard.

**What you will learn:**
- How to use a Claude Code skill to integrate Azure AI Foundry into an existing app
- How to configure environment variables for Azure authentication
- How to update your Supabase database to support the new agent
- How to deploy the updated app to Netlify
- How to track token usage and costs in Azure AI Foundry Traces

**Time to complete:** Approximately 30–45 minutes

---

## Before You Start

Make sure you have completed the following before jumping into Lab 01:

- **Week 1 Lab** — Your web application needs to be built and deployed
- **An Azure account** with Azure AI Foundry access — [Start a free trial here](https://azure.microsoft.com)
- **A Microsoft Teams account** — needed in Lab 01 Part 9 when you publish your agent

If you are missing any of these, get them set up first. Both labs assume these are ready to go.

---

*MLAI Community Labs · Bootcamp 3 · Week 3*