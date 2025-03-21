from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    # Public
    path("", views.IndexView.as_view(), name="index"),
    path("p/<slug:slug>/", views.PagesDetailView.as_view(), name="pages"),
    path("issues/<int:pk>/", views.IssuesDetailView.as_view(), name="issue_detail"),
    # Private
    path("admin/", include("dashboard.urls")),
    # Third party
    path("accounts/", include("allauth.urls")),
    path("summernote/", include("django_summernote.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns.append(path("djangoadmin/", admin.site.urls))
