from django.shortcuts import render
from .models import *

# Create your views here.
def inicio(request):
    Anais = Artigos.objects.all
    Norma = Normas.objects.all
    TextAP = Textos.objects.filter(nome='Apresentação')
    TextCTT = Textos.objects.filter(nome='Contato')
    context = {
        'TextAP':TextAP, 
        'TextCTT': TextCTT,
        'Anais': Anais,
        'Normas': Norma
    }
    return render(request, 'index.html', context)