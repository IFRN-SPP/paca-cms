from django.contrib import admin
from .models import (
    Publication,
    BackgroundImage,
    Issue,
    Page,
    Document,
    SocialMedia,
    PageAllowedDocumentCategory,
)

admin.site.register(Document)
admin.site.register(SocialMedia)
admin.site.register(BackgroundImage)
admin.site.register(PageAllowedDocumentCategory)
admin.site.register(Page)
admin.site.register(Publication)
admin.site.register(Issue)
