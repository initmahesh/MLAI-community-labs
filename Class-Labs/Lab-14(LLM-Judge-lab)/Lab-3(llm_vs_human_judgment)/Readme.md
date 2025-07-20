# Evaluating LLM Judge Responses Against Human Evaluation

In the previous two labs, we explored different approaches to evaluation:

- **Lab 1:** Utilized predefined evaluators provided by Azure to assess responses.
- **Lab 2:** Developed a custom judge using a Large Language Model (LLM) to perform evaluations.

In this lab, we aim to compare the effectiveness of LLM-based evaluation with human evaluation. The goal is to determine whether LLMs can provide judgments that are as reliable or insightful as those made by humans, and to analyze the strengths and limitations of each approach.

---

## How We Compare LLM and Human Evaluation

To compare the effectiveness of LLM-based evaluation with human evaluation, we follow these steps:

1. **Obtain LLM Evaluation Results:**
   - From Lab 2, after running your LLM judge, you download the evaluation results as a CSV file.
2. **Obtain Human Evaluation Results:**
   - You have a separate CSV file containing results that have already been evaluated by a human. You can access the human evaluation sheet [here](https://drive.google.com/file/d/1WMj5L4SNu3FboczMm6k2Qnw6lROed19x/view?usp=sharing).
3. **Comparison Process:**
   - For each item (e.g., response, clause, or case), compare the LLM’s judgment with the human’s judgment.
   - Create a table to visualize the comparison and calculate the accuracy.

---

## Precision, Recall, and Confusion Matrix

To better understand the performance of the LLM judge compared to human evaluation, we use a confusion matrix and calculate precision and recall.

|                       | Predicted: Correct  | Predicted: Incorrect |
| --------------------- | ------------------- | -------------------- |
| **Actual: Correct**   | True Positive (TP)  | False Negative (FN)  |
| **Actual: Incorrect** | False Positive (FP) | True Negative (TN)   |

**Example:**

Imagine you're using the Validator LLM to assess the accuracy of the Responder LLM’s answers to 100 factual questions:

- 50 answers were labeled as "Correct" by the Validator LLM and were indeed correct (**TP**).
- 20 answers were labeled as "Correct" by the Validator LLM but were actually incorrect (**FP**).
- 10 answers were labeled as "Incorrect" by the Validator LLM but were actually correct (**FN**).
- 20 answers were labeled as "Incorrect" by the Validator LLM and were indeed incorrect (**TN**).

**Using this confusion matrix:**

- **Precision** (for "Correct" classification):

  \[
  \text{Precision} = \frac{TP}{TP + FP} = \frac{50}{50 + 20} = \frac{5}{7} \approx 71.43\%
  \]
  Precision indicates the reliability of the Validator LLM’s "Correct" classification. A higher precision means that when the Validator LLM labels a response as correct, it is more likely to truly be correct.

- **Recall** (for the "Correct" category):

  \[
  \text{Recall} = \frac{TP}{TP + FN} = \frac{50}{50 + 10} = \frac{5}{6} \approx 83.33\%
  \]
  Recall shows how effectively the Validator LLM identifies all correct responses. A high number of false negatives (FN) will lower the recall, meaning the evaluator LLM is missing the mark in finding all correct entries.

---
