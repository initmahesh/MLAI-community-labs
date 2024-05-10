# Vetex AI Agents

In this readme we will show you how you can build you own agent and use it for generating answers regarding your queries, while customizing it to answer questions only related to particular questions. Integrating external knowledge sources, writing OpenAPI spec for these sources.

**PS**: Integration of these agents using Python SDK in a notebook will be coming soon. Hang tight!! :)

## So why do we need Agents?

Agents are like your customized personal assistants.
* They will learn whatever you train them to become.
* They can refer to external knowledge sources and API.
* They have information about external world knowledge.
* They can answer questions in a proper format that you provide.
* Integrate them to your existing system and use it for generating responses.

## Prerequisites

* Create a service accout and project in google cloud console.

  Service account:[Link Here tutorial](https://cloud.google.com/iam/docs/service-accounts-create#console)
  
  Project account:[Link Here tutorial](https://cloud.google.com/resource-manager/docs/creating-managing-projects)
* API for integrating with the Agent
  
  For example: Here we are using Google Places API for finding different places and their information.

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

## Configuration of the Agent

