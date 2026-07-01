from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

EMBEDDINGS_PATH = "data/embeddings"

##stap 4 workflow
def search_knowledge(query, k=3):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
##stap 5 workflow
    vector_db = Chroma(
        persist_directory=EMBEDDINGS_PATH,
        embedding_function=embeddings
    )

    results = vector_db.similarity_search(query, k=k)

    return results


if __name__ == "__main__":
    vraag = "Wanneer is deadline van Sprint 1?"
##stap 3 workflow
    resultaten = search_knowledge(vraag)

    for resultaat in resultaten:
        print(resultaat.page_content)
        print("-" * 50)