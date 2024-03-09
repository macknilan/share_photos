""" Model Post for the Blog """
import uuid

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

# Utilities
from apps.utils.models import TimeStampedModel

# Models
from .a_post_tags import Tag


# https://docs.djangoproject.com/en/3.2/topics/db/managers/#modifying-a-manager-s-initial-queryset
class PostLet(models.Manager):
    def get_queryset(self):
        """Show posts less than or equal to (lte) now"""
        now = timezone.now()
        return super().get_queryset().filter(publish_date__lte=now)


class Post(TimeStampedModel):
    """Post model."""

    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(_("title"), max_length=255)
    body = models.TextField(max_length=500)
    image = models.URLField(_("url_image"), max_length=500, blank=True, null=True)
    is_draft = models.BooleanField(_("is_draft"), default=False)
    publish_date = models.DateTimeField(_("published_date"), auto_now=False, auto_now_add=False, null=True, blank=True)
    url = models.SlugField(_("url"), max_length=255, null=True, blank=True)  # unique=True
    link = models.URLField(_("link"), max_length=500)
    artist = models.CharField(_("artist"), max_length=500)
    tags = models.ManyToManyField(Tag, verbose_name=_("tags for the post"))
    objects = models.Manager()  # The default manager
    published = PostLet()  # The Post Manager manager
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        db_column="author_id",
        on_delete=models.SET_NULL,
        null=True,
        related_name="posts",
        verbose_name=_("author of the post"),
    )  # SE HACE LA RELACIÓN POR QUE EN SETTINGS SE HACE LA RELACIÓN DE AUTH_USER_MODEL

    class Meta(TimeStampedModel.Meta):
        """Overwrite meta class of TimeStampedModel"""

        # ordering = ("title",)
        ordering = [
            "-created_at"
        ]
        db_table = "post_info"

    def __str__(self):
        """Return title and username."""
        return "{}".format(self.title)

    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


