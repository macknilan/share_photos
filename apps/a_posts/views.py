"""POSTS VIEWS."""
import requests
from bs4 import BeautifulSoup
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from apps.a_posts.forms import PostCreateFrom, PostEditFrom, CommentCreateForm, ReplyCommentCreateForm

# MODELS
from apps.a_posts.models import Post, Tag, Comment, Reply


def home_view(request, tag=None):
    """HOME VIEW."""
    if tag:
        posts = Post.objects.filter(tags__slug=tag)
        tag = get_object_or_404(Tag, slug=tag)
    else:
        posts = Post.objects.all()

    contex = {
        "posts": posts,
        "tag": tag,
    }

    return render(request, "a_posts/home.html", contex)


@login_required
def post_create_view(request):
    """VIEW CREATE A POST."""

    if request.method == "POST":
        form = PostCreateFrom(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            website = requests.get(form.data["image"])
            sourcecode = BeautifulSoup(website.text, "html.parser")
            find_image = sourcecode.select('meta[content^="https://live.staticflickr.com/"]')

            image = find_image[0]['content']
            post.image = image

            find_title = sourcecode.select('h1.photo-title')
            title = find_title[0].text.strip()
            post.title = title

            find_artist = sourcecode.select('a.owner-name')
            artist = find_artist[0].text.strip()
            post.artist = artist

            find_link = sourcecode.select('link')
            link = find_link[0].attrs["href"]
            post.link = link

            post.author = request.user

            post.save()
            # https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#the-save-method
            form.save_m2m()
            return redirect("home")
    else:
        form = PostCreateFrom()

    return render(request, "a_posts/post_create.html", {"form": form})


@login_required
def post_delete_view(request, pk):
    """POST DELETE VIEW."""
    post = get_object_or_404(Post, id=pk, author=request.user)

    if request.method == "POST":
        post.delete()
        messages.success(request, "Post deleted successfully")
        return redirect("home")

    return render(request, "a_posts/post_delete.html", {"post": post})


@login_required
def post_edit_view(request, pk):
    """POST EDIT VIEW."""
    post = get_object_or_404(Post, id=pk, author=request.user)
    form = PostEditFrom(instance=post)

    if request.method == "POST":
        form = PostEditFrom(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully")
            return redirect("home")

    context = {
        "form": form,
        "post": post
    }

    return render(request, "a_posts/post_edit.html", context)


def post_detail_view(request, pk):
    """
    VIEW FOR THE POST DETAIL AND THE FORM TO COMMENT
    """
    post = get_object_or_404(Post, id=pk)
    comment_form = CommentCreateForm()
    reply_comment_form = ReplyCommentCreateForm()

    # CHECK IF THE REQUEST IS A HTTPX REQUEST
    if request.META.get("HTTP_HX_REQUEST"):
        if "top" in request.GET:
            # comments = post.comments.filter(likes__isnull=False).distinct()
            comments = post.comments.annotate(num_likes=Count("likes")).filter(num_likes__gt=0).order_by("-num_likes")

        else:
            comments = post.comments.all()

        return render(
            request,
            "snippets/loop_post_detail_page_comments.html",
            {"comments": comments, "reply_comment_form": reply_comment_form}
        )

    contex = {
        "post": post,
        "comment_form": comment_form,
        "reply_comment_form": reply_comment_form
    }

    return render(request, "a_posts/post_detail.html", contex)


@login_required
def comment_create_view(request, pk):
    """
    VIEW TO CREATE A COMMENT
    """
    post = get_object_or_404(Post, id=pk)
    # FORM TO CREATE A REPLY TO USE IN THE SNIPPETS TEMPLATE
    reply_comment_form = ReplyCommentCreateForm()

    if request.method == "POST":
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.parent_post = post
            comment.save()

    contex = {
        "post": post,
        "comment": comment,
        "reply_comment_form": reply_comment_form
    }

    # return redirect("posts:post-detail", post.id)
    # return render(request, "a_posts/comment.html", {"comment": comment})
    return render(request, "snippets/add_comment.html", contex)


@login_required
def reply_comment_create_view(request, pk):
    """
    VIEW TO CREATE A REPLAY FOR THE COMMENT
    """
    comment = get_object_or_404(Comment, id=pk)
    # FORM TO CREATE A REPLY TO USE IN THE SNIPPETS TEMPLATE
    reply_comment_form = ReplyCommentCreateForm()

    if request.method == "POST":
        form = ReplyCommentCreateForm(request.POST)
        if form.is_valid():
            replay = form.save(commit=False)
            replay.author = request.user
            replay.parent_comment = comment
            replay.save()

    contex = {
        "comment": comment,
        "reply": replay,
        "reply_comment_form": reply_comment_form
    }

    # return redirect("posts:post-detail", comment.parent_post.id)
    return render(request, "snippets/add_reply.html", contex)


@login_required
def comment_delete_view(request, pk):
    """COMMENT DELETE VIEW."""
    post = get_object_or_404(Comment, id=pk, author=request.user)

    if request.method == "POST":
        post.delete()
        messages.success(request, "Comment deleted successfully")
        return redirect("posts:post-detail", post.parent_post.id)

    return render(request, "a_posts/comment_delete.html", {"comment": post})


@login_required
def replay_comment_delete_view(request, pk):
    """REPLY COMMENT DELETE VIEW."""
    reply = get_object_or_404(Reply, id=pk, author=request.user)

    if request.method == "POST":
        reply.delete()
        messages.success(request, "Reply deleted successfully")
        return redirect("posts:post-detail", reply.parent_comment.parent_post.id)

    return render(request, "a_posts/reply_delete.html", {"reply": reply})


def like_toggle(model):
    def inner_func(func):
        def wrapper(request, *args, **kwargs):
            post = get_object_or_404(model, id=kwargs.get("pk"))
            # REMOVE LIKE IF THE USER CLICK AGAIN THE LIKE BUTTON
            like_user_exists = post.likes.filter(email=request.user.email).exists()

            if post.author != request.user:
                if like_user_exists:
                    post.likes.remove(request.user)
                else:
                    post.likes.add(request.user)

            return func(request, post)

        return wrapper

    return inner_func


@login_required
@like_toggle(Post)
def like_post_view(request, post):
    """
    VIEW TO LIKE A POST
    """
    return render(request, "snippets/likes.html", {"post": post})


@login_required
@like_toggle(Comment)
def like_comment_view(request, post):
    """
    VIEW TO LIKE A COMMENT
    """
    return render(request, "snippets/likes_comments.html", {"comment": post})


@login_required
@like_toggle(Reply)
def like_reply_comment_view(request, post):
    """
    VIEW TO LIKE A COMMENT
    """
    return render(request, "snippets/likes_reply_comments.html", {"reply": post})

