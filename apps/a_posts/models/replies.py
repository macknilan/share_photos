#
import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from apps.a_posts.models import Comment

# Utilities
from apps.utils.models import TimeStampedModel


class Reply(TimeStampedModel):
    """
    REPLY MODEL
    """
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="replies",
        verbose_name=_("author of the reply"),
    )
    parent_comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name="replies",
        verbose_name=_("comment of the reply")
    )
    body = models.CharField(_("comment"), max_length=150)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="liked_reply_comments",
        through="LikedRepliesComment"
    )
    id = models.CharField(
        max_length=100,
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
        verbose_name=_("id of the reply")
    )

    class Meta(TimeStampedModel.Meta):
        verbose_name = _("reply")
        verbose_name_plural = _("replies")
        ordering = ["-created_at"]
        db_table = "reply_info"

    def __str__(self):
        try:
            return f"{self.author.username} - {self.body[:30]}"
        except:
            return f"no author - {self.body[:30]}"

