import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

KNOWLEDGE_BASE_PATH = "data/knowledge_base"
EMBEDDINGS_PATH = "data/embeddings"


def load_documents():
    documents = []

    for filename in os.listdir(KNOWLEDGE_BASE_PATH):
        if filename.endswith(".txt"):
            file_path = os.path.join(KNOWLEDGE_BASE_PATH, filename)
            loader = TextLoader(file_path, encoding="utf-8")
            documents.extend(loader.load())

    return documents


def chunk_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    return splitter.split_documents(documents)


def build_vector_database():
    documents = load_documents()
    chunks = chunk_documents(documents)

    embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=EMBEDDINGS_PATH
    )

    print("Vector database succesvol aangemaakt.")
    return vector_db


if __name__ == "__main__":
    build_vector_database()