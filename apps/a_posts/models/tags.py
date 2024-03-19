""" Model Tags for the Blog """

from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

# Utilities
from apps.utils.models import TimeStampedModel


class Tag(TimeStampedModel):
    """Tag model."""

    name = models.CharField(_("name"), max_length=20)
    slug = models.SlugField(_("slug"), max_length=20, unique=True, null=True, blank=True)
    image = models.FileField(_("image"), upload_to="icons/", null=True, blank=True)

    class Meta(TimeStampedModel.Meta):
        """Overwrite meta class of TimeStampedModel"""

        ordering = [
            "-created_at"
        ]
        db_table = "tag_info"

    def __str__(self):
        """Return name."""
        return "{}".format(self.name)

    def save(self, *args, **kwargs):
        self.url = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)






