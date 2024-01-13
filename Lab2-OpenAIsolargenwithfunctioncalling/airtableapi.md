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
6. Now save the key and the URL in the .env file 

   
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/5abb8d64-af27-486c-8a75-03ade49489f8)


   Keep the Airtable token/API in your .env, write the API as "Authorization":"Bearer p4323adfgAirtableAPI"(example).
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/6001bc8c-6754-41b7-9f15-b37a6ca24b43)
