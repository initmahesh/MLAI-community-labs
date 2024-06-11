## Retrieval Augmented Generation
What is RAG?


As NVIDIA quotes it in the best and easiest way possible "Retrieval-augmented generation (RAG) is a technique for enhancing the accuracy and reliability of generative AI models with facts fetched from external sources."

It is needed for mapping the best embeddings there are in a knowledge base index, to the prompt that will be submnitted to the model. The model will use these embeddings along with its generative AI capability to respond to the query in the best possible way.

In the notebook [RAG_Responsible_AI.ipynb](RAG_Responsible_AI.ipynb), we have curated the easiest implementation of RAG, using newer technologies like creating embeddings and using **faiss** for creating index of embeddings. Also we have implemented **sentence transformers** all of which you can see in action upon running the notebook.

### Prerequisites:

In order to implement these techniques, we would need to install some packages:

* sentence_transformers: This package provides us an easy way for loading models that are used for generating embeddings for the texts.
* langchain: This package is imported for using the RecursiveCharacterTextSplitter for generating chunks for longers texts. These chunks will be used for generating the embeddings.
* pypdf: This package is used for handling PDF documents.

### Code explanation:
```python
!pip install transformers faiss-cpu sentence-transformers langchain pypdf
```
This installs all the packages using PIP (package installer for Python).

```python
from transformers import pipeline
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
from pypdf import PdfReader
import faiss
import numpy as np
```
All the required imports are done so that they can be used in the code.

```python
encoder = SentenceTransformer("all-mpnet-base-v2")
```
Here we are using the all-mpnet-base-v2 for its tilt over quality than speed, because we are not working on any intensive task currently. You can try to use any other model that best suits your use case.

```python
def create_embedding_index(k_base):
  vectors = encoder.encode(k_base)
  print(vectors.shape)

  vector_dimension = vectors.shape[1]
  index = faiss.IndexFlatL2(vector_dimension)
  faiss.normalize_L2(vectors)
  index.add(vectors)
  return index
```
This function takes in the knowledge base and encodes them to continuous values(vectors), these values are then normalized and stored in the faiss index. This index is then returned and will be used for searching the closest embeddings resembling the prompt.

```python
def answer_question(question,index,results_len):
  """
  This function takes a question and uses RAG to answer it with Faiss for retrieval.

  Args:
      question: The user's question as a string.

  Returns:
      A dictionary containing the answer and retrieved passage.
  """
  search_vector = encoder.encode(question)
  _vector = np.array([search_vector])
  faiss.normalize_L2(_vector)

  # # # Encode the question
  # question_encoding = tokenizer(question, return_tensors="pt",truncation=True,padding=True)["input_ids"]
  # # Retrieve relevant passages using Faiss
  # question_vec = question_encoding.cpu().numpy()
  distances, retrieved_idxs = index.search(_vector, results_len)

  # Extract the answer and passage based on the retrieved index
  top_passage_idx = retrieved_idxs.ravel()[0]
  answer = knowledge_base[top_passage_idx]

  # Return the answer and retrieved passage for transparency
  return {"answer": answer, "retrieved_passage": knowledge_base[top_passage_idx]}
```
This function will be used for encoding the question(prompt) and storing then in a numpy array.

This numpy array will be used in the ```index.search()``` function to retrieve matching embedding using Eucledian Distance(L2). This will return the distances and indices of the best matching embeddings.

These indices will be used to extract the passages from the Knowledge base.
 
```python

knowledge_base = []
recursive_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap = 30,
    length_function = len
)
file = PdfReader("/content/Adverity1.pdf") # <------Make changes in the PDF file path that you want to use
for i in range(0,len(file.pages)):
  page = file.pages[i]
  text = page.extract_text()
  knowledge_base.append(recursive_splitter.split_text(text))
```
The chunk size is defined as 500 characters, and each chunk will have 30 characters overlapping.

The PDF file is read and the content on each page is converted into chunks and the ```knowledge_base``` is populated with it.
```python
embed_index = create_embedding_index(knowledge_base)
```
The embedding index is then created using the knowledge base
```python
# Example usage
question = "What is termination period of the contract?"


answer_dict = answer_question(question,embed_index,1)

print(f"Question: {question}")
for i in range(len(answer_dict['answer'])):
  print(f"Answer: \n {answer_dict['answer'][i]}")
print(f"Retrieved Passage: {answer_dict['retrieved_passage']}")
```
Here we are asking a question related to the document and this will fetch the chunks that are related to the question.
