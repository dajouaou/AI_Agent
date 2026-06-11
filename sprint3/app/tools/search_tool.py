from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

EMBEDDINGS_PATH = "data/embeddings"


def search_knowledge(query, k=3):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_db = Chroma(
    persist_directory=EMBEDDINGS_PATH,
    embedding_function=embeddings,
    collection_name="semester4"
)

    results = vector_db.similarity_search_with_score(query, k=k)

    return [doc for doc, score in results]


if __name__ == "__main__":
    vraag = "Wanneer is deadline van Sprint 1?"

    resultaten = search_knowledge(vraag)

    for resultaat in resultaten:
        print(resultaat.page_content)
        print("-" * 50)