from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"
)

def generate_answer_with_llm(question, context):
    try:
        response = client.chat.completions.create(
            model="local-model",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Je bent een Semester 4 AI-Agent voor HBO-ICT studenten. "
                        "Beantwoord de vraag alleen met de gegeven context. "
                        "Als het antwoord niet in de context staat, zeg dan dat je het niet zeker weet. "
                        "Gebruik simpele Nederlandse taal."
                    )
                },
                {
                    "role": "user",
                    "content": f"Vraag van student:\n{question}\n\nContext uit kennisbank:\n{context}"
                }
            ],
            temperature=0.2,
            max_tokens=400
        )

        return response.choices[0].message.content.strip()

    except Exception as error:
        return (
            "De lokale LLM kon niet worden gebruikt. "
            "Controleer of LM Studio aanstaat en of de server draait op localhost:1234.\n\n"
            f"Foutmelding: {error}"
        )