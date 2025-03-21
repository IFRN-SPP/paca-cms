from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from app.models import Publication, Issue, Page, Document
from users.models import User
from .mixins import PageTitleMixin, AllowedActionsMixin, AutoPermissionRequiredMixin


class DashboardListView(
    AutoPermissionRequiredMixin,
    AllowedActionsMixin,
    PageTitleMixin,
    ListView,
):
    template_name = "dashboard/list.html"
    permission_action = "view"
    table_template = ""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["table_template"] = self.table_template
        return context


class DashboardDetailView(
    AutoPermissionRequiredMixin,
    AllowedActionsMixin,
    PageTitleMixin,
    DetailView,
):
    template_name = "dashboard/detail.html"
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
                        "safe": True
                        if field.verbose_name in self.safe_fields
                        else False,
                    }
                )
        return selected_fields

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fields"] = self.get_fields()
        return context


class DashboardCreateView(
    AutoPermissionRequiredMixin,
    AllowedActionsMixin,
    PageTitleMixin,
    CreateView,
):
    template_name = "dashboard/create.html"
    permission_action = "create"


class DashboardUpdateView(
    AutoPermissionRequiredMixin,
    AllowedActionsMixin,
    PageTitleMixin,
    UpdateView,
):
    template_name = "dashboard/update.html"
    permission_action = "change"


class DashboardDeleteView(
    AutoPermissionRequiredMixin,
    AllowedActionsMixin,
    PageTitleMixin,
    DeleteView,
):
    page_title = "Remover"
    template_name = "dashboard/delete.html"
    permission_action = "delete"

    def get_success_url(self):
        return reverse_lazy(self.request.resolver_match.view_name.rsplit("_", 1)[0])


class IndexView(LoginRequiredMixin, PageTitleMixin, TemplateView):
    template_name = "dashboard/index.html"
    page_title = "Dashboard"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["issues"] = Issue.objects.filter(is_published=True).count()
        context["pages"] = Page.objects.filter(is_published=True).count()
        context["documents"] = Document.objects.filter(is_published=True).count()
        context["users"] = User.objects.count()
        return context


class PublicationDetailView(DashboardDetailView):
    page_title = "Publicação"
    model = Publication
    fields = ["organization", "description"]
    template_name = "dashboard/publication.html"

    def get_object(self, queryset=None):
        return Publication.objects.first()


class PublicationUpdateView(DashboardUpdateView):
    page_title = "Editar Publicação"
    model = Publication
    fields = "__all__"
    template_name = "dashboard/publication_form.html"
    success_url = reverse_lazy("dashboard:publication")

    def get_object(self, queryset=None):
        return Publication.objects.first()


class IssueListView(DashboardListView):
    page_title = "Edições"
    paginate_by = 10
    model = Issue
    table_template = "dashboard/includes/issues_table.html"


class IssueCreateView(DashboardCreateView):
    page_title = "Edições"
    model = Issue
    fields = "__all__"
    success_url = reverse_lazy("dashboard:issue_list")


class IssueDetailView(DashboardDetailView):
    page_title = "Edições"
    model = Issue


class IssueUpdateView(DashboardUpdateView):
    page_title = "Edições"
    model = Issue
    fields = "__all__"
    success_url = reverse_lazy("dashboard:issue_list")


class IssueDeleteView(DashboardDeleteView):
    model = Issue


class PageListView(DashboardListView):
    page_title = "Páginas"
    paginate_by = 10
    model = Page
    table_template = "dashboard/includes/pages_table.html"


class PageCreateView(DashboardCreateView):
    model = Page
    page_title = "Páginas"
    fields = "__all__"
    success_url = reverse_lazy("dashboard:page_list")


class PageDetailView(DashboardDetailView):
    model = Page
    page_title = "Páginas"


class PageUpdateView(DashboardUpdateView):
    model = Page
    page_title = "Páginas"
    fields = "__all__"
    success_url = reverse_lazy("dashboard:page_list")


class PageDeleteView(DashboardDeleteView):
    model = Page


class DocumentListView(DashboardListView):
    page_title = "Documentos"
    paginate_by = 10
    model = Document
    table_template = "dashboard/includes/documents_table.html"


class DocumentCreateView(DashboardCreateView):
    page_title = "Documentos"
    model = Document
    fields = "__all__"


class DocumentDetailView(DashboardDetailView):
    page_title = "Documentos"
    model = Document


class DocumentUpdateView(DashboardUpdateView):
    page_title = "Documentos"
    model = Document
    fields = "__all__"
    success_url = "dashboard:document_list"


class DocumentDeleteView(DashboardDeleteView):
    model = Document


class UserListView(DashboardListView):
    page_title = "Usuários"
    paginate_by = 10
    model = User
    table_template = "dashboard/includes/users_table.html"


class UserCreateView(DashboardCreateView):
    page_title = "Usuários"
    model = User
    table_template = "dashboard/users_create.html"


class UserDetailView(DashboardDetailView):
    page_title = "Usuários"
    model = User


class UserUpdateView(DashboardUpdateView):
    page_title = "Usuários"
    model = User
    fields = "__all__"
    success_url = "dashboard:user_list"


class UserDeleteView(DashboardDeleteView):
    model = User
