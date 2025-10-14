def load_pdf(file_path: str):
    """
    Load a PDF document and return its content as text.

    Args:
        file_path (str): The path to the PDF file.

    Returns:
        str: The text content of the PDF.
    """
    from PyPDF2 import PdfReader

    text = ""
    with open(file_path, "rb") as file:
        reader = PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    
    return text


def load_documents(file_paths: list):
    """
    Load multiple documents from given file paths.

    Args:
        file_paths (list): A list of paths to the documents.

    Returns:
        list: A list of document contents.
    """
    documents = []
    for path in file_paths:
        if path.endswith('.pdf'):
            documents.append(load_pdf(path))
        # Add more document types as needed
    return documents