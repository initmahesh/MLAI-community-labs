## Instructions on Setting up your Airtable Keys and base

1. Visit Airtable(Create an account if you do not have one)
   https://airtable.com/
2. Click on start from scratch
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/54f4a448-a8d7-446c-bb34-5182d97d53ae)

3. Add the column names to the table:
   * If you are here from `Lab 4` then use the following column names.
      * ```
        [
           Name,
           PhoneNumber,
           CurrentAddress
        ]
        ```
      * Also set the type for each column as Single Line Text.
   * Else If you are here from `Lab 0` then Add the key terms that you are planning to generate from ChatGPT Agents
      * Click on the `+` symbol
     ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/09bb6efb-5a85-4b9c-9352-c7d03ecc9f65)
      * Write your key term name and Hit Enter (**** Names should not have spave between them and should be same like the one's mentioned in the OpenAPI schema payload ****)
    
        **OR**
    
        Just insert these names in the column
        ```
        [
         ContractName
         ServiceProviderName
         CustomerName
         Contractstartdate
         Contractenddate
        ]
        ```

        ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/121d07f0-c3d2-45d5-ae76-9d35d5b0c720)

      * You can see the column has been created
        ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/4a529e41-6d31-4f0a-81f5-0c17d0008366)


      #### Similarly create all the Key term column names. 

   * Else if you are not from `Lab 0` or `Lab 4` follow the step below:
   Change/Add the column names. (Column names are case-sensitive)
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/e4c09999-3851-4d6f-825a-b77100bc3afe)
5. There are two ways you can set the Column Type in Airtable
   * Set the column type while adding the column name
     ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/773659eb-6275-4a7f-80cf-518a88f6a124)
     * After inserting the column name in the input text field, select the Field Types as Single Line Text
     ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/8108947b-3406-4549-bfb3-a91a260d7769)
     * After doing this, click on the Create field.
     ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/d0c1acb2-9de3-4e27-86bd-a64df921b3c3)
   * Edit the Column Type of column that is already created.
     
      * Click on the drop down button.
        
        ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/ac3ba1ae-1b38-4eff-b879-c9a74a2b2e57)
        
      * Click on the Edit field option in the drop down
        
        ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/e8320741-7a9d-485e-b225-d07d349a762e)
        
      * Click on the Field Type dropdown
        
        ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/9c173b9d-cd40-4772-b401-ce6eb48204be)
        
      * Select Single Line Text from the drop down
        
        ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/ae526de7-c954-4ea6-b81e-d13557cf9b30)
        
      * Click on the save button
        
        ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/cf59c4c8-40fa-4bb0-8a0d-c31870d03f14)


   


6. Go to the account section.

   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/d27d85b6-0142-4929-888e-c1d07ed4dff4)
7. On this screen you will find the Go to Developer Hub button, Click it.
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/ad40af4a-a27d-47b8-ba5d-14a532264eee)
8. Click on Personal Access tokens
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/b8bd759e-3850-4a58-aa00-96d45bdfa903)
9. Click on create new token
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/286cfcd4-b9f9-4825-8693-ef01b17cc195)
10. Specify the token name, add the base(Here base is the table you created) you just created, add scopes as

   `data:records:read`

   `data:record:write` and click create token
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/61168198-12e1-461d-9a82-f069b177d5f3)

11. You will be displayed the API key only once, so copy it somewhere safe.
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/214af80f-5907-414c-8c1d-702cd9c7b6f8)

12. You have successfully generated a token and you can see it in the personal token list
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/5a048ad4-f173-4f71-a894-d9a21d1ba09b)
13. Click on the Developer Doc option
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/f2502d32-59c1-4b61-802e-7373117590b2)
14. Click on the API docs button in the Web API section
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/d9de5765-ebef-4053-920a-c1c6128a5b39)
15. You will be landed on this page
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/1d1b4a3c-4b22-420b-b5ba-a54a11a53dc4)

16. Click on the table name that you created in the `My First Workspace` section

   
   Scroll down and you will find the `Authentication` section in the documentation
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/80465269-a1a7-4abc-9629-c62a6c13c32e)

17. Here you will find the URL, copy it and save it some where safe.


**** If you are here from `Lab 0` or `Lab 4`, then you need to break this URL into two parts for creating the OpenAPI schema.(ignore this if you are here from any other Lab) ****

   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/66d6a5d7-90f4-4305-9c85-920817fb4351)

   So save your path and server from the URL somewher, we will use this later in the lab
   
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/170d8343-d85c-42ac-a289-d6661bd4c5eb)


18. (Ignore this if you are from `Lab-0`) Now save the key and the URL in the .env file

   
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/5abb8d64-af27-486c-8a75-03ade49489f8)


   Keep the Airtable token/API in your .env, write the API as "Authorization":"Bearer p4323adfgAirtableAPI"(example).
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/6001bc8c-6754-41b7-9f15-b37a6ca24b43)
