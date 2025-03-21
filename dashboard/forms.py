from django import forms
from app.models import Issue, Document, Page


class IssueForm(forms.ModelForm):
    model = Issue
    fields = "__all__"


class DocumentForm(forms.ModelForm):
    model = Document
    fields = "__all__"


class PageForm(forms.ModelForm):
    model = Page
    fields = "__all__"
