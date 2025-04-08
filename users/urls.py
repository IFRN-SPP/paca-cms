from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path("users/", views.UserListView.as_view(), name="user_list"),
    path("users/add", views.UserCreateView.as_view(), name="user_add"),
    path("users/<int:pk>/", views.UserDetailView.as_view(), name="user_view"),
    path("users/<int:pk>/update/", views.UserUpdateView.as_view(), name="user_change"),
    path("users/<int:pk>/delete/", views.UserDeleteView.as_view(), name="user_delete"),
    path("users/profile", views.UserProfileView.as_view(), name="user_profile"),
    path(
        "users/profile/update/",
        views.UserProfileUpdateView.as_view(),
        name="user_profile_change",
    ),
    path("groups/", views.GroupListView.as_view(), name="group_list"),
    path("groups/add", views.GroupCreateView.as_view(), name="group_add"),
    path("groups/<int:pk>/", views.GroupDetailView.as_view(), name="group_view"),
    path(
        "groups/<int:pk>/update/", views.GroupUpdateView.as_view(), name="group_change"
    ),
    path(
        "groups/<int:pk>/delete/", views.GroupDeleteView.as_view(), name="group_delete"
    ),
]
