from django.shortcuts import render, get_object_or_404
from .models import Issue, Page


def index(request):
    return render(request, "index.html")


def pages(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, "page.html", {"page": page})


def issue_detail(request, id):
    issue = get_object_or_404(Issue, id=id)
    return render(request, "issue_detail.html", {"issue": issue})
