# Supabase Setup & SQL Execution

## Overview

In this lesson you will create a free Supabase project, run SQL to set up your database, and collect the API credentials needed for connecting Supabase to external tools like n8n.

By the end of this module you will:

- Have an active Supabase project with a live PostgreSQL database
- Know how to run SQL in the Supabase SQL editor
- Have your **Service Role Key** and **Supabase URL** saved for the n8n setup

---

## What is Supabase?

**Supabase** is an open-source Firebase alternative built on top of PostgreSQL. It gives you a hosted database, instant REST and GraphQL APIs, authentication, storage, and realtime subscriptions — all in one platform.

| Feature | What It Means |
|---|---|
| PostgreSQL | Full relational database — standard SQL |
| Auto-generated API | REST and GraphQL APIs built from your tables automatically |
| Row Level Security | Fine-grained access control per row |
| Free tier | Generous free plan — no credit card required |

---

## Step 1: Go to Supabase and Click "Start Your Project"

1. Open your browser and go to [https://supabase.com/](https://supabase.com/)
2. Click **"Start your project"**

![Supabase Homepage](./images/1.png)

---

## Step 2: Sign Up

Create a Supabase account:

- Sign up with **GitHub** (recommended — fastest), or
- Use your **email address**

![Sign Up](./images/2.png)

---

## Step 3: Create a New Organization

After signing in, Supabase will prompt you to create an organization:

1. Enter a name for your organization (e.g. your name or team name)
2. Select the **Free** plan
3. Click **"Create organization"**

![Create Organization](./images/4.png)

---

## Step 4: Create a New Project

Inside your organization:

1. Click **"New project"**
2. Enter a **Project Name** (e.g. `contract-risk-db`)
3. Set a strong **Database Password** — save this somewhere safe
4. Choose the **Region** closest to you
5. Click **"Create new project"**

> Wait 1–2 minutes while Supabase provisions your database.


![Project Setup](./images/5.png)

---

## Step 5: Open the SQL Editor

Once your project is ready:

1. In the left sidebar, click **"SQL Editor"**

![SQL Editor](./images/6.png)

---

## Step 6: Paste and Run the SQL Query

Click inside the editor, paste the full SQL query below, then run it:

```sql
-- Create playbook table
CREATE TABLE IF NOT EXISTS playbook (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  contract_type TEXT,
  topic TEXT,
  guidance TEXT,
  step_order INT,
  owner TEXT,
  created_at TIMESTAMP DEFAULT now()
);

-- Insert NDA data
INSERT INTO playbook (contract_type, topic, guidance, step_order, owner) VALUES
('NDA', 'review', 'Check mutual vs one-way NDA. Confirm disclosing and receiving party names match legal entities. Verify confidentiality period is between 1-5 years.', 1, 'Legal'),
('NDA', 'approval', 'NDA under 1 year term requires Manager approval only. NDA over 1 year requires Legal Head sign-off. NDA with foreign entities requires additional compliance check.', 2, 'Legal'),
('NDA', 'signing', 'Use DocuSign for all NDA signatures. Both parties must sign within 5 business days of draft finalisation. Store signed copy in Supabase with status active.', 3, 'Operations'),
('NDA', 'expiry', 'Set expiry reminder 30 days before NDA end date. If renewal needed restart review process from step 1. If not renewed update status to expired in database.', 4, 'Operations'),

-- Insert MSA data
('MSA', 'review', 'Verify SOW is attached before review. Payment terms must be Net-30 or better. Liability cap must be minimum 2x contract value. Check IP ownership clause exists.', 1, 'Legal'),
('MSA', 'approval', 'MSA above $50,000 requires CFO approval. MSA below $50,000 requires Department Head approval. All MSAs require Legal sign-off regardless of value.', 2, 'Finance'),
('MSA', 'signing', 'Both parties must sign MSA before any SOW work begins. No work or payments start without a fully executed MSA. Use DocuSign with audit trail enabled.', 3, 'Legal'),
('MSA', 'renewal', 'Send renewal review notice 60 days before MSA expiry. Review all SOWs under the MSA before renewal. If auto-renewal clause exists send opt-out notice 60 days before trigger date.', 4, 'Legal'),

-- Insert Lease data
('Lease', 'review', 'Confirm lease term, monthly rent amount, annual escalation clause percentage, security deposit amount, and maintenance responsibilities before signing.', 1, 'Finance'),
('Lease', 'approval', 'Lease above 3 years or above $100,000 per year requires Board approval. Lease below these thresholds requires CFO and Legal approval only.', 2, 'Finance'),
('Lease', 'signing', 'Property inspection report must be attached before signing. Lease must be signed by authorised signatory only. Register lease if term exceeds 12 months as per local law.', 3, 'Operations'),
('Lease', 'exit', 'Notice period for early exit is 90 days minimum. Penalty clause applies if exit is before 12 months. Conduct property inspection before handover. Recover security deposit within 30 days.', 4, 'Legal');

-- Verify data
SELECT * FROM playbook ORDER BY contract_type, step_order;
```

![Paste SQL](./images/7.png)

Click **"Run"** to execute. If prompted, click **"Run Without RLS"** — this bypasses Row Level Security so the insert succeeds during setup.

![Query Results](./images/9.png)

![Table Editor](./images/10.png)





---

## Step 7: Verify Your Data in the Table Editor

Confirm the data was inserted correctly:

1. In the left sidebar, click **"Table Editor"**
2. Click on the **`playbook`** table
   
![Table Editor](./images/12.png)

3. You should see all 12 rows of playbook data (4 steps each for NDA, MSA, and Lease)

![Table Data](./images/13.png)

---

## Step 8: Go to Project Settings and Open API Keys

1. In the left sidebar, click **"Project Settings"** (gear icon at the bottom)

![Project Settings](./images/14.png)

2. Click **"API"** in the settings menu
3. Scroll down to the **"Project API keys"** section

![API Keys](./images/15.png)


---

## Step 9: Copy the Service Role Secret Key

1. Find the **`service_role`** key (listed under *Legacy* or *Project API keys*)

![API Keys](./images/17.png)

2. Click **"Copy"** next to the service role key

![API Keys](./images/18.png)

3. **Paste and save it somewhere safe** — you will need this for the n8n setup

> Never expose your `service_role` key in client-side code or public repositories. It has full database access.



---

## Step 10: Copy the Supabase Project URL

1. CLick on the Connect 

![Project URL](./images/19.png)

2. At the top of the page, find the **"Project URL"** section
3. Copy the URL — it looks like:

```
https://<your-project-ref>.supabase.co
```

**Save this URL alongside your service role key** — both are required for the n8n integration.

![Project URL](./images/20.png)

---

## Summary

| Step | What You Did |
|---|---|
| Sign up | Created a Supabase account and organization |
| Project | Created a new Supabase project with a PostgreSQL database |
| SQL | Ran SQL to create the `playbook` table and insert 12 rows (NDA, MSA, Lease) |
| Verify | Confirmed data in the Table Editor |
| API Key | Copied the `service_role` secret key |
| URL | Copied the Supabase project URL |

Both the **Service Role Key** and **Project URL** are now saved — you will use them in the **n8n setup lesson**.

---

## Important Notes

### Keep Your Keys Safe

- The `service_role` key has **full database access** — treat it like a password
- Never commit it to Git or share it publicly
- Store it in a secure notes app or password manager

### Free Tier Limits

- Supabase free tier includes **500 MB database storage** and **2 GB bandwidth/month**
- Projects on the free tier **pause after 1 week of inactivity** — resume them from the dashboard if needed
