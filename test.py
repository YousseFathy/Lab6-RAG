# Test processor (Load, Split, Embed)
# ===============================
try:
    from processor import load_documents, split_documents, embed_and_store

    print("\n Running: processor.py")
    docs = load_documents('Documents')
    chunks = split_documents(docs)
    embed_and_store(chunks, model_name='all-MiniLM-L6-v2', save_path='faiss_store')
    embed_and_store(chunks, model_name='paraphrase-MiniLM-L12-v2', save_path='faiss_store_l12')
except Exception as e:
    print("processor.py failed:", e)


# Test Retrieval (with Metadata)
# ===============================
try:
    from retrieval import retrieve_similar_docs, retrieve_with_mmr

    print("\n Running: retrieval.py")

    results = retrieve_similar_docs("What is AI?")
    print(f"Top {len(results)} basic results:")
    for i, doc in enumerate(results, 1):
        print(f"--- Basic Result #{i} ---")
        print("Metadata:", doc.metadata)
        print("Snippet:", doc.page_content[:200])
        print()

    mmr_results = retrieve_with_mmr("What is AI?")
    print(f"Top {len(mmr_results)} MMR results:")
    for i, doc in enumerate(mmr_results, 1):
        print(f"--- MMR Result #{i} ---")
        print("Metadata:", doc.metadata)
        print("Snippet:", doc.page_content[:200])
        print()

except Exception as e:
    print(" retrieval.py failed:", e)



# Test RAG Generation
# ===============================
try:
    from RAG import run_rag

    print("\n Running: RAG.py")
    run_rag("What models are there for AI?")
    run_rag("What are the risks of AI?", use_alternative_prompt=True)
    run_rag("What are AI classifying methods?", model_name="paraphrase-MiniLM-L12-v2")
    run_rag("Is AI trustworthy?", rewrite=True)
except Exception as e:
    print(" RAG.py failed:", e)


#  Test Evaluation (Real RAG Output + Real Retrieval IDs)
# ===============================
try:
    from retrieval import retrieve_similar_docs
    from RAG import run_rag
    from Evaluate import evaluate_answer_quality, evaluate_retrieval

    print("\n Running: Evaluate.py")

    # Define a real test query
    query = "What models are there for AI?"
    expected_keywords = ["GPA", "Claude", "Gemini ", "LLaMA ", "Mistral", "Falcon"]

    # Step 1: Run RAG to get generated answer (for answer quality evaluation)
    generated_answer = run_rag(query)
    evaluate_answer_quality(generated_answer, expected_keywords)

    # Step 2: Run retrieval to get actual document metadata
    retrieved_docs = retrieve_similar_docs(query, k=2)
    retrieved_ids = [doc.metadata.get("source", f"doc{i}") for i, doc in enumerate(retrieved_docs)]

    
    relevant_ids = retrieved_ids[:3]  #actual relevant files

    # Step 4: Evaluate retrieval
    evaluate_retrieval(relevant_ids, retrieved_ids)

except Exception as e:
    print(" Evaluate.py failed:", e)"""


#  Test Configuration Comparison
# ===============================
try:
    import Configuration_test
except Exception as e:
    print(" Configuration_test.py failed:", e)