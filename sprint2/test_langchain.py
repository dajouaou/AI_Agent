from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Vector database
db = Chroma(
    persist_directory="data/embeddings",
    embedding_function=embeddings
)

# Lokale LM Studio
llm = ChatOpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",
    model="google/gemma-4-e4b",
    temperature=0.1
)

vraag = "Wat is PD3"

docs = db.similarity_search(vraag, k=3)
print("Aantal gevonden documenten:", len(docs))

for i, doc in enumerate(docs):
    print(f"\nDocument {i+1}:")
    print(doc.page_content)

context = "\n\n".join(doc.page_content for doc in docs)

prompt = ChatPromptTemplate.from_template("""
Gebruik alleen onderstaande context.

Context:
{context}

Vraag:
{question}
""")

chain = prompt | llm

antwoord = chain.invoke({
    "context": context,
    "question": vraag
})

print(antwoord.content)