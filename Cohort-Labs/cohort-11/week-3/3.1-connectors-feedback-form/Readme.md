# Lab 3.1: Connect Your App to Supabase Using Claude's Connectors

![image](./images/diagram.png)

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Part 1: Build a Feedback Form](#part-1-build-a-feedback-form)
- [Part 2: Store the Feedback Somewhere Real](#part-2-store-the-feedback-somewhere-real)
- [Part 3: Set Up Your Supabase Account and Project](#part-3-set-up-your-supabase-account-and-project)
- [Part 4: Connect Supabase to Claude (the Connector)](#part-4-connect-supabase-to-claude-the-connector)
- [Part 5: Connect the Application to Supabase](#part-5-connect-the-application-to-supabase)
- [Part 6: Test the Feedback Feature](#part-6-test-the-feedback-feature)

---

## Overview

In week 1 you built `contract-review-app`, and in week 2 you updated its backend. It works — but is the person using it actually satisfied? Right now you have no way to know.

To find out, we'll add a **feedback form** so users can tell you what they think.

But there's a second problem: the moment you refresh the app, your chat is gone, and your feedback has nowhere to go. So we'll also add a **database** — **Supabase**, integrated with Claude through a **connector** — to retain both the chats and the feedback.

Here's the flow for this lab:

- **Build a feedback form.** So real users can tell you how the app is doing.
- **Add a database with Supabase, connected through Claude.** So chats and feedback are saved for real instead of disappearing on refresh.

---

## Prerequisites

✅ **Lab 2.4 done** — you have a working `contract-review-app` folder.

✅ **Claude Code Desktop** installed and signed in.

---

## Part 1: Build a Feedback Form

The obvious first move is the one you'd expect: build the form itself.

Go to your Claude Code session, pointed at `contract-review-app`, and give it this prompt:

```
Add a Feedback feature to the existing Contract Review application.

Build only the frontend for the Feedback form.

- Add a "Feedback" button to the existing navbar.
- Open the form inside the app using the existing UI pattern (modal, drawer, or in-app view).
- Inspect the existing project structure and reuse existing components.
- Before implementing, follow the existing `design-system` skill for layout, typography, colors, spacing, buttons, form fields, and states.
- Keep the design consistent with the existing Contract Review application.
- Do not add login/signup.
- Do not change or break existing Contract Review functionality.

Feedback form fields:
- Rating: 1–5, required
- Feedback/comment: required
- Name: optional
- Email: optional

Include:
- Clear labels
- Client-side validation
- Submit button
- Loading state
- Success state
- Error state
- Prevent duplicate submissions while submitting

For this step, do NOT integrate Supabase yet. Use a temporary/mock submit handler so the complete frontend flow can be tested.
```

Claude will build the form itself — styled to match the rest of the app.

![feedback-form](./images/1.png)

It works — you can click through the whole flow, even see a fake success state. But hit submit for real and nothing actually happens: there's nowhere for that data to land yet. Once real users start filling this out, where does their feedback actually go?

---

## Part 2: Store the Feedback Somewhere Real

Right now the feedback form works, but its submit handler is fake — fill it out, hit submit, and the data just disappears into nothing. You need a real database — somewhere to actually store every rating and comment that comes in.

You could build that yourself: set up a database, write the code that talks to it, handle authentication, write the API endpoints that let your form send data back and forth. That's a lot of work, and it's exactly the kind of work that's easy to get wrong.

So instead of building and wiring up a database by hand, we're going to let Claude connect to database directly. Using Claude Connectors - A connector allows Claude to interact with another tool for you. Instead of switching between Claude and Database, copying information, or creating everything manually, Claude can use the connector to work with database directly.
for database we are going to use Supabase - Supabase is an online platform where we can store and manage the data our application needs. You can think of it as a ready-to-use place for keeping information, so we don’t need to build our own database from scratch.

---

## Part 3: Set Up Your Supabase Account and Project

Before Claude can connect to a database, you need a database for it to connect to. **Supabase** is a free, ready-made database — you get a real place to store data without setting up or managing a server yourself. In this lab, it's where every feedback submission and every saved chat will live.

1. Go to [supabase.com](https://supabase.com) and sign up. You can continue with GitHub, ChatGPT, SSO, or an email and password — whichever is easiest for you.

![Supabase sign up](./images/2.png)

   If you already have a Supabase account, sign in instead.

![Supabase sign in](./images/3.png)

2. If you signed up with an email and password, Supabase sends you a confirmation email. Open it and click **Confirm Email Address**.

![Confirm your email](./images/4.png)

3. Supabase will then ask you to create an organization — a container that holds your projects. Enter a name and keep the **Free - $0/month** plan.

![Create a new organization](./images/5.png)

   The remaining questions are optional and only help Supabase improve its product. Answer them or skip them, then click **Create organization**.

![Organization details](./images/6.png)

4. Next, create your first project inside the organization:
   - **Project name:** `contract-review-feedback`
   - **Database password:** set a strong password and save it somewhere safe (the **Copy** button helps).
   - **Region:** leave it on **Auto**, or pick one close to you.
   - Leave the other options at their defaults.

```
contract-review-feedback
```

![Create a new project](./images/7.png)

5. Click **Create new project** and wait a couple of minutes while Supabase finishes setting it up.

6. Once the project is ready, click **Copy** next to the project address and choose **Project URL** (it looks like `https://xxxxxxxxxxxx.supabase.co`). Save it somewhere handy — you'll paste it into a prompt in Part 5.

![Copy the Project URL](./images/8.png)

---

## Part 4: Connect Supabase to Claude (the Connector)

Your Supabase project is ready, but Claude can't reach anything outside this conversation on its own — it doesn't know your Supabase account exists. A **connector** is how you fix that: it's a direct link between Claude and an outside tool, so Claude can actually reach in and use it instead of just knowing the tool exists.

Let's add the Supabase connector:

1. In Claude, open **Customize** from the left sidebar and select the **Connectors** tab.
2. Click **Discover** and search for **Supabase**.
3. Find the **Supabase** entry listed as a **Connector** (not the Supabase *plugin*) and click **Connect**.

![Find the Supabase connector](./images/9.png)

4. Claude will show a **"Finish connecting a connector?"** screen. Click **Continue connecting**.

![Continue connecting](./images/10.png)

5. You'll land on a screen asking you to **Authorize Claude** to access your Supabase account. Select the organization you just created and click **Authorize Claude**.

![Authorize Claude](./images/11.png)

6. Claude takes you back to the connector's page, where you can review the tool permissions it now has for Supabase.

![Supabase connector details](./images/12.png)

7. Go back to **Customize → Connectors → Yours**. Supabase now appears in your list of connectors with a check mark in the **Status** column.

![Supabase connected](./images/13.png)

Your Supabase account is set up, and Claude is now connected to it. Let's put that connection to use.

---

## Part 5: Connect the Application to Supabase

Your Supabase account is ready, and Claude is connected to it. Now let's go back and replace that mock submit handler with the real thing — wiring the feedback form you already built to your actual Supabase project.

Go back to your Claude Code session, still pointed at `contract-review-app`, and give it this prompt:

> Replace `<YOUR SUPABASE PROJECT URL>` in the prompt below with the Supabase Project URL you copied in Part 3.

```
SUPABASE PROJECT (use only this one): <YOUR SUPABASE PROJECT URL>

TASK
Integrate the existing Feedback form and the Contract Review chat with Supabase.
Do not create or use any other Supabase project.

STEP 0: INSPECT FIRST
Review the existing Supabase config, client setup, env vars, and app architecture
before changing anything. Reuse what exists.

DATABASE (no auth, no user_id; the app has no login/signup)
1. `feedback`: id, rating, feedback, name, email, created_at
2. `chat_messages`: id, question, response, citation (text[], nullable),
   reasoning (text, nullable), created_at

RLS POLICIES (enable RLS on both tables)
- feedback: public INSERT only. No public SELECT, UPDATE or DELETE.
- chat_messages: public INSERT and SELECT only (the app reads chats back later).
  No public UPDATE or DELETE.

SECURITY
- The frontend uses only the anon/publishable key, read from env vars.
- Never expose a service-role key or other privileged credentials in frontend code.

FEEDBACK FORM
- Wire the existing form's submit to insert into `feedback`.
- Validate input before submit and reject invalid input (e.g. rating range,
  required fields, email format).
- Handle all states: loading (disabled submit/spinner), success, error,
  validation errors.
- Prevent duplicate submissions (disable while in flight, guard against
  double-clicks and repeat submits).

CONTRACT REVIEW CHAT
- After each question gets its response displayed, insert a new row into
  `chat_messages` with the question, response, citation and reasoning.
- If the reply has no citation or reasoning, leave those columns null/empty.
- If saving fails, the chat must keep working normally. The user must see no
  error, so log it silently. Never block or delay the response display.

CONSTRAINTS
- Preserve the existing frontend design and the `design-system` implementation.
  Reuse existing components and tokens; no visual redesign.

VERIFY (report pass/fail for each)
1. The Feedback button opens the form.
2. Valid feedback is inserted into Supabase.
3. Invalid input is rejected.
4. Success and error states work.
5. Duplicate submissions are prevented.
6. Each chat question, response, citation and reasoning is saved to `chat_messages`.
7. Existing Contract Review functionality still works.
Also confirm the RLS policies behave as specified (anon can't read feedback,
can't update or delete either table).
```

Claude will inspect your Supabase setup and create two tables: `feedback`, to store the feedback submitted by users, and `chat_messages`, to store every question asked in the chat along with the response, citation and reasoning it received. You'll use these saved chats in Lab 3.3 to build your evaluation dataset.

---

## Part 6: Test the Feedback Feature

Now that the feedback feature is ready, let's see what happens when a user actually interacts with it.

### 1. Start with the obvious test

Open the Contract Review app and click **Feedback** in the navbar.

Fill in the form with a rating and some feedback, then submit it.

![image](./images/14.png)

You should see a success message once the feedback is submitted.

### 2. What if we submit an empty form? 🤔

Try clicking **Submit Feedback** without entering anything.

![image](./images/15.png)

Check whether the app prevents the submission and shows the appropriate validation messages.

### 3. Where did our feedback go? 🔍

Now let's verify that the feedback actually reached the database.

Open your **Supabase project → Table Editor → `feedback`**.

![image](./images/16.png)

You should see your submitted feedback as a new row, including the rating, feedback, optional details, and timestamp.

### 4. Are the chat questions and responses saved too? 💬

Go back to the Contract Review chat, upload the sample contract, and ask a question like *"What are the payment terms?"*

Then open **Supabase project → Table Editor → `chat_messages`**. You should see a new row with the question you asked and the response the agent gave (plus citation and reasoning, if the agent returned them).

![image](./images/17.png)

🎉 **If you can see your feedback and your chat questions and responses in Supabase, the complete flow is working.**

---

## What You Learned

- **Connectors are how Claude reaches outside itself.** Supabase isn't something Claude has built in — the connector is what links your actual Supabase account to your Claude session, so Claude can create tables and write data on your behalf instead of you doing it by hand.

- **Now your app can hear back from real users.** With the feedback form wired to Supabase, every rating and comment a user submits lands as a real row in your database — turning "I think this app is good" into something you can actually check.

---

Feedback tells you how people feel about the app — but it doesn't tell you whether the code underneath is actually sound. That's what the next lab checks.

[Go to Lab 3.2: Review Your App Using Claude's Sub Agent →](../3.2-code-review-subagent/Readme.md)
