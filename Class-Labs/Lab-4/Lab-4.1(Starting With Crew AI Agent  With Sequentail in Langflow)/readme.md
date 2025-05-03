# Lab 4.1: Building Sequential Crew AI Agents in Langflow for MSA Document Processing

## Introduction

In this lab, we'll build a system that takes an MSA (Master Service Agreement) document and analyzes its risks. The system consists of three sequential agents, each with specific responsibilities:

1. **Extraction Agent**:

   - Extracts key terms from the document
   - Identifies important clauses and sections
   - Creates a structured representation of the document

2. **Comparison Agent**:

   - Compares the extracted key terms with reference values
   - Analyzes potential risks and deviations
   - Flags any concerning terms or conditions

3. **Report Generation Agent**:
   - Generates a comprehensive summary report
   - Provides risk assessment and recommendations
   - Creates an executive summary of findings

The system also provides an interactive chat interface where users can ask specific questions about the contract, and the appropriate agent(s) will provide detailed responses.

## Prerequisites

Before starting this lab, ensure you have the following:

### 1. Reference Documentation

- [Langflow Documentation](https://docs.langflow.org/)
- [CrewAI Documentation](https://docs.crewai.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs)

### 2. Required Files

- [⬇️ Download Langflow JSON Template](https://drive.google.com/file/d/1N401oyaYP-4Ftz3AsZLNd7x8JA7Us6UX/view?usp=sharing)
- [📄 Download Sample MSA Document](https://drive.google.com/file/d/1HPlEXqU-JnpWXe5arqRFXRfvOCtNIJHk/view?usp=sharing)

### 3. API Keys

- OpenAI API Key (Required for the LLM component)
- [🔑 Get Your OpenAI API Key](https://platform.openai.com/api-keys)

## Importing the Flow in Langflow

### Step 1: Access Langflow

1. Go to [https://langflow.org](https://langflow.org)
2. Click on "Get Started Free" button

![Step 1: Langflow Homepage](<Images/Screenshot%20(1515).png>)

### Step 2: Sign Up for Langflow

![Step 2: Langflow Sign Up](<Images/Screenshot%20(1516).png>)

### Step 3: Create New Flow

1. After logging in, click on the "New Flow" button in the dashboard

![Step 3: Create New Flow](<Images/Screenshot%20(1517).png>)

### Step 4: Select Blank Flow

1. In the flow creation menu, click on "Blank Flow" to start with an empty template
2. This will open a new workspace where you can build your application

![Step 4: Select Blank Flow](<Images/Screenshot%20(1518).png>)

### Step 5: Import JSON Flow File

1. Click on the "Import" button in the upper toolbar
2. Select the downloaded JSON flow file from your computer
3. Wait for the import process to complete
4. The flow components will be automatically loaded into your workspace

![Step 5: Import JSON Flow](<Images/Screenshot%20(1519).png>)

### Step 6: View Imported Flow

After successfully importing the JSON file, you will see the complete flow in your workspace. The flow will include all necessary components properly connected, showing the data flow from input to output.

> **Important Note:** After importing, always verify that all nodes are properly connected to each other. Sometimes during import, nodes might become disconnected. Check the flow diagram carefully and reconnect any disconnected nodes by dragging the connection points between them. The data flow should be continuous from the input to the output nodes.

![Step 6: Complete RAG Flow in Workspace](<Images/Screenshot%20(2020).png>)

### Step 7: Configure OpenAI API Key

1. Locate the OpenAI API Key component in your flow
2. Click on the component to open its settings
3. Enter your OpenAI API key in the designated field
4. Also provide the same API key to the Agent component

![Step 7: Configure API Key](<Images/Screenshot%20(2013).png>)

### Step 8: Upload MSA Document

1. Find the Document Upload component in your flow
2. Click on the upload button
3. Select the MSA document you downloaded earlier
4. Wait for the document to be processed

![Step 8: Upload Document](<Images/Screenshot%20(2017).png>)

### Step 9: Test in Playground

1. Click on the "Playground" tab in the top menu
2. You'll see a chat interface where you can:
   - Ask questions about the MSA document
   - Test different types of queries
   - See responses from different agents

#### Sample Questions to Test

- "What are the key terms in this contract?"
- "What are the potential risks in this agreement?"
- "Can you summarize the main points of this document?"

![Step 9: Playground Interface](<Images/Screenshot%20(2019).png>)

### Understanding Agent Responses

When you ask a question:

1. The appropriate agent analyzes the relevant parts of the document
2. The response combines insights from the document and agent expertise
3. You'll see which agent provided the answer in the response
4. The response will include relevant sections from the document

