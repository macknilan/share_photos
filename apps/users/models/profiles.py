"""Profile model."""

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _
# from traitlets import default

# Utilities
from apps.utils.models import TimeStampedModel


class Profile(TimeStampedModel):
    """Profile model.

    User profile data
    A profile holds a user's public data like biography, picture,
    """

    user = models.OneToOneField("users.User", on_delete=models.CASCADE)
    email = models.EmailField(
        _("email address"),
        db_index=True,
        max_length=255,
        unique=True,
        null=True,
        error_messages={"unique": _("A user with that email already exists.")},
    )  # THIS FIELD USES SIGNALS TO SYNC
    picture = models.ImageField(
        _("profile picture"),
        blank=True,
        max_length=100,
        null=True,
        upload_to="avatar/",
    )
    biography = models.TextField(
        _("About your profile"),
        blank=True,
        null=True,
        help_text=_("A small biography about the user"),
        max_length=500,
    )
    location = models.CharField(
        _("location"),
        max_length=30,
        blank=True,
        null=True,
        help_text=_("Where are you from?"),
    )
    real_name = models.CharField(
        _("real name"),
        blank=True,
        max_length=30,
        null=True,
        help_text=_("What is your real name?"),
    )

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")
        db_table = "profile_user_info"

    def __str__(self):
        """Return user's str representation."""
        return str(self.user)
