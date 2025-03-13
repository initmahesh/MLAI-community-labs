# Vertex AI Agents

In this readme we will show you how you can build you own agent and use it for generating answers regarding your queries, while customizing it to answer questions only related to particular questions. Integrating external knowledge sources, writing OpenAPI spec for these sources.

**PS**: Integration of these agents using Python SDK in a notebook will be coming soon. Hang tight!! :)

## So why do we need Agents?

Agents are like your customized personal assistants.
* They will learn whatever you train them to become.
* They can refer to external knowledge sources and API.
* They have information about external world knowledge.
* They can answer questions in a proper format that you provide.
* Integrate them to your existing system and use it for generating responses.

Also Here we will be using Multi Agent Configuration:

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/e4c870de-922d-4b11-b7ee-af371310388c)

Here One Main Agent `Car Repair Agent` will call `CRM Agent` that will use the Airtable tool to save data in the table. Also the Car Repair Agent will be interactive Car mechanic that can use the Places API to get nearest Garage information.


## Prerequisites

* Create a service accout and project in google cloud console.

  Service account:[Link Here tutorial](https://cloud.google.com/iam/docs/service-accounts-create#console)
  
  Project account:[Link Here tutorial](https://cloud.google.com/resource-manager/docs/creating-managing-projects)
* API for integrating with the Agent
  
  For example: Here we are using Google Places API for finding different places and their information.

  To get your own Google Places API follow the instruction given below:

  1. Go to Google Console platform.
     
     ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/4c97b699-aa5d-4e94-8af4-27a300e5d796)
  2. Click on the button shown below in the image.
 
     ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/ed8ffc44-6b32-4d8d-9b97-5bca9a92eb71)
     
  3.  Click on the API & Services show below.
 
     ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/307b0430-cfd0-487d-a16d-cf3af2f6e566)

  4. Click on the Enable APIS and Services
     
     ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/6e98b9af-a227-4fd0-a208-1681de0f4031)

  5. Search for the Places API
     
     ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/c5b82ffc-8554-4495-830d-09fed32883c5)
     
  6. You need to enable both of these APIs.

     ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/afff0b09-dba3-44c0-bead-d1ffb401e3e6)
     
  7. Click on API and enable it and you will see something like this. CLick on the manage button
 
     ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/a5008144-b462-470b-a54b-ba88cf01a849)
     
  8. You will land on this page.
     
     ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/ac3b2288-509c-4787-9f77-e181cec78444)

     Click on the Keys & Credentials

     ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/8c139e9f-1c27-445f-a1df-c31377917b3e)
  9. You will be landed on this page.
 
      ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/5ca369e9-ff89-487a-a876-27b19266b3a9)

     Click on the show key button

     ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/1668feac-1494-42e8-a0a4-20eb7e4a39a9)

  10. Copy the key somewhere safe for using it later.

      ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/4ba5f2ff-b33f-4cc5-a250-12b4a1529bd7)

* ### Any Airtable related query please refer to the instructions provide in the following file:

    [Click here](../../Lab2-solargen-with-function-calling/airtableapi.md)
    
    
    After creating an airtable account and setting up the API key, and adding key terms you should see something like this:
    ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/54a73384-eb81-4e4e-9cdd-29cbd496709e)


## Starting the creation of the Agent
1. Go to Google console platform and search for **Agents Builder** in the search tab.
   [Google Console Platform](https://console.cloud.google.com/)
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/889200ff-9afc-43d8-9247-c36b0d510ed2)

2. Click on the Agent builder and you will be redirected to this page.
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/e72fca2a-8438-42ee-a448-d53d0233f4e9)
   This is where you will be able to see your Agent builder app that you will be creating.
3. Click on the Create App option

   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/1cf97488-d862-46fd-968c-c0f8c1badaff)

   You will be shown this page, and you should select the **Agent** as app type
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/4cd3cdf0-1a36-4d72-84a3-f8585a4c25d1)

4. Mention the name of the app that you want to create and the region (best: leave it to us-central1)
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/17810ac6-224a-4e54-a5f1-161f8ba10668)
   Click on Create

5. This is the main page where you will land.
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/b6cac8a5-69bf-498e-8b23-7f852ed1dc41)

