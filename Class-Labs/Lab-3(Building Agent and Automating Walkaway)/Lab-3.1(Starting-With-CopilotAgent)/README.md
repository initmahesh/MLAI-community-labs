# Building and Integrating Knowledge Copilot Agent with MS Teams

A step-by-step guide to building an AI agent that processes knowledge sources and provides intelligent responses through MS Teams integration.

---

## What is Microsoft Copilot Agent?

Microsoft Copilot Agent is an AI-powered assistant that helps you build, customize, and deploy conversational AI solutions. It enables you to create intelligent agents that can understand natural language, process knowledge sources, and provide contextually relevant responses through various channels including Microsoft Teams.

---

# Important Note

Before starting with the implementation, please ensure you have:

- A working professional email address

If you don't have these prerequisites, please contact Sachin he will provide you the credentials for completing this lab.

---

## Step-by-Step Implementation Guide

### Prerequisites

1. Microsoft Copilot Studio access
2. Professional email address
3. MS Teams access

### Step 1: Access Copilot Studio

1. Open your web browser
2. Go to [https://copilotstudio.microsoft.com](https://copilotstudio.microsoft.com)
3. You will see the Microsoft Copilot Studio landing page
4. Click on "Sign in" in the top right corner
5. Use your professional email address to sign in. If you don't have one, please contact Sachin and he will provide it.
6. After signing in, you'll see the dashboard, something like this as provided in the below image:

![Copilot Studio Landing Page](Images\1.png)

---

### Step 2: Navigate to Agents

1. Navigate to the left side panel of the dashboard
2. Locate and select the "Agents" option in the navigation menu
3. This will direct you to the agents management page where you can create and manage your copilot agents
4. Click on the "New Agent" button

![Copilot Studio Agents Page](Images\2.png)

---

### Step 3: Create Your Agent

1. You'll see a chat interface where you can describe your agent idea
2. Type in the following prompt to create a knowledge-based agent:
   ```
   Create an agent that takes user input and responds using only the knowledge that has been previously provided to it. The agent should not generate responses from external sources or its own assumptions, but instead rely solely on the internal knowledge base we've given it.
   ```
3. The AI will ask you questions to understand your requirements better, such as:

   - What type of knowledge will be provided?
   - Suitable name for your agent

4. Based on your responses, it will:
   - Suggest a suitable flow for your use case
   - Provide recommendations for implementation
   - Help you define the agent's capabilities

![Agent Creation Chat Interface](Images\3.png)

---

### Step 4: Create Your Agent

1. After exploring the interface and understanding the flow, look for the "Create" button at the top of the page
2. Click on the "Create" button to start building your agent
3. Since we already have a clear idea of what we're building (a knowledge-based agent), we can skip the chat interface and proceed directly to creation

![Create Button Location](Images\4.png)

---

### Step 5: Review Agent Description

1. After clicking Create, you'll see a new interface where the agent has already provided a description based on your prompt
2. **The agent has automatically generated a description that matches your requirements for a knowledge-based agent that only responds using provided knowledge**
3. Review the description to ensure it aligns with your needs

![Agent Description](Images\5.png)

---

### Step 6: Let's Add Knowledge to Our Agent

Great! Now that we have our agent set up, let's teach it some knowledge. Here's what we'll do:

1. Look at the top of the page - you'll see several tabs
2. Click on the "Knowledge" tab - this is where we'll add all the information our agent needs to know
3. Think of this as teaching our agent everything it needs to help users

![Knowledge Tab](Images\6.png)

---

### Step 7: Add Knowledge Sources

Now, let's feed our agent with some knowledge! You'll see various options to add resources:

1. Upload files (PDFs, documents, etc.)
2. Add website URLs
3. Connect to other data sources
4. Import from existing knowledge bases

For this example, we're using an MSA document, but you can use any type of content that contains the information you want your agent to know about. The agent will process and learn from whatever resources you provide.

![Adding Knowledge Sources](Images\7.png)

---

### Step 8: Test Your Agent

Great! Now that your agent has learned from the knowledge you provided, let's test it out:

1. Look for the "Test" button in the top right corner
2. Click on it to open the testing interface
3. Here you can ask questions about the content you provided
4. The agent will respond based only on the knowledge you've given it

This is where you can see your agent in action and make sure it's working as expected!

#### Test Button

![Testing Interface](Images\10.png)

#### Testing Interface

![Testing Interface](Images\11.png)

---

### Step 9: Publish Your Agent

Now that we've tested our agent and it's working well, let's make it available for your team:

1. Look for the "Publish" button in the top right corner
2. Click on it to start the publishing process
3. This will make your agent available for integration with MS Teams
4. The publishing process might take a few minutes

![Publish Button](Images\12.png)

---

### Step 10: Connect to MS Teams

Now that your agent is published, let's connect it to MS Teams:

1. Click on the "Channels" tab at the top
2. Look for "Microsoft 365 Copilot" in the available channels
3. Select it to start the Teams integration process
4. This will make your agent available as a Teams app

![Channels Selection](Images\13.png)

---

### Step 11: Add the Channel

Let's add the Teams channel to your agent:

1. After selecting Microsoft 365 Copilot, click the "Add Channel" button
2. This will start the process of connecting your agent to Teams
3. You'll see a confirmation message once the channel is added successfully

![Add Channel Button](Images\14.png)

---

### Step 12: Access Your Agent in Teams

Great! Now that the channel is added, let's see your agent in Teams:

1. Look for the "See agent in your team" button
2. Click on it to open your agent in MS Teams
3. This will take you directly to your agent in the Teams interface
4. You can now start using your knowledge-based agent in Teams!

![See Agent in Teams](Images\15.png)

---

### Step 13: Open MS Teams

Now, let's open MS Teams to start using your agent:

1. Open the MS Teams application on your computer
2. Sign in with your professional account
3. You'll see your agent available in the Teams interface

![MS Teams Interface](Images\16.png)

---

### Step 14: Add Agent to Teams

Let's add your agent to MS Teams:

1. CLick "Add" button
2. Your agent will be added as a Teams app

![Add to Teams Button](Images\17.png)

---

### Step 15: Open Your Agent

Now that your agent is added to Teams, let's open it:

1. Look for the "Open" button
2. Click on it to launch your agent in Teams
3. This will open a chat interface where you can start interacting with your knowledge-based agent

![Open Agent Button](Images\18.png)

---

### Step 16: Start Using Your Agent

Congratulations! Your agent is now fully integrated with MS Teams:

1. You can start chatting with your agent in the Teams interface
2. The agent will respond using only the knowledge you provided
3. Try asking questions about the content you uploaded
4. You'll notice that the agent's responses are based on your specific knowledge sources

![Agent Chat Interface](Images\19.png)

---

# Video Tutorial: Building the Lab

# [Video Link](https://pragyaallc-my.sharepoint.com/:v:/g/personal/sachin_parmar_legalgraph_ai/EXnZJ1i0y7RFtjR84hUvZbsBkQJeL-ea0JIRwpH58e8yZg?e=k31j8a&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D)

The video covers:

- Building the Copilot agent from scratch
- Adding knowledge processing capabilities
- Integrating with MS Teams
