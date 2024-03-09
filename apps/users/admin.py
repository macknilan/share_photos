from django.contrib import admin

# Register your models here.
"""User models admin."""

from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

# from apps.users.forms import UserAdminChangeForm, UserAdminCreationForm
# Models
from apps.users.models import Profile, User

# User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    # form = UserAdminChangeForm
    # add_form = UserAdminCreationForm

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("username", "first_name", "last_name", "phone_number")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_verified",
                    "is_client",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    list_display = [
        "id",
        "username",
        "email",
        "created_at",
        "updated_at"
    ]
    search_fields = ["username", "email"]


@admin.register(Profile)
class UserProfile(admin.ModelAdmin):
    """Profile model admin"""

    # def picture_tag(self, obj):
    #     return format_html(
    #         '<img src="{}" style="max-width:150px; max-height:150px"/>'.format(
    #             obj.picture.url
    #         )
    #     )

    def username(self, obj):
        return obj.user.username
    username.short_description = 'Username'

    list_display = [
        "username",
        "biography",
        "picture",
        "created_at",
        "updated_at",
    ]

    search_fields = (
        "user__username",
        "user__email",
        "user__first_name",
        "user__last_name",
    )

    fieldsets = [
        (
            _("Profile"),
            {
                "fields": (("user", "biography", "picture", "email", "location", "real_name"),),
            },
        ),
    ]

# admin.site.register(User, UserAdmin)
