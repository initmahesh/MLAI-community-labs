## Introduction
As you get started in GenAI, prompting is something you will do a lot. In this deep dive we will understand prompt and best practices within live and interactive video lessons. 

## Understanding Prompt Engineering
Prompt engineering is a key concept in AI development, especially when working with Large Language Models (LLMs). It involves crafting precise and effective prompts to guide the AI in generating relevant and high-quality responses.

### What is LangFlow?
LangFlow is a cutting-edge no-code AI ecosystem that enables developers, entrepreneurs, and even non-technical individuals to build AI applications with ease. It provides a visually appealing and intuitive drag-and-drop interface, allowing users to create AI workflows by connecting reusable components. This modular and interactive design fosters rapid experimentation and prototyping, making it an ideal tool for both beginners and experienced AI enthusiasts.

### Key Features of LangFlow
- **Dynamic Input Customization:** Allows users to tailor AI applications using curly brackets `{}` for flexible data input.
- **Fine-Tuning Capabilities:** Enables users to train LLMs with custom datasets (CSV, JSON) for domain-specific AI applications.
- **Python-Native Architecture:** Supports seamless integration with powerful ML and data manipulation libraries.

### How Prompt Engineering Works in LangFlow
LangFlow simplifies prompt engineering by:
- Providing a **graphical interface** for designing AI pipelines visually.
- Offering **modular components** to integrate APIs, data sources, and AI functionalities.
- Supporting **customizable workflows** to fit specific use cases.
- Enabling **multi-LLM support** for different AI models like OpenAI's GPT and Hugging Face models.

### Use Cases of LangFlow for Prompt Engineering
- **Building Local RAG Chatbots:** By integrating embedding models like Ollama, LangFlow enables personalized AI responses.
- **Document Interaction:** Users can chat with PDFs, DOCX, TXT, and websites to extract meaningful insights.
- **Workflow Automation:** Integration with Zapier allows seamless automation of various tasks.

## Setup the Project

- Go to the LangFlow page and click on "Get Started for Free", as shown in the image below.

![Langflow Screenshot](./Images/Screenshot%20(1515).png)

- Create your account on LangFlow.

![Langflow Screenshot](./Images/Screenshot%20(1516).png)

- After creating your account, click on "New Flow".

![Langflow Screenshot](./Images/Screenshot%20(1517).png)

- Now click on Blank Flow, as we are building it from scratch.

![Langflow Screenshot](./Images/Screenshot%20(1518).png)

- Now, click on the untitled document above, and in the dropdown, click on the Import Option to import the JSON file that has been provided to you.

![Langflow Screenshot](./Images/Screenshot%20(1520).png)

- Now, you will see that your project has been successfully imported, and you can view all the agents.

![Langflow Screenshot](./Images/Screenshot%20(1571).png)

- Provide the Open API Key to the agent and the Open API Key component to enable authentication and access. Ensure that the API key is securely stored and used only for authorized requests.

- In the Text Section Component, click on the text, and you can define the styling of your blog, such as the tone, the heading, etc.

![Langflow Screenshot](./Images/Screenshot%20(1555).png)

- Now, from here, you can edit your prompt and click on Check, then Save.

![Langflow Screenshot](./Images/Screenshot%20(1554).png)

- Now, click on the Playground Section.

![Langflow Screenshot](./Images/Screenshot%20(1553).png)

- In the Playground section, enter a query such as: 'Please provide the input particular user.' The system will fetch and display the output based on the document that you have uploaded.

  Example:

  Input: "Create a table with the following columns: Key Term, Description, and Location in Contract. Populate it with the extracted details of the service provider name, customer name, and termination clauses."
  Output:
  Fetched the answer from the document uploaded by you.
  
![Langflow Screenshot](./Images/Screenshot%20(1573).png)

- ⚠️ Note: If no document is found in the upload document, the URL component will fail, and the output generation will not proceed.

# **Deep Dive : Prompt Engineering and Best Practices**


## **Building Blocks of a Prompt:**  
Prompts are not created equal and have ways to get different responses. Here are the building blocks that make a prompt:

- **Instruction** - A specific task or instruction you want the model to perform:  
  *"Find the capital of the top 10 countries by GDP?"*
  
- **Context** - Can involve external information or additional context that can steer the model to better responses.  
  *Context (You are a student listing all countries and their capitals as comma-separated files); Instruction (Find the capital of the top 10 countries by GDP?)*
  
- **Input Data** - The input or question that we are interested in finding a response for.  
  *Context (You are a student, preparing a list of countries and capitals in any order); Input (Can you list the capital of the USA in that format?)*
  
- **Output Indicator** - Indicates the type or format of the output.  
  *Context (You are a student, preparing a list of countries and capitals in any order); Input (Can you list the capital of the USA in the given output format?); Output Format: "Paris; France", "New Delhi; India"*

Like Legos, you can pick up all or any combination of these prompts to perform the task at hand.

---

## **Methods Used in Prompts**

There are different types of prompts that you can use to interact with large models based on your task:

### **1) Instructions**  
Here, you simply tell the machine what to do, and it does that for you. For example:

