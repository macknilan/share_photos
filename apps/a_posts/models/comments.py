#
import uuid

from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


# Utilities
from apps.utils.models import TimeStampedModel

# Models
from apps.a_posts.models import Post


class Comment(TimeStampedModel):
    """
    COMMENT MODEL.
    """
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="comments",
        verbose_name=_("author of the comment"),
    )
    parent_post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name=_("post of the comment")
    )
    body = models.CharField(_("comment"), max_length=150)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="liked_comments",
        through="LikedComment"
    )
    id = models.CharField(
        max_length=100,
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
        verbose_name=_("id of the comment")
    )

    class Meta(TimeStampedModel.Meta):
        verbose_name = _("comment")
        verbose_name_plural = _("comments")
        ordering = ["-created_at"]
        db_table = "comment_info"

    def __str__(self):
        try:
            return f"{self.author.username} - {self.body[:30]}"
        except:
            return f"no author - {self.body[:30]}"
