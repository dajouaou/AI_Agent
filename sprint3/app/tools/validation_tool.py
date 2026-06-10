from app.config import CONFIDENCE_THRESHOLD


def validate_answer(question, context):
    question_lower = question.lower()
    context_lower = context.lower()

    confidence = 0
    reasons = []

    if not context or len(context.strip()) < 30:
        return {
            "is_valid": False,
            "confidence": 0,
            "reasons": ["Geen bruikbare context gevonden."]
        }

    important_words = [
        word for word in question_lower.split()
        if len(word) > 3
    ]

    matches = sum(1 for word in important_words if word in context_lower)

    if matches >= 3:
        confidence += 50
        reasons.append("Meerdere woorden uit de vraag komen terug in de context.")
    elif matches == 2:
        confidence += 35
        reasons.append("Enkele woorden uit de vraag komen terug in de context.")
    elif matches == 1:
        confidence += 15
        reasons.append("Weinig overlap tussen vraag en context.")
    else:
        confidence += 0
        reasons.append("Geen duidelijke overlap tussen vraag en context.")

    semester_terms = [
        "deai",
        "pd3",
        "boulder",
        "niveautest",
        "portfolio",
        "ai-agent",
        "machine learning",
        "neuraal",
        "data engineering",
        "beoordeling"
    ]

    if any(term in context_lower for term in semester_terms):
        confidence += 20
        reasons.append("Semester 4 termen gevonden.")

    # Belangrijke check: vraagt student naar persoonlijke info?
    personal_terms = [
        "mijn cijfer",
        "mijn beoordeling",
        "mijn datapunt",
        "ben ik geslaagd",
        "heb ik gehaald",
        "mijn aanwezigheid",
        "mijn portfolio goed"
    ]

    if any(term in question_lower for term in personal_terms):
        confidence = 20
        reasons.append("Persoonlijke beoordeling kan niet betrouwbaar worden beantwoord.")

    # Check voor vragen buiten scope
    out_of_scope_terms = [
        "weer",
        "voetbal",
        "recept",
        "vakantie",
        "trein",
        "geld",
        "crypto",
        "belasting"
    ]

    if any(term in question_lower for term in out_of_scope_terms):
        confidence = 10
        reasons.append("Vraag valt buiten de Semester 4 kennisbank.")

    confidence = min(confidence, 100)

    return {
        "is_valid": confidence >= CONFIDENCE_THRESHOLD,
        "confidence": confidence,
        "reasons": reasons
    }