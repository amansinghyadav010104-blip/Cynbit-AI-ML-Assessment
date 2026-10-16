CYNBIT AI/ML DELIVERABLES
1. AI_Opportunity_Report.docx / .md — industry opportunity analysis and prioritization.
2. Technical_Approach_Report.docx / .md — architecture, model choices, data, prompt strategy, evaluation, security, execution plan.
3. poc/ — Streamlit demo, reusable Python logic, synthetic sample inquiries, requirements, tests, and run instructions.

Run:
  cd poc
  pip install -r requirements.txt
  streamlit run app.py

Test:
  python -m unittest test_lead_intelligence.py

Limitations:
This is a local rules-based PoC, not a production system, trained conversion model, or live Cynbit integration. It does not store input or send messages. Verify public-company details and validate the use case with Cynbit before presenting claims as measured facts.
