# Open the Jupyter Notebook in Google Colab

You can open this Jupyter notebook directly in Google Colab by clicking the link below:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/initmahesh/MLAI-community-labs/blob/main/Class-Labs/Module-2(Understanding-Agentic-RAG)/Lab-2.1(Generating-Response-without-RAG)/WithoutRAGGeneration.ipynb)





# Welcome to Lab 1

#### In this Lab we will show you how to Generated/analyse contracts using GPT-3.5-turbo 16k context length.

### We will also stumble across an error which might seem like the end of the world but we will fix it using an awesome technique called RAG, so hang tight.

### Pre-requisites (If you have already completed Lab-0 then ignore this)

1. OPEN_API_KEY (You can create OpenAI key using these Instruction: [Click Here](https://medium.com/@lorenzozar/how-to-get-your-own-openai-api-key-f4d44e60c327))
2. Google colab setup. Follow the Instructions here to set them up: [Click Here](https://medium.com/@aditya_dev30/getting-started-with-google-colab-your-ultimate-setup-guide-for-generative-ai-projects-53fe25f3fc04)
3. You can find some contracts here: [Small Doc](AWS1.pdf),
   [Large Doc](credit_agreement.pdf)



## First Let Us learn the basics of Prompt Engineering (Essential for using GPT)

You can say that Prompts are the languages of LLM models, the better you speak it the more the LLM understands and replies. Prompt engineering consists of templates and much more to explain the question better to the LLM models. Below you can see an example of how the LLM model expects its prompts to be configured.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/617ec5c3-731d-47cd-8131-15e7a7d68f18)

This just show the high level view of how prompts look like.

The template of prompts consists of lots of tags and line break, also adding more instructions after every iteration/test of get the desired results. if we were to convert the above prompt in a format that we would, provide it while programming, then it would look somewhat like this.

```
system:You are a  brilliant professor of commerce and you are can answer questions true to your Knowledge. Explain it in detailed format. If you do not know the answer just say "I do not know" rather than making something up.
User:
<Context>
Those assets that a company can quickly convert into cash within a short timeframe are called liquid assets. These can be commodities for sale or inventory, money in the bank, accounts receivable and other items that you may exchange for cash within a year. Liquid assets are also referred to as current assets on the balance sheets. It is important for a company to have a certain amount of liquid assets as it helps with day-to-day operating costs.
</Context>
<Question>What are liqued assets?</Question>
<Answer>Put your answer here</Answer>
```

As you can see how different this became than earlier in the picture. This is because we tried to state the entire content in a crystal clear format.

Also you may have noticed how we have used tags in our prompts. Tags are an essential part of Prompting, that helps the LLM model understand the different parts of the problem.

- <Context> tag tells the model where the context starts and ends
- <Question> tag tells the model which is the question.
- <Answer> tag tells the model where to insert the answer.

Tags help in avoiding confusion for the LLM model.

## Set up

Click on this link to go to the Colab: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Ttn-dVX88D-NjqoHNTpKJmhWZSQljYnk?usp=sharing)

In cell 2 Paste the OpenAI key as `os.environ["OPENAI_API_KEY"] = <Key>`

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/5eda36e8-3a8c-48ae-ad11-adfc592c94d9)

## Moving on to the coding bit.

In this notebook we have tried to upload the entire document content along with the question, so the prompt created is in this format

```
<Context>
The entire document content
</Context>

<Question>The question that is being asked about the document</Question>
```

#### Step 1:

Run cell 1, as this will install all the packages required for running the notebook. Each package has been described in the notebook itself. Please go through it to understand what each of them does.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/0047d8ad-0b4b-4b30-903c-7291865fc996)

If you get this prompt, you can click on `Run Anyway`.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/25182fbf-8e5a-40b6-9c04-0c0261d6aa2c)

Step 2:

Running Cell 2, will import the required modules from the installed packages. Also it will set all the keys in the environment for easy access and making connection to OpenAI.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/da10109f-b689-4d3d-a0d3-c9688f183980)

One thing you will notice is that we have used tiktoken for counting the number of tokens while we send a prompt to OpenAI.

Step 3:

Running cell 3 will initialize the `CallOpenAI()` function for further usage/calling.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/a42b7c34-e04f-46dc-8230-c31fa5623114)

Step 4:

Run cell 4 to initialize the `extract_text()` function for further usage.

This function extract the content from PDF and returns the entire content. The package used to do this is PyMUPDF. This will also print the tokens of the content.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/ca7c8aed-1581-4100-b91e-56cf4b00ccd5)

Step 5:

Run cell 5 to call the `extract_text()` function that we initialized in Step 6, also you need to change the path of the document you want to analyse.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/c7b4ec3d-d9c2-4397-91b7-a7df9f02695e)

Copy your path to the document and paste it here

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/4363429a-95b2-4f2f-bb43-15a8fddc3fe1)

Step 6:

Run cell 6, this will initialize the question and convert the question along with the PDF document content with proper tags.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/f034b7d5-f43f-4be7-8c11-409bd85e53d9)

If you want to change the question, write it here that is marked with red line

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/b2f396ae-01ab-48c6-9888-815a13532f7b)

Step 7:

Run cell 7, to call the OpenAI function, where we are giving it the prompt and the system message.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/7f9968d6-96a4-4f0c-87c0-1843d4281225)

Step 8:

Run cell 8, to print the message from the GPT.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/fa83983d-be7a-44d0-a731-f9c05ab63304)

Step 9:

Run cell 9, to load a longer document, and extract its entire content.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/2bb94a5c-166f-4f6b-9395-faab36ad3d39)

Change the path here

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/50c6ce20-cf2c-4cb8-9a55-5d843a09c923)

As you can see that the Document content is 163227, and the limit of GPT-3.5 is 16k.

Step 10:

Run cell 10, to change the question like you did before.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/9dcaacf0-638e-4c4d-a7ac-1609abd1db60)

Step 11:

Run cell 11, to generate the response from the model. But this time it will throw an error saying, the model maximum context length is 16000 tokens.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/5da6754c-8857-46a1-9f60-a121119f7ea7)

## So here we face the famous Context length problem that every LLM faces at some point. In Lab 0.2 we will solve this problem with an intuitive approach called Retrieval Augmented Generation (**RAG**)
