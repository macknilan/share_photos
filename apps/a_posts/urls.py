from django.urls import path

from apps.a_posts.views import (
    home_view,
    post_create_view,
    post_delete_view,
    post_detail_view,
    post_edit_view,
)

app_name = "a_posts"
urlpatterns = [
    path("categoy/<tag>/", home_view, name="category"),
    path("create/", post_create_view, name="post-create"),
    path("delete/<pk>/", post_delete_view, name="post-delete"),
    path("edit/<pk>/", post_edit_view, name="post-edit"),
    path("detail/<pk>/", post_detail_view, name="post-detail"),
]







