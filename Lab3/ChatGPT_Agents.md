# Analysing a contract and generating results for key terms and storing them in a CRM

In this tutorial we will learn how to create a ChatGPT agent that can extract key terms and store them in a CRM for an uploaded contract.

## Pre-requisites
1. Airtable API key
2. Airtable URL
3. ChatGPT subscription
4. OpenAPI schema for Airtable API

### Any Airtable related query please refer to the instructions provide in the following file:

**** Insert you key term names in the column instead of the ones given in the instruction below ****

[Click here](../Lab2-solargen-with-function-calling/airtableapi.md)


After creating an airtable account and setting up the API key, and adding key terms you should see something like this:
![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/85980200-3045-4c52-901f-6c03fcc05785)

### OpenAPI Schema
Now we will create the OpenAPI schema for the Agent to call in order to save the data generated

Click here to find the OpenAPI schema that we are using: [Schema](Airtable_OpenAPI.yaml)

1. The Airtable URL that you had just saved is broken into two parts-
   1. Base URL- This is how the base URL looks like ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/9c1b0118-75ab-4489-85f7-57c58820c270)

   2. Paths- This is how the path of the table looks like ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/11c83431-8b26-42e1-a283-fc4efd86defa)

  Replace the servers URL and the paths in the OpenAPI schema like shown below.

  ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/6d943202-3299-496d-a90c-ab0dc13eb889)


2. Now as we are trying to save the data in the CRM, we will be using POST method. This POST method has the request body that will be sent with the request.

   It will store the names, parameters to be sent to the airtable API. So basically this is how the Airtable expects the request.
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/8f9dbcb9-4e1c-450b-b053-adf2430725e9)

   And this is what we have created in the OpenAPI schema.

   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/a3f82e64-3f0e-4932-92ac-bf8c5aca9bfc)

   We have the records parameter as array, which stores the fields dictionary containing the keys, and the values will come from the Agent.

3. Finally we mention the response format after calling the API.
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/8f0e2131-6260-4dea-9410-158ae5c31beb)

### Now lets move on to creating the Agent itself.

Lets go through this step by step.

1. Click on this [link](https://chat.openai.com/g/g-POb5UhhJ6-autogpt-agent) and it will take you to the Agent creation page of ChatGPT
2. After logging in/signing up, you will be prompted to buy subscription. This is what it looks like.
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/aeaaac7a-6355-4b34-a856-b1154c2b3dd9)

   Buy the Plus plan if you want to use it for individual learning, else if you want to share you models with you team/work you need to buy the Team plan.
3. Click on the Explore GPT option
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/70e348c1-d34c-4240-acaa-dbf483d66315)
4. This is the page you will land in
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/2b18876e-dd6c-4919-98c6-810642ca5dec)

   Click on the Create button to create a new Agent.
5. You will be brought here.
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/9a3b9920-8d8d-4158-bdb8-60ac2b2fa99e)

   This is where the real stuff will happen.
6. If you notice you have two tabs as Create and Configuration.
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/730d1efb-83f2-4563-b989-1a81e52f2cab)

   Create tab can be used to set up the agents using prompting. For example: This is the prompt we will use "you are an professional lawyer who's job is to analyse uploaded contracts and generate answers to key terms also use actions to store the answers in a CRM."
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/a09ccdaa-afbf-4cd5-a2c5-7b433dc1f35c)

   You will see that the Agents has been auto configured and is set for minimal use
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/81853f3b-8370-4863-9b3c-f0bc5611c3b0)

  Also if you switch to the configuration tab the fields have been populated without the need to perform manual configuration
  ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/acb919a0-e6f9-468f-bb45-f915b586cc79)

