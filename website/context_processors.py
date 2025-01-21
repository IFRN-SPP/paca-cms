from .models import Evento


def evento_info(request):
    evento = Evento.objects.first()
    if evento:
        response = {"evento": evento}
    else:
        return {}
    return response
