# ⚡️ Langflow Integration with v0 - (Build a Complete AI-Powered Competitor Analysis Tool)



### Overview

You’ve built your frontend. It looks clean, it works fast, and it’s powered by AI prompts — thanks to **V0**.

But now you want more.

Imagine this: your users input two companies and click “Analyze.” Behind the scenes, your own **Langflow backend** wakes up — processing, reasoning, and comparing data using powerful AI chains you've designed.

The result? A fully connected product — where the frontend and backend work in sync, delivering real-time insights with just one click.

This lab is where it all comes together.

You’ll learn how to connect your **Langflow backend** to your **V0-generated frontend**, transforming a static interface into a truly intelligent competitor analysis tool.

---

### What You Will Build

- A fully functional AI-powered competitor comparison tool  
- A modern, responsive frontend built with V0  
- Real-time API connection to your Langflow backend  
- A professional UI that displays dynamic AI-generated results


---

## Prerequisites

Before beginning, ensure you have completed the following requirements:

### 1. Get Your OpenAI API Key

You will need your personal OpenAI API key to connect Langflow to GPT models. Follow this guide to get your key:  
🔗 [How to Get Your OpenAI API Key](https://medium.com/@lorenzozar/how-to-get-your-own-openai-api-key-f4d44e60c327)

---

### 2. Get Your Tavily API Key

Before you proceed, you need a Tavily API Key. Follow these steps:

1. Navigate to [https://www.tavily.com/](https://www.tavily.com/)
2. Click on the **Login** button in the top-right corner  
   ![Tavily Login](./images/img-20.png)
3. Once logged in, go to your dashboard and copy your Tavily API key  
   ![Tavily Dashboard](./images/img-19.png)

**Important:** Keep your Tavily API key secure. You will use it later inside the Langflow component.

---

### 3. Langflow Login Setup

Follow the instructions provided in the Langflow Login Guide:  
📘 [Langflow Login Guide](../../Lab-0(Pre-requisites)/Langflow-Login-Guide/Readme.md)

---

### 4. Langflow Flow File

Download the required Langflow flow from the link below:  
📁 [Download Langflow Flow](https://drive.google.com/file/d/1B4ZCKSxQXmrtmxR2AcW3ybVtmpAnXBaf/view?usp=sharing)

---

### 5. Access to the V0 Platform

Log in to the official v0 platform:  
🌐 [Visit V0](https://v0.dev/)

---

### 6. Postman Login

Download the desktop app from the [Postman Downloads Page](https://www.postman.com/downloads/).


---

> # **Important Note:** After importing, always verify that all nodes are properly connected to each other. Sometimes during import, nodes might become disconnected. Check the flow diagram carefully and reconnect any disconnected nodes by dragging the connection points between them. The data flow should be continuous from the input to the output nodes.

---

## Step-by-Step Integration Instructions

### Step 1: Log in to Langflow Web
Ensure you are logged in to Langflow web. Refer to the login guide if you have not completed this step.

### Step 2: Create a New Flow
Click the **New Flow** button on your Langflow dashboard.

![New Flow Button](./images/img-1.png)

### Step 3: Select Blank Flow
Choose **Blank Flow** to start with a clean canvas.

![Blank Flow Selection](./images/img-2.png)

### Step 4: Import a Flow
Click the dropdown menu in the top-left corner and select **Import**.

![Import Flow Option](./images/img-3.png)

### Step 5: Import the Langflow JSON File
Select the `.json` file downloaded in the prerequisites step to load the predefined flow.

![Select JSON File](./images/img-24.png)

**Note:** Ensure all components in the flow are properly connected as shown in the interface.

### Step 6: Add API Keys to Components
Locate the components that require API keys (OpenAI, Tavily) and enter your respective keys.

![Add API Keys](./images/img-5.png)

**Important:** Verify that the keys are valid and placed in the correct fields.

### Step 7: Edit the Prompt and Save
1. Click on the highlighted **Prompt** field to edit it
2. Use the **Check** button to validate your changes
3. Click **Save** once completed

![Edit Prompt](./images/img-6.png)

**Tip:** Customizing prompts improves accuracy and relevance of the AI responses.

### Step 8: Navigate to the Publish Section

You can also test the flow in the **Playground** section before publishing:

> **Tip 1:**  
> Click on the **Playground Section** button to open the interactive testing environment.  
> ![Playground Section](./images/img-21.png)

> **Tip 2:**  
> Click on **Run Flow** — make sure to provide the competitors' names in both text input components.  
> ![Run Flow](./images/img-22.png)

---

#### ✅ Now, proceed to publish:

1. **Go to the Publish Tab**  
   In the top-right corner of Langflow, navigate to the **Publish** tab to expose your flow as an API.  
   ![Publish Tab](./images/img-24%20-%20Copy.png)



### Step 9: Access the API Endpoint
Click on the **API Access** tab to retrieve your flow's base URL and authorization details.

![API Access](./images/img-25.png)

**Note:** This API endpoint will be required for v0 integration.

### Step 10: Access the cURL Command
Scroll to the **cURL Command** section and click **Tweak** in the top-right corner to adjust request parameters visually.

![cURL and Tweak](./images/img-9.png)

### Step 11: Modify Tweak Parameters
Under **Input Variables**, change the values to competitors you would like to compare (e.g., `Google` and `Microsoft`).

![Tweak Parameters](./images/img-10.png)

### Step 12: Generate Token and Copy cURL Command
Complete the following steps:

**Important:** Before copying the cURL command, remove `input_value = hello world` or similar default values from the command to ensure clean integration.

1. Click **Generate Token** to obtain a valid authentication token
2. Copy the **cURL command** displayed below

![Generate Token and CURL](./images/img-11.png)

> 💡 **Note:**  
> When you're ready to test your Langflow backend, your `cURL` command should look like this:

```bash
curl --request POST \
--url 'https://api.langflow.astra.datastax.com/lf/54941d66-0c11-4ef7-9c95-c7c80194b2be/api/v1/run/3518ac99-790a-4672-b2a3-0f507c9b6083?stream=false' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer AstraCS:pClJHlQZdoUoDGzyTYnQRoQh:679219da964bc27070547762e971b9c08d96fde8b12490ac762b238f49e231bd' \
--data '{
  "output_type": "chat",
  "input_type": "text",
  "tweaks": {
    "TextInput-EvFZI": {
      "input_value": "Google"
    },
    "TextInput-lRnOb": {
      "input_value": "Microsoft"
    }
  }
}'
```

> Replace the `<YOUR_APPLICATION_TOKEN>` token and input values with your own to match your Langflow setup.

### Step 13: Test the API Call Using Postman

Once you're done with the previous steps, it's time to test your API.

1. If you haven’t already, download the **Postman** app from the link provided in the **Prerequisites** section.
2. Install and open the app, then log in with your credentials.
3. You will see an interface similar to the one shown in the image provided.
4. Click on **"New"** → **"HTTP Request"** or simply **"Request"** to begin.

This will help you validate your API is working as expected.
![Open Postman](./images/img-23.png)

### Step 14: Postman Interface
 Once you've completed the login process, you will see an interface like the one shown in the image below.

![Open Postman](./images/img-12.png)

### Step 15: Import cURL Command
Copy the cURL command from Langflow and paste it into the Postman input field. Postman will automatically configure the request with the appropriate method, URL, headers, and body.

![Paste cURL in Postman](./images/img-13.png)


### Step 16: Send Request and Retrieve Response
Click the **Send** button in Postman. The Langflow backend will process the request and provide a response based on your prompt and parameters. You can copy this response for further use or testing.

![Send Request and Response](./images/img-15.png)

**Note:** Sometimes the request may take longer to process due to Langflow server latency. If the response does not appear immediately, retry the request.

### Step 17: Navigate to V0 Interface
Access the [V0 Platform](https://v0.dev/). Once logged in, you will see an interface similar to the one shown below:

![V0 Interface](./images/img-16.png)

### Step 18: Use the Reference Prompt in V0
Below is a reference prompt you can use in V0 to connect your Langflow API.

**Important:** Make sure to replace the Bearer Token with your actual token and update the sample response with the one you received from Postman.

#### Prompt Template

 > 📌 **Note:**  
> This prompt is designed to connect your Langflow API with a frontend landing page.  
> 🔄 Be sure to:
> - Replace the **Endpoint** section with your actual cURL command (with Bearer token)
> - Replace the **Request Body** with the **actual sample response** you received from Postman

 ```
Build a **modern, responsive landing page** for a **Competitor Comparison Tool** using the provided API.

Requirements

* Two input fields (Company A & B) + Compare button
* Call API with inputs (handle **CORS** and show **loading spinner**)
* Extract markdown table from:
  `response.outputs[0].outputs[0].results.message.text`
* Convert to **responsive HTML table**
* Show **summary** below table
* Add **error handling** for failed API calls
* Use **smooth animations & transitions**

Resources

Here is my cURL Command:
  `<your curl command>`   // You’ve already created the cURL command in **Step 12** — copy it from there.
  

Here is my sample Response:
  `<your Postman sample response>`  // Use the response you captured in **Step 15** (from Postman)

```
### 19. Final Integration & Frontend Behavior

Once you are done with all the setup:

- You will see a **fully functional frontend landing page**.
- When you click on the **"Compare"** button:
  - It will send a **request to your Langflow backend** using the input values.
  - The request uses the **curl command structure** with your **Bearer Token**.

> ⚠️ **Note:** The request might take some time to process because **Langflow servers can be slow**. If no response appears, try hitting the Compare button again.

![Send Request and Response](./images/img-17.png)

![Send Request and Response](./images/img-18.png)
---

### What Happens Behind the Scenes

1. The frontend sends a `POST` request to your Langflow API.
2. Langflow processes the prompt and returns a **markdown response**.
3. The frontend:
   - Extracts the markdown from:  
     ```js
     response.outputs[0].outputs[0].results.message.text
     ```
   - Parses it into a **responsive HTML table**.
   - Displays a **summary** below the comparison table.
   - Shows **loading spinners** and handles any **API errors**.

---
## Troubleshooting

### Common Issues & Solutions

| Issue | Symptoms | Solution |
|-------|----------|----------|
| **API Timeout** | No response after clicking Compare | Retry request; Langflow servers can be slow |
| **Invalid Token** | 401 Authorization error | Regenerate token in Langflow Publish section |
| **CORS Error** | Request blocked by browser | Ensure proper headers in frontend code |
| **Malformed Response** | Table not displaying correctly | Verify response extraction path |

---
**🎉 Huraaaah!** You've successfully built a complete AI-powered competitor analysis tool with modern frontend and intelligent backend integration. 

You’ve just taken an idea and transformed it into a sleek, interactive, and insightful **Competitor Comparison Tool**.

From setting up the UI and handling API calls, to transforming complex data into a responsive table — you've done what a true **Product Manager and Developer** does best: **turn vision into a working product**.

Take a step back and appreciate the impact of what you've built.  
Whether it's helping startups benchmark competitors or enabling enterprises to make strategic decisions your tool delivers real value.

👏 Be proud. You didn’t just code a page — you built a product.

---

## Additional Resources

- **Langflow Documentation:** [Official Docs](https://docs.langflow.org/)
- **V0 Platform Guide:** [v0.dev Documentation](https://v0.dev/docs)
- **Postman API Testing:** [Testing Best Practices](https://learning.postman.com/)



