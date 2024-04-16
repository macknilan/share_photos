#
# from allauth.account.forms import SignupForm
# from allauth.socialaccount.forms import SignupForm as SocialSignupForm

from django import forms
from django.contrib.auth import forms as admin_forms
from django.forms import EmailField, ModelForm
from django.utils.translation import gettext_lazy as _

from apps.users.models import Profile, User


class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User
        field_classes = {"email": EmailField}


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    FORM FOR USER CREATION IN THE ADMIN AREA.
    TO CHANGE USER SIGNUP, SEE usersignupform AND usersocialsignupform.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User
        fields = ("email",)
        field_classes = {"email": EmailField}
        error_messages = {
            "email": {"unique": _("This email has already been taken.")},
        }


# class UserSignupForm(SignupForm):
#     """
#     FORM THAT WILL BE RENDERED ON A USER SIGN UP SECTION/SCREEN.
#     DEFAULT FIELDS WILL BE ADDED AUTOMATICALLY.
#     CHECK usersocialsignupform FOR ACCOUNTS CREATED FROM SOCIAL.
#     """
#
#
# class UserSocialSignupForm(SocialSignupForm):
#     """
#     RENDERS THE FORM WHEN USER HAS SIGNED UP USING SOCIAL ACCOUNTS.
#     DEFAULT FIELDS WILL BE ADDED AUTOMATICALLY.
#     SEE usersignupform OTHERWISE.
#     """

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            "picture",
            "real_name",
            "email",
            "location",
            "biography"
        ]
        labels = {
            "picture": _("Profile picture"),
            "real_name": _("Name"),
            "email": _("Email"),
            "location": _("Location"),
            "biography": _("Somthing about you"),
        }
        widgets = {
            "picture": forms.FileInput(attrs={"id": "id_picture", "name": "image_profile", "accept": "image/*", "class": "block w-full cursor-pointer rounded-lg border border-gray-300 bg-gray-50 text-sm text-gray-900 focus:outline-none dark:placeholder-gray-400 dark:border-gray-600 dark:bg-gray-700 dark:text-gray-400"}),
            "real_name": forms.TextInput(attrs={"id": "id_name", "name": "real_name", "class": "block w-full rounded-lg border border-gray-300 bg-gray-50 text-sm text-gray-900 p-2.5 focus:border-blue-500 focus:ring-blue-500 dark:placeholder-gray-400 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:focus:border-blue-500 dark:focus:ring-blue-500"}),
            "email": forms.EmailInput(attrs={"id": "id_email", "name": "email", "maxlength": "254", "require": "true", "class": "block w-full rounded-lg border border-gray-300 bg-gray-50 text-sm text-gray-900 p-2.5 focus:border-blue-500 focus:ring-blue-500 dark:placeholder-gray-400 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:focus:border-blue-500 dark:focus:ring-blue-500"}),
            "location": forms.TextInput(attrs={"id": "id_location", "name": "location", "maxlength": "200", "class": "block w-full rounded-lg border border-gray-300 bg-gray-50 text-sm text-gray-900 p-2.5 focus:border-blue-500 focus:ring-blue-500 dark:placeholder-gray-400 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:focus:border-blue-500 dark:focus:ring-blue-500"}),
            "biography": forms.Textarea(attrs={"id": "id_biography", "name": "biography", "cols": "40", "rows": "3", "maxlength": "500", "class": "block w-full rounded-lg border border-gray-300 bg-gray-50 text-sm text-gray-900 p-2.5 focus:border-blue-500 focus:ring-blue-500 dark:placeholder-gray-400 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:focus:border-blue-500 dark:focus:ring-blue-500"}),
        }
        error_messages = {
            "picture": {
                "invalid_extension": _("This file extension is not supported. Please upload an image."),
            },
            "email": {
                "required": _("Body is required"),
                "invalid": _("Invalid email format"),
                "max_length": _("Location must be 254 characters or less"),
            },
            "location": {
                "max_length": _("Location must be 200 characters or less"),
            },
            "biography": {
                "max_length": _("Biography must be 500 characters or less"),
            }

        }
