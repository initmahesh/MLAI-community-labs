# Integrating Langflow with V0 and Lovable

This lab demonstrates how to integrate Langflow, a powerful tool for building frontend application. This integration allows you to create AI workflows that can be controlled and visualized through a modern web interface.


# Prompt 
You need go build a chat bot  

Here is my curl command : 
```bash
curl --request POST \
  --url 'https://api.langflow.astra.datastax.com/lf/54941d66-0c11-4ef7-9c95-c7c80194b2be/api/v1/run/edb521bf-1041-4c0a-bc0f-edeb347682be?stream=false' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer <Replace With Your Token>' \
  --data '{
    "input_value": "Hello",
    "output_type": "chat",
    "input_type": "chat"
  }'
```

This is my sample respose 
```json
{
  "session_id": "edb521bf-1041-4c0a-bc0f-edeb347682be",
  "outputs": [
    {
      "inputs": {
        "input_value": "Hello"
      },
      "outputs": [
        {
          "results": {
            "message": {
              "text": "Hello! 🌟 I'm excited to help you get started on your journey to building something fresh! What do you have in mind? Whether it's a project, an idea, or a concept, let's dive in and make it happen!",
              "sender": "Machine",
              "sender_name": "AI",
              "session_id": "edb521bf-1041-4c0a-bc0f-edeb347682be",
              "timestamp": "2025-05-27T08:33:53+00:00",
              "flow_id": "edb521bf-1041-4c0a-bc0f-edeb347682be",
              "error": false,
              "edit": false,
              "properties": {
                "source": {
                  "id": "OpenAIModel-2AfbE",
                  "display_name": "OpenAI",
                  "source": "gpt-4o-mini"
                },
                "icon": "OpenAI",
                "state": "complete"
              }
            }
          },
          "artifacts": {
            "message": "Hello! 🌟 I'm excited to help you get started on your journey to building something fresh! What do you have in mind? Whether it's a project, an idea, or a concept, let's dive in and make it happen!",
            "sender": "Machine",
            "sender_name": "AI",
            "type": "object"
          }
        }
      ]
    }
  ]
}

the following is my token : <Replace with Yor Token>
```
