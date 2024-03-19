"""Post models admin."""

from django.contrib import admin

# Models
from apps.a_posts.models import Post, Tag, Comment, Reply


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """PROFILE MODEL ADMIN"""

    list_display = [
        "id",
        "title",
        "body",
        "image",
        "is_draft",
        "url",
        "publish_date",
    ]
    search_fields = [
        "title",
        "publish_date",
    ]
    list_filter = [
        "is_draft",
        "publish_date",
    ]
    list_display_links = [
        "id",
        "title",
    ]
    list_editable = [
        "is_draft",
    ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """TAG MODEL ADMIN"""

    list_display = [
        "id",
        "name",
        "slug",
        "image",
    ]
    search_fields = [
        "name",
    ]
    list_display_links = [
        "id",
        "name",
    ]
    list_editable = [
        "slug",
    ]
    prepopulated_fields = {"slug": ("name",)}
    fieldsets = (
        (
            "Tag",
            {
                "fields": (
                    "name",
                    "slug",
                    "image",
                )
            },
        ),
    )
    readonly_fields = [
        "created_at",
        "updated_at",
    ]
    ordering = [
        "-created_at"
    ]
    list_filter = [
        "created_at",
        "updated_at",
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """COMMENT MODEL ADMIN"""
    list_display = [
        "id",
        "author",
        "parent_post",
        "body",
    ]
    search_fields = [
        "author",
        "parent_post",
    ]
    list_display_links = [
        "id",
        "author",
    ]
    list_editable = [
        "body",
    ]
    list_filter = [
        "created_at",
        "updated_at",
    ]
    fieldsets = (
        (
            "Comment",
            {
                "fields": (
                    "author",
                    "parent_post",
                    "body",
                )
            },
        ),
    )
    readonly_fields = [
        "created_at",
        "updated_at",
    ]
    ordering = [
        "-created_at"
    ]


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    """
    REPLY MODEL ADMIN
    """
    list_display = [
        "id",
        "author",
        "parent_comment",
        "body",
    ]
    search_fields = [
        "author",
        "parent_comment",
    ]
    list_display_links = [
        "id",
        "author",
    ]
    list_editable = [
        "body",
    ]
    list_filter = [
        "created_at",
        "updated_at",
    ]
    fieldsets = (
        (
            "Comment",
            {
                "fields": (
                    "author",
                    "parent_comment",
                    "body",
                )
            },
        ),
    )
    readonly_fields = [
        "created_at",
        "updated_at",
    ]
    ordering = [
        "-created_at"
    ]
