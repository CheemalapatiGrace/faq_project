from django.test import TestCase
from .models import FAQ

class FAQModelTest(TestCase):
    def test_translation(self):
        faq = FAQ.objects.create(question="What is Django?", answer="A Python framework")
        faq.translate_question()
        self.assertIsNotNone(faq.question_hi)

