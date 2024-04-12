"""Post models admin."""

from django.contrib import admin

# Models
from apps.a_posts.models import (
    Comment,
    LikedComment,
    LikedPost,
    LikedRepliesComment,
    Post,
    Reply,
    Tag,
)


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


@admin.register(LikedPost)
class LikedPostAdmin(admin.ModelAdmin):
    """
    LIKED POST MODEL ADMIN
    """
    list_display = [
        "id",
        "user",
        "post",
    ]
    search_fields = [
        "user",
        "post",
    ]
    list_display_links = [
        "id",
        "user",
    ]
    list_editable = [
        "post",
    ]
    list_filter = [
        "created_at",
        "updated_at",
    ]
    fieldsets = (
        (
            "Liked Post",
            {
                "fields": (
                    "user",
                    "post",
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


@admin.register(LikedComment)
class LikedCommentAdmin(admin.ModelAdmin):
    """
    LIKED COMMENT MODEL ADMIN
    """
    list_display = [
        "id",
        "user",
        "comment",
    ]
    search_fields = [
        "user",
        "comment",
    ]
    list_display_links = [
        "id",
        "user",
    ]
    list_editable = [
        "comment",
    ]
    list_filter = [
        "created_at",
        "updated_at",
    ]
    fieldsets = (
        (
            "Liked Comment",
            {
                "fields": (
                    "user",
                    "comment",
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


@admin.register(LikedRepliesComment)
class LikedRepliesCommentAdmin(admin.ModelAdmin):
    """
    LIKED REPLY COMMENT MODEL ADMIN
    """
    list_display = [
        "id",
        "user",
        "reply",
    ]
    search_fields = [
        "user",
        "reply",
    ]
    list_display_links = [
        "id",
        "user",
    ]
    list_editable = [
        "reply",
    ]
    list_filter = [
        "created_at",
        "updated_at",
    ]
    fieldsets = (
        (
            "Liked Reply Comment",
            {
                "fields": (
                    "user",
                    "reply",
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