from django import template
from ..models import Post, Category


register = template.Library()


@register.inclusion_tag('blog/show_categories.html')
def show_categories(count=10, path=""):
    posts = Post.published.all()
    ids_category = []
    for post in posts:
        for category in post.categories.all():
            ids_category.append(category.id)
    if ids_category:
        categories = Category.objects.filter(id__in=ids_category).order_by('name')[:count]
    else:
        categories = None
    return {'categories': categories, 'posts': posts, 'path': path}
