# Open the Jupyter Notebook in Google Colab

You can open this Jupyter notebook directly in Google Colab by clicking the link below:

[Open in Google Colab](<https://colab.research.google.com/github/initmahesh/MLAI-community-labs/blob/main/Class-Labs/Lab-2(Generating-Response-with-RAG)/RAG_GRADIO.ipynb>)

# Welcome to Lab 2

## In this Lab we will show you how to Generated/analyse contracts using GPT-3.5-turbo 16k context length and adding RAG to solve the issue that we face in Lab 0.1.

## What is Retrieval Augmented Generation or RAG?

As NVIDIA quotes it in the best and easiest way possible "Retrieval-augmented generation (RAG) is a technique for enhancing the accuracy and reliability of generative AI models with facts fetched from external sources."

It is needed for mapping the best embeddings there are in a knowledge base index, to the prompt that will be submnitted to the model. The model will use these embeddings along with its generative AI capability to respond to the query in the best possible way.

In the notebook [RAG_Responsible_AI.ipynb](WithRagGeneration.ipynb), we have curated the easiest implementation of RAG, using newer technologies like creating embeddings and using **faiss** for creating index of embeddings. Also we have implemented **sentence transformers** all of which you can see in action upon running the notebook.

### Pre-requisites (If you have already completed Lab-0 then ignore this)

1. OPEN_API_KEY (You can create OpenAI key using these Instruction: [Click Here](../../Lab2-solargen-with-function-calling/openaiAPI.md))
2. Google colab setup. Follow the Instructions here to set them up: [Click Here](<../Lab-0(Setting-up-Google-Colab)/README.md>)
3. You can find some contracts here: [Small Doc](AWS1.pdf), [Large Doc](https://github.com/initmahesh/MLAI-community-labs/blob/main/Lab-0/Lab-0.1/PROFRAC%20HOLDINGS%2C%20LLC%20credit%20agreement.pdf)

### **_ You can use GPT-3.5 key from OpenAI _**

You can create OpenAI key using these Instruction: [Click Here](../../Lab2-solargen-with-function-calling/openaiAPI.md)

## Set up

Click on this link to go to the Colab: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/15JwxQqnyIhgx1Upmgm_dwH759jxFEeXW?usp=sharing)

Paste the OpenAI key here in Cell 2

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/5eda36e8-3a8c-48ae-ad11-adfc592c94d9)

## Moving on to the coding bit.

Step 1:

Run cell 1 to install all the required packages to run the notebook.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/4cb32efd-603f-4d23-b2dc-79b64f0d86e5)

If you get this prompt, you can click on `Run Anyway`.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/25182fbf-8e5a-40b6-9c04-0c0261d6aa2c)

Step 2:

Run cell 2 to import all the required modules from the packages to be used in the notebook also this will load the keys and credentials in the environment.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/716b14d1-a4f1-449a-992c-2aa4258947ca)

Step 3:

Run cell 3 to load the sentence transformer model, read the description in the notebook as to why we are using all-MiniLM for sentence transformation.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/2098d762-2be6-4cc3-903d-8b5e93de6f65)

Step 4:

Run cell 4 to load the PDF, paste the path to the PDF here.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/7d173daa-af49-4330-a349-083296bcf168)

Step 5:

Run cell 5 to create chunks of the document and store them is a Knowledge base

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/16958980-8744-45e4-a72a-4177386ae63b)

Step 6:

Run cell 6, to use the knowledge_base to create the vector index

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/672d6f8f-1bca-4deb-a87c-c0cb969ef459)

Step 7:

Run cell 8 to load the `answer_question()` function in the memory, this function when called will retrieve relevant chunks on the basis of the question from the knowledge base.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/f98fc8b5-e5bb-461e-b6c2-b800b251a278)

Step 8:

Run cell 9 to load `return_RAG_passage()` function that is used for getting the most relevant chunks and converting them to proper formatted prompt following this pattern:

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

Step 9:

Running cell 10 will initialize the `CallOpenAI()` function for further usage/calling.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/5c7b5a59-b732-42da-a6c9-b71c16050fa7)

Step 10:

Running cell 11 will initialize the quesiton and call the `return_RAG_passage()` function and the relevant chunks are returned.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/84c796e3-0e24-46e1-ab17-7daaf644c13f)

Step 11:

Run cell 12 to combine the question with the RAG chunks that were created and will print the token count of the entire prompt.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/fcda4748-3207-4ca2-8e44-03bb775f57f4)

Step 12:

Run cell 13 to call the `CallOpenAI()` function to get the response from GPT.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/ca17a6da-3e24-420f-b333-01af875ac514)

Step 13:

Run cell 14 to print the response from the GPT.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/dbe126f9-018e-41c4-91f5-9592947f3583)

Step 14:

Now we will try to do the same thing with a larger document, preferably the one that we faced problems with in Lab 0.1 due to context length.

Run cell 15 to load the larger document, paste the path to your PDF here.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/ec7d05d5-71b3-498f-9614-d68392639f8b)

Step 15:

Run cell 16 to create chunks of the document and store them is a Knowledge base

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/16958980-8744-45e4-a72a-4177386ae63b)

Step 16:

Run cell 17 to use the knowledge_base to create the vector index

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/672d6f8f-1bca-4deb-a87c-c0cb969ef459)

Step 17:

Running cell 19 will initialize the quesiton and call the `return_RAG_passage()` function and the relevant chunks are returned.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/a35eead8-ebb0-48b7-af7d-4c9b9d2e7c24)

Step 18:

Run cell 20 to combine the question with the RAG chunks that were created and will print the token count of the entire prompt.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/b48e1cc7-9a18-41e9-a2b1-7faeac710e21)

Step 19:

Run cell 21 to call the `CallOpenAI()` function to get the response from GPT.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/f77a60ea-cf60-44c0-8758-53301aee50e6)

Step 18:

Run cell 18 to print the response.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/ad67c57c-7747-41d3-bad7-8ab67784982a)

## So here we see that using RAG we were even able to process very large document and get the accurate answer without facing the problem of context length.
