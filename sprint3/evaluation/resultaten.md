# Resultaten Sprint 3

## Test 1 – Deadline ophalen
Vraag:
Wanneer is de deadline van Sprint 3?

Resultaat:
De agent kan de deadline ophalen uit `planning_deadlines.txt`.

Status:
Geslaagd

---

## Test 2 – Projectdoel ophalen
Vraag:
Wat is het doel van de Semester AI-Agent?

Resultaat:
De agent vindt informatie uit `projectomschrijving.txt`.

Status:
Geslaagd

---

## Test 3 – Technologieën ophalen
Vraag:
Welke technologieën gebruiken we?

Resultaat:
De agent vindt Python, LangChain, ChromaDB, HuggingFace embeddings, Streamlit en LM Studio/Qwen.

Status:
Geslaagd

---

## Bevindingen
- De knowledge base wordt ingelezen.
- De documenten worden opgesplitst in chunks.
- Embeddings worden opgeslagen in de vector database.
- De search tool kan relevante informatie terugvinden.

## Verbeterpunten
- Meer documenten toevoegen aan de knowledge base.
- Betere bronverwijzingen tonen.
- Confidence score koppelen aan zoekresultaten.

# Resultaten

## Geteste vragen

1. Wat is DEAI?
2. Wat houdt PD3 in?
3. Wanneer is de Machine Learning niveautest?
4. Hoe wordt Semester 4 beoordeeld?
5. Wat is de leeruitkomst van het AI-Agent project?

## Bevindingen

De agent haalt relevante informatie op uit de Semester 4 knowledge base. De vector database werkt met HuggingFace embeddings en ChromaDB. De workflow bevat retrieval, validatie, confidence score, feedback en logging.

## Verbeterpunten

- Antwoorden korter samenvatten
- Betere bronverwijzing toevoegen
- Webinterface maken met Streamlit