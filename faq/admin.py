from django.contrib import admin
from .models import FAQ
from translate import Translator

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'language', 'question_hi', 'question_bn', 'question_kn', 'question_te', 'question_ta','answer_hi','answer_bn','answer_kn','answer_te','answer_ta')    
    list_filter = ('language',)
    search_fields = ('question', 'answer')

    def save_model(self, request, obj, form, change):
        # Translate the question to Hindi and Bengali if not provided
        if not obj.question_hi:
            translator = Translator(to_lang="hi")
            obj.question_hi = translator.translate(obj.question)
        if not obj.question_bn:
            translator = Translator(to_lang="bn")
            obj.question_bn = translator.translate(obj.question)
        if not obj.question_kn:
            translator = Translator(to_lang="kn")
            obj.question_kn = translator.translate(obj.question)
        if not obj.question_te:
            translator = Translator(to_lang="te")
            obj.question_te = translator.translate(obj.question)
        if not obj.question_ta:
            translator = Translator(to_lang="ta")
            obj.question_ta = translator.translate(obj.question)
        
        if not obj.answer_hi:
            translator = Translator(to_lang="hi")
            obj.answer_hi = translator.translate(obj.answer)
        if not obj.answer_bn:
            translator = Translator(to_lang="bn")
            obj.answer_bn = translator.translate(obj.answer)
        if not obj.answer_kn:
            translator = Translator(to_lang="kn")
            obj.answer_kn = translator.translate(obj.answer)
        if not obj.answer_te:
            translator = Translator(to_lang="te")
            obj.answer_te = translator.translate(obj.answer)
        if not obj.answer_ta:
            translator = Translator(to_lang="ta")
            obj.answer_ta = translator.translate(obj.answer)
             
        super().save_model(request, obj, form, change)