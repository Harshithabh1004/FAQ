from django.db import models
from django.core.cache import cache
from ckeditor.fields import RichTextField

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()  # WYSIWYG editor support
    language = models.CharField(max_length=10, default='en')  # Language code (e.g., 'en', 'hi', 'bn','kn','te','ta')

    question_hi = models.TextField(blank=True, null=True)  # Hindi
    question_bn = models.TextField(blank=True, null=True)  # Bengali
    question_kn = models.TextField(blank=True, null=True)  # Kannada
    question_te = models.TextField(blank=True, null=True)  # Telugu
    question_ta = models.TextField(blank=True, null=True)  # Tamil
    answer_hi = RichTextField(blank=True, null=True)  # Hindi
    answer_bn = RichTextField(blank=True, null=True)  # Bengali
    answer_kn = RichTextField(blank=True, null=True)  # Kannada
    answer_te = RichTextField(blank=True, null=True)  # Telugu
    answer_ta = RichTextField(blank=True, null=True)  # Tamil

    def get_translated_text(self, field, lang='en'):
        """Retrieve translated text dynamically for a given field."""
        cache_key = f'faq_{self.id}_{field}_{lang}'
        cached_text = cache.get(cache_key)
        if cached_text:
            return cached_text

        # Fetch the translation
        translated_field = f"{field}_{lang}"
        translated_text = getattr(self, translated_field, None)
        if translated_text:
            # Cache the translation
            cache.set(cache_key, translated_text, timeout=60 * 60)  # Cache for 1 hour
            return translated_text

        # Fallback to english
        return getattr(self, field)

    def get_translated_question(self, lang='en'):
       
        return self.get_translated_text('question', lang)

    def get_translated_answer(self, lang='en'):
        
        return self.get_translated_text('answer', lang)

    def __str__(self):
        return self.question