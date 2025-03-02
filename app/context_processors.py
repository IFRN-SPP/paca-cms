from .models import Publication


def publication_data(request):
    publication = Publication.objects.first()
    response = {}
    if publication:
        response = {"publication": publication}
    return response
