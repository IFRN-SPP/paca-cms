from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)

# Apply summernote to all TextField in model.
class HTMLTextAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(Textos, HTMLTextAdmin)
admin.site.register(Normas)
admin.site.register(Areas)
admin.site.register(Artigos)
admin.site.register(Edicoes)
admin.site.register(Comissao)
