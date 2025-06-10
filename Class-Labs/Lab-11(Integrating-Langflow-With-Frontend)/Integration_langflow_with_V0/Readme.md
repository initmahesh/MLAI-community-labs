# Langflow Integration with V0 Frontend

## Overview

This project demonstrates how to integrate Langflow, a powerful tool for building and visualizing LangChain flows, with a modern frontend built using V0. This integration allows you to create interactive and user-friendly interfaces for your LangChain applications.

---

## What is V0?

V0 is a generative user interface system developed by Vercel Labs that leverages AI to create modern React components. It offers several key features:

- Generates copy-and-paste friendly React code based on shadcn/ui and Tailwind CSS
- Allows users to describe desired interfaces in plain text
- Automatically generates the necessary React code based on text descriptions
- Built on top of shadcn/ui and Tailwind CSS for consistent, modern design
- Ideal for rapid prototyping and creating initial ("v0") versions of UI ideas

While V0 is powerful for frontend development, it's important to note that:

- Generated code requires review and refinement
- Currently focuses only on frontend development
- Does not handle backend logic
- Best used as a starting point for UI development

> **Note: V0 Pricing**
> V0 offers a free tier that includes:
>
> - $0/month
> - $5 of included monthly credits
> - Deploy apps to Vercel
> - Access to v0-1.5-md
> - Sync with GitHub
>
> This free tier is perfect for exploring and prototyping your Langflow integration.

---

## What is Postman?

Postman is a popular API development platform that simplifies the process of building, testing, and documenting APIs. It provides an intuitive interface for making HTTP requests, testing endpoints, and managing API collections. In this project, Postman will be used to test and interact with the Langflow API endpoints before integrating them with the frontend.

---

## Prerequisites

Before you begin, ensure you have access to the following tools:

1. **Langflow**

   - Download the Langflow JSON Flow File From Here: [Click Here](https://drive.google.com/file/d/1g84nSN4_BmuK_v1QHFlmolS3Ok_f9Yrt/view?usp=sharing)

2. **V0**

   - Access V0 at [https://v0.dev/chat](https://v0.dev/chat)
   - Create an account if you don't have one

3. **Postman**
   - Access Postman at [https://www.postman.com/](https://www.postman.com/)
   - Download the Postman desktop application or use the web version
   - Create a free account to save your API collections

## **Note:** For file uploads, please ensure the file is in .txt format. You can download the reference documentation file from here: [Reference Documentation](https://drive.google.com/file/d/1YfVQI9ZbEppM00CGi5aU0yJsuyFfe7WH/view?usp=sharing).

---

## Integration Tutorial

Watch our step-by-step video tutorial on how to integrate Langflow with V0:

# [Langflow V0 Integration Tutorial Video Link Click Here](https://pragyaallc-my.sharepoint.com/:v:/g/personal/sachin_parmar_legalgraph_ai/EWnlC99x7TBIq4rU1xqspKsB-427y4wpWObRB0DPy55biQ?e=e52WxU&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D)

The video covers:

- Setting up Langflow API endpoints
- Creating a V0 frontend interface
- Connecting Langflow with V0
- Testing the integration using Postman
- Best practices and troubleshooting tips

---

## Prompt for V0

```
You have to build a neat and clean frontend the task is pretty simple the user will upload a file and you need to first extract all the text from that file and then pass the complete file context in the curl command in input_value param and also the user can chat now so you need to build a chatbot also in the same divide the process into two steps step1 file uploading step 2 chat bot

Below is my curl command :
curl --request POST \
  --url 'https://api.langflow.astra.datastax.com/lf/54941d66-0c11-4ef7-9c95-c7c80194b2be/api/v1/run/a6436f86-2228-491f-8fd6-c0479116767e?stream=false' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer <YOUR_APPLICATION_TOKEN>' \
  --data '{
  "input_value": "hello world!",
  "output_type": "chat",
  "input_type": "chat",
  "tweaks": {
    "TextInput-kO36e": {
      "input_value": "Hello"
    }
  }
}'

Here is my token : <YOUR TOKEN KEY>


and below is the sample_response : {
    "session_id": "a6436f86-2228-491f-8fd6-c0479116767e",
    "outputs": [
        {
            "inputs": {
                "input_value": "hello world!"
            },
            "outputs": [
                {
                    "results": {
                        "message": {
                            "text_key": "text",
                            "data": {
                                "timestamp": "2025-06-10T03:00:57+00:00",
                                "sender": "Machine",
                                "sender_name": "AI",
                                "session_id": "a6436f86-2228-491f-8fd6-c0479116767e",
                                "text": "Hello there! How can I help you today?\n",
                                "files": [],
                                "error": false,
                                "edit": false,
                                "properties": {
                                    "text_color": "",
                                    "background_color": "",
                                    "edited": false,
                                    "source": {
                                        "id": "GoogleGenerativeAIModel-p1RXP",
                                        "display_name": "Google Generative AI",
                                        "source": "learnlm-2.0-flash-experimental"
                                    },
                                    "icon": "GoogleGenerativeAI",
                                    "allow_markdown": false,
                                    "positive_feedback": null,
                                    "state": "complete",
                                    "targets": []
                                },
                                "category": "message",
                                "content_blocks": [],
                                "id": "c23a6742-b5e4-4939-b6a4-e6b611f80ae6",
                                "flow_id": "a6436f86-2228-491f-8fd6-c0479116767e"
                            },
                            "default_value": "",
                            "text": "Hello there! How can I help you today?\n",
                            "sender": "Machine",
                            "sender_name": "AI",
                            "files": [],
                            "session_id": "a6436f86-2228-491f-8fd6-c0479116767e",
                            "timestamp": "2025-06-10T03:00:57+00:00",
                            "flow_id": "a6436f86-2228-491f-8fd6-c0479116767e",
                            "error": false,
                            "edit": false,
                            "properties": {
                                "text_color": "",
                                "background_color": "",
                                "edited": false,
                                "source": {
                                    "id": "GoogleGenerativeAIModel-p1RXP",
                                    "display_name": "Google Generative AI",
                                    "source": "learnlm-2.0-flash-experimental"
                                },
                                "icon": "GoogleGenerativeAI",
                                "allow_markdown": false,
                                "positive_feedback": null,
                                "state": "complete",
                                "targets": []
                            },
                            "category": "message",
                            "content_blocks": []
                        }
                    },
                    "artifacts": {
                        "message": "Hello there! How can I help you today?\n\n",
                        "sender": "Machine",
                        "sender_name": "AI",
                        "files": [],
                        "type": "object"
                    },
                    "outputs": {
                        "message": {
                            "message": "Hello there! How can I help you today?\n",
                            "type": "text"
                        }
                    },
                    "logs": {
                        "message": []
                    },
                    "messages": [
                        {
                            "message": "Hello there! How can I help you today?\n\n",
                            "sender": "Machine",
                            "sender_name": "AI",
                            "session_id": "a6436f86-2228-491f-8fd6-c0479116767e",
                            "stream_url": null,
                            "component_id": "ChatOutput-67yGN",
                            "files": [],
                            "type": "text"
                        }
                    ],
                    "timedelta": null,
                    "duration": null,
                    "component_display_name": "Chat Output",
                    "component_id": "ChatOutput-67yGN",
                    "used_frozen_result": false
                }
            ]
        }
    ]
}


make sure to handle the CORS error and also make sure the Ui should be neat and clean and user friendly
```
