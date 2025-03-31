from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from app.models import Publication, Issue, Page, Document
from users.models import User
from .mixins import (
    PageTitleMixin,
    AutoPublicationFieldMixin,
    DashboardBaseMixin,
    DashboardBaseEditMixin,
)


class DashboardListView(
    DashboardBaseMixin,
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
    DashboardBaseMixin,
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
                        "safe": True if field.name in self.safe_fields else False,
                    }
                )
        return selected_fields

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fields"] = self.get_fields()
        return context


class DashboardCreateView(DashboardBaseEditMixin, CreateView):
    template_name = "dashboard/create.html"
    permission_action = "add"


class DashboardUpdateView(DashboardBaseEditMixin, UpdateView):
    template_name = "dashboard/update.html"
    permission_action = "change"


class DashboardDeleteView(DashboardBaseEditMixin, DeleteView):
    page_title = "Remover"
    template_name = "dashboard/delete.html"
    permission_action = "delete"


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
    fields = "__all__"
    template_name = "dashboard/publication.html"

    def get_object(self, queryset=None):
        return Publication.objects.first()


class PublicationUpdateView(DashboardUpdateView):
    page_title = "Editar Publicação"
    model = Publication
    fields = "__all__"
    template_name = "dashboard/publication_form.html"
    success_url = reverse_lazy("dashboard:publication_detail")

    def get_object(self, queryset=None):
        return Publication.objects.first()


class IssueListView(DashboardListView):
    page_title = "Edições"
    paginate_by = 10
    model = Issue
    table_template = "dashboard/includes/issues_table.html"


class IssueCreateView(AutoPublicationFieldMixin, DashboardCreateView):
    page_title = "Edições"
    model = Issue
    fields = ["title", "presentation", "file", "pub_date", "url", "is_published"]


class IssueDetailView(DashboardDetailView):
    page_title = "Edições"
    model = Issue


class IssueUpdateView(DashboardUpdateView):
    page_title = "Edições"
    model = Issue
    fields = ["title", "presentation", "file", "pub_date", "url", "is_published"]


class IssueDeleteView(DashboardDeleteView):
    model = Issue


class PageListView(DashboardListView):
    page_title = "Páginas"
    paginate_by = 10
    model = Page
    table_template = "dashboard/includes/pages_table.html"


class PageCreateView(AutoPublicationFieldMixin, DashboardCreateView):
    model = Page
    page_title = "Páginas"
    fields = ["title", "order", "page_type", "is_published"]


class PageDetailView(DashboardDetailView):
    model = Page
    page_title = "Páginas"


class PageUpdateView(DashboardUpdateView):
    model = Page
    page_title = "Páginas"
    fields = ["title", "order", "page_type", "is_published"]


class PageDeleteView(DashboardDeleteView):
    model = Page


class DocumentListView(DashboardListView):
    page_title = "Documentos"
    paginate_by = 10
    model = Document
    table_template = "dashboard/includes/documents_table.html"


class DocumentCreateView(AutoPublicationFieldMixin, DashboardCreateView):
    page_title = "Documentos"
    model = Document
    fields = ["title", "category", "file", "is_published"]


class DocumentDetailView(DashboardDetailView):
    page_title = "Documentos"
    model = Document


class DocumentUpdateView(DashboardUpdateView):
    page_title = "Documentos"
    model = Document
    fields = ["title", "category", "file", "is_published"]


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
    fields = ["email", "first_name", "last_name", "groups"]


class UserDetailView(DashboardDetailView):
    page_title = "Usuários"
    model = User
    context_object_name = "user_obj"
    fields = ["email", "first_name", "last_name", "groups", "last_login"]


class UserUpdateView(DashboardUpdateView):
    page_title = "Usuários"
    model = User
    context_object_name = "user_obj"
    fields = ["email", "first_name", "last_name", "groups"]


class UserDeleteView(DashboardDeleteView):
    model = User
    context_object_name = "user_obj"


class GroupListView(DashboardListView):
    page_title = "Grupos"
    paginate_by = 10
    model = Group
    table_template = "dashboard/includes/groups_table.html"


class GroupCreateView(DashboardCreateView):
    page_title = "Grupos"
    model = Group
    fields = "__all__"


class GroupDetailView(DashboardDetailView):
    page_title = "Grupos"
    model = Group
    fields = "__all__"


class GroupUpdateView(DashboardUpdateView):
    page_title = "Grupos"
    model = Group
    fields = "__all__"


class GroupDeleteView(DashboardDeleteView):
    model = Group


class UserProfileView(LoginRequiredMixin, PageTitleMixin, TemplateView):
    page_title = "Perfil"
    template_name = "dashboard/profile.html"


class UserProfileUpdateView(LoginRequiredMixin, PageTitleMixin, UpdateView):
    page_title = "Atualizar Perfil"
    model = User
    fields = ["first_name", "last_name"]
    template_name = "dashboard/profile_edit.html"
    success_url = reverse_lazy("dashboard:user_profile")

    def get_object(self, queryset=None):
        return self.request.user
