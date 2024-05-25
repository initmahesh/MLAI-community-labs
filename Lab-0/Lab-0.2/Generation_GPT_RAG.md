# Welcome to Lab 0.2
## In this Lab we will show you how to Generated/analyse contracts using GPT-3.5-turbo 16k context length and adding RAG to solve the issue that we face in Lab 0.1.

## What is Retrieval Augmented Generation or RAG?

As NVIDIA quotes it in the best and easiest way possible "Retrieval-augmented generation (RAG) is a technique for enhancing the accuracy and reliability of generative AI models with facts fetched from external sources."

It is needed for mapping the best embeddings there are in a knowledge base index, to the prompt that will be submnitted to the model. The model will use these embeddings along with its generative AI capability to respond to the query in the best possible way.

In the notebook [RAG_Responsible_AI.ipynb](WithRagGeneration.ipynb), we have curated the easiest implementation of RAG, using newer technologies like creating embeddings and using **faiss** for creating index of embeddings. Also we have implemented **sentence transformers** all of which you can see in action upon running the notebook.

### Pre-requisites

1. AZURE_OPENAI_ENDPOINT
2. AZURE_OPENAI_API_KEY
3. AZURE_OPENAI_ENDPOINT
4. AZURE_OPEN_AI_MODEL
5. OPENAI_API_TYPE
6. Python version 3.9+ (https://www.python.org/downloads/)
7. VS code(Optional if you are using Google Colab) (https://code.visualstudio.com/download)

### *** You can either use GPT-3.5 key from OpenAI, or deploy an instance in Azure like us and use it endpoints. ***

You can use this video as reference for setting up Azure OpenAI: [Click Here](https://youtu.be/XqoqgIZS2rc?t=245)

**OR**

You can create OpenAI key using these Instruction: [Click Here](../../Lab2-solargen-with-function-calling/openaiAPI.md)

## Set up

Click on this link to go to the Jupyter Notebook: [Notebook](Without_RAG_Generation.ipynb)

#### If you are using GPT from OpenAI:

You can create OpenAI key using these Instruction: [Click Here](../../Lab2-solargen-with-function-calling/openaiAPI.md)
1. Comment out these Lines:
   * Code Cell 2:
     
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/8fbaf5e3-4a60-4a2e-84da-d6ed249d1929)
2. Uncomment out these Lines:
   * Code Cell 2:
     
     ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/01b9a8e0-9808-4903-8890-35d59d3d898b)

   * Place the OpenAI key as ```os.environ["OPENAI_API_KEY"] = <Key>```
     
     ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/5eda36e8-3a8c-48ae-ad11-adfc592c94d9)

## Moving on to the coding bit.

Step 1:

Run cell 1 to install all the required packages to run the notebook.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/4cb32efd-603f-4d23-b2dc-79b64f0d86e5)

Step 2:

Run cell 2 to import all the required modules from the packages to be used in the notebook also this will load the keys and credentials in the environment.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/7a21a4d6-9382-47e5-87f3-71abe6822a96)

Step 3:

Run cell 3 to load the sentence transformer model, read the description in the notebook as to why we are using all-MiniLM for sentence transformation.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/2098d762-2be6-4cc3-903d-8b5e93de6f65)

Step 4:

Run cell 4 to load `create_embedding_index()` function that takes the chunks generated using the Recursive Character Splitter and converts them to Faiss index.

Step 5:

Run cell 5 to load `answer_question()` function that takes the question from the user and returns the 10 most relevant chunks from the document.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/b079085c-6f2e-4238-8e89-e7cb47957105)

Step 5:

