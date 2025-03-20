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
    path("issues/add", views.IssueCreateView.as_view(), name="issues_add"),
    path("issues/<int:pk>/", views.IssueDetailView.as_view(), name="issues_view"),
    path(
        "issues/<int:pk>/edit/", views.IssueUpdateView.as_view(), name="issues_change"
    ),
    path(
        "issues/<int:pk>/delete/", views.IssueDeleteView.as_view(), name="issues_delete"
    ),
    path("pages/", views.PageListView.as_view(), name="pages"),
    path("pages/add", views.PageCreateView.as_view(), name="pages_add"),
    path("pages/<int:pk>/", views.PageDetailView.as_view(), name="pages_view"),
    path("pages/<int:pk>/update/", views.PageUpdateView.as_view(), name="pages_change"),
    path("pages/<int:pk>/delete/", views.PageDeleteView.as_view(), name="pages_delete"),
    path("documents/", views.DocumentListView.as_view(), name="documents"),
    path("documents/add", views.DocumentCreateView.as_view(), name="documents_add"),
    path(
        "documents/<int:pk>/",
        views.DocumentDetailView.as_view(),
        name="documents_view",
    ),
    path(
        "documents/<int:pk>/update/",
        views.DocumentUpdateView.as_view(),
        name="documents_change",
    ),
    path(
        "documents/<int:pk>/delete/",
        views.DocumentDeleteView.as_view(),
        name="documents_delete",
    ),
    path("users/", views.UserListView.as_view(), name="users"),
    path("users/add", views.UserCreateView.as_view(), name="users_add"),
    path("users/<int:pk>/", views.IssueDetailView.as_view(), name="users_view"),
    path("users/<int:pk>/update/", views.UserUpdateView.as_view(), name="users_change"),
    path("users/<int:pk>/delete/", views.UserDeleteView.as_view(), name="users_delete"),
]
