# Sprint 1 – Workflow Diagram

## Overzicht Research Workflow

```mermaid
flowchart TD
    A[Start] --> B[Student stelt vraag]
    B --> C[Analyseer vraag]
    C --> D[Zoek in semesterspecifieke kennis]
    D --> E{Voldoende informatie?}

    E -- Ja --> F[Genereer antwoord]
    F --> G[Valideer antwoord]
    G --> H{Correct & volledig?}
    H -- Ja --> I[Stuur antwoord naar student]
    H -- Nee --> D

    E -- Nee --> J[Escaleren naar docent]
    J --> K[Docent beantwoordt vraag]
    K --> I

    I --> L[Einde]
```

---

## Uitleg per stap

### 1. Analyse
De vraag wordt geclassificeerd (deadline, inhoud, beoordeling, planning).

### 2. Retrieval
De agent raadpleegt interne bronnen zoals studiewijzers en projectdocumentatie.

### 3. Generatie
Op basis van gevonden informatie genereert het LLM een antwoord.

### 4. Validatie
Controle op:
- Relevantie
- Bronverwijzing
- Volledigheid
- Confidence score

### 5. Escalatie
Bij onvoldoende informatie of lage confidence wordt de vraag doorgestuurd naar de docent.

---

## Technische implicaties voor volgende sprint
- Orchestration nodig
- State management nodig
- Retrieval (RAG) implementatie
- Validatielogica
- Escalatiemechanisme
