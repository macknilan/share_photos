from django.urls import path

from apps.users.views import profile_delete_view, profile_edit_view, profile_view

app_name = "users"
urlpatterns = [
    path("profile/", profile_view, name="profile"),
    path("edit/", profile_edit_view, name="profile-edit"),
    path("delete/", profile_delete_view, name="profile-delete"),
    path("<username>/", profile_view, name="profile-user"),
]

