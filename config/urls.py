from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from app import views
from users import views as users_views

urlpatterns = [
    # Public
    path("", views.IndexView.as_view(), name="index"),
    path("p/<slug:slug>/", views.PagesDetailView.as_view(), name="pages"),
    path("issues/<int:pk>/", views.IssuesDetailView.as_view(), name="issue_detail"),
    # Private
    path("admin/", include("dashboard.urls")),
    # Third party
    re_path(
        r"^accounts/password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
        users_views.CustomPasswordResetFromKeyView.as_view(),
        name="account_reset_password_from_key",
    ),
    path("accounts/", include("allauth.urls")),
    path("tinymce/", include("tinymce.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns.append(path("djangoadmin/", admin.site.urls))
