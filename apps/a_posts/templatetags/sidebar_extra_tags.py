from django.template import Library

from apps.a_posts.models import Tag


register = Library()


@register.inclusion_tag("includes/sidebar.html")
def sidebar_extra_tag_view():
    """
    RETURN CUSTOM TEMPLATE TAG TO INCLUDE IN THE SIDEBAR
    """

    categories = Tag.objects.all()

    context = {
        "categories": categories,
    }

    return context

