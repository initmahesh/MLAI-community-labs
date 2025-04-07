## Project Objective

Develop an AI-driven document processing system where:  

1. Key terms are extracted from the uploaded PDF.  
2. Extracted terms are compared with reference values.  
3. A report is generated highlighting mismatched data.  

---
# CrewAI Overview

CrewAI is a Python framework for orchestrating multiple AI agents to collaborate on complex tasks.

## Key Features  
- **Multi-Agent Collaboration** – Enables AI agents to work together.  
- **Task Automation** – Automates workflows by assigning tasks to specialized agents.  
- **Customizable Roles** – Each agent has distinct responsibilities and behaviors.  
- **Memory & Context Handling** – Agents retain information and share context.  
- **Integration with LLMs** – Supports models like OpenAI’s GPT for decision-making.  

In our project, CrewAI powers agents that extract key terms, compare them with reference values, and generate a mismatch report efficiently. 🚀

---
## Prerequisite

- First, [download the required JSON file](https://drive.google.com/file/d/18fqyhRNpIbqo2rjLQSXIeEzJIyDv6YJG/view?usp=sharing) to proceed with the setup.
- Make sure to review [the contract we are using](https://drive.google.com/file/d/142cTmwtzkly2SkAhgwGwAJ-xKo4B4Ogk/view?usp=drive_link) before continuing.
- If you don’t have one yet, [here’s how you can generate your API key](https://github.com/initmahesh/MLAI-community-labs/tree/main/Class-Labs/Lab-0(Pre-requisites)).

---
# **Let's Start Learning with Hands-On Experience!**  

The best way to learn **anything** is by practicing it in real-time.
🚀 **Let's dive in and start experimenting**  


## Setup the Project

- Go to the [LangFlow page](https://accounts.datastax.com/session-service/v1/login) and create your account first.

![Langflow Screenshot](./Images/Screenshot%20(1920).png)

- Now, from the top dropdown, click on **LangFlow**.

![Langflow Screenshot](./Images/Screenshot%20(1921).png)

- Click on **"New Flow"**.

![Langflow Screenshot](./Images/Screenshot%20(1922).png)

- Now click on **Blank Flow**, as we are building it from scratch.

![Langflow Screenshot](./Images/Screenshot%20(1518).png)

- Now, click on the untitled document above, and in the dropdown, click on the **Import Option** to import the [JSON File](https://drive.google.com/file/d/18fqyhRNpIbqo2rjLQSXIeEzJIyDv6YJG/view?usp=sharing) to view the flow diagram that has been provided to you.

![Langflow Screenshot](./Images/Screenshot%20(1520).png)

- Now, you will see that your project has been successfully imported, and you can view all the components.

**⚠️ Note: Sometimes while uploading your JSON file the links can be disconnected from each other, so make sure all the links are connected to each other as shown in the screenshot provided to you below.**

![Langflow Screenshot](./Images/Screenshot%20(1923).png)

- Now the first step is you have to provide the document in the file component. We are using a reference MSA document, you can upload yours as well. Click on the blue circle icon to upload your document.

Reference MSA Document link: [MSA document link](https://drive.google.com/file/d/142cTmwtzkly2SkAhgwGwAJ-xKo4B4Ogk/view?usp=drive_link)

![Langflow Screenshot](./Images/Screenshot%20(1780).png)

---

⚠️ **Important Note**  
- Provide your **OpenAI API Key** to the agent and the **OpenAI Model** component to enable authentication and access.  
- **[Follow this article](https://github.com/initmahesh/MLAI-community-labs/tree/main/Class-Labs/Lab-0(Pre-requisites))** to generate an OpenAI API key. 🔑  
- Ensure that the **API key is securely stored** and used **only for authorized requests** to prevent misuse.  

![Langflow Screenshot](./Images/Screenshot%20(1776).png)

---

- Now, click on the **Playground Section**.

![Langflow Screenshot](./Images/Screenshot%20(1924).png)

---

- In the **Playground** section, click on **"Run Flow"**.  
![Langflow Screenshot](./Images/Screenshot%20(1778).png)
- The system will fetch and display the output based on the document you have uploaded.  
- It will then extract key terms from the document, compare them with reference values, and generate a report highlighting any mismatched data.  

## > **Note:** Sometimes, on the first run, you might not get the expected response due to hallucination. Just try again — you will likely see the expected output.Make sure to wait for the flow to execute completely before retrying.


![Langflow Screenshot](./Images/Screenshot%20(1925).png)

- **⚠️ Note: If no document is found in the upload document, the file uploader component will fail, and the output generation will not proceed**.
---

# Our Agents and Their Tasks  

## Agents Overview  

### 1. **PDF Data Extractor Agent**  
- **Role:** PDF Data Extractor  
- **Purpose:** Extract the following key contract terms from PDF documents and present them in a structured JSON format:

    1 Limitation of Liability

    2 Owner Expiry Date

    3 Notice Period

    4 Agreement Duration

    5 Payment Terms

    6 Confidentiality Period

    7 Insurance Coverage

    8 Maximum Monthly Hours

    These terms should be extracted accurately and presented in a JSON format for easy reference and further analysis..  
- **Description:** This agent specializes in scanning and extracting important contract terms with precision.  
  
  ---

### 2. **Comparison Agent**  
- **Role:** Data Comparison Analyst  
- **Purpose:** Compare the extracted contract terms with our reference values and identify any discrepancies. For each term:

    Compare the extracted value against our reference standard
    Determine if the contract term is equal to, more favorable, or less favorable than our reference
    Calculate the variance (where applicable)
    Flag terms requiring negotiation

    **Reference values:**

    Limitation of liability: 30 days
    Owner expiry date: 34 days
    Notice period: 10 days
    Agreement duration: 12 months
    Payment terms: 80 days
    Confidentiality period: 3 years
    Insurance coverage: $1,000,000
    Maximum monthly hours: 120  
- **Description:** This agent ensures that extracted terms align with expected reference data, highlighting discrepancies.  

  ---

### 3. **Report Gererator Agent**  
- **Role:** Compliance Report Generator  
- **Purpose:** Create a comprehensive comparison report in table format showing how extracted contract terms compare with reference values. For each key term:

    Compare the extracted value from the document against our reference standard
    Evaluate the level of risk any discrepancy presents
    Provide a brief analysis of implications
    Assign a status indicator based on the comparison:

    GREEN: Values match exactly or contract term is more favorable
    YELLOW: Values are close but not exact (within acceptable tolerance)
    RED: Values significantly differ or term is missing/unfavorable



    Format the output as a table with these columns:
    | Term Name | Reference Value | Extracted Value | Risk Level | Analysis Summary | Status |  
- **Description:** This agent analyzes discrepancies and provides a structured compliance report with insights.  
  

---  

## Task Assignments  

### 1. **PDF Extraction Task**  
- **What it does:** Extracts key terms from the uploaded contract document.  
- **Who performs it:** PDF Data Extractor Agent
- **Expected Output:** A structured list of key terms from the document.  

### 2. **Data Comparison Task**  
- **What it does:** Compares extracted terms with reference data to identify mismatches.  
- **Who performs it:** Comparison Agent
- **Expected Output:** A report listing all mismatched data points.  

### 3. **Final Report Generation Task**  
- **What it does:** Creates a detailed compliance report based on mismatches found.  
- **Who performs it:** Report Gererator Agent 
- **Expected Output:** A structured compliance report with insights and recommendations.  

---  

## Summary  

This AI-powered system automates contract analysis using three specialized agents:  
1. **PDF Data Extractor Agent**  extracts key terms from PDFs.  
2. **Comparison Agent**  compares the extracted data with reference values.  
3. **Report Gererator Agent**  generates a compliance report highlighting mismatches.  

---  



 

🔗 Feel free to **modify and play around** with these resources to deepen your understanding! 🎯  




---

## ⚠️ Challenges You May Face in Langflow
While running Langflow, you might encounter some bugs related to network connectivity and session creation. If you see an error or face issues while creating a new session, don’t worry. Simply refresh the page and try again.

Behind the scenes, everything continues to function properly—this is just a known Langflow bug that you can safely ignore.




