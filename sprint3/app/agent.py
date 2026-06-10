from app.workflow import run_workflow


def run_agent(question):
    state = run_workflow(question)

    return {
        "answer": state["answer"],
        "confidence": state["confidence"],
        "status": state["status"]
    }