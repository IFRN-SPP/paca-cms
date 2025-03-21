from django.urls import path
from . import views

app_name = "dashboard"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path(
        "publication/", views.PublicationDetailView.as_view(), name="publication_detail"
    ),
    path(
        "publication/update/",
        views.PublicationUpdateView.as_view(),
        name="publication_change",
    ),
    path("issues/", views.IssueListView.as_view(), name="issue_list"),
    path("issues/add", views.IssueCreateView.as_view(), name="issue_add"),
    path("issues/<int:pk>/", views.IssueDetailView.as_view(), name="issue_view"),
    path("issues/<int:pk>/edit/", views.IssueUpdateView.as_view(), name="issue_change"),
    path(
        "issues/<int:pk>/delete/", views.IssueDeleteView.as_view(), name="issue_delete"
    ),
    path("pages/", views.PageListView.as_view(), name="page_list"),
    path("pages/add", views.PageCreateView.as_view(), name="page_add"),
    path("pages/<int:pk>/", views.PageDetailView.as_view(), name="page_view"),
    path("pages/<int:pk>/update/", views.PageUpdateView.as_view(), name="page_change"),
    path("pages/<int:pk>/delete/", views.PageDeleteView.as_view(), name="page_delete"),
    path("documents/", views.DocumentListView.as_view(), name="document_list"),
    path("documents/add", views.DocumentCreateView.as_view(), name="document_add"),
    path(
        "documents/<int:pk>/",
        views.DocumentDetailView.as_view(),
        name="document_view",
    ),
    path(
        "documents/<int:pk>/update/",
        views.DocumentUpdateView.as_view(),
        name="document_change",
    ),
    path(
        "documents/<int:pk>/delete/",
        views.DocumentDeleteView.as_view(),
        name="document_delete",
    ),
    path("users/", views.UserListView.as_view(), name="user_list"),
    path("users/add", views.UserCreateView.as_view(), name="user_add"),
    path("users/<int:pk>/", views.UserDetailView.as_view(), name="user_view"),
    path("users/<int:pk>/update/", views.UserUpdateView.as_view(), name="user_change"),
    path("users/<int:pk>/delete/", views.UserDeleteView.as_view(), name="user_delete"),
]
