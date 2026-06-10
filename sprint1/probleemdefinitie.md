# Sprint 1 – Probleemdefinitie

## 1. Context
Binnen het HBO-ICT onderwijs worden studenten regelmatig verwezen naar generieke AI-tools zoals ChatGPT en GitHub Copilot voor ondersteuning bij vragen over lesstof, projecten en deadlines. Deze tools zijn echter niet afgestemd op één specifieke opleiding, semester of module.

## 2. Probleemstelling
Generieke AI-tools beschikken niet over semesterspecifieke context. Hierdoor:

- Ontstaan misverstanden over opdrachtvereisten
- Worden onvolledige of foutieve antwoorden gegenereerd
- Ontbreken concrete verwijzingen naar studiewijzers, beoordelingsrubrics en deadlines
- Hebben docenten geen controle over de juistheid van gegeven antwoorden

Dit leidt tot inefficiëntie, extra vragen aan docenten en mogelijke studievertraging.

## 3. Doelstelling
Het ontwikkelen van een gespecialiseerde Semester AI-Agent die:

- Alle vragen over één specifiek semester kan beantwoorden
- Gebruikmaakt van goedgekeurde semesterspecifieke kennisbronnen
- Antwoorden valideert op relevantie en volledigheid
- Indien nodig automatisch escaleert naar een docent

## 4. Scope en Afbakening
### Binnen scope
- Eén specifiek HBO-ICT semester
- Informatie-output (uitleg, verwijzing, verduidelijking)
- Gebruik van interne bronnen zoals:
  - Studiewijzers (PDF)
  - Brightspace content
  - Projectdocumentatie
  - Beoordelingsrubrics
  - Planning en deadlines
  - Veelgestelde vragen van docenten

### Buiten scope
- Automatische cijferverwerking
- Volledig autonoom beoordelingssysteem
- Gebruik van ongecontroleerde externe AI-platformen

## 5. Validatie en Kwaliteitscontrole
De AI-Agent valideert antwoorden door:

- Controle op aanwezigheid van bronverwijzing
- Controle op relevantie ten opzichte van de vraag
- Controle op volledigheid (bijv. deadline + locatie + beoordelingscriteria)
- Confidence-indicator (laag → escalatie)

Indien onvoldoende zekerheid: automatische melding naar docent.

## 6. Privacy & AVG
- Geen opslag van persoonsgegevens
- Logging zonder student-ID
- Alleen gebruik van goedgekeurde onderwijsbronnen
- Data blijft binnen schoolomgeving

## 7. Verwachte Impact
- Minder repetitieve vragen aan docenten
- Consistente en gecontroleerde informatievoorziening
- Snellere ondersteuning voor studenten
- Betere studievoortgang

## 8. Workflow-type
Research workflow

## 9. Outputtype
Informatie-output (antwoord, uitleg, verwijzing of escalatie)
