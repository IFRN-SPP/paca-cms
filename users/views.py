from allauth.account.views import PasswordResetFromKeyView
from django.urls import reverse_lazy


class CustomPasswordResetFromKeyView(PasswordResetFromKeyView):
    success_url = reverse_lazy("account_login")
