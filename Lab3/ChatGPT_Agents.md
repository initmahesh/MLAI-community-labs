# Analysing a contract and generating results for key terms and storing them in a CRM

In this tutorial we will learn how to create a ChatGPT agent that can extract key terms and store them in a CRM for an uploaded contract.

## Pre-requisites
1. Airtable API key
2. Airtable URL
3. ChatGPT subscription
4. OpenAPI schema for Airtable API

Any Airtable related query please refer to the instructions provide in the following file:

[Click here](Lab2-solargen-with-function-calling/airtableapi.md)

**** Insert you key term names in the column instead of the ones given in the instruction above,****


After creating an airtable account and setting up the API key, and adding key terms you should see something like this:
![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/85980200-3045-4c52-901f-6c03fcc05785)


Now we will create the OpenAPI schema for the Agent to call in order to save the data generated
