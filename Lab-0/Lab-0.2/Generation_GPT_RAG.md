![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/f1431206-b5aa-4121-9ad9-9a754dc9c40a)# Welcome to Lab 0.2
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

Step 6:

Run cell 6, to load `create_document_embedding()` function that generated chunks of the entire document and uses them to call the `create_embedding_index()` function that creates a faiss index and returns this embed index.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/acc7ff45-46e2-4c88-98de-03325aa67df4)

Step 7:

Run cell 7 to load `return_RAG_passage()` function that is used for  getting the most relevant chunks and converting them to proper formatted prompt following this pattern:
```
<Context1>
Chunk 1
</Context1>
<Context2>
Chunk 2
</Context2>
<Context3>
Chunk 3
</Context3>
.
.
.
<ContextN>
Chunk N
</ContextN>
<Question>The question that is being asked about the document</Question>
```
![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/fbb87e3c-3194-41dc-b45c-7c863ec03f6a)

Step 8:

Running cell 8 will initialize the `CallOpenAI()` function for further usage/calling.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/5c7b5a59-b732-42da-a6c9-b71c16050fa7)

Step 9:

Run cell 9 to create embedding index of the document. Change the document path 

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/24738cf4-1a82-495d-8cea-e9438c46d10d)

Step 10:

Run cell 10 to call the `return_RAG_passage()` which returns the chunks that is relevant to the question in a proper format. You can also change the question if you want to try any other question.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/5f6d070a-90c8-497b-b10d-b32e91cb84d1)

Step 11:

Run cell 11 to combine the question with the RAG chunks that were created and will print the token count of the entire prompt.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/fcda4748-3207-4ca2-8e44-03bb775f57f4)

Step 12:

Run cell 12 to call the `CallOpenAI()` function to get the response from GPT.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/ca17a6da-3e24-420f-b333-01af875ac514)

Step 13:

Run cell 13 to print the response from the GPT.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/dbe126f9-018e-41c4-91f5-9592947f3583)

Step 14:

Now we will try to do the same thing with a larger document, preferably the one that we faced problems with in Lab 0.1 due to context length.

Run cell 14 to create the embeddings of the document. Change the document path here.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/34de34a3-4237-4bc3-8cab-f44eca0b9403)

Step 15:

Run cell 15 to call the `return_RAG_passage()` which returns the chunks that is relevant to the question in a proper format. You can also change the question if you want to try any other question.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/ce08f5aa-d8b9-46f9-a322-daa563635911)

Step 16:

Run cell 16 to combine the question with the RAG chunks that were created and will print the token count of the entire prompt. As you can see the token count has come down to a staggering 8347 which was 163227 before.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/daa72ef3-47f2-4d7c-b453-80b67915d7f2)

Step 17:

Run cell 17 to call the `CallOpenAI()` function to get the response from GPT.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/f77a60ea-cf60-44c0-8758-53301aee50e6)

Step 18:

Run cell 18 to print the response.


## So here we see that using RAG we were even able to process very large document and get the accurate answer without facing the problem of context length.