7. So, in our case we did the entire process manually, using the configuration tab. Here's how we did it.
```
  Name: Workshop101
  Description : This agent analyzes contracts, extracts key terms, and stores them to a CRM.
  ```
  The Instructions we procvided was large and needs to be very detailed for the agent to funciton properly.
  ```
You are a legal agent whose job is to analyze a contract and get answers to the key terms mentioned below in square brackets:
Also remember that the Contract Name is the file name itself.
[Contract Name
Service Provider Name
Customer Name
Contract start date
Contract end date
Term Period In Months
Deal Value
Governing Law
Auto Renewal
Termination Notice In Days
Data Breach Notice In Hours
Billing frequency (monthly, quarterly, annually, other)
Renewal Period (Months)
Notice of termination for convenience
Net payment terms (Net 30, 45, 60, 75, 90, other) 
Termination for Breach (Yes, No, N/A)
Termination for cause (Yes, No, N/A)
Termination without cause (Yes, No, N/A)
Termination for convenience (Yes, No, N/A)
Late Payment Charges (Yes, No, N/A)
Late Payment Penalty
Limitations of liability (Amount)
Assignment (consent, No consent, N/A)
Name and logo use (Yes, No, N/A)
Deletion of Data (Yes, No, N/A)
Customer Indemnity
Service Provider indemnity
Customer notice for indemnity claim
Indemnify Attorney fees (Yes, No, N/A)
Price increase (Yes, No, N/A)
Notice for price increase (days)
Insurance Clause
Maintenance of Insurance
Provide notice for insurance (Days)
Service Provider Intellectual Property Rights
Customer Intellectual property rights]

After getting the results for these key terms, display them in a tabular format with column names as key terms and the rows containing the value for each of these key terms.
 Once the table is generated, call the appropriate action created to save these results to a CRM.
```
You can also add Conversation starters that the users can use.

We have our conversation starters as:
![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/f88241f7-dcc0-44f3-af9b-7e6c691b3402)

This is what the initial setup looks like:
![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/9a64cdc5-a06c-46d8-aff9-285a8f69c81d)


8. Now let's go and add out Action, that is the using the OpenAPI schema to enable the agent to use Airtable CRM.
9. Scroll Down and you will find the Actions section where you need to click on `Create New action` button
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/15adfde7-cb2a-45b5-aa19-dc2576ce583f)
10. On the following page you will see some thing as such.
    ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/1d6d810e-9573-45e6-9acf-f5aeab4db56f)
11. Click on Authentication and select the following option.
    * Select Authentication type as `API_KEY`
    * Select Auth type as `Bearer`
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/9021d378-a57a-4c91-8310-d24fdd4bcfc4)


    * In the API Key input field insert the Airtable API key you had saved earlier.
    
    ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/0360c5e8-9f32-4fce-bc35-13369afc3d47)

13. Insert the OpenAPI schema you had created earlier in the Schema field. This is what it should look like.
    ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/516759a8-3788-4dc7-96bf-fc27cfe000a2)

    Down below you will find the `Test` button. You can use this button to see if the agent is able to use the OpenAPI schema to call the API successfully or not.
    ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/87fff992-28c5-4b8a-bfaf-910cc836d729)

    Here the Agent will user dummy values for the Request body and try to send POST request to the Airtable API.

    While testing you might be prompted with this `Confirm` button. Click on it. If your Request was successfull you will be shown this.
    ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/0bebf92c-2056-41e2-b1b0-49ee81f79522)

14. Now, go back to the Configuration page. As all the set up is now complete, we will test our agent.

## Testing/Output
1. First we will upload a contract that we want to analyse. Click on the button circled in red.
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/29388ac5-e8f0-4b77-87d7-d1ccc47ceecf)

2. We have uploaded a Master Service Agreement and given it a simple instruction on what to do.
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/4690259d-fdce-4cc8-9c68-3d393e9a5f3b)

   Hit Enter

   The Contract will be analysed and the answer to the key terms will be generated in a tabular format as we have explicitly mentioned it in the instruction while configuring the agent.
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/2f1b5f03-9ee0-4cbe-bbb4-7b634435f749)
After this the Agent will try to store it in the Airtable CRM. Just like we did it previously, click on Confirm.

If everything goes smoothly, this is what you will be shown.
![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/7010f1c3-0bcf-46fb-9480-6320924877ea)

3. Check the Airtable CRM now.
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/06a8bfc6-921c-4726-b30a-225cd309bd9b)

As you can see the Record has been stored in the CRM. And that's it. You have successfully built your Agent.

## Final Note

You will not be able to Update it but you configurations will be saved. As we mention earlier the API we are using of Airtable is a private URL and cannot be exposed to the Public. Due to this reason the Model you created cannot be published in the GPT store.

Any API that you use that provide free access will allow you to publish the model in the GPT store.
