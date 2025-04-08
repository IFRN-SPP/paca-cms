from django.urls import path
from . import views

app_name = "cms"
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
    path(
        "publication/social_media/",
        views.SocialMediaListView.as_view(),
        name="socialmedia_list",
    ),
    path(
        "publication/social_media/add",
        views.SocialMediaCreateView.as_view(),
        name="socialmedia_add",
    ),
    path(
        "publication/social_media/<int:pk>/",
        views.SocialMediaDetailView.as_view(),
        name="socialmedia_view",
    ),
    path(
        "publication/social_media/<int:pk>/update/",
        views.SocialMediaUpdateView.as_view(),
        name="socialmedia_change",
    ),
    path(
        "publication/social_media/<int:pk>/delete/",
        views.SocialMediaDeleteView.as_view(),
        name="socialmedia_delete",
    ),
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
]
