from django import forms
from app.models import Issue, Document, Page


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ["title", "presentation", "file", "pub_date", "url", "is_published"]
        widgets = {
            "pub_date": forms.DateInput(
                format="%Y-%m-%d",
                attrs={
                    "type": "date",
                },
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields["pub_date"].initial = self.instance.pub_date.strftime(
                "%Y-%m-%d"
            )


class DocumentForm(forms.ModelForm):
    model = Document
    fields = "__all__"


class PageForm(forms.ModelForm):
    model = Page
    fields = "__all__"
