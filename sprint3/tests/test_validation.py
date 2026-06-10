from app.tools.validation_tool import validate_answer

def test_valid_answer():
    result = validate_answer(
        "Wat is DEAI?",
        "DEAI is onderdeel van Semester 4. DEAI gaat over Data Engineering, AI, machine learning, niveautests, portfolio en AI-agent ontwikkeling."
    )
    assert result["confidence"] >= 70
    assert result["is_valid"] is True

def test_empty_answer():
    result = validate_answer("Wat is DEAI?", "")
    assert result["is_valid"] is False