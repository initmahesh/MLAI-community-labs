# Week 1: Build Your First AI Agent

Welcome to Week 1 of the AI PM Certification.

This week you go from zero to a working product. You'll build an AI agent that answers questions about a document, then put a web app in front of it so anyone on your team can use it, without ever opening a workflow tool.

The labs build on each other. Work through them in order. No coding experience needed. You just need the accounts listed in each lab and the setup from the [Foundation module](../pre-reads/README.md).

---

## The Labs

### [Lab 1.1: Build Your First AI Agent in n8n](./1.1-n8n-agent/README.md)

A teammate sends you a 40-page document and asks, "When does this renew?" You'll build a Document Q&A Agent in n8n that takes a file and a question, and returns a short answer pointing to where it came from. If the answer isn't in the document, it says so instead of guessing.

You can import a ready-made workflow, or [build it from scratch](./1.1-n8n-agent/build-from-scratch.md) block by block to see why it works. You'll also learn how to write the instructions that control the agent.

**You'll need:** an n8n account and an OpenAI API key.

---

### [Lab 1.2: Build Your Project with Claude Code](./1.2-claude-prototype/README.md)

Your agent works, but only inside n8n. This lab gives it a face: a Contract Review web app where a user uploads a PDF, asks a question in a chat panel, and gets an answer. You'll build it with Claude Code without writing code yourself.

You'll start with simulated responses so you can check the interface first. Along the way you'll learn when to use Claude Chat, Cowork or Code, and how to pick the right model for the job.

**You'll need:** the agent from Lab 1.1 and Claude Code set up.

---

### [Lab 1.3: Build the Webhook and Connect It to Your Project](./1.3-connect-webhook/README.md)

Your agent and your app don't know about each other yet. This lab gives your n8n agent a web address (a webhook) so other apps can send it a document and a question. Then you connect your project to that address, replacing the simulated responses with real answers from your agent.

You can import a ready-made webhook workflow, or build it yourself block by block to see how it's wired.

**You'll need:** the agent from Lab 1.1 and the project from Lab 1.2.

---

### [Lab 1.4: Push Your Project to GitHub](./1.4-push-code-to-github/README.md)

Your app only exists on your laptop. This lab puts it on GitHub, so it is backed up, shareable, and has a history you can go back to. Claude Code runs the Git commands for you, and you check the result in your repo. You'll also learn why to keep the repo private when your code holds a webhook address.

**You'll need:** the app from Lab 1.3 and the GitHub account and `contract-review-app` repo from the [GitHub setup lesson](../pre-reads/0.2-setup-github-account/README.md).

---

## What You'll Have at the End

- A working document Q&A agent in n8n
- A web app that talks to your agent
- That web app saved on GitHub, with its change history
- A clear sense of which Claude mode and model to use for which task

---

> If you get stuck in any lab, each one has troubleshooting guidance built in. Read the error carefully, since most issues have a one-line fix.
