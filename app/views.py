from django.http import Http404
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from .models import Issue, Page, Document


class Unpublished404Mixin:
    def get_object(self, **kwargs):
        obj = super().get_object(**kwargs)
        if not obj.is_published:
            raise Http404()
        return obj


class IndexView(TemplateView):
    template_name = "index.html"


class PagesDetailView(Unpublished404Mixin, DetailView):
    template_name = "page.html"
    model = Page
    context_object_name = "page"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = context["page"]
        if page.page_type == Page.PageType.DOWNLOADS:
            inner_template = "download_page.html"
            allowed_categories = page.pagealloweddocumentcategory_set.all().values_list(
                "category", flat=True
            )
            content = Document.objects.filter(category__in=allowed_categories).order_by(
                "title"
            )
        elif page.page_type == Page.PageType.ISSUES:
            inner_template = "issues_page.html"
            content = Issue.objects.filter(is_published=True)
        else:
            inner_template = "text_page.html"
            content = page.text_set.filter(is_published=True)

        context["inner_template"] = inner_template
        context["content"] = content
        return context


class IssuesDetailView(Unpublished404Mixin, DetailView):
    template_name = "issue_detail.html"
    model = Issue
    context_object_name = "issue"
