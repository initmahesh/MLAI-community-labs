# Building a RAG System with n8n

![](./images/poster.png)

## Description

In the previous lab, you encountered a limitation where ChatGPT failed to analyze a contract document due to token limit length errors. In this lab, we will build a solution using a RAG (Retrieval-Augmented Generation) workflow that overcomes this limitation.

We will use **Simple Vector Store n8n** to store document chunks and implement a retrieval system. Using the same document that failed in Lab 1, you'll now be able to query the document and receive accurate responses without hitting token limits. This approach demonstrates how RAG systems can handle large documents by breaking them into manageable chunks and retrieving only relevant information for each query.

---

## Introduction to RAG (Retrieval-Augmented Generation)

### What is RAG?

RAG (Retrieval-Augmented Generation) is a powerful AI architecture that combines the strengths of information retrieval systems with large language models (LLMs). Instead of relying solely on the knowledge embedded in an LLM during training, RAG systems dynamically retrieve relevant information from external knowledge bases to generate more accurate and contextual responses.

### How Does RAG Work?

The RAG workflow consists of three main stages:

1. **Document Processing & Storage**: Large documents are split into smaller chunks and converted into vector embeddings, which are then stored in a vector database (like Simple Vector Store or Supabase with pgvector).

2. **Retrieval**: When a user submits a query, the system converts it into a vector embedding and searches the database for the most semantically similar document chunks.

3. **Generation**: The retrieved relevant chunks are combined with the user's query and sent to the LLM, which generates a response based on the specific context provided.

### Why Use RAG?

RAG systems offer several key advantages:

- **Overcomes Token Limitations**: Traditional LLMs have context window limits. RAG systems only send relevant information to the model, allowing you to work with documents of any size.

- **Up-to-Date Information**: You can update your knowledge base without retraining the model, ensuring responses are based on the latest information.

- **Improved Accuracy**: By grounding responses in specific retrieved documents, RAG reduces hallucinations and provides more factually accurate answers.

- **Cost-Effective**: Instead of fine-tuning models or processing entire documents repeatedly, RAG efficiently retrieves only what's needed for each query.

- **Source Attribution**: RAG systems can reference specific document chunks, making it easy to verify and cite sources.

- **Domain-Specific Knowledge**: You can create specialized AI assistants for specific domains (legal, medical, technical) by providing relevant document collections.

![](./images/flow-diagram.png)

---

## Prerequisites

Before beginning this lab, ensure you have completed the following:

**Important:** Make sure you have completed **Module 1** and **Lab 1.1 of Module 2** before starting this lab.

- **New to n8n!** Set up your account: **[Click Here](../../Module%200%20-%20Prerequisite/n8n-loginSetup/Doc.md)**
- **Generate your OpenAI API key:** **[Click Here](https://youtu.be/YyaZ8zaGS-Q?si=bOw8C_TWgMg8S1hU)**
- **Download n8n workflow file:** **[Click Here](https://drive.google.com/file/d/1bsHT4DsEvLFZv2WPBdnXJoEAfEn9R6Ka/view?usp=sharing)**
- **Download Small Contract reference document:** **[Click Here](https://drive.google.com/file/d/1RMzUyryxh88qiXTW6psH6lEfrhQ8H2ZQ/view?usp=sharing)**

---

# > **💡 Note:** You have two options:
> 
> 1. **Build it From Scratch:** **[Click Here](https://maven.com/mahesh-yadav/genaipm/7/syllabus/modules/e4d850?item=631eb82b63738807)**

### OR 


> 2. **Use the provided workflow file** from the Prerequisites section above and follow the **Hands-On: Building Your RAG System** instructions below.

---

## Hands-On: Building Your RAG System

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

> **💡 Note:** Make sure you have configured your OpenAI API key. If you have already completed **Lab 1.1**, you don't need to do it again — n8n will automatically use the credentials you saved from the environment variables.

> **If you haven't configured it yet:** Click on the **OpenAI Chat Model** component and add your API key as shown in the GIF below.

![](./images/openapi.gif)

> Your workflow is now ready to be configured!

---

### Understanding the Workflow: Two Main Steps

Before we dive into configuration, let's understand what this workflow does:

**Step 1: Document Segmentation & Vectorization (Indexing)**

- Upload your contract document
- The system will automatically split it into smaller chunks
- Each chunk is converted into vector embeddings
- These embeddings are stored in Simple Vector Store for later retrieval

**Step 2: Query & Retrieval Part (Q&A)**

- Submit a query about your document
- The system searches the Simple Vector Store for relevant chunks
- Retrieved chunks are sent to the LLM along with your query
- You receive an accurate response based on the document content

Now let's configure each step!

![](./images/flow.png)

---

### Step 3: Upload Your Contract Document

Now it's time to upload the contract document that failed in Lab 1 and store it in Simple Vector Store:

1. **Click the "Execute Workflow" button** - This will activate your workflow and make it ready to receive the document

2. **Upload the contract** - Upload the same contract document that failed in Lab 1.1 due to token limit errors

3. **Wait for processing** - The workflow will:
   - Split your document into smaller chunks
   - Generate vector embeddings for each chunk
   - Store the embeddings in Simple Vector Store

> Your contract document is now chunked and stored as vector embeddings in Simple Vector Store, ready for retrieval!

![](./images/gif-1.gif)

---

### Step 4: Configure Step 2 - Query & Retrieval

Now let's set up the retrieval workflow to query your document:

1. **Locate Step 2 components** - In your workflow, find the **Step 2: Retrieval Part** section

2. **Configure OpenAI Chat Model:**

   - Click on the **OpenAI Chat Model** node
   - Ensure your OpenAI API key is configured
   - If you completed Lab 1.1, the credentials should already be saved
   - Click "Save"

3. **Configure OpenAI Embeddings Model:**
   - Click on the **OpenAI Embeddings** node
   - Verify your OpenAI API key is configured
   - This model will convert your queries into vector embeddings for searching
   - Click "Save"

---

### Step 5: Test Your RAG System

Now it's time to test your RAG system and see it in action!

1. **Open the Chat Window:**

   - Click on the **"Open Chat"** button in your workflow
   - This will launch the chat interface

   ![](./images/gif-2.gif)

2. **Start Asking Queries:**

   - Type any question about your contract document
   - Ask the same questions that failed in Lab 1.1 due to token limits
   - Press Enter or click Send

3. **Watch the Magic Happen:**

   - The system will search your Simple Vector Store for relevant chunks
   - Retrieved information will be sent to the LLM
   - You'll receive accurate responses based on your document content

   ![](./images/finalss.png)

4. **Try Multiple Queries:**
   - Ask different questions about your contract
   - Test complex queries that require information from multiple sections
   - Compare the results with Lab 1.1 where the document failed to process

> **🎉 Success!** You've successfully built a RAG system that can handle large documents without token limit errors!

---

## Conclusion

Congratulations! You've successfully built a complete RAG (Retrieval-Augmented Generation) system using n8n and Simple Vector Store. In this lab, you learned:

- How RAG systems overcome token limitations by chunking documents and retrieving relevant information
- How to configure n8n workflows for both document indexing and retrieval
- How to integrate OpenAI embeddings and chat models for semantic search and response generation 

---

## Need Help?

If you encounter any issues:

- Review the Prerequisites section to ensure all accounts and keys are properly configured
- Verify that your document chunks were processed and stored correctly in Simple Vector Store
- Ensure all OpenAI API credentials are valid and have sufficient credits
- Connect with Sachin

---

**Happy Building! 🚀**
