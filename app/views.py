from django.http import Http404
from django.db.models import QuerySet
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
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
    issue_paginate_by = 6
    download_paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = context["page"]
        if page.page_type == Page.PageType.DOWNLOADS:
            inner_template = "download_page.html"
            allowed_categories = page.pagealloweddocumentcategory_set.all().values_list(
                "category", flat=True
            )
            content = Document.objects.filter(
                category__in=allowed_categories, publication=page.publication
            ).order_by("title")
            paginate_by = self.download_paginate_by
        elif page.page_type == Page.PageType.ISSUES:
            inner_template = "issues_page.html"
            content = Issue.objects.filter(
                is_published=True, publication=page.publication
            )
            paginate_by = self.issue_paginate_by
        else:
            inner_template = "text_page.html"
            content = page.text

        context["inner_template"] = inner_template
        if isinstance(content, (QuerySet, list, tuple)):
            paginator = Paginator(content, paginate_by)
            context["page_obj"] = paginator.get_page(self.request.GET.get("page"))
            context["paginator"] = paginator
        else:
            context["content"] = content
        return context


class IssuesDetailView(Unpublished404Mixin, DetailView):
    template_name = "issue_detail.html"
    model = Issue
    context_object_name = "issue"
