#
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from apps.a_posts.forms import ReplyCommentCreateForm
from apps.users.forms import ProfileForm
from apps.users.models import User


def profile_view(request, username=None):
    """
    VIEW FOR THE USER PROFILE AND VIEW FOR THE USER PROFILE LINK
    """
    if username:
        # PROFILE TAKING THE USERNAME
        profile = get_object_or_404(User, username=username).profile
    else:
        try:
            # PROFILE OF THE LOGIN USER
            profile = request.user.profile
        except:
            raise Http404()

    posts = profile.user.posts.all()

    # CHECK IF THE REQUEST IS A HTTPX REQUEST
    if request.META.get("HTTP_HX_REQUEST"):
        template_name = "snippets/loop_profile_posts.html"
        context = {}

        if "top-posts" in request.GET:
            posts = profile.user.posts.annotate(num_likes=Count("likes")).filter(num_likes__gt=0).order_by("-num_likes")
            context = {"posts": posts}
        elif "top-comments" in request.GET:
            reply_comment_form = ReplyCommentCreateForm()
            comments = profile.user.comments.annotate(num_likes=Count("likes")).filter(num_likes__gt=0).order_by("-num_likes")
            template_name = "snippets/loop_profile_comments.html"
            context = {"comments": comments, "reply_comment_form": reply_comment_form}
        elif "liked-post" in request.GET:
            posts = profile.user.liked_posts.order_by("created_at")
            context = {"posts": posts}
        else:
            posts = posts.order_by("-created_at")
            context = {"posts": posts}

        return render(request, template_name, context)

    context = {
        "profile": profile,
        "posts": posts
    }

    return render(request, "users/profile.html", context)


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
