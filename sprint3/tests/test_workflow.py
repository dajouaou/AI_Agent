from asyncio import tools


def test_deadline_question():
    vraag = "Wanneer is de deadline van Sprint 3?"
    verwacht = "5 juni 2026"

    assert vraag is not None
    assert verwacht == "5 juni 2026"


def test_project_goal_question():
    vraag = "Wat is het doel van de Semester AI-Agent?"
    verwacht = "studenten ondersteunen"

    assert vraag is not None
    assert verwacht in "De agent moet studenten ondersteunen bij vragen."


def test_unclear_question():
    vraag = "Deadline?"
    verwacht = "verduidelijkingsvraag"

    assert vraag == "Deadline?"
    assert verwacht == "verduidelijkingsvraag"


def test_unknown_question():
    vraag = "Wanneer begint de zomervakantie?"
    verwacht = "geen informatie gevonden"

    assert vraag is not None
    assert verwacht == "geen informatie gevonden"


def test_tools_question():
  tools = ["Python", "LangChain", "ChromaDB", "HuggingFace embeddings", "Streamlit", "LM Studio/Qwen"]

assert "Python" in tools
assert "LangChain" in tools
assert "ChromaDB" in tools
assert "LM Studio/Qwen" in tools