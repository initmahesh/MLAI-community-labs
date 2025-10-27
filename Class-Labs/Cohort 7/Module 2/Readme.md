# Module 2: Understanding Agentic RAG

[](./images/poster.png)

## Lab Overview

This module guides you through building a complete RAG (Retrieval-Augmented Generation) system from scratch, solving token limitations and creating production-ready applications.

### **Lab 1.1: Generating Response without RAG**

- **Goal:** Understand LLM limitations
- **What you'll learn:** Analyze contracts using GPT-3.5, encounter token limit errors
- **Key takeaway:** Traditional LLMs fail with large documents
- **Tech:** OpenAI GPT-3.5, Google Colab, PyPDF2

---

### **Lab 1.2: Building a RAG System with n8n**

- **Goal:** Overcome token limitations with RAG
- **What you'll learn:**
  - Document chunking and vector embeddings
  - Store chunks in Supabase vector database
  - Query documents using semantic search
- **Key takeaway:** RAG enables handling documents of any size
- **Tech:** n8n, Supabase (pgvector), OpenAI Embeddings

---

### **Lab 1.3: Connecting RAG with v0 (Frontend)**

- **Goal:** Build a beautiful UI for your RAG system
- **What you'll learn:**
  - Connect n8n workflows with webhooks
  - Create interactive UI with v0.dev
  - Build file upload and chat interface
- **Key takeaway:** Complete end-to-end RAG application
- **Tech:** v0.dev, React, Tailwind CSS, n8n webhooks

---

### **Lab 1.4: Understanding Agentic RAG**

- **Goal:** Add AI decision-making to RAG
- **What you'll learn:**
  - Build AI agents with autonomous decision-making
  - Implement confidence scoring and knowledge graphs
  - Enhance query retrieval with intelligent routing
- **Key takeaway:** Agents improve accuracy by choosing when to refine queries
- **Tech:** ChromaDB, LangChain, OpenAI Agents

---

### **Lab 1.5: Building Authentication with V0 and Supabase**

- **Goal:** Secure your RAG application
- **What you'll learn:**
  - Build sign-up and login flows
  - Implement secure session management
  - Integrate Supabase authentication
- **Key takeaway:** Production-ready authentication without backend code
- **Tech:** v0.dev, Supabase Auth, React


**Start with Lab 1.1 and follow the sequence for the complete journey! **
