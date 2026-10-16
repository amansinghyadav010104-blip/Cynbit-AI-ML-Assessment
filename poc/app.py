import streamlit as st
from lead_intelligence import analyze_inquiry

st.set_page_config(page_title="Cynbit Lead Intelligence PoC", page_icon="🎯", layout="centered")
st.title("Cynbit Lead Intelligence Assistant")
st.caption("Functional PoC · local rules · synthetic/sample inputs recommended")

st.info(
    "This demo uses keyword rules and an illustrative heuristic score. "
    "The score is not a trained model or a probability of conversion. "
    "Nothing is saved, sent, or connected to Cynbit's systems."
)

examples = {
    "E-commerce + chatbot": "We need an e-commerce website with payment integration and an AI customer-support chatbot. We want to launch within six weeks. Please share the process and estimated cost.",
    "Cloud migration": "Our team needs help migrating our application to AWS next month. Please provide an estimate and explain the migration process.",
    "Marketing": "We are looking for SEO and digital marketing support for our new campaign. We have a budget of INR 50000 and want to start next week.",
    "Custom inquiry": ""
}
chosen = st.selectbox("Load a sample inquiry", list(examples.keys()))
default_text = examples[chosen]
inquiry = st.text_area("Customer inquiry", value=default_text, height=160,
                       placeholder="Paste a business inquiry here (avoid sensitive personal data).")

if st.button("Analyze inquiry", type="primary", use_container_width=True):
    result = analyze_inquiry(inquiry)
    st.session_state["analysis_result"] = result

result = st.session_state.get("analysis_result")
if result:
    st.divider()
    st.subheader("Analysis")
    c1, c2 = st.columns(2)
    c1.metric("Priority indicator", f'{result["score"]}/100')
    c2.metric("Service category", result["category"])
    st.caption(result["priority"] + " — illustrative heuristic only; not a conversion prediction.")

    st.markdown("**Why this score?**")
    for reason in result["score_explanation"]:
        st.write(f"- {reason}")

    st.markdown("**Detected service areas**")
    st.write(", ".join(result["matched_services"]) if result["matched_services"] else "No clear match; manual review recommended.")

    st.markdown("**Clarification questions / next steps**")
    for question in result["missing_information"]:
        st.write(f"- {question}")

    st.markdown("**Email draft for human review**")
    st.text_area("Draft (edit before use)", value=result["draft"], height=220, key="draft_output")
    st.download_button("Download draft as TXT", data=result["draft"],
                       file_name="cynbit_followup_draft.txt", mime="text/plain")

st.divider()
st.caption("Before production: validate with Cynbit stakeholders, approved data, offline evaluation, security review, and human approval.")
