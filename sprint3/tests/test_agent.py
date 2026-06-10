from app.agent import run_agent

def test_agent_returns_answer():
    result = run_agent("Wat is DEAI?")
    assert "answer" in result
    assert "confidence" in result
    assert "status" in result

def test_agent_confidence_is_number():
    result = run_agent("Wat is PD3?")
    assert isinstance(result["confidence"], int)

def test_agent_status_exists():
    result = run_agent("Hoe wordt semester 4 beoordeeld?")
    assert result["status"] in ["answered", "needs_clarification"]