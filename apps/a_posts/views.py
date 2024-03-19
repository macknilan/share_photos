"""POSTS VIEWS."""
import requests
from bs4 import BeautifulSoup
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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

    categories = Tag.objects.all()

    contex = {
        "posts": posts,
        "categories": categories,
        "tag": tag
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
    DETAIL OF THE POST VIEW AND PRESENT THE FORM TO COMMENT
    """
    post = get_object_or_404(Post, id=pk)
    comment_form = CommentCreateForm()
    reply_comment_form = ReplyCommentCreateForm()

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

    if request.method == "POST":
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.parent_post = post
            comment.save()

    return redirect("posts:post-detail", post.id)


@login_required
def reply_comment_create_view(request, pk):
    """
    VIEW TO CREATE A REPLAY FOR THE COMMENT
    """
    comment = get_object_or_404(Comment, id=pk)

    if request.method == "POST":
        form = ReplyCommentCreateForm(request.POST)
        if form.is_valid():
            replay = form.save(commit=False)
            replay.author = request.user
            replay.parent_comment = comment
            replay.save()

    return redirect("posts:post-detail", comment.parent_post.id)


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
    """REPLAY COMMENT DELETE VIEW."""
    reply = get_object_or_404(Reply, id=pk, author=request.user)

    if request.method == "POST":
        reply.delete()
        messages.success(request, "Reply deleted successfully")
        return redirect("posts:post-detail", reply.parent_comment.parent_post.id)

    return render(request, "a_posts/reply_delete.html", {"reply": reply})


