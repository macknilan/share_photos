#
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from apps.users.forms import ProfileForm
from apps.users.models import User


def profile_view(request, username=None):
    """
    VIEW FOR THE USER PROFILE AND VIEW FOR THE USER PROFILE LINK
    """
    if username:
        profile = get_object_or_404(User, username=username).profile
    else:
        try:
            profile = request.user.profile
        except:
            raise Http404()

    return render(request, "users/profile.html", {"profile": profile})


@login_required
def profile_edit_view(request):
    """
    VIEW FOR THE USER PROFILE EDIT
    """
    form = ProfileForm(instance=request.user.profile)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect("users:profile")

    # https://docs.djangoproject.com/en/dev/ref/urlresolvers/#reverse
    if request.path == reverse("users:profile-onboarding"):
        template = "users/profile_onboarding.html"
    else:
        template = "users/profile_edit.html"

    return render(request, template, {"form": form})


@login_required
def profile_delete_view(request):
    """
    VIEW FOR THE USER PROFILE DELETE
    """
    user = request.user

    if request.method == "POST":
        # https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.backends.base.SessionBase.flush
        logout(request)
        user.delete()
        messages.success(request, "User deleted successfully")
        return redirect("home")

    return render(request, "users/profile_delete.html")
