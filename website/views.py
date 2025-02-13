from django.shortcuts import render, get_object_or_404
from .models import Issue, Page, Document


def index(request):
    return render(request, "index.html")


def pages(request, slug):
    page = get_object_or_404(Page, slug=slug)
    if page.page_type == Page.PageType.DOWNLOADS:
        template = "download_page.html"
        content = Document.objects.all()
    elif page.page_type == Page.PageType.ISSUES:
        template = "issues_page.html"
        content = Issue.objects.all()
    else:
        template = "text_page.html"
        content = page.text_set.filter(is_published=True)

    return render(
        request,
        template,
        {
            "page": page,
            "content": content,
        },
    )


def issue_detail(request, id):
    issue = get_object_or_404(Issue, id=id)
    return render(request, "issue_detail.html", {"issue": issue})
