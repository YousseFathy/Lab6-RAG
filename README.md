# Lab6-RAG
# CSAI 422 - Lab Assignment 6: Retrieval-Augmented Generation (RAG) System


 Project Overview

This project implements a **Retrieval-Augmented Generation (RAG)** system using open-source tools including LangChain, Sentence Transformers, and FAISS with local vector storage. The system is capable of loading, processing, embedding, retrieving, and generating responses based on a local document corpus.

---

 Setup Instructions

 Requirements

- Python 3.10+
- pip
- LLM API key (e.g., OpenAI GPT-3.5/4 or Claude)

 Installation

```bash
git clone https://github.com/yourusername/csai422-rag-lab.git
cd csai422-rag-lab

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt

csai422-rag-lab6/
│
├── Documents/                
├── faiss_store/            
├── faiss_store_l12/      
│
├── processor.py             
├── retrieval.py      
├── RAG.py               
├── Evaluate.py             
├── Configuration_test.py 
├── test_all.py
│
├── requirements.txt
└── README.md

Testing Functionality
Run all core components of your RAG system via:
python test_all.py

Processor Testing
Loading documents from /Documents

Splitting them into chunks

Embedding using:

all-MiniLM-L6-v2

paraphrase-MiniLM-L12-v2

Storing embeddings into FAISS vector stores

Retrieval Testing
Basic similarity search using retrieve_similar_docs()

MMR-based retrieval using retrieve_with_mmr()

Outputs top-k document snippets and metadata

RAG Generation
Queries integrated with retrieved context:

General prompt

Alternate prompt (with use_alternative_prompt=True)

Custom embedding model (model_name="paraphrase-MiniLM-L12-v2")

Query rewriting (rewrite=True)

Evaluation
Answer Quality Evaluation:

Compares LLM output to a list of expected keywords

Retrieval Evaluation:

Precision, recall, and F1 score using actual and retrieved document IDs

Configuration Comparison
Runs experimental configs from Configuration_test.py to compare:

Different embedding models

Retrieval strategies

Prompt styles

Sample Queries Tested
"What models are there for AI?"

"What are the risks of AI?"

"What are AI classifying methods?"

"Is AI trustworthy?"

Evaluation Metrics
Implemented in Evaluate.py:

Answer Quality: keyword match, relevance

Retrieval Performance: precision, recall, F1

Comparison Framework: multiple configurations evaluated and printed

Embedding Models Used
all-MiniLM-L6-v2

paraphrase-MiniLM-L12-v2

Prompt Strategies
Default factual query prompt

Alternative template (for opinion-based or causal queries)

Rewritten queries (via LLM)

Retrieval Strategies
Basic top-k similarity search

Maximum Marginal Relevance (MMR)

(Optional) Metadata filtering and hybrid search

Bonus Features
Query Rewriting
Post-Retrieval Filtering

Author
Name: Youssef Fathy

Course: CSAI 422 – Spring 2025
