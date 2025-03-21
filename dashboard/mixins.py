from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.exceptions import ImproperlyConfigured


class PageTitleMixin:
    page_title = ""

    def get_page_title(self):
        return self.page_title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.get_page_title()
        return context


class AllowedActionsMixin:
    actions = ["add", "change", "delete", "view", "list"]

    def get_allowed_actions(self):
        allowed_actions = {}
        app_label = self.model._meta.app_label
        model_name = self.model._meta.model_name
        for action in self.actions:
            perm_string = f"{app_label}.{action}_{model_name}"
            if self.request.user.has_perm(perm_string):
                allowed_actions[action] = (
                    f"{self.request.resolver_match.namespace}:{model_name}_{action}"
                )
        return allowed_actions

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["allowed_actions"] = self.get_allowed_actions()
        return context


class AutoPermissionRequiredMixin(PermissionRequiredMixin):
    permission_action = "view"

    def get_permission_required(self):
        if not self.permission_required:
            model = getattr(self, "model", None)
            if model is None and hasattr(self, "get_queryset"):
                model = self.get_queryset().model
            if model is None:
                raise ImproperlyConfigured(
                    "AutoPermissionRequiredMixin requires either a 'model' attribute "
                    "or a 'get_queryset()' method returning a model-aware queryset."
                )

            app_label = model._meta.app_label
            model_name = model._meta.model_name
            self.permission_required = (
                f"{app_label}.{self.permission_action}_{model_name}"
            )

        return super().get_permission_required()
