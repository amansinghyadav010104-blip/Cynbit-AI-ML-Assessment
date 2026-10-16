import unittest
from lead_intelligence import analyze_inquiry

class LeadIntelligenceTests(unittest.TestCase):
    def test_empty_input(self):
        result = analyze_inquiry("")
        self.assertEqual(result["score"], 0)
        self.assertEqual(result["category"], "Needs manual classification")

    def test_web_and_ai_category(self):
        result = analyze_inquiry("We need an e-commerce website and AI chatbot within six weeks.")
        self.assertIn(result["category"], ["Web / App Development", "AI / ML"])
        self.assertGreater(result["score"], 30)
        self.assertTrue(result["draft"])

    def test_budget_missing_question(self):
        result = analyze_inquiry("We need a website for our business.")
        self.assertTrue(any("budget" in q.lower() for q in result["missing_information"]))

    def test_score_is_bounded(self):
        result = analyze_inquiry("AI chatbot website app cloud aws azure marketing seo budget price urgent within six weeks")
        self.assertGreaterEqual(result["score"], 0)
        self.assertLessEqual(result["score"], 95)

if __name__ == "__main__":
    unittest.main()
