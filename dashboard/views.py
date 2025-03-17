from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from app.models import Publication, Issue, Page, Document
from users.models import User
from .mixins import PageTitleMixin


class DashboardListView(
    LoginRequiredMixin, PermissionRequiredMixin, PageTitleMixin, ListView
):
    template_name = "dashboard/list.html"
    permission_required = ""
    table_template = ""
    actions = ["add", "change", "delete", "view"]

    def get_allowed_actions(self):
        allowed_actions = []
        app_label = self.model._meta.app_label
        model_name = self.model._meta.model_name
        for action in self.actions:
            perm_string = f"{app_label}.{action}_{model_name}"
            if self.request.user.has_perm(perm_string):
                allowed_actions.append(perm_string)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.request.user)
        context["table_template"] = self.table_template
        self.get_allowed_actions()
        return context


class DashboardDetailView(LoginRequiredMixin, PageTitleMixin, DetailView):
    pass


class DashboardUpdateView(LoginRequiredMixin, PageTitleMixin, UpdateView):
    pass


class DashboardDeleteView(LoginRequiredMixin, PageTitleMixin, DeleteView):
    pass


class IndexView(LoginRequiredMixin, PageTitleMixin, TemplateView):
    template_name = "dashboard/index.html"
    page_title = "Dashboard"


class PublicationDetailView(DashboardDetailView):
    page_title = "Publicação"
    model = Publication
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


class IssueDetailView(DashboardDetailView):
    page_title = "Edições"
    model = Issue
    template_name = "dashboard/issues_detail.html"


class IssueUpdateView(DashboardListView):
    page_title = "Edições"
    model = Issue
    template_name = "dashboard/issues.html"


class IssueDeleteView(DashboardListView):
    page_title = "Edições"
    model = Issue
    template_name = "dashboard/issues.html"


class PageListView(DashboardListView):
    page_title = "Páginas"
    paginate_by = 10
    model = Page
    table_template = "dashboard/includes/pages_table.html"


class PageDetailView(DashboardDetailView):
    pass


class PageUpdateView(DashboardUpdateView):
    pass


class PageDeleteView(DashboardDeleteView):
    pass


class DocumentListView(DashboardListView):
    page_title = "Documentos"
    paginate_by = 10
    model = Document
    table_template = "dashboard/includes/documents_table.html"


class DocumentDetailView(DashboardDetailView):
    pass


class DocumentUpdateView(DashboardUpdateView):
    pass


class DocumentDeleteView(DashboardDeleteView):
    pass


class UserListView(DashboardListView):
    page_title = "Usuários"
    paginate_by = 10
    model = User
    table_template = "dashboard/includes/users_table.html"


class UserDetailView(DashboardDetailView):
    pass


class UserUpdateView(DashboardUpdateView):
    pass


class UserDeleteView(DashboardDeleteView):
    pass
