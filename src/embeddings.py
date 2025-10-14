from langchain_community.embeddings import HuggingFaceEmbeddings

def create_embeddings(documents, model_name="sentence-transformers/all-MiniLM-L6-v2"):
    """
    Create embeddings for the given documents using the specified model.

    Parameters:
    - documents: List of documents to create embeddings for.
    - model_name: The name of the model to use for creating embeddings.

    Returns:
    - embeddings: List of embeddings for the documents.
    """
    embeddings_model = HuggingFaceEmbeddings(model_name=model_name)
    embeddings = embeddings_model.embed_documents(documents)
    return embeddings