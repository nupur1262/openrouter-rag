# openrouter-rag

## Description
The `openrouter-rag` project implements the Open Router Chat and RAG (Retrieve, Augment, Generate) processes. It includes functionality for loading documents, splitting text, creating embeddings, and querying a language model. This project leverages various libraries to facilitate document processing and interaction with the OpenRouter API.

## Installation Instructions
To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/nupur1262/openrouter-rag.git
   ```

2. Navigate to the project directory:
   ```
   cd openrouter-rag
   ```

3. Install the required libraries:
   ```
   pip install -r requirements.txt
   ```

4. Set up your environment variables by copying `.env.example` to `.env` and filling in your API keys:
   ```
   cp .env.example .env
   ```

## Usage
To run the application, execute the main script:
```
python src/main.py
```

You can also interact with the Jupyter notebook located in the `notebooks` directory for a hands-on experience with the RAG processes.


## Acknowledgments
- OpenAI for providing the API.
- LangChain for document processing utilities.
- FAISS for efficient vector storage and retrieval.