# Set Up Your Jev API Key

**Jev** is a **System One** model from [Typesafe](https://docs.typesafe.ai/agent-skill): built for fast decisions, not writing. It picks an option, scores it, or gives a probability in an instant.

In this lab you'll install the Jev plugin, create your Typesafe API key, store it securely, and run a quick test to confirm everything works.

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Step 1: Install the Jev Plugin](#step-1-install-the-jev-plugin)
- [Step 2: Create Your API Key](#step-2-create-your-api-key)
- [Step 3: Store Your API Key Securely](#step-3-store-your-api-key-securely)
- [Step 4: Verify the Connection](#step-4-verify-the-connection)
- [What You Learned](#what-you-learned)
- [Reference](#reference)

---

## Prerequisites

✅ **Claude Code Desktop** installed and signed in.

✅ **Claude Code available in your terminal.** You'll run two `claude plugin` commands in Step 1.

---

## Step 1: Install the Jev Plugin

The plugin is what teaches Claude about Jev: what it can do and how to call it.

In your terminal (in Claude Code Desktop, click the terminal icon at the top right), run these two commands:

```bash
claude plugin marketplace add typesafe-ai/skills
claude plugin install typesafe@typesafe-ai
```

The first command adds Typesafe's skill marketplace. The second installs the Typesafe plugin from it.

![image](../images/3.png)

Restart Claude Code so it picks up the plugin.

---

## Step 2: Create Your API Key

Before Claude can reach Jev, you need a Typesafe API key.

1. Go to [https://console.typesafe.ai/](https://console.typesafe.ai/).
2. Enter your email.
3. Agree to the terms and conditions.

![image](../images/5.png)

4. Skip the next steps.
5. Click **Enter console**.

![image](../images/6.png)

6. When asked "Can you chat with Jev, TypeSafe's new model?", click **No**.
7. A message says "TypeSafe only responds with structured decisions". Click **Close**.
8. Click **API keys** in the sidebar.
9. Click **Create API key**, give the key a name, and click **Create key**.

![image](../images/7.png)

10. Copy the key and keep it somewhere safe for the next step.
11. If your balance shows zero, click **Balance**, then **Add funds**.

> ⚠️ Keep your key private. Don't paste it into any file you might share, and never commit it to GitHub.

---

## Step 3: Store Your API Key Securely

Keep the key out of the chat. Use one of these two options.

**Option A — environment variable** (simplest):

```bash
export TYPESAFE_API_KEY="your-key-here"
```

Run this before launching Claude Code, or add it to your shell profile (`~/.zshrc` or `~/.bashrc`) so it persists across sessions.

**Option B — credentials file** (more durable):

```bash
mkdir -p ~/.config/jev && umask 077
echo 'JEV_API_KEY=your-key-here' > ~/.config/jev/credentials
chmod 600 ~/.config/jev/credentials
```

The `jev-evaluate` skill reads from `JEV_API_KEY`, `TYPESAFE_API_KEY`, or `~/.config/jev/credentials` — whichever it finds first. It never prints the key, even in error messages.

---

## Step 4: Verify the Connection

Open Claude Code Desktop, start a new chat, and paste this prompt:

```text
I've installed the TypeSafe plugin in Claude Code.

Here is my API key: <ADD YOUR API KEY HERE>

1. UNDERSTAND JEV
Read https://docs.typesafe.ai/llms.txt. Jev returns three shapes only: Choice (pick one
option), Score (a position on an ordered rubric), Noul (a probability from 0 to 1).
It does not generate text.

2. VERIFY THE CONNECTION
Make one trivial Jev call and report ok/fail plus latency. On failure, print the exact
error text. Never print any part of the key.

3. RULES
- Jev stays OFF by default. Use it only when I say "use jev".
- Jev decides, Claude writes.
- If Jev's confidence is below 0.7, flag the row for human review rather than accepting
  it silently.
- Ask before sending contract text to Jev.
- NEVER fall back to Claude silently if a Jev call fails. Stop and show the error.
  A silent fallback would make a failed demo look like a successful one.

4. INSTRUMENT EVERY CALL
For every Jev call record latency_ms, input_tokens, output_tokens, and cost at $0.042
per 1M input tokens with output free. Keep a running session total. After any batch,
print: total calls, wall-clock time, total tokens, total cost.
Report Jev's cost separately from Claude's. Never merge them into one number.
```

You should see something like:

```text
OK  latency_ms=360  detail=positive
total calls : 1
tokens      : 325 (in 294 / out 31)
Jev cost    : $0.00001235  @ $0.042/1M input, output free
```

If you see an error instead, check:
- The key is set in your environment or credentials file and Claude Code was restarted after.
- Your Typesafe account has a non-zero balance.
- You pasted the full key with no extra spaces.

> The `$0.042 per 1M input tokens, output free` rate is the one used in this lab. Check your own TypeSafe plan for your rate.

---

## What You Learned

- **Jev needs a plugin and a key.** The plugin teaches Claude how to call it; the key is what lets the calls through.
- **Store the key outside the chat.** Use an env var or a credentials file — never paste it into a file you might share.
- **Jev is off by default.** It only runs when you say "use jev", so Claude keeps working normally otherwise.
- **Jev makes three kinds of decisions.** Choice, Score, and Noul (probability).
- **Jev decides, Claude writes.** Claude orchestrates; Jev makes the judgment.
- **Failed calls must be loud.** Never let Claude silently substitute its own answer if Jev fails.

---

## Reference

- [Typesafe agent skill docs](https://docs.typesafe.ai/agent-skill)
- [Typesafe LLM docs](https://docs.typesafe.ai/llms.txt)
- [Typesafe console](https://console.typesafe.ai/)