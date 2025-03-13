## What is Agentic AI?
At its core, Agentic AI is a type of AI that’s all about autonomy. This means that it can make decisions, take actions, and even learn on its own to achieve specific goals. It’s kind of like having a virtual assistant that can think, reason, and adapt to changing circumstances without needing constant direction.

## What is a Tool in Agents?  
In the context of agents, a tool is a function or interface that an agent can use to perform specific actions or tasks. Tools extend the agent's capabilities, allowing it to interact with the environment or access external systems to gather information or execute commands. For example, an agent might use a tool to retrieve the current time, access an external database, or perform web searches.

## What Is Reflection?
Reflection is a prompting strategy used to improve the quality and success rate of agents and similar AI systems. It involves prompting an LLM to reflect on and critique its past actions, sometimes incorporating additional external information such as tools and observations.

## 📌 Note
For this lab, we are using **Power Automate** to create and manage automated workflows. This tool helps streamline repetitive tasks, improve efficiency, and integrate various services seamlessly.  

## What is Power Automate?  

Power Automate is a **low-code, drag-and-drop automation tool** by Microsoft that enables users to **automate repetitive tasks and business processes** across various apps and services. Previously known as **Microsoft Flow**, it integrates seamlessly with **Microsoft Office 365** and **Microsoft Azure**, helping boost productivity by eliminating manual workflows.  

With **150+ standard connectors** (and additional premium ones), Power Automate supports everything from **simple task automation to complex system workflows**, allowing users to focus on more strategic work.  

🎥 **Watch this video to learn more:** [Power Automate Overview](https://youtu.be/yVAEH6-ui0w?si=Ne3pXYQp-uZnHGOR)  


### Step 1:  
> **Click on** [this link](https://make.powerautomate.com) **to be redirected to Power Automate.**

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
📥 **Download the ZIP file from here:** [https://github.com/initmahesh/MLAI-community-labs/blob/main/Class-Labs/Lab-3(Power-Automate)/PowerAutomateLab_20250312211304.zip] 
![Power Automate Dashboard](Images/Screenshot%20(1747).png)

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
> **2. Click on "Open Flow" to access and review your imported flow.**  
![Power Automate Dashboard](Images/Screenshot%20(1753).png)

## Step 5 : Interacting with Your Flow  

Now that your flow has been successfully imported, you can see it in your **My Flows** section.  
![Power Automate Dashboard](Images/Screenshot%20(1754).png)

> **Feel free to explore and experiment with it!** 🎯  
> You can modify actions, add conditions, or test the flow to ensure it works as expected.  

# Step 6 : Demo Video  

## Demo Video 1  
In this video, I extract all the key terms from the MSA document and pass them to the user, showing the extracted terms.  
![Watch Demo Video 1](Videos/v1.mp4)  

## Demo Video 2  
If any key term is not found, the system enhances the query and tests again. If still not found, it sends an email to the admin for manual review.  
![Watch Demo Video 2](Videos/v2.mp4)  

## Demo Video 3  
If the attachment contains irrelevant content, the flow will not proceed.  
[Watch Demo Video 3](Videos/v3.mp4)  


🚀 **Start automating now!**  
