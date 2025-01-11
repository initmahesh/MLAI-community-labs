[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](<https://colab.research.google.com/github.com/sachin0034/MLAI-community-labs/blob/main/Class-Labs/Lab-3(Fine-tuning-PEFT-LoRA)/Fine_Tuning_Lora_Lab.ipynb>)
# Fine tuning models using PEFT for generating adapters.

Open source models are a great bargain if you have a GPU strong enough to run them, as you have better control over them. The second plus point being the ability to train their parameters(weights). But training all the weights
of a model can be time consuming and also can be resource-intensive and costly, as we will be modifying all the milions of paramters, as part of training. Fine tuning the model requires a lot of training data, huge infrastructure and effort.

**Parameter Efficient Fine Tuning**, comes to play here. This technique is used to train only the low rank modular weights, retaining valuable information and also adding newer values.

**LoRA** and **QLoRA** are the most popular techniques used for fine tuning a model.

* LoRA = In this technique, a set of parameters are modularly added to the network, with lower dimensional space. Instead of modifying the whole network, only these modular low-rank network is modified, to achieve the results.
* QLoRA = This technique is the same as LoRA, but here we used Quantized versions of the model.
* * nf4 being a 4 bit quantization technique, where the weights of the models are converted to 4 bits. This is an extensize process, you can read about it [here](https://www.kaggle.com/code/lorentzyeung/what-s-4-bit-quantization-how-does-it-help-llama2)
 
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](<https://colab.research.google.com/github.com/sachin0034/MLAI-community-labs/blob/main/Class-Labs/Lab-3(Fine-tuning-PEFT-LoRA)/Fine_Tuning_Lora_Lab.ipynb>)

### Prerequisites

* Connect to a T4 runtime in Google Colab, you will have a GPU runtime of 3 hours 20 mins.

* 1. Click on the drop down arrow beside the connect button.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/0b897c5e-fd81-41cd-8fc4-879a1f2640ea)

* 2. Click on change runtime type

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/433e2115-443c-4716-b605-5cffd419c2f9)

* 3. Select T4 GPU and hit save.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/429f86b4-69e5-437e-85d4-9baf3fd9054c)

* Training and testing datasets by the name of "formatted_test_set.jsonl","formatted_train_set.jsonl"
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
* Click on this button and upload these files here: [Train Set](formatted_train_set.jsonl), [Test Set](formatted_test_set.jsonl)

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/d8920030-b617-41c9-b638-e18c10da977d)


### About the code

1. Here we are installing all the required packages in the runtime session
```python
 !pip install -q accelerate bitsandbytes transformers==4.39.3 datasets==2.17.0 peft==0.4.0 #trl==0.4.7
```
2. Importing the required packages needed for fine tuning and inference
```python
import os
import torch
import transformers
from datetime import datetime
from datasets import load_dataset
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    HfArgumentParser,
    TrainingArguments,
    pipeline,
    logging,
)
from peft import prepare_model_for_kbit_training, PeftModel
```
3. Initializing the accelerator for offloading weights to the CPU.
```python
from accelerate import FullyShardedDataParallelPlugin, Accelerator
from torch.distributed.fsdp.fully_sharded_data_parallel import FullOptimStateDictConfig, FullStateDictConfig

fsdp_plugin = FullyShardedDataParallelPlugin(
    state_dict_config=FullStateDictConfig(offload_to_cpu=True, rank0_only=False),
    optim_state_dict_config=FullOptimStateDictConfig(offload_to_cpu=True, rank0_only=False),
)

accelerator = Accelerator(fsdp_plugin=fsdp_plugin)
```
4. Defining the model name, and using BnB config for quantization using nf4 (4-bit) and loading the model from huggingface
```python
model_name = "microsoft/Phi-3-mini-128k-instruct"

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)

# Load base model
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=bnb_config,
    # attn_implementation='eager',
    low_cpu_mem_usage=True,
    trust_remote_code=True
)
```
5. We would also need to create a tokenizer according to the model for building the input
```python
tokenizer = AutoTokenizer.from_pretrained(model_name)
```
6. Using the formatted_train_set.jsonl and formatted_test_set.jsonl, we create the training and the testing split, the will be used for fine tuning the model
```python
from datasets import load_dataset
train_dataset = load_dataset('json', data_files='formatted_train_set.jsonl', split='train')
validation_dataset = load_dataset('json', data_files='formatted_test_set.jsonl', split='train')
```
7. We then move on to the core part of the fine tuning code we generate the lora config that would be needed for generating the adapters
```python
from peft import LoraConfig, get_peft_model

config = LoraConfig(
    r=32,
    lora_alpha=64,
    target_modules=[
        "o_proj",
        "qkv_proj",
        "gate_up_proj",
        "up_proj",
        "down_proj",
        "lm_head",
    ],
    bias="none",
    lora_dropout=0.05,
    task_type="CAUSAL_LM",
)

model = get_peft_model(model, config)
print_trainable_parameters(model)

# Apply the accelerator. You can comment this out to remove the accelerator.
model = accelerator.prepare_model(model)
```
Here we set the rank of the low rank matrix as 32, this sets the rank of the update matrices used in LoRA. The rank determines the size and complexity of these matrices, which in turn affect the trade-off between parameter reduction and accuracy.

