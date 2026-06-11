from app.tools.search_tool import search_knowledge
from app.tools.validation_tool import validate_answer
from app.memory.state_manager import StateManager
from app.logger import log_event
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

memory = StateManager()


def create_answer(question, context):
    prompt = f"""
Je bent een studie-assistent voor Semester 4 (DEAI & PD3).

Beantwoord de vraag zo concreet en specifiek mogelijk.
Gebruik alleen informatie uit de context.
Als het antwoord niet in de context staat, zeg dat duidelijk.

Vraag:
{question}

Context:
{context}

Antwoord:
"""

    response = llm.invoke(prompt)
    return response.content

def run_workflow(question):
    state = memory.create_state(question)

    log_event(f"Nieuwe vraag: {question}")

    results = search_knowledge(question, k=6)
    context = "\n\n".join([result.page_content for result in results])

    # ✅ bronnen verzamelen
    sources = list(set([
        r.metadata.get("source", "Onbekend")
        for r in results
    ]))

    state["retrieved_context"] = context

    validation = validate_answer(question, context)
    state["confidence"] = validation["confidence"]

    if validation["is_valid"]:
        answer = create_answer(question, context)

        # bronnen toevoegen onderaan antwoord
        answer += "\n\n📚 Bronnen: " + ", ".join(sources)

        state["answer"] = answer
        state["status"] = "answered"

    else:
        state["answer"] = (
            "Ik weet dit niet zeker op basis van de beschikbare Semester 4 bronnen. "
            "Stel je vraag specifieker of controleer Brightspace."
        )
        state["status"] = "needs_clarification"

    memory.save_interaction(
        question=question,
        answer=state["answer"],
        confidence=state["confidence"],
        status=state["status"]
    )

    return state