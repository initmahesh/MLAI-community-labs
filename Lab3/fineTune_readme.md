# Fine tuning models using PEFT for generating adapters.

Open source models are a great bargain if you have a GPU strong enough to run them, as you have better control over them. The second plus point being the ability to train their parameters(weights). But training all the weights
of a model can be time consuming and also can be resource-intensive and costly, as we will be modifying all the milions of paramters, as part of training. Fine tuning the model requires a lot of training data, huge infrastructure and effort.

**Parameter Efficient Fine Tuning**, comes to play here. This technique is used to train only the low rank modular weights, retaining valuable information and also adding newer values.

**LoRA** and **QLoRA** are the most popular techniques used for fine tuning a model.

* LoRA = In this technique, a set of parameters are modularly added to the network, with lower dimensional space. Instead of modifying the whole network, only these modular low-rank network is modified, to achieve the results.
* QLoRA = This technique is the same as LoRA, but here we used Quantized versions of the model.
* * nf4 being a 4 bit quantization technique, where the weights of the models are converted to 4 bits. This is an extensize process, you can read about it [here](https://www.kaggle.com/code/lorentzyeung/what-s-4-bit-quantization-how-does-it-help-llama2)
 
Running the Notebook [FineTuning_models_custom.ipynb](FineTuning_models_custom.ipynb)

### Prerequisites

* Connect to a T4 runtime in Google Colab, you while have a GPU runtime of 3 hours 20 mins.

* 1. Click on the drop down arrow beside the connect button.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/0b897c5e-fd81-41cd-8fc4-879a1f2640ea)

* 2. Click on change runtime type

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/433e2115-443c-4716-b605-5cffd419c2f9)

* 3. Select T4 GPU and hit save.

![image](https://github.com/initmahesh/MLAI-community-labs/assets/72710483/429f86b4-69e5-437e-85d4-9baf3fd9054c)

* Training and testing datasets by the name of "formatted_test_set.jsonl","formatted_train_set.jsonl","validation_set.jsonl"
