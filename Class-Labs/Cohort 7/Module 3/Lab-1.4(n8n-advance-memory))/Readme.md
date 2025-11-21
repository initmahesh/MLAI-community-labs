# Lab 1.4: n8n Advanced Memory - Long-Term Memory Demonstration

![](./images/banner.jpg)

## Description

In this lab, we will be creating a workflow that demonstrates how you can integrate simple memory in n8n. You have already seen examples of basic memory integration. Now, in this lab, we will be showing you an example of long-term memory.

**Key Difference:** In the previous lab, when you create a new session, the memory will vanish. However, in this lab, even after you create a new session, the memory will stay and persist.

## Key Differences: Short-Term Memory vs Long-Term Memory

| Feature | Short-Term Memory | Long-Term Memory |
|---------|-------------------|------------------|
| **Persistence** | Memory is cleared when a new session is created | Memory persists across sessions |
| **Duration** | Temporary - exists only during the current session | Permanent - stored and retrievable across multiple sessions |
| **Storage** | Stored in memory/RAM (volatile) | Stored in persistent storage (database/file system) |
| **Use Case** | Quick, temporary context for a single conversation | Historical context that needs to be remembered across sessions |
| **Session Independence** | Tied to the current session | Independent of session creation |

---

## Prerequisites

Before beginning this lab, ensure you have completed the following:

