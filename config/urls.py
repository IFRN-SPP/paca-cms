from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from users import views as users_views

urlpatterns = [
    # Public
    path("", include("website.urls")),
    # Private
    path("admin/", include("cms.urls")),
    path("admin/", include("users.urls")),
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
