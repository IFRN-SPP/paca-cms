from django.contrib.auth.models import Group
import django_tables2 as tables
from cms.tables import CmsTable
from .models import User


class UserTable(CmsTable):
    full_name = tables.Column(verbose_name="Nome", empty_values=())

    def render_full_name(self, record):
        return f"{record.first_name} {record.last_name}"

    class Meta:
        model = User
        fields = ("full_name", "email", "groups", "last_login")


class GroupTable(CmsTable):
    class Meta:
        model = Group
        fields = [
            "name",
        ]
