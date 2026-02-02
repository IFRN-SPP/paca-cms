import django_tables2
from .models import Issue, Page, Document


class CmsTable(django_tables2.Table):
    actions = django_tables2.TemplateColumn(
        template_name="cms/includes/actions.html",  # 👈 load from file
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
    class Meta:
        model = Page
        fields = ("url", "icon")


class DocumentTable(CmsTable):
    class Meta:
        model = Document
        fields = ("title", "category", "created_at", "updated_at", "is_published")
