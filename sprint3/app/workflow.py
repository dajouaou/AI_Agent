from app.tools.search_tool import search_knowledge
from app.tools.validation_tool import validate_answer
from app.memory.state_manager import StateManager
from app.logger import log_event

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-large")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-large")
# Lokaal gratis model (openai kostte geld)


memory = StateManager()

def create_answer(question, context):
    # Neem alleen eerste relevante stuk
    context = context.strip()

    # Splits in zinnen
    sentences = context.split(". ")

    # Pak maximaal 5 duidelijke zinnen
    clean_sentences = sentences[:5]

    answer = ". ".join(clean_sentences)

    # Zorg dat het eindigt met punt
    if not answer.endswith("."):
        answer += "."

    return answer

def run_workflow(question):
    state = memory.create_state(question)

    log_event(f"Nieuwe vraag: {question}")

    results = search_knowledge(question, k=3) # van 6 naar 3 gegaan want bij meer chunks= meer herhaling
    context = "\n\n".join([result.page_content for result in results])
    context = context[:800]

    # bronnen verzamelen
    sources = list(set([
        r.metadata.get("source", "Onbekend")
        for r in results
    ]))

    state["retrieved_context"] = context

    validation = {"is_valid": True, "confidence": 80}
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