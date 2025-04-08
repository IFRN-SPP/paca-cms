from allauth.account.views import PasswordResetFromKeyView
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.contrib.auth import get_user_model
from cms.mixins import PageTitleMixin
from cms.views import (
    CmsListView,
    CmsCreateView,
    CmsDetailView,
    CmsUpdateView,
    CmsDeleteView,
)

User = get_user_model()


class ExcludeAdminMixin:
    admin_id = 1

    def get_queryset(self):
        base_qs = super().get_queryset()
        return base_qs.exclude(id=self.admin_id)


class CustomPasswordResetFromKeyView(PasswordResetFromKeyView):
    success_url = reverse_lazy("account_login")


class UserListView(ExcludeAdminMixin, CmsListView):
    page_title = "Usuários"
    paginate_by = 10
    model = User
    table_template = "cms/includes/users_table.html"


class UserCreateView(CmsCreateView):
    page_title = "Usuários"
    model = User
    fields = ["email", "first_name", "last_name", "groups"]


class UserDetailView(ExcludeAdminMixin, CmsDetailView):
    page_title = "Usuários"
    model = User
    context_object_name = "user_obj"
    fields = ["email", "first_name", "last_name", "groups", "last_login"]


class UserUpdateView(ExcludeAdminMixin, CmsUpdateView):
    page_title = "Usuários"
    model = User
    context_object_name = "user_obj"
    fields = ["email", "first_name", "last_name", "groups"]


class UserDeleteView(ExcludeAdminMixin, CmsDeleteView):
    model = User
    context_object_name = "user_obj"


class GroupListView(CmsListView):
    page_title = "Grupos"
    paginate_by = 10
    model = Group
    table_template = "cms/includes/groups_table.html"


class GroupCreateView(CmsCreateView):
    page_title = "Grupos"
    model = Group
    fields = "__all__"


class GroupDetailView(CmsDetailView):
    page_title = "Grupos"
    model = Group
    fields = "__all__"


class GroupUpdateView(CmsUpdateView):
    page_title = "Grupos"
    model = Group
    fields = "__all__"


class GroupDeleteView(CmsDeleteView):
    model = Group


class UserProfileView(LoginRequiredMixin, PageTitleMixin, TemplateView):
    page_title = "Perfil"
    template_name = "cms/profile.html"

    def get_object(self, queryset=None):
        return self.request.user


class UserProfileUpdateView(LoginRequiredMixin, PageTitleMixin, UpdateView):
    page_title = "Atualizar Perfil"
    model = User
    fields = ["first_name", "last_name", "email"]
    template_name = "cms/profile_edit.html"
    success_url = reverse_lazy("cms:user_profile")

    def get_object(self, queryset=None):
        return self.request.user
