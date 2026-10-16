# Week 1: Build Your First AI Agent

Welcome to Week 1 of the AI PM Certification.

This week you go from zero to a working product. You'll build an AI agent that answers questions about a document, then put a web app in front of it so anyone on your team can use it, without ever opening a workflow tool.

The labs build on each other. Work through them in order. No coding experience needed. You just need the accounts listed in each lab and the setup from the [Foundation module](../0-foundation/README.md).

---

## The Labs

### [Lab 1.1: Build Your First AI Agent in n8n](./1.1-n8n-agent/README.md)

A teammate sends you a 40-page document and asks, "When does this renew?" You'll build a Document Q&A Agent in n8n that takes a file and a question, and returns a short answer pointing to where it came from. If the answer isn't in the document, it says so instead of guessing.

You can import a ready-made workflow, or [build it from scratch](./1.1-n8n-agent/build-from-scratch.md) block by block to see why it works. You'll also learn how to write the instructions that control the agent, and how to give it a web address other apps can call.

**You'll need:** an n8n account and an OpenAI API key.

---

### [Lab 1.2: Build and Connect Your Prototype with Claude Code](./1.2-claude-prototype/README.md)

Your agent works, but only inside n8n. This lab gives it a face: a Contract Review web app where a user uploads a PDF, asks a question in a chat panel, and gets an answer. You'll build it with Claude Code without writing code yourself.

You'll start with simulated responses so you can check the interface first. Then you'll connect the app to the real agent from Lab 1.1. Along the way you'll learn when to use Claude Chat, Cowork or Code, and how to pick the right model for the job.

**You'll need:** the agent from Lab 1.1 and Claude Code set up.

---

## What You'll Have at the End

- A working document Q&A agent in n8n
- A web app that talks to your agent
- A clear sense of which Claude mode and model to use for which task

---

> If you get stuck in any lab, each one has troubleshooting guidance built in. Read the error carefully, since most issues have a one-line fix.
