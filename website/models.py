from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class UsuarioAutorizado(models.Model):
    class FuncaoUsuario(models.TextChoices):
        LEITOR = "LE", "Leitor"
        EDITOR = "ED", "Editor"
        ADMIN = "AD", "Administrador"

    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    funcao = models.CharField(max_length=2, default=FuncaoUsuario.LEITOR)


class Evento(models.Model):
    nome = models.CharField(max_length=100)
    nome_curto = models.CharField(max_length=40)
    logo = models.ImageField()
    issn = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_curto


class Pagina(models.Model):
    class TipoPagina(models.TextChoices):
        DOWNLOADS = "DL", "Downloads"
        GALERIA = "GR", "Galeria"
        TEXTO = "TX", "Texto"

    titulo = models.CharField(max_length=20)
    ordem = models.IntegerField()
    tipo = models.CharField(max_length=2, choices=TipoPagina, default=TipoPagina.TEXTO)
    evento = models.ForeignKey(Evento, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Página"
        verbose_name_plural = "Páginas"

    def __str__(self):
        return self.titulo


class Texto(models.Model):
    titulo = models.CharField(max_length=20, null=False)
    subtitulo = models.CharField(max_length=100, null=False)
    texto = models.TextField()
    ordem = models.IntegerField()
    pagina = models.ForeignKey(Pagina, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Texto"
        verbose_name_plural = "Textos"

    def __str__(self):
        return self.titulo


class Edicao(models.Model):
    nome = models.CharField(max_length=20, null=True)
    capa = models.ImageField()
    documento = models.FileField()
    data_publicacao = models.DateField()

    class Meta:
        verbose_name = "Edição"
        verbose_name_plural = "Edições"

    def __str__(self):
        return self.nome
