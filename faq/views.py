# views.py
from rest_framework import viewsets
from .models import FAQ
from .serializers import FAQSerializer
from translate import Translator

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def perform_create(self, serializer):
        # Automatically translate question and answer during creation
        instance = serializer.save()

        translator_hi = Translator(to_lang="hi")
        translator_bn = Translator(to_lang="bn")
        translator_kn = Translator(to_lang="kn")
        translator_te = Translator(to_lang="te")
        translator_ta = Translator(to_lang="ta") 
        
        if not instance.question_hi:
            instance.question_hi = translator_hi.translate(instance.question)
        if not instance.question_bn:
            instance.question_bn = translator_bn.translate(instance.question)
        if not instance.question_ka:
            instance.question_ka = translator_kn.translate(instance.question)
        if not instance.question_te:
            instance.question_te = translator_te.translate(instance.question)
        if not instance.question_ta:
            instance.question_ta = translator_ta.translate(instance.question)

        if not instance.answer_hi:
            instance.answer_hi = translator_hi.translate(instance.answer)
        if not instance.answer_bn:
            instance.answer_bn = translator_bn.translate(instance.answer)
        if not instance.answer_kn:
            instance.answer_kn = translator_kn.translate(instance.answer)
        if not instance.answer_te:
            instance.answer_te = translator_te.translate(instance.answer)
        if not instance.answer_ta:
            instance.answer_ = translator_ta.translate(instance.answer)

        instance.save()