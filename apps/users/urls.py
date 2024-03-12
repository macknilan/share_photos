from django.urls import path

from apps.users.views import profile_delete_view, profile_edit_view, profile_view

app_name = "users"
urlpatterns = [
    path("profile/", profile_view, name="profile"),
    path("<username>/", profile_view, name="profile-user"),
    path("profile/edit/", profile_edit_view, name="profile-edit"),
    path("profile/delete/", profile_delete_view, name="profile-delete"),
    path("profile/onboarding/", profile_edit_view, name="profile-onboarding"),
]

