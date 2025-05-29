# MSA Document Processing Copilot Agent

## Overview

This project implements an intelligent Copilot agent that processes Master Service Agreement (MSA) documents. The agent is designed to automatically extract key terms and trigger relevant workflows based on the document content.

## Features

- Automated MSA document processing
- Key term extraction from legal documents
- Intelligent workflow triggering based on document content
- Integration with document management systems

## Implementation Steps

### Step 1: Building Flow

[Video Tutorial: How to Build Flow](https://pragyaallc-my.sharepoint.com/:v:/g/personal/sachin_parmar_legalgraph_ai/EcK7u0NBywJBhYGlNafqN1YBvUq9mAX0BLUduQnzX7XIKw?e=0fFiRh&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D)

#### Required Tools

- [Power Apps](https://make.powerapps.com/) - For building prompts
- [Copilot Studio](https://copilotstudio.microsoft.com/) - For creating and managing the Copilot agent

The initial flow setup includes document processing and key term extraction using two main prompts:

#### Flow Expression For the ComposeDataURItoBinary

```javascript
dataUriToBinary(first(outputs('Parse_JSON')?['body']?['OriginalAttachments'])?['contentUrl'])
```

#### File Context Schema for Parse JSON

```json
{
  "type": "object",
  "properties": {
    "content": {
      "type": "object",
      "properties": {
        "OriginalAttachments": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "contentType": {
                "type": "string"
              },
              "contentUrl": {
                "type": "string"
              },
              "name": {
                "type": "string"
              }
            }
          }
        },
        "attachmentSizes": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "Value": {
                "type": "integer"
              }
            }
          }
        },
        "clientActivityID": {
          "type": "string"
        },
        "enableDiagnostics": {
          "type": "boolean"
        },
        "testMode": {
          "type": "string"
        }
      }
    },
    "schema": {
      "type": "object"
    }
  }
}
```

#### Prompt 1: MSA Document Verification

```
Analyze the provided text and determine whether it is a Master Service Agreement (MSA). An MSA typically includes key terms such as:
- Scope of Services
- Term and Termination
- Payment Terms
- Confidentiality
- Indemnification
- Limitation of Liability
- Dispute Resolution
- Governing Law
- Statements of Work (SOW) References

If the document contains most of these key terms and follows the standard structure of an MSA, respond with 'Yes'. Otherwise, respond with 'No'. No additional text or explanation is needed.
```

#### Prompt 2: Key Information Extraction

```
Analyze the provided text and extract the following key information:
- Service Provider Name
- Customer Name
- Termination Clauses
- Contract Term/Duration
- Payment Terms

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

#### JSON Schema (PARSONJSON Component)

```json
{
  "type": "object",
  "properties": {
    "Service Provider Name": {
      "type": "string",
      "description": "Name of the service provider"
    },
    "Customer Name": {
      "type": "string",
      "description": "Name of the customer"
    },
    "Contract Term/Duration": {
      "type": "string",
      "description": "Duration of the contract"
    },
    "Payment Terms": {
      "type": "string",
      "description": "Payment terms of the contract"
    },
    "Termination Clauses": {
      "type": "string",
      "description": "Termination clauses of the contract"
    }
  },
  "required": [
    "Service Provider Name",
    "Customer Name",
    "Contract Term/Duration",
    "Payment Terms",
    "Termination Clauses"
  ]
}
```

### Step 2: Building Flow in Copilot Agent

[Video Tutorial: How to Build Flow in Agent](https://pragyaallc-my.sharepoint.com/:v:/g/personal/sachin_parmar_legalgraph_ai/EdP3eSOYjMxOs-bnEzVija8ByjmMUSfJBkfCFdZveDfMwg?e=QhZpNk&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D)

### Step 3: Integrating Flow with Agent

[Video Tutorial: How to Integrate Flow with Agent](https://pragyaallc-my.sharepoint.com/:v:/g/personal/sachin_parmar_legalgraph_ai/EfsRw4YyUQNNjhS2OfdHqTsBVAzqvhcXAWjB5t5oBXD49A?e=y9XP9Z&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D)

### Testing

[Video Tutorial: Testing the Implementation](https://pragyaallc-my.sharepoint.com/:v:/g/personal/sachin_parmar_legalgraph_ai/Ea98XcoBDZBEhgHvD3Xn1UIBIzdlMdoIOJ1wVVghu5OlBQ?e=XnakYm&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D)

## How It Works

1. **Document Input**: The system accepts MSA documents in various formats
2. **Processing**: The Copilot agent analyzes the document content
3. **Key Term Extraction**: Important terms and clauses are automatically identified and extracted
4. **Workflow Automation**: Based on the extracted information, relevant workflows are triggered
