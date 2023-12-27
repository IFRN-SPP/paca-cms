from django.shortcuts import render
from .models import HTMLText, Anal

# Create your views here.
def inicio(request):
    Anais = Anal.objects.all
    TextAP = HTMLText.objects.filter(Nome='Apresentação')
    TextCTT = HTMLText.objects.filter(Nome='Contato')
    context = {
        'TextAP':TextAP, 
        'TextCTT': TextCTT,
        'Anais': Anais
    }
    return render(request, 'index.html', context)