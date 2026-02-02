import django_tables2
from django.utils.html import format_html
from .models import Issue, Page, Document, SocialMedia


class CmsTable(django_tables2.Table):
    actions = django_tables2.TemplateColumn(
        template_name="cms/includes/actions.html",
        orderable=False,
        verbose_name="Ações",
        exclude_from_export=True,
    )


class IssueTable(CmsTable):
    class Meta:
        model = Issue
        fields = (
            "title",
            "volume",
            "number",
            "created_at",
            "updated_at",
            "pub_date",
            "is_published",
        )


class PageTable(CmsTable):
    class Meta:
        model = Page
        fields = ("title", "order", "created_at", "updated_at", "is_published")


class SocialMediaTable(CmsTable):
    icon_preview = django_tables2.Column(
        empty_values=(),
        orderable=False,
        verbose_name="Preview",
    )

    def render_icon_preview(self, record):
        return format_html('<i class="{} fs-4"></i>', record.icon)

    class Meta:
        model = SocialMedia
        fields = ("url", "icon", "icon_preview")


class DocumentTable(CmsTable):
    class Meta:
        model = Document
        fields = ("title", "category", "created_at", "updated_at", "is_published")
