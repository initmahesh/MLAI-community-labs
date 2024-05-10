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
