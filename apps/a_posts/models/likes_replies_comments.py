""" MODEL FOR THE REPLIES LIKES IN COMMENTS """

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from .replies import Reply

# Utilities
from apps.utils.models import TimeStampedModel


class LikedRepliesComment(TimeStampedModel):
    """MODEL FOR THE REPLIES LIKES IN COMMENTS"""

    reply = models.ForeignKey(
        Reply,
        on_delete=models.CASCADE,
        related_name="liked_reply_comments",
        verbose_name=_("liked reply comments")
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_liked_reply_comment",
        verbose_name=_("user who liked the reply comment")
    )

    class Meta(TimeStampedModel.Meta):
        """OVERWRITE META CLASS OF TIMESTAMPEDMODEL"""

        ordering = [
            "-created_at"
        ]
        db_table = "liked_reply_comment_info"

    def __str__(self):
        """RETURN NAME."""
        return f"{self.user.username} - {self.reply.body[:30]}"


