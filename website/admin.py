from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin, SummernoteModelAdminMixin
from .models import (
    User,
    Publication,
    Issue,
    Page,
    Text,
    Document,
    SocialMedia,
    BackgroundImage,
)
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(Issue)
admin.site.register(Document)
admin.site.register(SocialMedia)


class TextInline(SummernoteModelAdminMixin, admin.StackedInline):
    model = Text
    summernote_fields = "__all__"
    extra = 0


class BackgroundImageInline(admin.StackedInline):
    model = BackgroundImage
    extra = 0


class PageAdmin(SummernoteModelAdmin):
    summernote_fields = "__all__"
    inlines = [TextInline]


class PublicationAdmin(SummernoteModelAdmin):
    summernote_fields = "__all__"
    inlines = [BackgroundImageInline]


admin.site.register(Page, PageAdmin)
admin.site.register(Publication, PublicationAdmin)
