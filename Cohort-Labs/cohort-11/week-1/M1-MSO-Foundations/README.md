# CCA Developer · M1 — MSO Foundations

A hands-on Colab lab for the first module of the Claude certification track. You learn how LLMs behave, how to pick a model and control its reasoning, how to prompt it, and the two ways to call Claude in production: the **Messages API** and the **Claude Agent SDK**. You run every idea on real contracts.

| Lab | What you'll do | Open |
|-----|----------------|------|
| MSO Foundations | Learn how LLMs behave, then call Claude with the Messages API and the Agent SDK on real contracts | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/initmahesh/MLAI-community-labs/blob/main/Cohort-Labs/cohort-11/week-1/M1-MSO-Foundations/module1-mso-foundation-colab.ipynb) |

## What this lab is about

| Section | What you learn | Subtopics |
|---|---|---|
| **1.1 How LLMs Behave** | What the model reads, how much fits, and why answers vary | Tokens<br>Context window<br>Sampling and temperature<br>Non-determinism<br>Evaluation |
| **1.2 Model and Reasoning** | Pick a model for the task and control how much it thinks | The Claude model family<br>Alias vs pinned model IDs<br>Reasoning (thinking) |
| **1.3 Prompting** | Use examples to control the output, and keep a conversation going | Zero-shot<br>One-shot<br>Few-shot<br>Multi-turn |
| **1.4 The Messages API** | Choose how your code waits for an answer | SDK vs raw REST<br>Synchronous<br>Streaming<br>Async<br>Message Batches |
| **1.5 Agent SDK vs Messages API** | Run the same task through both interfaces | Same task, two interfaces<br>Which should you use? |

## Before you start

- Have your **Anthropic API key** ready. The notebook asks for it once and does not save it.
- Download both contracts. You upload them in the Setup cell:
  - [AWS1.pdf](https://drive.google.com/file/d/1XSe2pSsGN1ssAbif92rvb80AnHb_Ni0F/view?usp=sharing): short, about 12 pages
  - [PROFRAC HOLDINGS, LLC credit agreement.pdf](https://drive.google.com/file/d/1UyOxeaEQsK5TFxXHI63PshoKmj0yjTmW/view?usp=sharing): long, about 216 pages
- Click the badge above, then run the cells from top to bottom. Don't skip ahead.
- Most cells use a small number of tokens. The cells that send the long contract (1.1.2 and 1.4.5) use the most.
- The batch cell in 1.4.5 runs in the background and can take a few minutes. That is normal.
- The Claude Agent SDK is installed later, in section 1.5, when the notebook needs it.
