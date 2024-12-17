from django.urls import path
from . import views


urlpatterns = [
    path("", views.inicio, name="areadmin"),
    path("comissao", views.comissao, name="comissao"),
    path("normas", views.normas, name="normas"),
    path("textos", views.textos, name="textos"),
    path("eixos", views.eixos, name="eixos"),
    path("add", views.Add, name="add"),
    path("update/<str:id>", views.Update, name="update"),
    path("delete/<str:id>", views.Delete, name="delete"),
]
