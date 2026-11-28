# Lab 2.3: Knowledge Graph RAG

## Run all, then open the app

1. Open the notebook in Colab: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/initmahesh/MLAI-community-labs/blob/main/Cohort-Labs/cohort-11/week-2/2.3-knowledge-graph-RAG/notebook.ipynb)
2. Click **Runtime → Run all**.
3. When the last cell finishes, open the link ending in **`.gradio.live`**.
4. On the **1. Setup** tab, paste your OpenAI API key, upload the [loan agreement PDF](https://pragyaallc-my.sharepoint.com/:b:/g/personal/sachin_parmar_legalgraph_ai/IQD6lbbrDHV5ToSGrWurVlejAZ9kRJYW40iwWLtE5fzC54M?e=VtD4Mp) (any contract works), and press **Build**. **Fast demo** is ticked by default (Graphify reads only Article 2). Untick it to build the graph of the whole contract (several minutes).
5. Open **2. Knowledge graph**. Drag dots, zoom, search a term (try `Interest Rate`), and click a dot to read its clause.
6. Open **3. The problem and the fix** and press **Run the showcase**. It asks the same question three ways (plain GPT, plain RAG, graph RAG) and shows a scorecard.
7. Open **4. Ask and compare**, ask your own question, for example: *What interest rate applies if Term SOFR is 0.80%?*

The **Knowledge graph** tab shows the graph of the whole contract:

![assets](assets/1.png)

**Run the showcase** shows what each mode got right:

![assets](assets/2.png)

> Do not share the `.gradio.live` link. It stops working when you stop the notebook.

---

## What is a knowledge graph?

A **knowledge graph** stores a document as **dots** (the things in it) and **lines** (how they connect).

Normal search finds passages that *look similar* to your question. An answer spread across several clauses can be missed, because the clauses that link to each other don't look alike. A knowledge graph keeps those links, so you can follow them from one clause to the next.

## What we are doing in this lab

We add a **knowledge graph** to RAG:

- **Graphify** reads the contract and builds a graph. Things in the contract (like `Interest Rate`, `Spread`, `Index Floor`) become **dots**, and how they connect becomes **lines**.
- When you ask a question, the model picks the starting dots, and the app follows their lines to find every related clause.
- The model answers from the contract text those dots point to.

**Example:** the interest rate is the `Spread` (4.20%) plus `Term SOFR`, which is limited by the `Index Floor` (1.12606%). So 4.20% + 1.12606% = **5.32606%**.
