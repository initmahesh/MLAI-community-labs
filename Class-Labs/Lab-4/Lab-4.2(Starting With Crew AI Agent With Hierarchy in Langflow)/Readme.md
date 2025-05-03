# Lab 4.2: Building Hierarchical Crew AI Agents in Langflow for MSA Document Processing

## Introduction

In this lab, we'll build a sophisticated AI system using Langflow that can process and analyze Master Service Agreement (MSA) documents. The system uses a hierarchical crew of specialized AI agents, each focusing on different aspects of the contract:

- **Main Controller Agent**: Orchestrates the entire process and routes tasks
- **Legal Agent**: Analyzes legal clauses and liabilities
- **Financial Agent**: Reviews payment terms and financial conditions
- **IP & Confidentiality Agent**: Checks intellectual property and confidentiality clauses
- **Compliance Agent**: Ensures regulatory compliance (GDPR, etc.)

The system not only processes documents but also provides an interactive chat interface where users can ask specific questions about the contract, and the appropriate agent(s) will provide detailed responses.

---

## Prerequisites

Before starting this lab, ensure you have the following:

1. **Reference Documentation**

   - [Langflow Documentation](https://docs.langflow.org/)
   - [CrewAI Documentation](https://docs.crewai.com/)
   - [OpenAI API Documentation](https://platform.openai.com/docs)

2. **Required Files**

   - [⬇️ DOWNLOAD LANGFLOW JSON TEMPLATE](https://drive.google.com/file/d/1NpGlDNhrNK-q1JLwb3DDj8agaRjS3h6W/view?usp=sharing)
   - [📄 DOWNLOAD SAMPLE MSA DOCUMENT](https://drive.google.com/file/d/1mO4JF0YjgQ1NIoU2IC51j2-70g8Kq70r/view?usp=sharing)

3. **API Keys**
   - OpenAI API Key (Required for the LLM component)
   - [🔑 GET YOUR OPENAI API KEY](https://platform.openai.com/api-keys)

---

## Importing the Flow in Langflow

Follow these steps to import and set up the RAG flow in Langflow:

### Step 1: Access Langflow

1. Go to [https://langflow.org](https://langflow.org) and click on "Get Started Free" button

![Step 1: Langflow Homepage](<./Images/Screenshot%20(1515).png>)

---

### Step 2: Sign Up for Langflow

![Step 2: Langflow Sign Up](<./Images/Screenshot%20(1516).png>)

---

### Step 3: Create New Flow

1. After logging in, click on the "New Flow" button in the dashboard

![Step 3: Create New Flow](<./Images/Screenshot%20(1517).png>)

---

### Step 4: Select Blank Flow

1. In the flow creation menu, click on "Blank Flow" to start with an empty template
2. This will open a new workspace where you can build your application

![Step 4: Select Blank Flow](<./Images/Screenshot%20(1518).png>)

---

### Step 5: Import JSON Flow File

1. Click on the "Import" button in the upper toolbar
2. Select the downloaded JSON flow file from your computer
3. Wait for the import process to complete
4. The flow components will be automatically loaded into your workspace

![Step 5: Import JSON Flow](<./Images/Screenshot%20(1519).png>)

---

### Step 6: View Imported Flow

After successfully importing the JSON file, you will see the complete flow in your workspace. The flow will include:

All components will be properly connected, showing the data flow from input to output. You can now proceed to configure the components and test the flow.

> # **Important Note:** After importing, always verify that all nodes are properly connected to each other. Sometimes during import, nodes might become disconnected. Check the flow diagram carefully and reconnect any disconnected nodes by dragging the connection points between them. The data flow should be continuous from the input to the output nodes.

![Step 6: Complete RAG Flow in Workspace](<./Images/Screenshot (2013) - Copy.png>)

### Step 7: Configure OpenAI API Key

1. Locate the OpenAI API Key component in your flow
2. Click on the component to open its settings
3. Enter your OpenAI API key in the designated field

![Step 7: Configure API Key](<./Images/Screenshot (2013).png>)

---

### Step 8: Upload MSA Document

1. Find the Document Upload component in your flow
2. Click on the upload button
3. Select the MSA document you downloaded earlier
4. Wait for the document to be processed

![Step 8: Upload Document](<./Images/Screenshot (2014) - Copy - Copy.png>)

---

### Step 9: Test in Playground

1. Click on the "Playground" tab in the top menu
2. You'll see a chat interface where you can:

   - Ask questions about the MSA document
   - Test different types of queries
   - See responses from different agents

3. **Reference Questions for Testing:**

   🧑‍⚖️ **Legal Agent Questions:**

   - "Who is liable in case of service delivery failure?"
   - "What's the notice period required before termination?"
   - "Does the agreement include arbitration or litigation in disputes?"

   💸 **Financial Agent Questions:**

   - "What are the payment due dates and late fee terms?"
   - "Is there any clause about milestone-based invoicing?"
   - "Are financial penalties applicable for delayed work delivery?"

   🔐 **IP & Confidentiality Agent Questions:**

   - "Who retains ownership of deliverables?"
   - "Is there any clause restricting me from working with competitors?"
   - "What protections are mentioned for confidential data or trade secrets?"

   🛡️ **Compliance Agent Questions:**

   - "Does this contract comply with GDPR requirements?"
   - "What happens if there's a personal data breach?"
   - "Are there specific obligations for securing customer data?"

![Step 9: Playground Interface](<./Images/Screenshot (2014) - Copy.png>)

---

### Understanding Agent Responses

When you ask a question:

1. The Main Controller Agent routes it to the appropriate specialist agent
2. The specialist agent analyzes the relevant parts of the document
3. The response combines insights from the document and agent expertise
4. You'll see which agent provided the answer in the response

![Step 9: Playground Interface](<./Images/Screenshot (2014).png>)
