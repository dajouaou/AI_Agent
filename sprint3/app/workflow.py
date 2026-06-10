from app.tools.search_tool import search_knowledge
from app.tools.validation_tool import validate_answer
from app.memory.state_manager import StateManager
from app.logger import log_event

memory = StateManager()


def create_answer(context):
    return (
        "Op basis van de Semester 4 kennisbank:\n\n"
        f"{context}\n\n"
        "Controleer belangrijke deadlines altijd ook in Brightspace."
    )


def run_workflow(question):
    state = memory.create_state(question)

    log_event(f"Nieuwe vraag: {question}")

    results = search_knowledge(question, k=3)
    context = "\n\n".join([result.page_content for result in results])

    state["retrieved_context"] = context

    validation = validate_answer(question, context)

    state["confidence"] = validation["confidence"]

    if validation["is_valid"]:
        state["answer"] = create_answer(context)
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