from django import forms
from app.models import *

class Form(forms.ModelForm):
    class Meta:
        model = Artigos
        fields = ('nome', 'area', 'equipe')