""" MODEL LIKES FOR THE POSTS """

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from apps.a_posts.models import Post

# Utilities
from apps.utils.models import TimeStampedModel


class LikedPost(TimeStampedModel):
    """LIKED POST MODEL FOR THE POSTS"""

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="liked_post",
        verbose_name=_("post liked")
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_liked_post",
        verbose_name=_("user who liked the post")
    )

    class Meta(TimeStampedModel.Meta):
        """OVERWRITE META CLASS OF TIMESTAMPEDMODEL"""

        ordering = [
            "-created_at"
        ]
        db_table = "liked_post_info"

    def __str__(self):
        """RETURN NAME."""
        return f"{self.user.username} - {self.post.title[:30]}"


