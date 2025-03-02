from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.conf import settings
from django_summernote.fields import SummernoteTextField
from autoslug import AutoSlugField
import os
import pymupdf


class User(AbstractUser):
    pass


class Publication(models.Model):
    title = models.CharField(max_length=100)
    short_title = models.CharField(max_length=40)
    logo = models.ImageField(upload_to="publication/", blank=True)
    logo_mini = models.ImageField(upload_to="publication/", blank=True)
    promo_image = models.ImageField(upload_to="publication/", blank=True)
    issn = models.CharField(max_length=50, blank=True)
    doi = models.CharField(max_length=50, blank=True)
    organization = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    description = SummernoteTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.short_title


class SocialMedia(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.PROTECT)
    url = models.URLField()
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.url


class BackgroundImage(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.PROTECT)
    order = models.IntegerField()
    image = models.ImageField(upload_to="background/")

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.image.url


class Issue(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.PROTECT)
    title = models.CharField(max_length=20, null=True)
    presentation = SummernoteTextField(blank=True)
    cover = models.ImageField(upload_to="issue/", blank=True)
    file = models.FileField(
        upload_to="issue/",
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=["pdf", "PDF"])],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    pub_date = models.DateField()
    url = models.URLField()

    class Meta:
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
        DOWNLOADS = "DL", "Downloads"
        GALLERY = "GL", "Gallery"
        TEXT = "TX", "Text"
        ISSUES = "IS", "Issues"

    publication = models.ForeignKey(Publication, on_delete=models.PROTECT)
    title = models.CharField(max_length=20)
    order = models.IntegerField()
    page_type = models.CharField(max_length=2, choices=PageType)
    slug = AutoSlugField(populate_from="title", unique=True, default="", null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


class Text(models.Model):
    page = models.ForeignKey(Page, on_delete=models.PROTECT)
    title = models.CharField(max_length=100, blank=True)
    subtitle = models.CharField(max_length=100, blank=True)
    order = models.IntegerField()
    text = SummernoteTextField()
    is_published = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


class Document(models.Model):
    class Category(models.TextChoices):
        RULE = "RULE", "Rule"
        TEMPLATE = "TEMPLATE", "Template"
        INFORMATION = "INFORMATION", "Information"
        OTHER = "OTHER", "Other"

    publication = models.ForeignKey(Publication, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=11, choices=Category)
    file = models.FileField(upload_to="documents/")
    is_published = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class PageAllowedDocumentCategory(models.Model):
    page = models.ForeignKey(Page, on_delete=models.PROTECT)
    category = models.CharField(max_length=11, choices=Document.Category)

    def __str__(self):
        return self.category
