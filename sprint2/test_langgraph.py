from typing import TypedDict

from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Lokale LLM
llm = ChatOpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",
    model="google/gemma-4-e4b",
    temperature=0.1
)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory="data/embeddings",
    embedding_function=embeddings
)

class State(TypedDict):
    question: str
    context: str
    answer: str

def retrieve(state):
    docs = db.similarity_search(state["question"], k=3)
    state["context"] = "\n\n".join(doc.page_content for doc in docs)
    return state

def generate(state):
    response = llm.invoke(f"""
Gebruik alleen deze context.

Context:
{state["context"]}

Vraag:
{state["question"]}
""")

    state["answer"] = response.content
    return state

builder = StateGraph(State)

builder.add_node("retrieve", retrieve)
builder.add_node("generate", generate)

builder.add_edge(START, "retrieve")
builder.add_edge("retrieve", "generate")
builder.add_edge("generate", END)

graph = builder.compile()

result = graph.invoke({
    "question": "Wat is DEAI?",
    "context": "",
    "answer": ""
})

print(result["answer"])

# START --> RETRIEVE --> GENERATE --> END
