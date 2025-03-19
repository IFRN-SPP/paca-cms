class PageTitleMixin:
    page_title = ""

    def get_page_title(self):
        return self.page_title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.get_page_title()
        return context


class AllowedActionsMixin:
    actions = ["add", "change", "delete", "view"]

    def get_allowed_actions(self):
        allowed_actions = {}
        app_label = self.model._meta.app_label
        model_name = self.model._meta.model_name
        for action in self.actions:
            perm_string = f"{app_label}.{action}_{model_name}"
            if self.request.user.has_perm(perm_string):
                allowed_actions[action] = (
                    self.request.resolver_match.view_name + "_" + action
                )
        return allowed_actions

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["allowed_actions"] = self.get_allowed_actions()
        return context
