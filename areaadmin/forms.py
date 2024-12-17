from django import forms
from app.models import Artigos


class Form(forms.ModelForm):
    class Meta:
        model = Artigos
        fields = ("nome", "area", "equipe")