- **New to n8n!** Set up your account: **[Click Here](../../Module%200%20-%20Prerequisite/n8n-loginSetup/Doc.md)**
- **Generate your OpenAI API key:** **[Click Here](https://youtu.be/YyaZ8zaGS-Q?si=bOw8C_TWgMg8S1hU)**
- **Download n8n workflow file:** **[Click Here](https://drive.google.com/file/d/1Lq8sbLLdIUtCsSeTGneGzVCfAdAnkj3L/view?usp=drive_link)**

---

### Step 1: Set Up Your n8n Account

If you haven't already set up your n8n account, follow the **[Prerequisites](#prerequisites)** section above to:

1. **Create** your n8n account (cloud or self-hosted)
2. **Log in** to your n8n dashboard

> Once logged in, you're ready to create your first workflow!

---

### Step 2: Import the Workflow

Now let's import the pre-built workflow into n8n:

1. Click on **"Create Workflow"** button in your n8n dashboard

   ![](./images/img-4.png)

2. Go to the menu (three dots or hamburger icon) and select **"Import from File"**

3. Upload the **JSON workflow file** that you downloaded from the Prerequisites section

   ![](./images/img-5.png)

4. The workflow will be imported and displayed on your canvas

   ![](./images/flow.png)

---

## Problem with Short-Term Memory & Why We Need Long-Term Memory

### Problems with Short-Term Memory

#### Step 1: Previous Lab

In the previous lab, your workflow was like this, as you can see in the image below:

![](./images/flow.png)

#### Step 2: Previous Lab Workflow

Now, when you open the chat query and tell the agent that "Hey, my name is XYZ", and then in the second iteration you ask the agent "What is my name?", the agent was able to tell your name.

![](./images/parttwo.png)

#### Step 3: Creating a New Session

Now, just save the workflow and refresh the page, and ask the agent to greet with your name. Now the agent fails because a new session has been created and all your previous context has been removed.

**Conclusion:** This demonstrates the limitation of short-term memory - it only works within a single session. Once a new session is created (by refreshing the page), all the previous context and information is lost. This is why we need long-term memory to persist information across multiple sessions.

![](./images/partone.png)

---

## Phase 2: Google Cloud Console Configuration

Now, before jumping to the long-term memory implementation, we need to setup some configuration first, which will be done in Google Cloud Console.

### Step 1: Access Google Cloud Console

Go to this URL: [Click here](https://docs.n8n.io/integrations/builtin/credentials/google/oauth-single-service/?utm_source=n8n_app&utm_medium=credential_settings&utm_campaign=create_new_credentials_modal) and click on **Google Cloud Account**.

![](./images/gcaccount.png)

---

### Step 2: Open Google Cloud Console

Now click on **Console**.

![](./images/console.png)

---

### Step 3: Connect Google Account

It will ask you to connect with your Google account. Once you are done, it will redirect to a dashboard, something like this as you can see in the image below:

![](./images/ds.png)

---

### Step 4: Create New Project

Now click on the **Project** dropdown and click on **New Project**.

![](./images/project.png)

![](./images/createproject.png)

---

### Step 5: Enter Project Details

Enter a project name and click on the **Create** button.

![](./images/projectname.png)

---

### Step 6: Select Project

Now, from the notification section, click on **Select Project**.

![](./images/notification.png)

---

### Step 7: Click on Breadcrumb Icon

![](./images/sidebar.png)

---

### Step 8: Navigate to OAuth Consent Screen

Click on **API & Services** > **Enable API and Services**.

![](./images/apiservices.png)

---

### Step 9: Configure OAuth Consent Screen

1. Click on **OAuth Consent screen**.

   ![](./images/oauthscreen.png)

2. Now click on **Get started**.

   ![](./images/getstarted.png)

3. Provide the **App name** and **Support email address**.

   ![](./images/appname.png)

4. Now in the **Audience** section, click on **External**.

   ![](./images/external.png)

5. In the **Contact information**, provide the email address again.

   ![](./images/contactinfo.png)

6. Final step: Click on **Agree** and click on **Create**.

   ![](./images/finish.png)

   ![](./images/create.png)

7. Now click on **Create OAuth client**.

   ![](./images/authclient.png)

8. Select **Web application**.

   ![](./images/webapplication.png)

9. Provide the **Name**.

   ![](./images/authname.png)

---

### Step 10: Select Google Doc Tool in n8n

Now go to n8n and click on **Agent Tools**. A tools section will appear on the right side. Select **Google Doc tool**.

**Important:** Make sure you are selecting the **Google Doc tool** - you are not using the Google Doc component, you are using the **Google Doc tool**.

![](./images/n8ntool.png)

1. Click on the **Google Doc tool**.
2. Click on **Create credentials**.
3. Copy the **OAuth Redirect URL**.

   ![](./images/urln8n.png)

---

### Step 11: Add OAuth Redirect URL in Google Cloud Console

Now go back to the Google Cloud Console where you left off. Click on **Add URI** and paste the URL that you copied from n8n.

![](./images/redirecturl.png)

![](./images/addingURL.png)

---

### Step 12: Copy Client ID and Client Secret

Now click on the **pen icon** and copy the **Client ID** and **Client Secret**. Store them somewhere safe as you will need them later.

![](./images/edit.png)

![](./images/cred.png)

---

### Step 13: Add Test User

Now from the sidebar, go to the **Audience** section and in the **Test users** section, add the test user email address.

![](./images/testuser.png)

![](./images/teset.png)

---

### Step 14: Navigate to API Library

1. Now go to **API & Services** > **Library**.

   ![](./images/lib.png)

2. In the search box, search for **Google Docs API** and press Enter.

   ![](./images/search.png)

3. Select **Google Docs API**.

   ![](./images/gdoc.png)

4. Make the API enable.

   ![](./images/enable.png)

---

### Step 15: Add Credentials in n8n

Now go to n8n in the **Credentials** section and add the **Client ID** and **Client Secret** that you have generated. Remember, we told you to store them somewhere in Step 12.

After that, click on **Sign in with Google** and add the same account that you mentioned in the test user while creating your Client ID and Client Secret.

### ⚠️ Most Important Point

**You must use the same Google account that you added as a test user in Step 13 when signing in with Google. This is critical for the authentication to work properly.**

![](./images/addingcred.gif)

---

### Step 16: Create a New Google Doc

Now create a new Google Doc and copy the **Document ID** from the URL.

![](./images/googledoc.png)

---

### Step 17: Configure Google Doc Tool

1. Now open the Google Doc tool and select the operation **Update**.
2. Add the **Document ID**.
3. In the **Text** field, select the **star icon** make it define by the model.

   ![](./images/addingdocURL.png)

4. Click on the **Description** field and add the description below:

   ![](./images/addingdecription.png)

   ```
   Use this tool to store all user and agent conversations into Google Docs. It serves as a long-term memory system, allowing the agent to recall information from past interactions whenever needed.
   ```

---

### Step 18: Duplicate and Configure Get Operation

1. Now copy the tool and paste it one more time.
2. Click on the copied tool and change the action to **Get** only.
3. Connect it with your agent.

   ![](./images/copy.gif)

---

### Step 19: Rename the Tools

Now change the name of both tools to the following:

- First tool (Update operation): `save_long_term_memory`
- Second tool (Get operation): `retrieve_long_term_memory`

![](./images/chamgingname.gif)

---

### Step 20: Add System Message to Agent

Now click on the **Agent** part and in the **System Message** field, add the prompt below:

```
You are a highly capable assistant with long-term memory.


TOOLS
save_long_term_memory: Stores conversation content in Google Docs for long-term memory.
retrieve_long_term_memory: Retrieves past stored information.
MEMORY RULES
ALWAYS SAVE
After every user message, you must call save_long_term_memory with the full user message, without exception.
This is mandatory and has no conditional checks.

WHEN TO RETRIEVE
Call retrieve_long_term_memory whenever:

The user asks something related to past discussions.
Context from earlier conversations may be useful.
PRIORITY
Storing memory is always executed after each user message.
You must not wait for user confirmation.
You must not skip saving.
If the user continues a topic or asks something dependent on past information, attempt retrieval first, then respond.

FALLBACK RULE
Never say "I don't know" without first attempting retrieve_long_term_memory.
```

![](./images/systemmessage.png)

---

### Step 21: Test the Workflow

Now you have completed all the steps. It's time to test!

1. First, open the chat and ask something, for example: **"My name is ABC"**.

   ![](./images/testone.png)

2. Then go to your Google Doc and you will see that it will store your conversation to the Google Doc now.

   ![](./images/userdoc.png)

3. Now, first save the workflow and refresh the page, and ask the agent to greet with your name. It will greet with your name!

   ![](./images/finalrespomse.png)

---

## Observation

Now you can see the key difference:

- **With Simple Memory:** When you refresh the page, it will lose your whole previous context. The agent cannot remember anything from the previous session.

- **With Long-Term Memory:** Even after a new session (refreshing the page), the agent has context to your previous conversation. The agent can retrieve and use information from past interactions stored in Google Docs.

This demonstrates the power of long-term memory - it persists across sessions and allows the agent to maintain continuity in conversations!
