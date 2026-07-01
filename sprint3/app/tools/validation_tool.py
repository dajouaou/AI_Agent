from app.config import CONFIDENCE_THRESHOLD

##stap 7 workflow
def validate_answer(question, context):
    question_lower = question.lower()
    context_lower = context.lower()

    if not context or len(context.strip()) < 20:
        return {
            "is_valid": False,
            "confidence": 0,
            "reasons": ["Geen context gevonden."]
        }

    confidence = 30

    important_words = [
        word.strip(".,?!")
        for word in question_lower.split()
        if len(word.strip(".,?!")) > 2
    ]

    matches = sum(1 for word in important_words if word in context_lower)
    confidence += min(matches * 15, 40)
    semester_terms = [
        "deai",
        "pd3",
        "semester",
        "niveautest",
        "machine learning",
        "data engineering",
        "ai-agent",
        "beoordeling",
        "portfolio",
        "etl"
    ]
    if any(term in context_lower for term in semester_terms):
        confidence += 30

    personal_terms = [
        "mijn cijfer",
        "ben ik geslaagd",
        "heb ik gehaald",
        "mijn beoordeling"
    ]

    if any(term in question_lower for term in personal_terms):
        confidence = 20

    confidence = min(confidence, 100)

    return {
        "is_valid": confidence >= CONFIDENCE_THRESHOLD,
        "confidence": confidence,
        "reasons": []
    }