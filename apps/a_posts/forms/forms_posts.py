"""
Forms for the posts app
"""
from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, Textarea, TextInput
from django.utils.translation import gettext_lazy as _

from apps.a_posts.models import Comment, Post, Reply


class PostCreateFrom(ModelForm):
    """
    Post create form.
    """

    def clean_body(self):
        """Validate body."""
        data = self.cleaned_data["body"]
        if len(data) < 10:
            raise ValidationError(_("The text is too short"))
        return data

    class Meta:
        model = Post
        fields = [
            # "title",
            "body",
            "image",
            "tags"
        ]
        labels = {
            # "title":  _("Title"),
            "body": _("Body"),
            "image": _("Image"),
            "tags": _("Tags for the post"),
        }
        widgets = {
            # "title": forms.TextInput(attrs={"required": True, "placeholder": "write a title ...", "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"}),
            "body": forms.Textarea(attrs={"required": True, "placeholder": "write a body ..", "rows": 3, "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"}),
            "image": forms.TextInput(attrs={"required": True, "placeholder": "write a url image ..", "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"}),
            "tags": forms.CheckboxSelectMultiple(attrs={"class": "bg-blue-100 text-blue-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded dark:bg-gray-700 dark:text-blue-400 border border-blue-400"})
        }
        error_messages = {
            # "title": {
            #     "required": _("Title is required"),
            # },
            "body": {
                "required": _("Body is required"),
            },
            "image": {
                "required": _("Image url is required"),
            },
            "tags": {
                "required": _("Tag is required"),
            }
        }


class PostEditFrom(ModelForm):
    """
    Post edit form.
    """

    def clean_body(self):
        """Validate body."""
        data = self.cleaned_data["body"]
        if len(data) < 10:
            raise ValidationError(_("The text is too short"))
        return data

    class Meta:
        model = Post
        fields = [
            "body",
            "tags"
        ]
        labels = {
            "body": _(""),  # _("Body"),
            "tags": _(""),  # _("Tags for the post")
        }
        widgets = {
            "body": forms.Textarea(attrs={"required": True, "rows": 4, "maxlength": 500, "class": "block w-full rounded-lg border border-gray-300 bg-gray-50 text-sm text-gray-900 p-2.5 focus:border-blue-500 focus:ring-blue-500 dark:placeholder-gray-400 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:focus:border-blue-500 dark:focus:ring-blue-500"}),
            "tags": forms.CheckboxSelectMultiple(attrs={"class": "bg-blue-100 text-blue-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded dark:bg-gray-700 dark:text-blue-400 border border-blue-400"})
        }
        error_messages = {
            "body": {
                "required": _("Body is required"),
            },
            "tags": {
                "required": _("Tag is required"),
            },
        }


class CommentCreateForm(ModelForm):
    """
    FORM FOR THE FORM TO CREATE A COMMENT
    """
    class Meta:
        model = Comment
        fields = [
            "body",
        ]
        labels = {
            "body": _(""),
        }
        widgets = {
            "body": forms.Textarea(attrs={"id": "post-comment", "required": True, "placeholder": "write a comment ..", "rows": 2, "maxlenght": "150", "class": "w-full border-0 bg-white px-0 text-sm text-gray-900 focus:ring-0 dark:placeholder-gray-400 dark:bg-gray-800 dark:text-white"}),
        }
        error_messages = {
            "body": {
                "required": _("Your comment is required"),
                "max_length": _("Biography must be 150 characters or less"),
            },
        }


class ReplyCommentCreateForm(ModelForm):
    """
    FORM FOR THE FORM TO CREATE A REPLY COMMENT
    """
    class Meta:
        model = Reply
        fields = [
            "body",
        ]
        labels = {
            "body": _(""),
        }
        widgets = {
            "body": forms.Textarea(attrs={"id": "reply-comment", "required": True, "placeholder": "add your comment ..", "rows": 1, "maxlenght": "150", "class": "block w-full rounded-lg border border-gray-300 bg-gray-50 p-4 text-sm text-gray-900 focus:border-blue-500 focus:ring-blue-500 dark:placeholder-gray-400 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:focus:border-blue-500 dark:focus:ring-blue-500"}),
        }
        error_messages = {
            "body": {
                "required": _("Your comment is required"),
                "max_length": _("The comment must be 150 characters or less"),
            },
        }
