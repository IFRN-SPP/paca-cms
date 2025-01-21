from django.views.generic.base import TemplateView

from .models import Texto, Pagina


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["paginas"] = Pagina.objects.all()
        context["textap"] = Texto.objects.filter(titulo="Apresentação")
        context["textctt"] = Texto.objects.filter(titulo="Contato")

        return context
