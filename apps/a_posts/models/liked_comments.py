""" MODEL LIKES FOR THE COMMENTS """

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from apps.a_posts.models import Comment

# Utilities
from apps.utils.models import TimeStampedModel


class LikedComment(TimeStampedModel):
    """LIKED POST MODEL FOR THE COMMENTS"""

    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name="liked_comment",
        verbose_name=_("comment liked")
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_liked_comment",
        verbose_name=_("user who liked the comment")
    )

    class Meta(TimeStampedModel.Meta):
        """OVERWRITE META CLASS OF TIMESTAMPEDMODEL"""

        ordering = [
            "-created_at"
        ]
        db_table = "liked_comment_info"

    def __str__(self):
        """RETURN NAME."""
        return f"{self.user.username} - {self.comment.body[:30]}"


