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
                        "Je bent een Semester 4 DEAI AI-Agent voor HBO-ICT studenten. "
                        "De vraag gaat altijd over Semester 4, DEAI, PD3, beoordeling of het AI-Agent project. "
                        "Doe nooit alsof jij zelf student bent. "
                        "Gebruik nooit zinnen zoals: 'ik weet', 'ik heb', 'ik ga studeren' of 'mijn beoordeling'. "
                        "Gebruik alleen de context uit de kennisbank. "
                        "Als het antwoord niet duidelijk in de context staat, zeg dan: "
                        "'Ik kan dit niet vinden in de Semester 4 kennisbank.' "
                        "Antwoord kort, duidelijk en in simpele Nederlandse taal."
                    )
                },
                {
                    "role": "user",
                    "content": (
                        f"Vraag van student:\n{question}\n\n"
                        f"Context uit kennisbank:\n{context}\n\n"
                        "Maak nu een antwoord voor de student. "
                        "Schrijf niet vanuit jezelf, maar over Semester 4."
                    )
                }
            ],
            temperature=0.1,
            max_tokens=300
        )

        return response.choices[0].message.content.strip()

    except Exception as error:
        return (
            "De lokale LLM kon niet worden gebruikt. "
            "Controleer of LM Studio aanstaat en of de server draait op localhost:1234.\n\n"
            f"Foutmelding: {error}"
        )