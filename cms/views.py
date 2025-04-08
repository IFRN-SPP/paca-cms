from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from .models import Publication, Issue, Page, Document, SocialMedia
from .mixins import (
    PageTitleMixin,
    AutoPublicationFieldMixin,
    CmsBaseMixin,
    CmsBaseEditMixin,
)
from .forms import IssueForm

User = get_user_model()


class CmsListView(
    CmsBaseMixin,
    ListView,
):
    template_name = "cms/list.html"
    permission_action = "view"
    table_template = ""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["table_template"] = self.table_template
        return context


class CmsDetailView(
    CmsBaseMixin,
    DetailView,
):
    template_name = "cms/detail.html"
    permission_action = "view"
    page_title = "Detalhar"
    fields = "__all__"
    safe_fields = ["description", "presentation"]

    def get_fields(self):
        selected_fields = []
        no_check = not isinstance(self.fields, (list, tuple))
        for field in self.object._meta.fields:
            if no_check or field.name in self.fields:
                selected_fields.append(
                    {
                        "label": field.verbose_name,
                        "value": getattr(self.object, field.name),
                        "safe": True if field.name in self.safe_fields else False,
                    }
                )
        return selected_fields

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fields"] = self.get_fields()
        return context


class CmsCreateView(CmsBaseEditMixin, CreateView):
    template_name = "cms/create.html"
    permission_action = "add"


class CmsUpdateView(CmsBaseEditMixin, UpdateView):
    template_name = "cms/update.html"
    permission_action = "change"


class CmsDeleteView(CmsBaseEditMixin, DeleteView):
    page_title = "Remover"
    template_name = "cms/delete.html"
    template_name_modal = "cms/includes/delete_modal.html"
    permission_action = "delete"

    def get_template_names(self):
        if not self.request.htmx:
            return [self.template_name]
        return [self.template_name_modal]


class IndexView(LoginRequiredMixin, PageTitleMixin, TemplateView):
    template_name = "cms/index.html"
    page_title = "Cms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["issues"] = Issue.objects.filter(is_published=True).count()
        context["pages"] = Page.objects.filter(is_published=True).count()
        context["documents"] = Document.objects.filter(is_published=True).count()
        context["users"] = User.objects.count()
        return context


class PublicationDetailView(CmsDetailView):
    page_title = "Publicação"
    model = Publication
    fields = "__all__"
    template_name = "cms/publication.html"

    def get_object(self, queryset=None):
        return Publication.objects.first()


class PublicationUpdateView(CmsUpdateView):
    page_title = "Editar Publicação"
    model = Publication
    fields = "__all__"
    template_name = "cms/publication_form.html"
    success_url = reverse_lazy("cms:publication_detail")

    def get_object(self, queryset=None):
        return Publication.objects.first()


class IssueListView(CmsListView):
    page_title = "Edições"
    paginate_by = 10
    model = Issue
    table_template = "cms/includes/issues_table.html"


class IssueCreateView(AutoPublicationFieldMixin, CmsCreateView):
    page_title = "Edições"
    model = Issue
    form_class = IssueForm


class IssueDetailView(CmsDetailView):
    page_title = "Edições"
    model = Issue


class IssueUpdateView(CmsUpdateView):
    page_title = "Edições"
    model = Issue
    form_class = IssueForm


class IssueDeleteView(CmsDeleteView):
    model = Issue


class PageListView(CmsListView):
    page_title = "Páginas"
    paginate_by = 10
    model = Page
    table_template = "cms/includes/pages_table.html"


class PageCreateView(AutoPublicationFieldMixin, CmsCreateView):
    model = Page
    page_title = "Páginas"
    fields = ["title", "order", "page_type", "text", "is_published"]


class PageDetailView(CmsDetailView):
    model = Page
    page_title = "Páginas"
    safe_fields = ["text"]


class PageUpdateView(CmsUpdateView):
    model = Page
    page_title = "Páginas"
    fields = ["title", "order", "page_type", "text", "is_published"]


class PageDeleteView(CmsDeleteView):
    model = Page


class SocialMediaListView(CmsListView):
    page_title = "Redes Sociais"
    paginate_by = 10
    model = SocialMedia
    table_template = "cms/includes/socialmedia_table.html"


class SocialMediaCreateView(AutoPublicationFieldMixin, CmsCreateView):
    page_title = "Redes Sociais"
    model = SocialMedia
    fields = ["url", "icon"]


class SocialMediaDetailView(CmsDetailView):
    page_title = "Redes Sociais"
    model = SocialMedia


class SocialMediaUpdateView(CmsUpdateView):
    page_title = "Redes Sociais"
    model = SocialMedia
    fields = ["url", "icon"]


class SocialMediaDeleteView(CmsDeleteView):
    model = SocialMedia


class DocumentListView(CmsListView):
    page_title = "Documentos"
    paginate_by = 10
    model = Document
    table_template = "cms/includes/documents_table.html"


class DocumentCreateView(AutoPublicationFieldMixin, CmsCreateView):
    page_title = "Documentos"
    model = Document
    fields = ["title", "category", "file", "is_published"]


class DocumentDetailView(CmsDetailView):
    page_title = "Documentos"
    model = Document


class DocumentUpdateView(CmsUpdateView):
    page_title = "Documentos"
    model = Document
    fields = ["title", "category", "file", "is_published"]


class DocumentDeleteView(CmsDeleteView):
    model = Document