Now we have created our App and we will move on to customizing it.

## Configuration of the First Agent

1. First set the Name of the Agent, here this Agent will be responsible for Inserting data to Airtable CRM, so we name the agent as `CRM_Agent`
   
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/5557733b-c688-4853-b8d4-225b6cfcf9ac)

2. Then we set the description of the Agent as
   
   `You are a database engineer and you need to make entries to a CRM table.`

   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/42f138fc-bb4e-49b2-a5dc-7d032573b8dd)

3. Then click on the `+ Data Store` option to add the Airtable tool for the Agent to use.

   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/ca92ad23-0639-4832-83be-9df1990bc351)

4. You will be landed on this page, where we will Configure out tool.

   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/92db4794-2651-43e3-a121-a74b4d06aa1c)

5. Set the Name of the tool as `Airtable CRM`

   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/c862c6a3-c739-4904-8e45-a00389175a78)

6. Select `Open API` from the dropdown menu in the `Type` field

   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/6f13e7fc-8eb8-45ff-a23e-08922922a85f)

7. Set the description of the tool as

   `This tool is used to call the Airtable CRM to save the information.`
   
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/2d5cb5fd-a1fd-4c94-9adf-df19ddefa994)

8. Then we will setup the `Schema`, Select `YAML` as the type

   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/be87aeef-334a-4bf3-b56e-15ccb2ba4a10)

9. Copy paste the schema given below and replace the path of the Airtable with you own.

   ```yaml
    openapi: 3.0.1
    info:
      title: Airtable CRM insert data API
      description: Inserts the customer information in the Airtable CRM using the API
      version: "1.0.0"
    
    servers:
      - url: https://api.airtable.com/v0 # Base URL for the API
    
    # Paths for the API endpoints
    paths:
      /appdp97LZaCHF7uuy/Table%201:
        post:
        #   parameters:
        #       - in: query
        #         name: fields
        #         schema:
        #           type: string
        #           default: "places.name,places.formatted_address,places.price_level"
          summary: Insert customer information in the table
          operationId: customerInformation
          requestBody:
            required: true
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    records:
                      type: array
                      items:
                        type: object
                        properties:
                          fields:
                            type: object
                            properties:
                            # type: object
                            # properties:
                              Name:
                                type: string
                                description: Name of the customer.
                              PhoneNumber:
                                type: number
                                description: Phone Number of the customer.
                              CurrentAddress:
                                type: string
                                description: Current address of the customer.
                              
                        
          responses:
            '200':
              description: Successful response
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                        result:
                          type: string
                          description: The response from the API after sending POST request.
                    
                    # $ref: "#/components/schemas/placeResponse"
                
   ```
    
    ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/11aa0ea6-dd56-43e5-bfb6-071bc8de68b4)

10. Select the `Bearer Token` option in the `Authentication type` and paste your Airtable Token in the field like shown below.

    ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/6dc34935-2fca-465a-8583-9f8ea33a7b74)
    
11. Now Click on `Save`

    ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/409589b5-4a57-4c13-82f8-2d897de99d61)
    
13. Now we need to go back to the CRM Agent again, so click on the Agents option in the side bar.
    
    ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/8ba5ebe0-70f3-4566-a7d7-32bebf72f675)

14. Click on the `CRM_Agent`.

    ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/a2947fed-b032-4461-a10b-0f0fd6b6b1ba)
    
16. This Agent will save the Name, Phone number and the Current Address of a Customer to the CRM, thus we set the instruction of the Agent.

   ```
     - Take the Name, Phone Number, Current Address and use ${TOOL:Airtable CRM} to save them in the CRM
     - Format the Phone Number as String before calling the tool.
   ```
    
  ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/74aea9bc-0e0c-4ed5-954c-cef1d1b0ea2a)


17. In the Available tools section you will see the tool that you just created for Airtable. Click on it.

    ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/7db6d767-0531-4dd9-a68e-61e7b91565d2)

18. Click on `Save`

    ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/47a0795d-4902-4e7b-9da7-f8629deef34f)


Now, your first agent is ready. Lets Configure our second agent.
   

## Configuration of the Second Agent

