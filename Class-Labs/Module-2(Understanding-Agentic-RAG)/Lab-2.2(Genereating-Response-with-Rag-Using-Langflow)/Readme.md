# Build RAG Application using Langflow


## The Limitations of Generative Models

Think about a very smart student.  
They’ve studied for years, read thousands of books, articles, and websites, and know a lot about many subjects.  

Now imagine you ask them a question about your company’s internal policy, a new law that was passed last month, or a small detail from a specific technical manual.  
The problem is — they’ve never seen that information before.  

What do they do?  
Sometimes they guess.  
And because they are confident, their guess sounds true, even when it’s wrong. In AI, this guessing is called **hallucination**. It can lead to wrong answers, and in business, that can cause real problems.  

There’s another issue: even if you give the AI a huge document to help it answer, there’s a limit to how much it can read at once.  
If the document is too long, you might get an error like **"maximum context length exceeded"**.  
This means the model’s “memory window” is full, and it can’t process all your text in one go.  

So, we need a way to give the model exactly the right pieces of information — enough to answer well, but without overloading it.

---

## The Solution — Retrieval-Augmented Generation (RAG)

Retrieval-Augmented Generation (RAG) is a framework that augments the general knowledge of a generative LLM by providing it with additional data relevant to the task at hand retrieved from an external data source.

External data sources can include internal databases, files, and repositories, as well as publicly available data such as news articles, websites, or other online content. Access to this data empowers the model to respond more factually, cite its sources in its responses, and avoid “guessing” when prompted about information not found in the model’s original training dataset.

Common use cases for RAG include retrieving up-to-date information, accessing specialized domain knowledge, and answering complex, data-driven queries. 

Here’s how it works:  

1. **Retrieve** — When you ask a question, the system searches your documents, databases, or other sources for the most relevant pieces of information.  
2. **Augment** — These pieces are added to your question so the AI has all the important details right in front of it.  
3. **Generate** — The AI uses both its general knowledge and the new context to write a clear, accurate answer.  

This approach solves both major problems:  
- The AI no longer has to guess because it has the exact facts it needs.  
- We avoid hitting the context length limit by giving the AI only the most relevant chunks instead of the entire document.

With RAG, even the largest, most complex documents can be turned into quick, accurate, and trustworthy answers.

![New Flow Button](./Images/flow-diagram.png)

By the end, you won’t just have built a RAG system — you’ll have learned how to tame even the largest, most complex documents into a resource that delivers instant, intelligent insights.

---

## Prerequisites

Before getting started with this RAG application, you'll need to download the following resources:

1. **Document for Processing**

   - Download the document from: **[Document Link](https://drive.google.com/file/d/1GYAKFyXLitx83xCMVWkh-cc2OcIxq3d-/view?usp=sharing)**
   - This document will be used as the knowledge base for the RAG system

2. **Langflow JSON Flow File**
   - Download the pre-configured flow from: **[Flow File Link](https://drive.google.com/file/d/1ntOfttJ-BacL6ru-nVXTOEyxUFqKC1q7/view?usp=sharing)**
   - This JSON file contains the complete Langflow configuration for the RAG pipeline
   - Import this file into your Langflow instance to get started quickly

3. **Langflow Login Guide**
   - Follow the instructions provided in the Langflow Login Guide:  **[Click Here](../../Lab-0(Pre-requisites)/Langflow-Login-Guide/Readme.md)**
---

## Importing the Flow in Langflow

Follow these steps to import and set up the RAG flow in Langflow:

### Step 1: Log in to Langflow Web
Ensure you are logged in to Langflow web. Refer to the login guide if you have not completed this step.

### Step 2: Create a New Flow
Click the **New Flow** button on your Langflow dashboard.

![New Flow Button](./Images/img-1.png)

---

### Step 3: Select Blank Flow

1. In the flow creation menu, click on "Blank Flow" to start with an empty template
2. This will open a new workspace where you can build your RAG application

![Step 4: Select Blank Flow](<./Images/Screenshot%20(1518).png>)

---

### Step 4: Import JSON Flow File

1. Click on the "Import" button in the upper toolbar
2. Select the downloaded JSON flow file from your computer
3. Wait for the import process to complete
4. The RAG flow components will be automatically loaded into your workspace

![Step 5: Import JSON Flow](<./Images/Screenshot%20(1520).png>)

---

### Step 5: View Imported Flow

After successfully importing the JSON file, you will see the complete RAG flow in your workspace. The flow will include:

All components will be properly connected, showing the data flow from input to output. You can now proceed to configure the components and test the flow.

> # **Important Note:** After importing, always verify that all nodes are properly connected to each other. Sometimes during import, nodes might become disconnected. Check the flow diagram carefully and reconnect any disconnected nodes by dragging the connection points between them. The data flow should be continuous from the input to the output nodes.

![Step 6: Complete RAG Flow in Workspace](<./Images/Screenshot%20(1977).png>)

---

### Step 6: Setup Document Processing (Part 1)

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

### Step 7: Run Part 1 of the Flow

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

### Step 8: Question Answering (Part 2)

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

### Step 9: Access Playground

1. Go to the top of the interface
2. Click on the "Playground" section
3. This will open the interactive

![Step 9: Question Answering Interface](<./Images/Screenshot%20(1982).png>)

---

### Step 10: Ask Questions and Get Answers

1. In the playground interface, type your question about the document content
2. The system will:
   - Search the vector database for relevant information
   - Generate a response based on the retrieved content
   - Display the answer
3. Each response will be based on the actual content of your uploaded document

> **Tip:** Try asking questions that:
>
> - Test specific details from the document
> - Require understanding of the document's context
> - Compare different parts of the document
> - Ask for summaries or explanations

![Step 11: Question and Answer Example](<./Images/Screenshot%20(1983).png>)

---


## Conclusion

Boom we are done ! 🎉  

You’ve just built a **RAG application** that transforms the way large, complex documents can be explored and understood.  

You now know how to :
   - Break massive documents into context-rich chunks for smarter retrieval  
   - Empower language models to answer with precision and depth  
   - Build a visual, no-code/low-code AI workflow in Langflow  
   - Turn dense, hard-to-navigate information into something your users can query like a live expert  
