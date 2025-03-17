from django.urls import path
from . import views

app_name = "dashboard"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("publication/", views.PublicationDetailView.as_view(), name="publication"),
    path(
        "publication/update/",
        views.PublicationUpdateView.as_view(),
        name="publication_update",
    ),
    path("issues/", views.IssueListView.as_view(), name="issues"),
    path("issues/<int:pk>/", views.IssueDetailView.as_view(), name="issues_detail"),
    path(
        "issues/<int:id>/edit/", views.IssueUpdateView.as_view(), name="issues_update"
    ),
    path(
        "issues/<int:id>/delete/", views.IssueDeleteView.as_view(), name="issues_delete"
    ),
    path("pages/", views.PageListView.as_view(), name="pages"),
    path("pages/<int:pk>/", views.PageDetailView.as_view(), name="pages_detail"),
    path("pages/<int:id>/update/", views.PageUpdateView.as_view(), name="pages_update"),
    path("pages/<int:id>/delete/", views.PageDeleteView.as_view(), name="pages_delete"),
    path("documents/", views.DocumentListView.as_view(), name="documents"),
    path(
        "documents/<int:pk>/",
        views.DocumentDetailView.as_view(),
        name="documents_detail",
    ),
    path(
        "documents/<int:id>/update/",
        views.DocumentUpdateView.as_view(),
        name="documents_update",
    ),
    path(
        "documents/<int:id>/delete/",
        views.DocumentDeleteView.as_view(),
        name="documents_delete",
    ),
    path("users/", views.UserListView.as_view(), name="users"),
    path("users/<int:pk>/", views.IssueDetailView.as_view(), name="users_detail"),
    path("users/<int:id>/update/", views.UserUpdateView.as_view(), name="users_update"),
    path("users/<int:id>/delete/", views.UserDeleteView.as_view(), name="users_delete"),
]