1. Click on the back button shown below

   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/fe67b72c-530f-42df-a944-6acbfbcde004)

2. Click on `Create` button

   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/2188df35-94e3-4d28-af08-f1134b26aace)

3. Set the name of the Agent as `Car Repair Agent`

   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/a93c8fe9-6975-4c1e-8f4f-18506191274b)

1. Then we will set the Goal of the Agent

   In our case we are building a car repair agent who is helpful in answering questions related to the car problems. So we set the Goal as per the requirement as such.
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/87c68c43-a5a9-434c-9f54-354171c40753)

   Click the save button.

   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/b62cac3a-bfcf-4180-9ba6-c16f8fa062fe)

2. Next step we will create a Tool for the agent to use.

   Head over to the Tools section and click on it
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/c0f1d2c1-6d20-4db4-a940-6d60b9ff8fca)

   Click on the create button. This is what you will be shown

   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/05c4c377-f7a8-407d-84a1-b22bdde4052f)
   * Select the type of the tool as OpenAPI

     ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/670010a6-13a1-4ff1-91e5-26a2074f2f62)

   * Also set the description of the Tools. As we are integrating the Places API from Google we will set the description as that.

     ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/af74736d-1cec-43d7-9037-b42657dac564)

   * Now we will create an OpenAPI schema that we need to provide the tool for making API calls and getting the request. This will help the agent to know when it needs to call the API on its own, without having to explicitly mention it.
  
     **Open API schema**

     In our case we write the Open API schema in YAML format, but if you are already well versed in writing schema you can choose JSONL format too and try to create you own, else feel free to follow along.

   * *   ```YAML
          openapi: 3.0.1
          info:
            title: Google Places Text Search API
            description: Search for places by text query.
            version: "1.0.0"
         ```
         In this sction we are mentioning the version of Open API schema that we will be using. We are going with the latest version currently.

         The **info** section mentions the title of the OpenAPI schema, the description of what this schema does and version of our schema.

    * * ```YAML
        servers:
            - url: https://places.googleapis.com/v1  # Base URL for the API
        ```
        Here, we are setting the base URL of the API, that the Agent is supposed to call.
    * * ```YAML
        paths:
          /places:searchText?fields=places.displayName,places.formatted_address,places.price_level:
            post:
        ```
        Here we are mentioning the path on which a Post request will be sent.

        (Notice how we have specified a query parameter in the path itself as (fields=places.displayName,places.formatted_address,places.price_level)? This is done because the Tools in Agent builder does not provide more than one field for mentioning the query parameter which is already taken up by the API key. Same goes for Request Headers.)
    * * ```YAML
        summary: Search for places by text query.
        operationId: searchPlaces
        requestBody:
          required: true
          content:
            application/json:
              schema:
                type: object
                properties:
                  textQuery:
                    type: string
                    description: Text query to search for places.
        ```
        The POST request sent should have a request body. So, here we are describing the requestBody and the contents of the requestBody. Also, the summary describes the POST request.

        The content section describes the type of the payload, and the properties describes the variables and they type with descriptions.
    * * ```YAML
        responses:
          '200':
            description: Successful response
            content:
              application/json:
                schema:
                  $ref: "#/components/schemas/placeResponse"
        ```

        This section mentions the responses, and their description and the content should be taken from the Path "#/components/schemas/placeResponse" which will be mentioned below.
    * * ```YAML
        components:
          schemas:
            placesNames:
              type: object
              properties:
                name:
                  type: string
                  description: Name of the place.
                formattedAddress:
                  type: string
                  description: Formatted address of the place.
                priceLevel:
                  type: string
                  description: Price level of the place (e.g., PRICE_LEVEL_EXPENSIVE).
            placeResponse:
              type: object
              properties:
                places:
                  type: array
                  items:
                    $ref: "#/components/schemas/placesNames"
        ```
        This section mentions the components that we are referencing in the point above as "#/components/schemas/placeResponse". So, lets understand the flow:

        Path: "#/components/schemas/placeResponse"

        References the PlaceResponse schema from the components section which in turn references "#/components/schemas/placesNames", this will call the placesNames schema that in turn mentions the contents and the description of each property.
        Properties:
        * * * name: The name of the place and type as string
            * formattedAddress: The formatted address of the place.
            * priceLevel: The pricing level of the place from high to low.
