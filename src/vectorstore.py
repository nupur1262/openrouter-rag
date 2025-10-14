from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

class VectorStoreManager:
    def __init__(self, documents):
        self.documents = documents
        self.embeddings = self.create_embeddings()
        self.vectorstore = self.create_vectorstore()

    def create_embeddings(self):
        model_name = "sentence-transformers/all-MiniLM-L6-v2"
        embeddings = HuggingFaceEmbeddings(model_name=model_name)
        return embeddings

    def create_vectorstore(self):
        vectorstore = FAISS.from_documents(self.documents, self.embeddings)
        return vectorstore

    def retrieve(self, query):
        retriever = self.vectorstore.as_retriever()
        return retriever.invoke(query)