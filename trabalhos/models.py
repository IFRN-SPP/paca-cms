from django.db import models
from homepage.models import Evento


class Area(models.Model):
    nome = models.CharField(max_length=60, unique=True)
    nome_curto = models.CharField(max_length=30, blank=True)
    evento = models.ForeignKey(Evento, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Área"
        verbose_name_plural = "Áreas"

    def __str__(self):
        return self.nome


class TipoTrabalho(models.Model):
    tipo = models.CharField(max_length=200)


class Trabalho(models.Model):
    titulo = models.CharField(max_length=200)
    resumo = models.TextField()
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    evento = models.ForeignKey(Evento, on_delete=models.PROTECT)
    evento = models.ForeignKey(TipoTrabalho, on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo


class Instituicao(models.Model):
    nome = models.CharField(max_length=200)
    sigla = models.CharField(max_length=100)


class Autor(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    instituicao = models.ForeignKey(Instituicao, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


class ChaveCitacao(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    chave = models.CharField(max_length=200)


class AutorTrabalho(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT)
    trabalho = models.ForeignKey(Trabalho, on_delete=models.PROTECT)
    ordem = models.IntegerField()


# Create your models here.