## The Full Open AI Schema
```YAML
openapi: 3.0.1
info:
  title: Google Places Text Search API
  description: Search for places by text query.
  version: "1.0.0"

servers:
  - url: https://places.googleapis.com/v1  # Base URL for the API

# Paths for the API endpoints
paths:
  /places:searchText?fields=places.displayName,places.formatted_address,places.price_level:
    post:
    #   parameters:
    #       - in: query
    #         name: fields
    #         schema:
    #           type: string
    #           default: "places.name,places.formatted_address,places.price_level"
      summary: Search for places by text query.
      operationId: searchPlaces
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                textQuery:
                  type: string
                  description: Text query to search for places.
                    
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/placeResponse"
                
components:
  schemas:
    placesNames:
      type: object
      properties:
        name:
          type: string
          description: Name of the place.
        formattedAddress:
          type: string
          description: Formatted address of the place.
        priceLevel:
          type: string
          description: Price level of the place (e.g., PRICE_LEVEL_EXPENSIVE).
    placeResponse:
      type: object
      properties:
        places:
          type: array
          items:
            $ref: "#/components/schemas/placesNames"
```

## Set the Authentication
![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/030414af-cbac-493a-8cf4-aca59d33ed31)

* Select the Authentication type as API key
* Set the API key location as Query string parameter

  Specify the name as the one required by the API. In our case the name is simply "key". Also enter the API key secret in the field the one which you got by enabling the Places API in google console while doing the pre-requisite section.

## Continuing on our Agents creation.
* Select the tool that you just created in the available tools
  ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/d3ef8ad9-2abe-4f3f-84e1-c7b5010d578b)

* The last step is to create the Instructions.

  In the Instructions set, you will need to mention the tool that you created along with the situation when the agent needs to call the tool and also the Agent name.
  ```
  ${TOOL: tool name}
  &{AGENT: Agent name}
  ```
  Full Instructions-

  ```
  - Greet the users.
  - Answer car related questions and car repair questions to the best of your ability.Any question or sentences not related to cars or car repair should not be answered and is out of your knowledge.
  - You can also use ${TOOL:Places} to help you answer questions.
  - Display the listing in a bullet proof, markdown format. You should not show more than 5 output response.
      - After displaying the results using the tool, Always ask the user "Do you want us to connect you to them?"
          - If they say "yes", ask them for their Name, Phone Number, Current address.
              - If the Name, Phone Number, Current address is provided by them, route them to ${AGENT:CRM_Agent}. Save the Name, Phone Number, Current address in the CRM
          - After storing the data successfully output response "Someone from the Company will get back to you.
  ```

  ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/f0612f38-1e56-4b86-8dc2-fea87b4f1c25)

### Quick Note:

We mention the Agent to `use` a Tool whereas we mention it to `route to` another Agent while setting the instructions, else the Agent will hallucinate and not give proper results.

## Last one Thing before testing the Agent we need to increase the context length of Gemini:

1. Click on the settings in the side bar.

   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/0d027706-2208-4ab4-8343-6be1c9449be3)

2. Click on the `GenAI` Nav bar.

   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/ce229ce5-05d4-4779-a53e-70deef44b7c5)

3. Select Upto 32k in the input token limit

   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/ce2bf4e9-221c-4683-bc83-c08289810169)

4. Select Output token limit as upto 2048

   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/d005b24d-344f-4ca7-900b-695b7136118c)

5. Click on the save button.

   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/14f40211-be27-4cf5-b012-df08a9bd4f8a)

  
## Output
You can test out your agent by talkin to it in the Preview agent tab.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/ae83ffc0-e8af-4acf-aa13-b0b628ed8955)

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/e65f11fe-2147-4641-8941-9d59bdb4ff4f)

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/fd04b17e-0f0d-4a5a-a25d-9a9670a42891)

Also we can see the data has been stored in the Airtable CRM:

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/2ed7c136-7c9a-4318-94ae-bd8cb9fdc7b4)


