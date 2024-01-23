# Invoking agents present in AWS and also creation of Agents using python.

## Prerequisites

For generating AWS Access keys follow this->https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html

### First we create the Lambda Function in AWS

1. Login to AWS platform
2. Firstly we will created a Lambda function that our agent will use to generate the output.
   Search Lambda in the AWS search bar.
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/f38b9426-844b-4183-bee3-8e2871153352)
   Click on the create function
    ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/57579212-8457-4c9b-b732-c79723fedb46)
3. Create the name of the lambda function, then select Python 3.10 as the runtime. Click on create function
4. Copy the code from the lambda_function.py here:
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/5b3c8a5f-7a26-45ae-899b-58fafe87eff8)
15. Next step
    Go to the Lambda->Configuration->Permission
    Click Add Permissions
    ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/0da7a57b-acf4-4f9e-b41c-69263e699fe1)
    ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/c1c882f7-08f2-4934-95b5-d0aab30cadac)
    ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/fc8967b9-7dab-474f-82ea-b52c3910b0a7)
    Specify a statement id.(It can be anything that you want it to be.)
    Specify the principle as bedrock.amazonaws.com
    Select lambda:InvokeFunction from the Action Dropdown. Click on Save
    ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/5915fa64-bd3a-402b-9084-4aef41dacc9c)

    Go to Configuration->General Configuration. Click on Edit.
    ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/6045a8b3-4c1e-4337-93c8-839d86479703)
    ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/6f2cc632-690d-4c1a-9aa7-d102ab54fc49)

    Change the Timeout value to 20 sec and hit save.
16. Go to Configurations->Environment Variables
    
    ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/6e1ebe2d-bb9d-4597-b1e0-ee87900dc5d4)

    Click on Edit to add environment variables. Here you can store your API keys for the lambda function to access.
    ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/c44bc41d-c20e-4e65-a3e3-9ce35bb152ad)
6. Click on Deploy.

###  we generate the Google APIs.

1. Visit the google cloud console
   https://console.cloud.google.com/welcome/
2. Go to APIs and services
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/48db1bb6-0178-4955-99ca-df00f0c43acf)
   Click on Enable APIS and Services
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/934500c8-2c1c-4ba5-98cc-7cbf337de43b)
3. Search for Geocoding API
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/49ddce46-1c10-49b2-9eea-5ece3e034f70)
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/c1413fc2-5e79-462a-be93-39818c848b2c)
   Select the API and Enable it.
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/aab3bb9a-ffc2-4887-b780-f205e1cca3dd)
4. Similarly search for Solar API and enable it.
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/ab431aea-4df4-4632-aa44-d92ee6d34d2c)
5. You will find your API key here
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/fe0286e6-2132-4ec9-a50f-9b5e0bf4d72f)
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/416eee6e-0660-4b69-bdec-a0c789399036)
   Click on show key.
6. Copy the key and keep it in the environment variable as shown while the creation of lambda function.
   and access them like this
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/85efc460-d6e5-4608-9ee9-172a2eea206e)
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/25308a83-6230-4fee-9b98-346f6d350cf1)


   After that click on Deploy.

Now that google API is set and ready to use. Finally we will setup the Airtable for CRM. Let's set it up.

1. Visit Airtable(Create an account if you do not have one)
   https://airtable.com/
2. Click on start from scratch
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/54f4a448-a8d7-446c-bb34-5182d97d53ae)
3. Change/Add the column names. (Column names are case-sensitive)
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/5623e480-30ce-495c-96e6-4af667bde130)
4. Once done, go to your account and click on Go to Developer Hub
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/169b5145-fd6c-481d-bc87-220a88eae507)
   Click on create token
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/40c61913-2e33-4fd8-affc-3925acabd8f5)
   Click on create new token
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/286cfcd4-b9f9-4825-8693-ef01b17cc195)
   Specify the token name, add the base you just created, add scopes as data:records:read, data:record:write and click create token
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/61168198-12e1-461d-9a82-f069b177d5f3)
   You have successfully generated a token and you can see it in the personal token list
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/5a048ad4-f173-4f71-a894-d9a21d1ba09b)
   Go through the web API documentations
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/c65e3a11-4174-4a08-996b-c4912fe6da40)

   Click on My first workspace
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/32e91a9b-ee1c-4b23-b800-4de3359925f1)
   Get the URL from the Authentication content
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/7f8cea08-72b3-4306-9f84-1044ee6ac460)
6. Now go to the lambda function and replace the URL with the URL copied earlier.
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/222a0ec3-ada1-413e-8551-c74b008f1750)

   Create the environment variable for the Airtable token/API in the Lambda function. Write the API as "Authorization":"Bearer p4323adfgAirtableAPI"(example).
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/6001bc8c-6754-41b7-9f15-b37a6ca24b43)

   Access the Airtable Token as such:
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/39b412b8-2c66-4eff-9c39-5bb38dba5393)



Now the Airtable is set up.

## Creating an Agent

1. Now we need to upload the OpenAPI spec in the S3 bucket.
   Search for S3 in the search bar.
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/24e1efa5-8ec8-4d60-90f4-297b07a05483)
   Click on the Create bucket option.
2. Give the name for the bucket.
   Give the Object Owner as ACL enabled, with Bucket owner preferred.
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/beb9b3fb-3efd-472e-942a-3fa1d4375443)
   Click on the Create Bucket option.