**INPUT:**  
```text
Read the following sales email. Remove any personally identifiable information (PII), and replace it with the appropriate placeholder. For example, replace the name "Mahesh Yadav" with "[NAME]".

Hi John,

I'm writing to you because I noticed you recently purchased a new car. I'm a salesperson at a local dealership (Cheap Dealz), and I wanted to let you know that we have a great deal on a new car. If you're interested, please let me know.

Thanks,
Mahesh Yadav  
Phone: 410-805-2345  
Email: initmahesh@gmail.com  
```

**OUTPUT:**  
```text
Hi [NAME],

I'm writing to you because I noticed you recently purchased a new car. I'm a salesperson at a local dealership, and I wanted to let you know that we have a great deal on a new car. If you're interested, please let me know.

Thanks,
[SALESPERSON]
Phone: [PHONE]
Email: [EMAIL]
```

### **2) Role Prompting**  
Here, you assign a role and then ask questions based on that role.

**INPUT:**  
```text
You are a frontend engineer. Now estimate what it takes to build a stunning website for a startup with 10 pages, with very basic interactions and simple functionality. Just give the estimate in weeks, restrict your answer to 2 lines.
```

**OUTPUT:**  
```text
A stunning website for a startup with 10 pages, basic interactions, and simple functionality could take approximately 4-8 weeks to complete. However, the actual time required may vary depending on project-specific requirements and available resources.
```

---

## **Parameters You Can Tweak**  
We have seen how we can use the above blocks, tune our model response, or get different responses. Here are some parameters that affect the results:

- **Temperature** - Controls randomness. A lower temperature leads to more predictable responses, while a higher value increases creativity.
- **Top_p** - Controls response diversity. A lower value gives exact answers, while a higher value encourages varied responses.

📌 *Recommendation: Alter only one of these at a time.*

- **Penalty** - Discourages overuse of specific words or patterns in the response.

---

## **Top 10 Best Practices Walkthrough**  
Using our *Contract Summarization App*, we will apply ten best practices for prompt engineering:

1. **Be Specific with Information Requests**  
   📌 *Example:* Extract the service provider name, start and end date of the contract, and the total deal value.

2. **Supply Examples for Context**  
   📌 *Example:* Given the format "Service Provider Name: [Name], Start Date: [Date], End Date: [Date], Deal Value: [Amount]", summarize accordingly.

3. **Include Relevant Data**  
   📌 *Example:* Referencing Section 1.5, summarize the deal value and billing frequency terms.

4. **Specify Desired Output Format**  
   📌 *Example:* Create a table with "Key Term", "Description", and "Location in Contract" columns.

5. **Use Positive Instructions**  
   📌 *Example:* Extract key terms including 'termination for breach' and 'limitations of liability' in JSON format.

6. **Assign a Persona or Frame of Reference**  
   📌 *Example:* Imagine you are a legal analyst. Summarize auto-renewal terms, notice periods, and liabilities.

7. **Implement Chain of Thought Prompting**  
   📌 *Example:* Identify 'termination without cause' clauses → Summarize → Explain implications.

8. **Break Down Complex Tasks**  
   📌 *Example:* Identify and summarize indemnification terms. Then extract coverage for attorney fees.

9. **Acknowledge the Model's Limitations**  
   📌 *Example:* Extract governing law and indemnification terms. Flag unclear sections for expert review.

10. **Take an Experimental Approach**  
    📌 *Example:* Extract 'termination for cause' using a bullet list, then as a paragraph. Compare clarity.

---

## **Example Final Prompt for Contract GPT**  

```xml
<Role>
You are an in-house general counsel trained to find liabilities and other clauses from contracts.
</Role>

<Instruction>
Use your legal expertise to review the provided contract document. Your primary goal is to extract and summarize specific terms accurately, following the structured format specified.
</Instruction>

<Task>
1. Extract key terms including 'Service Provider Name', 'Start Date', 'End Date', and 'Deal Value'. Present these in a list format.
2. Review and identify clauses related to 'termination for breach', 'data breach notice', and 'limitations of liability'. Provide a summary in JSON format.
3. Analyze 'auto-renewal' terms and specify the required notice period.
4. Summarize 'indemnification' and 'attorney fees' coverage terms separately.
5. Highlight any ambiguous or unclear language, suggesting further review if necessary.
</Task>

<Guardrails>
1. Be specific and concise in term extraction.
2. Provide summaries in the specified format (JSON, table, or bullet points as directed).
3. Emulate a legal analyst persona.
4. Use positive instructions: focus on terms to include, rather than avoid.
5. Acknowledge model limitations: flag uncertain sections for professional review.
</Guardrails>
```

---

© **All rights reserved Mahesh Yadav Institute**. No part of this course can be reproduced, distributed, or transmitted in any form without permission.


## **Conclusion**
Prompt engineering is a crucial skill in working with AI models effectively. By understanding the different prompt structures, applying best practices, and fine-tuning parameters, users can achieve highly specific and accurate responses. As AI continues to evolve, mastering these techniques will be essential for optimizing AI interactions and improving task outcomes.