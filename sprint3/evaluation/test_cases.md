# Test Cases Semester AI-Agent

## Test 1 – Deadline ophalen

### Vraag
Wanneer is de deadline van Sprint 3?

### Verwacht resultaat
De AI-Agent geeft als antwoord:
"De deadline van Sprint 3 is 5 juni 2026."

### Doel
Controleren of de agent informatie correct uit de knowledge base kan ophalen.

---

## Test 2 – Projectinformatie ophalen

### Vraag
Wat is het doel van de Semester AI-Agent?

### Verwacht resultaat
De AI-Agent legt uit dat het project gericht is op het ondersteunen van studenten bij vragen over lesmateriaal, opdrachten en deadlines.

### Doel
Controleren of de agent projectinformatie correct kan terugvinden.

---

## Test 3 – Onduidelijke vraag

### Vraag
Deadline?

### Verwacht resultaat
De AI-Agent stelt een verduidelijkingsvraag, bijvoorbeeld:
"Van welke sprint of opdracht wil je de deadline weten?"

### Doel
Controleren of de workflow om extra context vraagt bij onduidelijke input.

---

## Test 4 – Vraag buiten de knowledge base

### Vraag
Wanneer begint de zomervakantie?

### Verwacht resultaat
De AI-Agent geeft aan dat hierover geen betrouwbare informatie beschikbaar is in de knowledge base.

### Doel
Controleren hoe de agent omgaat met ontbrekende informatie.

---

## Test 5 – Technologieën van het project

### Vraag
Welke technologieën worden gebruikt binnen dit project?

### Verwacht resultaat
De AI-Agent noemt:
- Python
- LangChain
- ChromaDB
- HuggingFace embeddings
- Streamlit
- LM Studio/Qwen

### Doel
Controleren of de agent meerdere relevante gegevens uit documenten kan combineren.