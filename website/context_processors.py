from cms.models import Publication


def publication_data(request):
    publication = Publication.objects.first()
    response = {}
    if publication:
        pages = publication.page_set.filter(is_published=True)
        response = {"publication": publication, "pages": pages}
    return response
