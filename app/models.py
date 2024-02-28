from django.db import models

# Create your models here.
class Areas(models.Model):
    nome = models.CharField(max_length=60,unique=True,primary_key=True)
    
    class Meta:
        verbose_name = 'Área'
        verbose_name_plural = 'Áreas'
    
    def __str__(self):
        return self.nome
class Artigos(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    area = models.ForeignKey(Areas, on_delete=models.CASCADE)
    equipe = models.CharField(max_length=255, null=False, blank=False)
    
    class Meta:
        verbose_name = 'Artigo'
        verbose_name_plural = 'Anais'
    
    def __str__(self):
        return self.nome
    
class Textos(models.Model):
    titulo = models.CharField(max_length=20, null=False)
    subtitulo = models.CharField(max_length=100, null=False)
    texto = models.TextField(null=False)
    class Meta:
        verbose_name = 'Texto'
        verbose_name_plural = 'Textos'
    
    def __str__(self):
        return self.titulo
    
class Comissao(models.Model):
    nome = models.CharField(max_length=20, null=True)
    
    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Comissão'
    
    def __str__(self):
        return self.nome
    
class Normas(models.Model):
    norma = models.CharField(max_length=20, null=True)
    arquivo = models.FileField()
    
    class Meta:
        verbose_name = 'Norma'
        verbose_name_plural = 'Normas'
    
    def __str__(self):
        return self.norma
    
class Edicoes(models.Model):
    nome = models.CharField(max_length=20, null=True)
    imagem = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    
    class Meta:
        verbose_name = 'Edição'
        verbose_name_plural = 'Edições'
    
    def __str__(self):
        return self.nome