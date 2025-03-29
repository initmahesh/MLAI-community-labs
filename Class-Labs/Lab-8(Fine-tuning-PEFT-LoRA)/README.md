[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](<https://colab.research.google.com/github.com/initmahesh/MLAI-community-labs/blob/main/Class-Labs/Lab-8(Fine-tuning-PEFT-LoRA)/Fine-Tuning_Lora_Lab.ipynb>)

# Fine tuning models using PEFT for generating adapters.

Open source models are a great bargain if you have a GPU strong enough to run them, as you have better control over them. The second plus point being the ability to train their parameters(weights). But training all the weights
of a model can be time consuming and also can be resource-intensive and costly, as we will be modifying all the milions of paramters, as part of training. Fine tuning the model requires a lot of training data, huge infrastructure and effort.

**Parameter Efficient Fine Tuning**, comes to play here. This technique is used to train only the low rank modular weights, retaining valuable information and also adding newer values.

**LoRA** and **QLoRA** are the most popular techniques used for fine tuning a model.

- LoRA = In this technique, a set of parameters are modularly added to the network, with lower dimensional space. Instead of modifying the whole network, only these modular low-rank network is modified, to achieve the results.
- QLoRA = This technique is the same as LoRA, but here we used Quantized versions of the model.
- - nf4 being a 4 bit quantization technique, where the weights of the models are converted to 4 bits. This is an extensize process, you can read about it [here](https://www.kaggle.com/code/lorentzyeung/what-s-4-bit-quantization-how-does-it-help-llama2)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](<https://colab.research.google.com/github.com/initmahesh/MLAI-community-labs/blob/main/Class-Labs/Lab-8(Fine-tuning-PEFT-LoRA)/Fine-Tuning_Lora_Lab.ipynb>)

### Prerequisites

- Connect to a T4 runtime in Google Colab, you will have a GPU runtime of 3 hours 20 mins.

- 1. Click on the drop down arrow beside the connect button.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/0b897c5e-fd81-41cd-8fc4-879a1f2640ea)

- 2. Click on change runtime type

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/433e2115-443c-4716-b605-5cffd419c2f9)

- 3. Select T4 GPU and hit save.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/429f86b4-69e5-437e-85d4-9baf3fd9054c)

- Training and testing datasets by the name of "formatted_test_set.jsonl","formatted_train_set.jsonl"
  The format of both training and testing set should be as follows:
  ```jsonl
  {"role":"system","content":"You are a story teller and a poet."}
  {"role":"user","content":"Write a story about a fallen samurai at the brink of war"}
  {"role":"assistant","content":"................The answer................"}
  {"role":"system","content":"You are a story teller and a poet."}
  {"role":"user","content":"Write a poem about a bird"}
  {"role":"assistant","content":"................The answer................"}
  ```
  The training and testing files should have a 70-30 split, meaning if the training file has 7 question and answers, the testing file should have 3 question and answers.
- Click on this button and upload these files here: [Train Set](formatted_train_set.jsonl), [Test Set](formatted_test_set.jsonl)

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/d8920030-b617-41c9-b638-e18c10da977d)

## 📌 Project Overview

We are fine-tuning **Phi-3-mini-128k-instruct** on our datase. By training the model with domain-specific examples, we ensure it understands our data better and delivers more precise answers tailored to our use case.

---

## 🛠️ Key Features

### 1️⃣ Custom Fine-Tuning with LoRA

✅ Fine-tune **only specific layers** to reduce computational cost.  
✅ Ensures **faster adaptation** to AT&T-specific queries.

### 2️⃣ Efficient Model Compression (4-bit Quantization)

✅ Uses **BitsAndBytes** to reduce model size.  
✅ Enables deployment on **low-cost GPUs**.

### 3️⃣ Custom Dataset for Personalized Responses

✅ Dataset: `dataset.jsonl` (AT&T-specific Q&A pairs).  
✅ Helps AI provide **relevant & contextual answers**.

### 4️⃣ ChatML-Powered Prompt Engineering

✅ Uses **ChatML formatting** to structure inputs & outputs.  
✅ Helps in **reducing hallucinations & improving accuracy**.

### 5️⃣ Smart Inference Pipeline

✅ Optimized parameters: `temperature`, `top_p`, `top_k`.  
✅ Limits **response length** for more **precise answers**.

---

## 📂 Project Structure

| Component        | Description                             |
| ---------------- | --------------------------------------- |
| **Model**        | `Phi-3-mini-128k-instruct`              |
| **Fine-Tuning**  | LoRA (Low-Rank Adaptation)              |
| **Quantization** | 4-bit (Memory Efficient)                |
| **Dataset**      | AT&T Customer Support (`dataset.jsonl`) |

---

### Example :

### Question

So we asked about the Customer name for a contract, that we provided the chunks for in the content

### Answer

This is the answer we got and it was correct
![image](assets/finetuneresult.png)
