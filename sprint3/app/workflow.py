from app.tools.search_tool import search_knowledge
from app.tools.validation_tool import validate_answer
from app.memory.state_manager import StateManager
from app.logger import log_event

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")
# Lokaal gratis model (openai kostte geld)


memory = StateManager()

def create_answer(question, context):
    prompt = f"""
Beantwoord de vraag kort en duidelijk op basis van de context.
Gebruik maximaal 5 zinnen.

Vraag: {question}

Context: {context}

Antwoord:
"""

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=1024)

    outputs = model.generate(
        **inputs,
        max_new_tokens=200,
        temperature=0.7
    )

    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return answer.strip()

def run_workflow(question):
    state = memory.create_state(question)

    log_event(f"Nieuwe vraag: {question}")

    results = search_knowledge(question, k=3) # van 6 naar 3 gegaan want bij meer chunks= meer herhaling
    context = "\n\n".join([result.page_content for result in results])
    context = context[:1500]

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