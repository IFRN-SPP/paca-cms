from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import User, Texto, Evento, Pagina
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(Evento)
admin.site.register(Pagina)


# Apply summernote to all TextField in model.
class HTMLTextAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = "__all__"


admin.site.register(Texto, HTMLTextAdmin)
