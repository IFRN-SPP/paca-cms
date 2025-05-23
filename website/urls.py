from django.urls import path
from . import views

app_name = "website"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("p/<slug:slug>/", views.PagesDetailView.as_view(), name="pages"),
    path("issues/<int:pk>/", views.IssuesDetailView.as_view(), name="issue_detail"),
]
