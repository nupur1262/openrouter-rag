def main():
    """
    Entry point for the Open Router RAG application.
    This function orchestrates the loading of documents, 
    processing of queries, and interaction with the user.
    """
    import os
    from loader import load_documents
    from rag import answer_query

    # Load documents from the specified path
    documents_path = "my_document.pdf"  # Update with your document path
    documents = load_documents(documents_path)

    # Example query to ask the RAG model
    user_query = input("Please enter your question about the document: ")

    # Get the answer from the RAG application
    answer = answer_query(user_query)

    print("\n--- Final Answer ---")
    print(answer)

if __name__ == "__main__":
    main()