from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.utils import user_email, user_field
from django.conf import settings


class CustomAccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        return settings.OPEN_FOR_SIGNUP or False


class SuapSocialAccountAdapter(DefaultSocialAccountAdapter):
    def populate_user(self, request, sociallogin, data):
        # Extra data in: sociallogin.account.extra_data
        user = sociallogin.user
        user_email(user, data.get("email") or "")
        user_field(user, "first_name", data.get("first_name"))
        user_field(user, "last_name", data.get("last_name"))
        return user

    def is_open_for_signup(self, request, sociallogin):
        return settings.OPEN_FOR_SIGNUP or False
