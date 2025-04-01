## Enterprise scale automation with MSFT Power Automate

For this lab, we are using Power Automate to create and manage automated workflows. This tool helps streamline repetitive tasks, improve efficiency, and integrate various services seamlessly. 

In this flow, you will learn how you can automate workflows, we will also cover reflection where we will check if the extracted terms meet our expectation. For example, if they all terms are extracted and they don't have "not found" key term from contract - in cases where we do have not found terms we call "human in loop" to verify and respond to customers.

## What is Power Automate?  

Power Automate is a **low-code, drag-and-drop automation tool** by Microsoft that enables users to **automate repetitive tasks and business processes** across various apps and services. Previously known as **Microsoft Flow**, it integrates seamlessly with **Microsoft Office 365** and **Microsoft Azure**, helping boost productivity by eliminating manual workflows.  

With **150+ standard connectors** (and additional premium ones), Power Automate supports everything from **simple task automation to complex system workflows**, allowing users to focus on more strategic work.  

🎥 **Watch this video to learn more:** [Power Automate Overview](https://youtu.be/yVAEH6-ui0w?si=Ne3pXYQp-uZnHGOR)  

# Note: Account Creation Prerequisite

**To create your account and access the 30-day free trial, you will need a valid work or college email address. If you don't have a work or college email address, please don't go further. Reach out to our team and they will help you.**

### Step 1:  
> **Click on** [this link](https://make.powerautomate.com) **to be redirected to Power Automate.**
![Create Account Button](Images/Screenshot%20(1783).png)

### Step 2:  
> **Click on "Create one"** to start setting up your account.  
![Create Account Button](Images/Screenshot%20(1731).png)

### Step 3:  
> **Enter your email address** and proceed to the next step.Provide your basic details like **Date of Birth (DOB)** and enter the **OTP** sent to your email for verification.
![Create Account Button](Images/Screenshot%20(1732).png)

### Step 4:  
> Once you create your account, you will be redirected to the **Power Automate Dashboard**, which will look something like this:  

![Power Automate Dashboard](Images/Screenshot%20(1733).png)  


# Let's Start with My Flow  

In this section, we will go through the **flow** that I have created using Power Automate. This flow automates tasks efficiently and enhances productivity. Let's dive in! 🚀 

![Flow Diagram](Images/flow.png)  


## Step 1: Importing the Flow  

> **1. Click on "My Flows"** in the sidebar.  
> **2. At the top, click on "Import".**  
> **3. Select the Import Package** you want to import.  
> **4. You will be redirected to the upload page.**  

![Power Automate Dashboard](Images/Screenshot%20(1735).png)  

## Step 2 : Uploading the Flow  

> **1. Select and upload the **ZIP file** that has been provided to you in the repo.** 

## **"This is the ZIP file you need. Just click on the file and download it from the top."**
![Power Automate Dashboard](Images/Screenshot%20(1791).png)
![Power Automate Dashboard](Images/Screenshot%20(1792).png)

> **2. Click on "Upload"** 

## Step 3: Flow Imported Successfully ✅  

![Power Automate Dashboard](Images/Screenshot%20(1736).png)  

> **1 Once you upload your package file, click on "Update"**. 
![Power Automate Dashboard](Images/Screenshot%20(1748).png)
> **2. From the dropdown above, select "Create as New".**  
![Power Automate Dashboard](Images/Screenshot%20(1749).png)
> **3. Click on the "Save" button" to finalize the import process.**  
> **4. Click on "Select During Import".**  
![Power Automate Dashboard](Images/Screenshot%20(1750).png)
> **5. You will see your email address—select it.**  
![Power Automate Dashboard](Images/Screenshot%20(1751).png)
> **6. Click on the "Save" button.**  
> **7. Repeat the same procedure for the below required connection as well.**  
> **8. Make sure all the connections are marked with a ❌ cross symbol before clicking the "Import" button.**  
![Power Automate Dashboard](Images/Screenshot%20(1752).png)

### 📌 Step 4 : Final Step: Accessing Your Imported Flow   

> **1. Once you click on "Import", you will see a confirmation message that the package has been imported successfully.**  
> **2. Once the flow is imported, go to 'My Flow' in the sidebar, click on your flow, and then click 'Turn On,' as shown in the image.**  
![Power Automate Dashboard](Images/Screenshot%20(1787).png)
> **3."Now, click on the 'Edit' option."**
![Power Automate Dashboard](Images/Screenshot%20(1788).png)
## Step 5 : Interacting with Your Flow  

Now that your flow has been successfully imported, you can see it in your **My Flows** section.  
![Power Automate Dashboard](Images/Screenshot%20(1754).png)

## **Note : In Condition 3, if the condition is false, click on the Email component. In the sidebar, provide a different email address to which the document should be sent for human evaluation. Enter the email of the specific human reviewer or admin.**

![Power Automate Dashboard](Images/Screenshot%20(1790).png)


## **When using this agent, you might be prompted to log in to an agent account. You will need to log in to another app, and you will receive a notification indicating that login is required to access it. Please note that the agent account comes with a 30-day free trial.**
![Power Automate Dashboard](Images/Screenshot%20(1793).png)


> **Feel free to explore and experiment with it!** 🎯  
> You can modify actions, add conditions, or test the flow to ensure it works as expected.  

# Step 6 : Demo Video  

## Demo Video 1  
In this video, I extract all the key terms from the MSA document and pass them to the user, showing the extracted terms.  
📄 [Reference Doc Link](https://drive.google.com/file/d/13LbQtQTd43SMMokCSB1JHcg3V5B0Qgvo/view?usp=sharing)  
🎬 [Watch Demo Video 1](https://drive.google.com/file/d/1DUcY_b7Q0yZDd-4qxagVOltawgOMvwCu/view?usp=sharing)  

## Demo Video 2  
If any key term is not found, the system enhances the query and tests again. If still not found, it sends an email to the admin for manual review.  
📄 [Reference Doc Link](https://drive.google.com/file/d/1o9FG4zd4C0GwKTjMvumNzIS6UoGobFOd/view?usp=sharing)  
🎬 [Watch Demo Video 2](https://drive.google.com/file/d/14AQZ-Z87t2dgsRTX13uZKM9O4jnoGyok/view?usp=sharing)  

## Demo Video 3  
If the attachment contains irrelevant content, the flow will not proceed.  
🎬 [Watch Demo Video 3](https://drive.google.com/file/d/1hAJg4cDSTOr0P0pl_wDuaa8EuoDQYPc_/view?usp=sharing)  

---

# 📄 Resources If You're Building It from Scratch

## Note : Don't replace the text of the prompt with my text. Just use the text that is given in the prompt. If you don't use them, there will be no save button to save your prompt.  

### Prompt 1  
- You can see the poition where we have to use this prompt.  
![Power Automate Dashboard](Images/Screenshot%20(1889).png)
---
- Structure Prompt In Power App
![Power Automate Dashboard](Images/Screenshot%20(1892).png)
---
## Prompt 
```
Analyze the provided  textand determine whether it is a Master Service Agreement (MSA). An MSA typically includes key terms such as:
Scope of ServicesTerm and TerminationPayment TermsConfidentialityIndemnificationLimitation of LiabilityDispute ResolutionGoverning LawStatements of Work (SOW) References
If the document contains most of these key terms and follows the standard structure of an MSA, respond with 'Yes'. Otherwise, respond with 'No'. No additional text or explanation is needed.*
```
---

### Prompt 2
- You can see the poition where we have to use this prompt.  
![Power Automate Dashboard](Images/Screenshot%20(1890).png)
---
- Structure Prompt In Power App
![Power Automate Dashboard](Images/Screenshot%20(1893).png)
---

## Prompt 
```
Analyze the provided text and extract the following key information:
Service Provider NameCustomer NameTermination ClausesContract Term/DurationPayment Terms
If ANY of these five elements cannot be found in the contract, your entire response must be only the two words "Not Found" without any other text, formatting, or explanation.
If ALL five elements are found, return them in this JSON format without any markdown formatting or code block indicators:
{
  "Service Provider Name": "extracted value",
  "Customer Name": "extracted value",
  "Termination Clauses": "extracted value",
  "Contract Term/Duration": "extracted value",
  "Payment Terms": "extracted value"
}
```
---

### Prompt 3
- 1 You can see the poition where we have to use this prompt.  
![Power Automate Dashboard](Images/Screenshot%20(1891).png)
---
- Structure Prompt In Power App
![Power Automate Dashboard](Images/Screenshot%20(1894).png)
---
## Prompt
```
The following is my previous prompt for extracting key terms from a document:
Reference Prompt:
"Analyze the provided document and extract only the following key terms in a structured key-value format:
Service Provider Name – Full legal entity name, including any DBA (Doing Business As) names.
Customer Name – Full legal entity name of the customer.
All Termination Clauses – Extract details of both for-cause and without-cause termination provisions, including required notice periods and any applicable termination fees.
Contract Term/Duration – Specify the initial term and any renewal provisions.
Payment Terms – Extract due dates, late fees, and any escalation clauses.
If any of the above details are not available in the document, enter 'Not Found' and return the response as 'Not Found' only. Else, return the response in the following structured JSON format:
{ 'Service Provider Name': '<Extracted Value>',
'Customer Name': '<Extracted Value>',
'Termination Clauses': '<Extracted Value>',
'Contract Term/Duration': '<Extracted Value>',
'Payment Terms': '<Extracted Value>'
}
Return the response as clean JSON with no markdown formatting, no code block indicators, and no text property wrapper."

Updated Prompt:
Please enhance the above reference prompt and extract key terms from the provided text . First, examine if ALL five required key terms (Service Provider Name, Customer Name, Termination Clauses, Contract Term/Duration, Payment Terms) are explicitly found in the document.

If ANY ONE of these five key terms contains "Not Found" or cannot be extracted from the document, respond with "NO" only - no additional text, no explanation.

Only if ALL five key terms are successfully extracted with actual values (not "Not Found"), return the complete extracted details in the following structured JSON format:
{
"Service Provider Name": "<Extracted Value>",
"Customer Name": "<Extracted Value>",
"Termination Clauses": "<Extracted Value>",
"Contract Term/Duration": "<Extracted Value>",
"Payment Terms": "<Extracted Value>"
}

The response must be either "NO" (if any key term is missing) or clean JSON with no markdown formatting, no code block indicators, and no text property wrapper.
```
---

## PARSE JSON SCHEMA

![Power Automate Dashboard](Images/Screenshot%20(1895).png)

## Schema
```
{
    "type": "object",
    "properties": {
        "Service Provider Name": {
            "type": "string",
            "description": "The name of the service provider."
        },
        "Customer Name": {
            "type": "string",
            "description": "The name of the customer."
        },
        "Termination Clauses": {
            "type": "string",
            "description": "Conditions under which either party may terminate the agreement."
        },
        "Contract Term/Duration": {
            "type": "string",
            "description": "The duration and terms of the contract."
        },
        "Payment Terms": {
            "type": "string",
            "description": "Payment conditions, including charges and billing details."
        }
    },
    "required": [
        "Service Provider Name",
        "Customer Name",
        "Termination Clauses",
        "Contract Term/Duration",
        "Payment Terms"
    ]
}
```
🚀 **Start automating now!**  
