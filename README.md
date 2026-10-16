# Cynbit AI/ML Engineer Intern Assessment

## Project Overview
This project explores an AI/ML opportunity for Cynbit and provides a proof of concept for lead intelligence and follow-up assistance.

The prototype accepts inquiry details and produces:
- Suggested service category
- Heuristic priority score
- Missing information and clarification questions
- Draft follow-up email for human review

**Note:** The current prototype uses rule-based logic. The priority score is a heuristic indicator, not a validated conversion probability. The application does not automatically send emails or connect to a production CRM.

## Deliverables
- `AI_Opportunity_Report.docx` — AI opportunity analysis
- `Technical_Approach_Report.docx` — technical architecture and execution plan
- `poc/` — Streamlit application, logic, tests, and setup instructions

## Run the Application

Open PowerShell in the project root and run:

```powershell
cd poc
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run app.py
```

## Run Tests

Run from the `poc` directory:

```powershell
python -m unittest test_lead_intelligence.py -v
```

## Limitations
This is a rule-based demonstration prototype using local/sample input. It has not been validated as a production lead-scoring model, does not connect to a production CRM, and does not automatically send emails. Human review is required before any real-world communication.