3. Now go back to the Bucket list page and click on the bucket that you just created
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/e2b416f1-2ff4-4609-b910-e18ba4108a27)
   Click the upload option to upload the Open API spec. Upload the lead_generation.json file here.
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/e34bddc0-0d68-4f5b-9383-7aa312a46c2f)
9. Now we create the agent.
    Search AWS bedrock and select the agents option.
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/14b4b9a0-f890-42a5-a417-ae1951346749)
10. Click on the create agents option
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/0372c905-a6c2-4a49-8656-e9747abeceed)
   Specify the Agent name and the description (Note: you can find the descriptions in the agents_description.txt file in this directory.)
   You can create the IAM permission automatically for new user, or use an existing IAM permission if available.
   Click Next.
11. Select model from the drop down and give the descriptions(agents_description.txt).We have selected Claude v2 since Claude v2.1 is still not available. Click Next
    ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/a1b08666-2d81-46fb-8bdf-dec85743893a)

12. Create an action group.
    ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/a41e28e5-a043-4032-8f29-6c8ddfc541f0)
    Give the action group name.
    Select the lambda function created earlier from the drop down menu.
    ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/060e9d83-fd35-4c97-af5a-d1345c1825cd)
    Select the file from the Browse option for S3. Click on the bucket then the Open API .json file inside it.
    ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/d7fdc6d0-8453-49bd-93f3-e46868d22b3d)
    ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/921d1a7f-b21d-4582-a39b-5c9b371d5b1c)
    Click on Choose then click on next.
13. Knowledge base is optional, it uses Open Search service of AWS and might charge for the uses, or you can just skip it.
14. Create Agent.
    ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/f62a5a55-2d6e-4c9e-8ccc-5750c8128a25)


Our Agent is now fully setup and can be used with functionalities such as creating data entries and generating solar potential through google apis.

Now you are ready to use the agents.

## Invoking agents present in AWS
Once an agent is created in the AWS Bedrock console, it can be accessed through python using the agent ID and agent alias ID.

Here is an example of an agent already created and existing in AWS Bedrock.

![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/82454e61-a011-4f65-ac40-4c4dfc6d12b5)
In this case lead_gen is the agent that is already created and existing in AWS Bedrock. We need its agentId and aliasId.
![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/c9e859b6-d352-407a-82ee-71806c9832ce)
![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/d9af29c1-43b7-4f97-ab67-c510db990570)
Now we can invoke this agent as such:

![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/3e724925-4e1c-4a2a-b2ed-c5d821a1db06) ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/a6230482-06d2-4ad3-a5c2-f01c3129f82b)

The response contains completion message as event byte chunks. (This is the message from the agents)

## Creating agents and Invoking them

Now, creating a new agent using python.

```python
aws_agent = bedrock_agent.create_agent(
    agentName='Lead_gen_notebook',
    description='Extract name, phone number and address for lead generation. Or extract address and monthly bill for calculating solar potential',
    foundationModel='anthropic.claude-v2',
    instruction="""You are a solar panel financial advisor, your job is to extract address and monthly bills for calling functions to calculate solar potential. You also are a solar panel lead generation employee, your job is to extract personal details like name, phone number and address for returning as response for calling functions to generate leads. Strictly respond to the question for calling the function that is required to answer.""",
    agentResourceRoleArn='arn:aws:iam::674564987265:role/service-role/AmazonBedrockExecutionRoleForAgents_KT4F6CHPJV'
)
```
This will create a new agent in our AWS bedrock as Lead_gen_notebook
![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/d7a56f08-ac91-4e47-8111-56076c876f54)

Then we give this agent an action group that stores our S3 bucket and Lambda Function informations
```python
#Creating the action group for the agent
response = bedrock_agent.create_agent_action_group(
    agentId=aws_agent['agent'].get('agentId'),
    agentVersion="DRAFT",
    actionGroupName='LeadGenAction',
    actionGroupExecutor={
        'lambda': 'arn:aws:lambda:us-east-1:674564987265:function:lead_gen_solar'
    },
    apiSchema={
        's3': {
            's3BucketName': 'legalgraphbucket',
            's3ObjectKey': 'lead_generation.json'
        }
    },
    actionGroupState='ENABLED'
)
```
![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/bd53fc94-161e-4e4d-a613-4e0bc5770029)

After this we give an alias to the agent while passing the agent id
```python
# Creating the alias
agent_alias = bedrock_agent.create_agent_alias(
    agentId=aws_agent['agent'].get('agentId'),
    agentAliasName='Dummy',
)
```
![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/3f8eba3c-0fc8-44e4-8f52-08115bb0e6f1)

Now the process of Agent creation with minimal configuration is done and ready to be invoked as done earlier.

# Testing the Agent

At the bottom right of the agent screen you will find a place to enter your message for the agent
![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/4e92e654-d8cf-4832-adf7-1e27b1b2acbb)

Example Question:
1. Calculate solar potential for 9813 Sherborne Ave, Bakersfield, CA 93311, USA with monthly bill as 300 USD
2. Create a Lead for Jhon Doe, California, 336-2126-7543

#### Solar Potential Calculation and Creating a lead.

![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/623b134e-9ee8-42d2-8c73-49032781bd46)

#### Entry in Airtable
![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/3e22dfe0-58b2-4766-becf-d233d2b6bc38)







   



   










