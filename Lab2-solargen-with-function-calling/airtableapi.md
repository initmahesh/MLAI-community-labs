## Instructions on Setting up your Airtable Keys and base

1. Visit Airtable(Create an account if you do not have one)
   https://airtable.com/
2. Click on start from scratch
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/54f4a448-a8d7-446c-bb34-5182d97d53ae)

3. Add the column names to the table:
   * If you are here from `Lab 0` then Add the key terms that you are planning to generate from ChatGPT Agents
      * Click on the `+` symbol
     ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/09bb6efb-5a85-4b9c-9352-c7d03ecc9f65)
      * Write you key term name and Hit Enter
        ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/97d5a4e9-55b9-4064-8338-d6add9af16af)
      * You can see the column has been created
        ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/748368b4-ebf2-4a1e-9028-205ac553a255)

      #### Similarly create all the Key term column names. 

   * Else if you are not from Lab 0 follow the step below:
   Change/Add the column names. (Column names are case-sensitive)
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/e4c09999-3851-4d6f-825a-b77100bc3afe)

5. Go to the account section.

   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/d27d85b6-0142-4929-888e-c1d07ed4dff4)
6. On this screen you will find the Go to Developer Hub button, Click it.
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/ad40af4a-a27d-47b8-ba5d-14a532264eee)
7. Click on Personal Access tokens
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/b8bd759e-3850-4a58-aa00-96d45bdfa903)
8. Click on create new token
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/286cfcd4-b9f9-4825-8693-ef01b17cc195)
9. Specify the token name, add the base(Here base is the table you created) you just created, add scopes as

   `data:records:read`

   `data:record:write` and click create token
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/61168198-12e1-461d-9a82-f069b177d5f3)

10. You will be displayed the API key only once, so copy it somewhere safe.
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/214af80f-5907-414c-8c1d-702cd9c7b6f8)

11. You have successfully generated a token and you can see it in the personal token list
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/5a048ad4-f173-4f71-a894-d9a21d1ba09b)
12. Click on the Developer Doc option
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/f2502d32-59c1-4b61-802e-7373117590b2)
13. Click on the API docs button in the Web API section
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/d9de5765-ebef-4053-920a-c1c6128a5b39)
14. You will be landed on this page
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/1d1b4a3c-4b22-420b-b5ba-a54a11a53dc4)

15. Click on the table name that you created in the `My First Workspace` section

   
   Scroll down and you will find the `Authentication` section in the documentation
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/80465269-a1a7-4abc-9629-c62a6c13c32e)

17. Here you will find the URL, copy it and save it some where safe.


**** If you are here from `Lab 0`, then you need to break this URL into two parts for creating the OpenAPI schema.(ignore this if you are here from any other Lab) ****

   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/66d6a5d7-90f4-4305-9c85-920817fb4351)

   So save your path and server from the URL somewher, we will use this later in the lab
   
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/170d8343-d85c-42ac-a289-d6661bd4c5eb)


18. (Ignore this if you are from `Lab-0`) Now save the key and the URL in the .env file

   
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/5abb8d64-af27-486c-8a75-03ade49489f8)


   Keep the Airtable token/API in your .env, write the API as "Authorization":"Bearer p4323adfgAirtableAPI"(example).
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/6001bc8c-6754-41b7-9f15-b37a6ca24b43)
