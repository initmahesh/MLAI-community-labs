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
   - You have a separate CSV file containing results that have already been evaluated by a human. You can access the human evaluation sheet [here](https://drive.google.com/file/d/1jaiun8mi6OMHYnlCdWIcHvSgU-s-ZBOR/view?usp=sharing).
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

## let's Start Comparing 

Looking at both CSV files, there's a critical mismatch in the data:

**LLM Judge Results (File 1):**
- Governing Law: India
- Limitation of Liability In Months: 12  
- Product Name: WhatfixDigitalAdoptionPlatform

**Human Evaluation Results (File 2):**
- Product Name: WhatfixDigitalAdoptionPlatform
- Limitation of Liability In Months: 12 *(Matches)*
- Governing Law: India *

### Assumption for Analysis
Assuming the values got swapped in the human evaluation file, the correct mapping should be:
- Product Name: WhatfixDigitalAdoptionPlatform → WhatfixDigitalAdoptionPlatform
- Limitation of Liability: 12 → 12
- Governing Law: India → India

## Evaluation Metrics Analysis

For each question, I'll compare LLM Judge (all "True") vs Human Evaluation:

### Question 1: "Was the information extracted as per the question asked in the key term?"
- **LLM Judge**: All 3 = True
- **Human Eval**: All 3 = Yes (True)
- **Result**: Perfect match

### Question 2: "Was the information complete?"
- **LLM Judge**: All 3 = True
- **Human Eval**: Product Name = No, Others = Yes
- **Mismatch**: 1 case

### Question 3: "Was the information enough to make a conclusive decision?"
- **LLM Judge**: All 3 = True
- **Human Eval**: Governing Law = No, Others = Yes
- **Mismatch**: 1 case

### Question 4: "Was the AI reasoning discussing the relevant clause?"
- **LLM Judge**: All 3 = True
- **Human Eval**: All 3 = No
- **Mismatch**: 3 cases

### Question 5: "Does the information stay within document scope?"
- **LLM Judge**: All 3 = True
- **Human Eval**: All 3 = Yes
- **Result**: Perfect match

### Question 6: "Were results free from misleading claims?"
- **LLM Judge**: All 3 = True
- **Human Eval**: All 3 = Yes
- **Result**: Perfect match

### Question 7: "Does the tool avoid generic/non-contract answers?"
- **LLM Judge**: All 3 = True
- **Human Eval**: All 3 = Yes
- **Result**: Perfect match

### Question 8: "Did the tool prevent false claims about people/entities?"
- **LLM Judge**: All 3 = True
- **Human Eval**: All 3 = No
- **Mismatch**: 3 cases

## Confusion Matrix Calculation

**Total Evaluations**: 3 key terms × 8 questions = 24 evaluations

### Agreement Analysis:
- **Perfect Matches (Both True/Yes)**: 15 cases
- **Perfect Matches (Both False/No)**: 0 cases
- **Disagreements (LLM=True, Human=No)**: 9 cases
- **Disagreements (LLM=False, Human=Yes)**: 0 cases

### Confusion Matrix:
|                       | Human: Correct (Yes) | Human: Incorrect (No) |
|-----------------------|---------------------|----------------------|
| **LLM: Correct (True)**   | 15 (TP)            | 9 (FP)               |
| **LLM: Incorrect (False)** | 0 (FN)             | 0 (TN)               |

### Metrics Calculation:

**Precision** = TP / (TP + FP) = 15 / (15 + 9) = 15/24 = **62.5%**

**Recall** = TP / (TP + FN) = 15 / (15 + 0) = 15/15 = **100%**

**Accuracy** = (TP + TN) / (TP + TN + FP + FN) = (15 + 0) / 24 = **62.5%**

## Key Findings:

1. **High Recall (100%)**: The LLM judge never missed a case that humans marked as correct
2. **Moderate Precision (62.5%)**: The LLM judge was overly optimistic, marking 9 cases as correct that humans marked as incorrect
3. **Main Disagreement Areas**: 
   - "AI reasoning discussing relevant clause" (3 disagreements)
   - "Preventing false claims about people/entities" (3 disagreements)
   - Individual cases in completeness and conclusiveness

## Interpretation:
The LLM judge tends to be more lenient/optimistic compared to human evaluators, particularly in areas requiring nuanced judgment about reasoning quality and entity-related claims.
