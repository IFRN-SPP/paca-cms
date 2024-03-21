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
        'textap':TextAP, 
        'textctt': TextCTT,
        'anais': Anais,
        'normas': Norma,
        'comission': Comission,
        'editions': Editions
    }
    return render(request, 'index.html', context)