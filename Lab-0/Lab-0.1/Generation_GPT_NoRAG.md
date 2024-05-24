# Welcome to Lab 0.1
## In this Lab we will show you how to Generated/analyse contracts using GPT-3.5-turbo 16k context length.
### We will also stumble across an error which might seem like the end of the world but we will fix it using a, awesome technique called RAG, so hang tight.

### Pre-requisites

1. AZURE_OPENAI_ENDPOINT
2. AZURE_OPENAI_API_KEY
3. AZURE_OPENAI_ENDPOINT
4. AZURE_OPEN_AI_MODEL
5. OPENAI_API_TYPE
6. Python version 3.9+ (https://www.python.org/downloads/)
7. VS code(Optional if you are using Google Colab) (https://code.visualstudio.com/download)

### *** You can either use GPT-3.5 key from OpenAI, or deploy an instance in Azure like us and use it endpoints. ***

### Set up

Click on this link to go to the Jupyter Notebook: [Notebook](Without_RAG_Generation.ipynb)

If you are using GPT from OpenAI:
1. Comment out these Lines:
   * Code Cell 2:
     
   ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/8fbaf5e3-4a60-4a2e-84da-d6ed249d1929)
2. Uncomment out these Lines:
   * Code Cell 2:
     
     ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/01b9a8e0-9808-4903-8890-35d59d3d898b)

   * Place the OpenAI key as ```os.environ["OPENAI_API_KEY"] = <Key>```
     
     ![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/5eda36e8-3a8c-48ae-ad11-adfc592c94d9)

