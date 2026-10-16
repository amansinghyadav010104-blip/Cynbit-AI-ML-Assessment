# Cynbit AI Lead Intelligence Assistant — PoC

This repository contains a local, rules-based demo of an AI-assisted lead qualification workflow.

## Features
- Service category classification using transparent keyword rules
- Illustrative priority score (not a conversion probability)
- Missing-information prompts
- Follow-up email draft for human review
- Streamlit interface
- Unit tests

## Requirements
Python 3.10+ recommended.

## Run locally
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

## Run tests
```bash
python -m unittest test_lead_intelligence.py
```

## Safety and limitations
- Uses sample/local input only; no external LLM, CRM, or email integration.
- Does not save input or send messages.
- Keyword classification can be wrong.
- The score is a transparent demonstration heuristic, not a trained model or calibrated likelihood of conversion.
- Human review is required before any real-world communication.
- Do not paste sensitive customer data into demos without authorization.

## Project files
- `app.py`: Streamlit UI
- `lead_intelligence.py`: reusable analysis logic
- `test_lead_intelligence.py`: unit tests
- `sample_inquiries.json`: synthetic examples
- `AI_Opportunity_Report.docx`: business opportunity report
- `Technical_Approach_Report.docx`: implementation and evaluation approach
