"""Transparent baseline logic for the Cynbit Lead Intelligence Assistant PoC."""
import re
from typing import Dict, List, Any

SERVICE_KEYWORDS = {
    "AI / ML": ["ai", "machine learning", "chatbot", "automation", "llm", "agent"],
    "Web / App Development": ["website", "web app", "mobile app", "e-commerce", "ecommerce", "payment", "application"],
    "Cloud / Infrastructure": ["aws", "azure", "cloud", "migration", "server", "infrastructure"],
    "Marketing / SEO": ["marketing", "seo", "advertising", "campaign", "leads", "social media"],
    "Training / Education": ["training", "course", "mentorship", "learn", "workshop"],
}

def analyze_inquiry(inquiry: str) -> Dict[str, Any]:
    """Analyze an inquiry using simple rules. Score is not a conversion probability."""
    text = (inquiry or "").strip()
    low = text.lower()
    if not text:
        return {
            "category": "Needs manual classification",
            "score": 0,
            "priority": "Insufficient information",
            "matched_services": [],
            "missing_information": ["Please enter an inquiry."],
            "draft": "",
            "score_explanation": ["No inquiry text supplied."],
        }

    service_counts = {
        category: sum(1 for keyword in keywords if keyword in low)
        for category, keywords in SERVICE_KEYWORDS.items()
    }
    matched = sorted(
        [(name, count) for name, count in service_counts.items() if count > 0],
        key=lambda item: (-item[1], item[0])
    )
    category = matched[0][0] if matched else "Needs manual classification"

    timeline_present = bool(re.search(
        r"\b(urgent|asap|within \d+ days?|within \d+ weeks?|this month|deadline|six weeks|next week)\b",
        low
    ))
    budget_present = bool(re.search(r"(₹|\binr\b|\brs\.?\b|\$|\bbudget\b|\bcost\b|\bprice\b)", low))
    scope_present = bool(re.search(
        r"\b(we need|we want|looking for|need a|require|launch|build|develop|create)\b", low
    ))

    score = 30
    explanations: List[str] = []
    if matched:
        score += 15
        explanations.append("Service-related terms detected (+15).")
    keyword_hits = sum(count for _, count in matched)
    if keyword_hits:
        points = min(20, keyword_hits * 5)
        score += points
        explanations.append(f"{keyword_hits} service keyword match(es) (+{points}).")
    if timeline_present:
        score += 15
        explanations.append("Timeline/urgency signal detected (+15).")
    if budget_present:
        score += 10
        explanations.append("Budget/cost mentioned (+10).")
    if scope_present:
        score += 5
        explanations.append("Requirement intent detected (+5).")
    score = min(95, score)
    priority = "High (heuristic)" if score >= 70 else "Medium (heuristic)" if score >= 50 else "Low (heuristic)"

    missing = []
    if not budget_present:
        missing.append("What is your approximate budget range?")
    if not timeline_present:
        missing.append("What is your preferred delivery date?")
    if not re.search(r"\b(features|integrations|requirements|product catalogue|users|customers)\b", low):
        missing.append("Could you share the key features and integrations required?")
    if not missing:
        missing.append("Confirm the scope and success criteria before preparing a proposal.")

    questions = []
    if not budget_present:
        questions.append("your approximate budget")
    if not timeline_present:
        questions.append("your expected timeline")
    questions.append("the key features and integrations you require")
    question_text = ", ".join(questions)

    draft = (
        "Hi,\n\n"
        "Thank you for contacting Cynbit Technologies. We'd be happy to understand your "
        "requirements and explore a suitable solution.\n\n"
        f"To prepare a more accurate proposal, could you share {question_text}?\n\n"
        "Once we have these details, our team can review the scope and discuss the next steps.\n\n"
        "Best regards,\nCynbit Technologies"
    )

    return {
        "category": category,
        "score": score,
        "priority": priority,
        "matched_services": [name for name, _ in matched],
        "missing_information": missing,
        "draft": draft,
        "score_explanation": explanations or ["No service keywords matched; manual review recommended."],
    }
