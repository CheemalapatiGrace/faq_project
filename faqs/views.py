from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import FAQ

@api_view(['GET'])
def faq_list(request):
    lang = request.GET.get('lang', 'en')
    faqs = FAQ.objects.all()
    faq_data = []
    for faq in faqs:
        question = getattr(faq, f'question_{lang}', faq.question)
        faq_data.append({'question': question, 'answer': faq.answer})
    return Response(faq_data)

