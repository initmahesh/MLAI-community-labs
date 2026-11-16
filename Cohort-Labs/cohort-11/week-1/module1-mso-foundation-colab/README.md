# CCA Developer · M1 — MSO Foundations

A hands-on Colab lab for the first module of the Claude certification track. You learn the basics you need before building anything with Claude, and you run every idea on a real contract: the AWS Customer Agreement.

| Lab | What you'll do | Open |
|-----|----------------|------|
| MSO Foundations | Count tokens, budget the context window, see why answers vary, choose a model, use thinking, prompt and call Claude the right way, all on a real contract | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/initmahesh/MLAI-community-labs/blob/main/Cohort-Labs/cohort-11/week-1/mso-foundation-colab/mso-foundation-colab.ipynb) |

## What this lab is about

| Section | What you learn |
|---|---|
| 1.1 Tokens | See what Claude reads, and what it costs |
| 1.2 Context Window | Budget input and output together, and order a prompt so it can be cached |
| 1.3 Sampling and Non-Determinism | Understand why the same prompt gives different answers, and test for it |
| 1.4 The Claude Model Family | Choose a model with evidence, not intuition |
| 1.5 Reasoning Modes | Know when extended thinking is worth paying for |
| 1.6 Prompting Modes | Add only as much guidance as the task needs |
| 1.7 SDK vs REST vs Batch | Pick the right way to call Claude for each job |

## Before you start

- Have your **Anthropic API key** ready. The notebook asks for it once and does not save it.
- Download the contract: [AWS1.pdf](https://drive.google.com/file/d/1XSe2pSsGN1ssAbif92rvb80AnHb_Ni0F/view?usp=sharing). You upload it in the Setup cell.
- Click the badge above, then run the cells from top to bottom. Don't skip ahead.
- Every cell that calls Claude uses a small number of tokens. Sections 1.2, 1.4 and 1.7 send the whole contract, so they use the most.
- The batch cell in 1.7 runs in the background and can take a few minutes. That is normal.
