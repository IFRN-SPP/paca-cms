from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator


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
    description = models.TextField()
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
    presentation = models.TextField(blank=True)
    cover = models.ImageField(upload_to="issue/", blank=True)
    document = models.FileField(
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
    slug = models.SlugField(default="", null=False)
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
    text = models.TextField()
    is_published = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


class Document(models.Model):
    class DocumentType(models.TextChoices):
        RULE = "RULE", "Rule"
        TEMPLATE = "TEMPLATE", "Template"
        ISSUE = "ISSUE", "Issue"
        INFORMATION = "INFORMATION", "Information"
        OTHER = "OTHER", "Other"

    publication = models.ForeignKey(Publication, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    document_type = models.CharField(max_length=11, choices=DocumentType)
    file = models.FileField(upload_to="documents/")
    is_published = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["title"]
