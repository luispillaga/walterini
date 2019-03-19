from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Photography, Category, Drawing, Poem
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.views.generic.edit import FormMixin
from blog.forms import SearchForm


# Create your views here.
class PhotographyListView(ListView):
    queryset = Photography.objects.filter(published=True)
    context_object_name = 'photographs'
    template_name = 'portfolio/photography/photography_list.html'
    paginate_by = 12


def photos_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    # posts = Post.objects.filter(categories=category) rudimentario
    return render(request, "portfolio/photography/photos_by_category.html", {'category': category})


class DrawingListView(ListView):
    queryset = Drawing.objects.filter(published=True)
    context_object_name = 'drawings'
    template_name = 'portfolio/drawing/drawing_list.html'
    paginate_by = 12


def drawings_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    # posts = Post.objects.filter(categories=category) rudimentario
    return render(request, "portfolio/drawing/drawings_by_category.html", {'category': category})


class PoemListView(FormMixin, ListView):
    queryset = Poem.objects.filter(published=True)
    context_object_name = 'poems'
    template_name = 'portfolio/poem/poem_list.html'
    paginate_by = 12
    form_class = SearchForm

    def post(self, request, *args, **kwargs):
        return redirect(reverse_lazy('projects:search_poems', args=[request.POST.get('value')]))


class PoemDetailView(FormMixin, DetailView):
    model = Poem
    template_name = 'portfolio/poem/poem_details.html'
    form_class = SearchForm

    def get_object(self):
        return get_object_or_404(Poem, id=self.kwargs['poem_id'])

    def post(self, request, *args, **kwargs):
        return redirect(reverse_lazy('projects:search_poems', args=[request.POST.get('value')]))


def poems_by_category(request, category_id):
    if request.POST:
        return redirect(reverse_lazy('projects:search_poems', args=[request.POST.get('value')]))
    else:
        category = get_object_or_404(Category, id=category_id)
        # posts = Post.objects.filter(categories=category) rudimentario
        return render(request, "portfolio/poem/poems_by_category.html", {'category': category})


def search_poems(request, value):
    if request.POST:
        return redirect(reverse_lazy('projects:search_poems', args=[request.POST.get('value')]))
    else:
        search_vector = SearchVector('title', weight='A') + SearchVector('content', weight='B')
        search_query = SearchQuery(value)
        results = Poem.is_published.annotate(
            search=search_vector,
            rank=SearchRank(search_vector, search_query)
        ).filter(search=search_query).order_by('-rank')
        return render(request, "portfolio/poem/founded_poems.html", {'results': results, 'value': value})
