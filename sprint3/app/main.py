from app.agent import run_agent


if __name__ == "__main__":
    question = input("Stel je vraag: ")

    result = run_agent(question)

    print("\nAntwoord:")
    print(result["answer"])

    print("\nConfidence:")
    print(result["confidence"])

    print("\nStatus:")
    print(result["status"])