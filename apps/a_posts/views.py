"""Posts views."""
import requests
from bs4 import BeautifulSoup
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404

from apps.a_posts.forms import PostCreateFrom, PostEditFrom
from apps.a_posts.models import Post, Tag


def home_view(request, tag=None):
    """Home view."""
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


def post_create_view(request):
    """Post create view."""

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

            post.save()
            # https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#the-save-method
            form.save_m2m()
            return redirect("home")
    else:
        form = PostCreateFrom()

    return render(request, "a_posts/post_create.html", {"form": form})


def post_delete_view(request, pk):
    """Post delete view."""
    post = get_object_or_404(Post, id=pk)

    if request.method == "POST":
        post.delete()
        messages.success(request, "Post deleted successfully")
        return redirect("home")

    return render(request, "a_posts/post_delete.html", {"post": post})


def post_edit_view(request, pk):
    """Post edit view."""
    post = get_object_or_404(Post, id=pk)
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
    """Detail of the post view."""
    post = get_object_or_404(Post, id=pk)
    return render(request, "a_posts/post_detail.html", {"post": post})









