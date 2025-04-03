from django.db import models
from django.core.validators import FileExtensionValidator
from django.conf import settings
from tinymce.models import HTMLField
from autoslug import AutoSlugField
from django.utils.translation import gettext_lazy as _
import os
import pymupdf


class Publication(models.Model):
    title = models.CharField(_("Título"), max_length=100)
    short_title = models.CharField(_("Título curto"), max_length=40)
    logo = models.ImageField(_("Logo"), upload_to="publication/", blank=True)
    logo_mini = models.ImageField(_("Mini-logo"), upload_to="publication/", blank=True)
    promo_image = models.ImageField(
        _("Imagem promocional"), upload_to="publication/", blank=True
    )
    issn = models.CharField(_("ISSN"), max_length=50, blank=True)
    doi = models.CharField(_("DOI"), max_length=50, blank=True)
    organization = models.CharField(_("Instituição"), max_length=100, blank=True)
    address = models.CharField(_("Endereço"), max_length=200, blank=True)
    phone = models.CharField(_("Telefone"), max_length=100, blank=True)
    email = models.EmailField(_("E-mail"), blank=True)
    description = HTMLField(_("Descrição"))
    created_at = models.DateTimeField(_("Data de criação"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Data de atualização"), auto_now=True)

    class Meta:
        verbose_name = _("Publicação")
        verbose_name_plural = _("Publicações")

    def __str__(self):
        return self.short_title


class SocialMedia(models.Model):
    publication = models.ForeignKey(
        Publication, on_delete=models.PROTECT, verbose_name=_("Publicação")
    )
    url = models.URLField(_("URL"))
    icon = models.CharField(_("Ícone"), max_length=100)

    class Meta:
        verbose_name = _("Mídia Social")
        verbose_name_plural = _("Mídias Sociais")

    def __str__(self):
        return self.url


class BackgroundImage(models.Model):
    publication = models.ForeignKey(
        Publication, on_delete=models.PROTECT, verbose_name=_("Publicação")
    )
    order = models.IntegerField(_("Ordem"))
    image = models.ImageField(_("Imagem"), upload_to="background/")

    class Meta:
        verbose_name = _("Imagem de fundo")
        verbose_name_plural = _("Imagens de fundo")
        ordering = ["order"]

    def __str__(self):
        return self.image.url


class Issue(models.Model):
    publication = models.ForeignKey(
        Publication, on_delete=models.PROTECT, verbose_name=_("Publicação")
    )
    title = models.CharField(_("Título"), max_length=20, null=True)
    presentation = HTMLField(_("Apresentação"), blank=True)
    cover = models.ImageField(_("Capa"), upload_to="issue/", blank=True)
    file = models.FileField(
        _("Arquivo"),
        upload_to="issue/",
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=["pdf", "PDF"])],
    )
    created_at = models.DateTimeField(_("Data de criação"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Última modificação"), auto_now=True)
    pub_date = models.DateField(_("Data de publicação"))
    url = models.URLField(_("URL"), blank=True)
    is_published = models.BooleanField(_("Publicado?"), default=False)

    class Meta:
        verbose_name = _("Edição")
        verbose_name_plural = _("Edições")
        ordering = ["-pub_date"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.file and self.file.name.lower().endswith(".pdf"):
            self.generate_cover()

    def generate_cover(self):
        doc = pymupdf.open(self.file.path)
        page = doc[0]
        pix = page.get_pixmap(dpi=72)

        cover_filename = os.path.basename(self.file.name) + ".png"

        if callable(self.cover.field.upload_to):
            upload_path = self.cover.field.upload_to(self, self.cover.name)
        else:
            upload_path = self.cover.field.upload_to

        full_path = os.path.join(settings.MEDIA_ROOT, upload_path)
        cover_path = os.path.join(full_path, cover_filename)

        pix.save(cover_path)

        self.cover.name = f"{upload_path}/{cover_filename}"

        super().save(update_fields=["cover"])


class Page(models.Model):
    class PageType(models.TextChoices):
        DOWNLOADS = "DL", _("Downloads")
        GALLERY = "GL", _("Galeria")
        TEXT = "TX", _("Texto")
        ISSUES = "IS", _("Edições")

    publication = models.ForeignKey(
        Publication, on_delete=models.PROTECT, verbose_name=_("Publicação")
    )
    title = models.CharField(_("Título"), max_length=20)
    order = models.IntegerField(_("Ordem"))
    page_type = models.CharField(_("Tipo de página"), max_length=2, choices=PageType)
    slug = AutoSlugField(populate_from="title", unique=True, default="", null=False)
    created_at = models.DateTimeField(_("Data de criação"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Última modificação"), auto_now=True)
    is_published = models.BooleanField(_("Publicado?"))

    class Meta:
        verbose_name = _("Página")
        verbose_name_plural = _("Páginas")
        ordering = ["order"]

    def __str__(self):
        return self.title


class Text(models.Model):
    page = models.ForeignKey(Page, on_delete=models.PROTECT, verbose_name=_("Página"))
    title = models.CharField(_("Título"), max_length=100, blank=True)
    subtitle = models.CharField(_("Subtítulo"), max_length=100, blank=True)
    order = models.IntegerField(_("Ordem"))
    text = HTMLField(_("Texto"))
    is_published = models.BooleanField(_("Publicado?"))
    created_at = models.DateTimeField(_("Data de criação"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Última modificação"), auto_now=True)

    class Meta:
        verbose_name = _("Texto")
        verbose_name_plural = _("Textos")
        ordering = ["order"]

    def __str__(self):
        return self.title


class Document(models.Model):
    class Category(models.TextChoices):
        RULE = "RULE", _("Norma")
        TEMPLATE = "TEMPLATE", _("Template")
        INFORMATION = "INFORMATION", _("Informação")
        OTHER = "OTHER", _("Outro")

    publication = models.ForeignKey(
        Publication, on_delete=models.PROTECT, verbose_name=_("Publicação")
    )
    title = models.CharField(_("Título"), max_length=100)
    category = models.CharField(_("Categoria"), max_length=11, choices=Category)
    file = models.FileField(_("Arquivo"), upload_to="documents/")
    is_published = models.BooleanField(_("Publicado?"))
    created_at = models.DateTimeField(_("Data de criação"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Última modificação"), auto_now=True)

    class Meta:
        verbose_name = _("Documento")
        verbose_name_plural = _("Documentos")
        ordering = ["title"]

    def __str__(self):
        return self.title


class PageAllowedDocumentCategory(models.Model):
    page = models.ForeignKey(Page, on_delete=models.PROTECT, verbose_name=_("Página"))
    category = models.CharField(
        _("Categoria"), max_length=11, choices=Document.Category
    )

    class Meta:
        verbose_name = _("Categoria de documento permitida")
        verbose_name_plural = _("Categorias de documento permitidas")

    def __str__(self):
        return self.category
