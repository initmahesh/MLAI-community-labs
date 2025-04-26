# RAG Application using Langflow

## Introduction

This project implements a Retrieval-Augmented Generation (RAG) application using Langflow, a visual programming environment for building language model applications. RAG combines the power of large language models with external knowledge retrieval to provide more accurate and contextually relevant responses.

---

### What is RAG?

Retrieval-Augmented Generation (RAG) is an AI framework that:

1. Retrieves relevant information from external knowledge sources
2. Augments the input prompt with this retrieved information
3. Generates responses using a language model that has access to this additional context

---

### Why Langflow?

Langflow provides a visual interface to:

- Design and build complex language model workflows
- Connect different components like vector stores, language models, and retrieval systems
- Test and iterate on RAG pipelines without extensive coding
- Deploy and share your RAG applications easily

---

## Prerequisites

Before getting started with this RAG application, you'll need to download the following resources:

1. **Document for Processing**

   - Download the document from: [Document Link](https://drive.google.com/file/d/1-M_t0phSpNfPdyFuWqf0mcoy7LBlLYNr/view?usp=sharing)
   - This document will be used as the knowledge base for the RAG system

2. **Langflow JSON Flow File**
   - Download the pre-configured flow from: [Flow File Link](https://drive.google.com/file/d/1-M_t0phSpNfPdyFuWqf0mcoy7LBlLYNr/view?usp=sharing)
   - This JSON file contains the complete Langflow configuration for the RAG pipeline
   - Import this file into your Langflow instance to get started quickly

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
2. This will open a new workspace where you can build your RAG application

![Step 4: Select Blank Flow](<./Images/Screenshot%20(1518).png>)

---

### Step 5: Import JSON Flow File

1. Click on the "Import" button in the upper toolbar
2. Select the downloaded JSON flow file from your computer
3. Wait for the import process to complete
4. The RAG flow components will be automatically loaded into your workspace

![Step 5: Import JSON Flow](<./Images/Screenshot%20(1519).png>)

---

### Step 6: View Imported Flow

After successfully importing the JSON file, you will see the complete RAG flow in your workspace. The flow will include:

All components will be properly connected, showing the data flow from input to output. You can now proceed to configure the components and test the flow.

> # **Important Note:** After importing, always verify that all nodes are properly connected to each other. Sometimes during import, nodes might become disconnected. Check the flow diagram carefully and reconnect any disconnected nodes by dragging the connection points between them. The data flow should be continuous from the input to the output nodes.

![Step 6: Complete RAG Flow in Workspace](<./Images/Screenshot%20(1977).png>)

---

### Step 7: Setup Document Processing (Part 1)

The RAG flow is divided into two main parts. Let's set up Part 1 which handles document processing and vector storage:

1. **Document Upload**

   - Click on the "Document Loader" component
   - Upload your document file (PDF, TXT, or other supported format)
   - Configure the loader settings if needed

2. **Text Splitting**

   - The document will be automatically split into chunks
   - Configure chunk size and overlap in the "Text Splitter" component
   - This ensures optimal processing of the document content

3. **Vector Storage**

   - The split chunks will be processed by the "Vector Store" component
   - This component converts text into vector embeddings
   - The vectors are stored for efficient retrieval later

4. **OpenAI API Key Configuration**
   - Click on the "Language Model" component.
   - In the configuration panel, locate the "API Key" field.
   - Enter your OpenAI API key.
   - Save the configuration.

![Step 7: Document Processing Setup](<./Images/Screenshot%20(1978).png>)

---

### Step 8: Run Part 1 of the Flow

1. Locate the "Run" button in the upper toolbar (highlighted in the screenshot)
2. Click the "Run" button to execute Part 1 of the flow
3. The system will:
   - Process your uploaded document
   - Split it into chunks
   - Generate vector embeddings
   - Store them in the vector database
4. Wait for the process to complete - you'll see progress indicators for each step
5. Verify that all components show successful completion

![Step 8: Running Part 1](<./Images/Screenshot%20(1979).png>)

---

### Step 9: Question Answering (Part 2)

Now that your document is processed and stored in the vector database, you can ask questions about its content:

> ## **Important:** Before proceeding, make sure to configure the embedding model component:
>
> 1. Click on the "Embedding Model" component
> 2. In the configuration panel, locate the "API Key" field
> 3. Enter your OpenAI API key (same key used for the language model)
> 4. Save the configuration

![Step 9: Question Answering Interface](<./Images/Screenshot%20(1980).png>)

> ## **Note:** Also add your OpenAI API key to the OpenAI component in the flow.

![Step 9: Question Answering Interface](<./Images/Screenshot%20(1981).png>)

---

### Step 10: Access Playground

1. Go to the top of the interface
2. Click on the "Playground" section
3. This will open the interactive

![Step 9: Question Answering Interface](<./Images/Screenshot%20(1982).png>)

---

### Step 11: Ask Questions and Get Answers

1. In the playground interface, type your question about the document content
2. The system will:
   - Search the vector database for relevant information
   - Generate a response based on the retrieved content
   - Display the answer along with relevant document chunks
3. Each response will be based on the actual content of your uploaded document

> **Tip:** Try asking questions that:
>
> - Test specific details from the document
> - Require understanding of the document's context
> - Compare different parts of the document
> - Ask for summaries or explanations

![Step 11: Question and Answer Example](<./Images/Screenshot%20(1983).png>)
