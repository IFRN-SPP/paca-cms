from django.db import models

# Create your models here.
class HTMLText(models.Model):
    Nome = models.CharField(max_length=20, null=True)
    Título = models.CharField(max_length=20, null=False)
    Subtítulo = models.CharField(max_length=100, null=False)
    Texto = models.TextField(null=False)

    def __str__(self):
        return self.Nome

class Anal(models.Model):
    AREA_CHOICES = (
        ('LINGUAGENS, CÓDIGOS E SUAS TECNOLOGIAS', 'LINGUAGENS, CÓDIGOS E SUAS TECNOLOGIAS'),
        ('CIÊNCIAS HUMANAS, SOCIAIS APLICADAS E SUAS TECNOLOGIAS', 'CIÊNCIAS HUMANAS, SOCIAIS APLICADAS E SUAS TECNOLOGIAS'),
        ('CIÊNCIAS DA NATUREZA E SUAS TECNOLOGIAS', 'CIÊNCIAS DA NATUREZA E SUAS TECNOLOGIAS'),
        ('MEIO AMBIENTE E SUAS TECNOLOGIAS', 'MEIO AMBIENTE E SUAS TECNOLOGIAS'),
        ('EDIFICAÇÕES E SUAS TECNOLOGIAS', 'EDIFICAÇÕES E SUAS TECNOLOGIAS'),
        ('INFORMÁTICA PARA INTERNET E SUAS TECNOLOGIAS', 'INFORMÁTICA PARA INTERNET E SUAS TECNOLOGIAS'),
        ('MATEMÁTICA E SUAS TECNOLOGIAS', 'MATEMÁTICA E SUAS TECNOLOGIAS')
    )
    
    Nome = models.CharField(max_length=100, null=False, blank=False)
    Área = models.CharField(max_length=55, choices=AREA_CHOICES, blank=False, null=False)
    Equipe = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return self.Nome    