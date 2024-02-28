from django.shortcuts import render
from .models import *

# Create your views here.
def inicio(request):
    Anais = Artigos.objects.all
    Norma = Normas.objects.all
    Comission = Comissao.objects.all
    Editions = Edicoes.objects.all
    TextAP = Textos.objects.filter(titulo='Apresentação')
    TextCTT = Textos.objects.filter(titulo='Contato')
    context = {
        'TextAP':TextAP, 
        'TextCTT': TextCTT,
        'Anais': Anais,
        'Normas': Norma,
        'Comission': Comission,
        'Editions': Editions
    }
    return render(request, 'index.html', context)