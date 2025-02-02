import pytest
from .models import FAQ

@pytest.mark.django_db
def test_faq_translation():
    faq = FAQ.objects.create(question="What is Django?", answer="Django is a high-level Python web framework that enables rapid development of secure and maintainable websites")
    assert faq.get_translated_question('hi') == "What is Django?"