from django import template
from ..models import Photography, Category, Drawing, Poem


register = template.Library()


@register.inclusion_tag('portfolio/photography/show_photography_categories.html')
def show_photography_categories(count=10, path=""):
    photographs = Photography.objects.filter(published=True)
    ids_category = []
    for photography in photographs:
        for category in photography.categories.all():
            ids_category.append(category.id)
    if ids_category:
        categories = Category.objects.filter(id__in=ids_category).order_by('name')[:count]
    else:
        categories = None
    return {'categories': categories, 'photographs': photographs, 'path': path}


@register.inclusion_tag('portfolio/drawing/show_drawing_categories.html')
def show_drawing_categories(count=10, path=""):
    drawings = Drawing.objects.filter(published=True)
    ids_category = []
    for drawing in drawings:
        for category in drawing.categories.all():
            ids_category.append(category.id)
    if ids_category:
        categories = Category.objects.filter(id__in=ids_category).order_by('name')[:count]
    else:
        categories = None
    return {'categories': categories, 'drawings': drawings, 'path': path}


@register.inclusion_tag('portfolio/poem/show_poem_categories.html')
def show_poem_categories(count=10, path=""):
    poems = Poem.objects.filter(published=True)
    ids_category = []
    for poem in poems:
        for category in poem.categories.all():
            ids_category.append(category.id)
    if ids_category:
        categories = Category.objects.filter(id__in=ids_category).order_by('name')[:count]
    else:
        categories = None
    return {'categories': categories, 'poems': poems, 'path': path}