The target modules are the main layers that we are specifically aiming to train.

8. We then call the transformers.Trainer module and pass all the required configurations for training the model.
```python
# Defining the output directory name
base_model_name = "phi3-128k"
run_name = base_model_name + "-" + "-mini-custom-finetune"
output_dir = "./" + run_name

tokenizer.pad_token = tokenizer.eos_token

trainer = transformers.Trainer(
    model=model,
    train_dataset=tokenized_train_dataset,
    eval_dataset=tokenized_validation_dataset,
    args=transformers.TrainingArguments(
        output_dir=output_dir,
        warmup_steps=1,
        per_device_train_batch_size=2,
        gradient_accumulation_steps=1,
        gradient_checkpointing=True,
        fp16=True,
        max_steps=51,       # Training steps
        learning_rate=2e-4, # Want a smaller for finetuning
        bf16=False,         # Enable if GPU supports bfloat16
        optim="paged_adamw_32bit",
        logging_dir="./logs",         # Directory for storing logs
        save_strategy="steps",        # Save the model checkpoint every logging step
        save_steps=50,                # Save checkpoints every step
        evaluation_strategy="epoch", # Evaluate the model every logging step
        eval_steps=51,               # Evaluate and save checkpoints every 50 steps
        do_eval=True,                # Perform evaluation at the end of training
        logging_steps = 5,            # Log step and training loss info
        run_name=f"{run_name}-{datetime.now().strftime('%Y-%m-%d-%H-%M')}"          # Name of the W&B run (optional)
    ),
    data_collator=transformers.DataCollatorForLanguageModeling(tokenizer, mlm=False),
)
```
9. Start the training
```python
trainer.train()
```

10. Now we combine the Lora Adapters and the base model.
```python
ft_model = PeftModel.from_pretrained(model, "/content/phi3-128k--mini-custom-finetune/checkpoint-50")
```

11. Loading the content from the formatted_test_set.jsonl file, and used them for generating answers.
```python
import json
question = []
with open("/content/formatted_test_set.jsonl","r") as f:
    question = [json.loads(line) for line in f]
```

12. Now we put the question in a proper format and tokenize the prompt before feeding it to the model for answer generation.
```python
# eval_prompt =f"### Question:{question[1]['input_text']}."
eval_prompt = [
    {"role": "user", "content":question[0]["content"]+'\n'+question[1]["content"] }
]
# eval_prompt =f"Write a poem about a horse?"
model_input = tokenizer(str(eval_prompt), return_tensors="pt").to("cuda")

ft_model.eval()
```

13. We then pass the prompt to the model along with some generation config that controls the precision and uniqueness of the answer.
```python
def fine_tuned_pi(eval):
  pipe = pipeline(
        "text-generation",
        model=ft_model,
        tokenizer=tokenizer,
        trust_remote_code = True
    )

  generation_args = {
      "max_new_tokens": 1024,
      "return_full_text": False,
      "temperature": 0.6,
      "top_p" : 0.9,
      "top_k" : 10,
      "do_sample": True,
  }

  output = pipe(eval, **generation_args)
  print(output[0]['generated_text'])
```
The model will return and output and the answer will be displayed.

## Output
### Question
So we asked about the Customer name for a contract, that we provided the chunks for in the content
### Answer
This is the answer we got and it was correct
![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/37a006e1-6b51-4d29-9c04-4f6bd499e489)

