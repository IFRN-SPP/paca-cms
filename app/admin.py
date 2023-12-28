from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import HTMLText, Anal

# Register your models here.

# Apply summernote to all TextField in model.
class HTMLTextAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(HTMLText, HTMLTextAdmin)
admin.site.register(Anal)
