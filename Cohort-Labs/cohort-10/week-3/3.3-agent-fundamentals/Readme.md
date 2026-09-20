# Lab 3.3: Building Contract-IQ — A Production Contract Reviewer with Claude

Open the notebook using the link below:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/initmahesh/MLAI-community-labs/blob/main/Cohort-Labs/cohort-10/week-3/3.3-agent-fundamentals/notebook.ipynb)


### **Note:** When you open the notebook, you may see a warning that says *"This notebook was not authored by Google"*. This is expected since it's loaded from GitHub. If you get this prompt, click on **Run anyway**.

---

## What You'll Learn

| Section | The problem Contract-IQ hits | What you learn |
|---|---|---|
| **1** | Two clauses contradict each other and Contract-IQ misses it | Extended thinking, effort levels, thinking blocks across tool turns |
| **2** | Contract-IQ has no way to look anything up | Tool schemas, the tool-use loop, single vs parallel calls |
| **3** | A 40-second silence makes users think it crashed | Streaming, assembling events, recovering from a broken stream |
| **4** | Contract-IQ is about to email a vendor a rejection, by herself | Workflow vs agent, wiring a loop, human-in-the-loop checkpoints |
| **5** | Contract-IQ forgets this vendor already failed review last quarter | Memory across sessions, memory scope, context cost |
| **6** | Half the contracts arrive as scans and photos | Images, PDFs, and the Files API |

## Prerequisites

1. **Anthropic API key** — you'll need one to call Claude from the notebook.
2. **Google Colab setup.** If you haven't used Colab before, follow this guide: [Click Here](https://medium.com/@aditya_dev30/getting-started-with-google-colab-your-ultimate-setup-guide-for-generative-ai-projects-53fe25f3fc04)

---
