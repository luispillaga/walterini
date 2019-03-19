from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from blog.forms import SearchForm
from .models import Post, Category
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


# Create your views here.
class PostListView(FormMixin, ListView):
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'
    paginate_by = 12
    form_class = SearchForm

    def get_queryset(self):
        return Post.published.all()

    def post(self, request, *args, **kwargs):
        return redirect(reverse_lazy('posts:search_posts', args=[request.POST.get('value')]))


class PostDetailView(FormMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    form_class = SearchForm

    def get_object(self):
        return get_object_or_404(Post, id=self.kwargs['post_id'])

    def post(self, request, *args, **kwargs):
        return redirect(reverse_lazy('posts:search_posts', args=[request.POST.get('value')]))


def posts_by_category(request, category_id):
    if request.POST:
        return redirect(reverse_lazy('posts:search_posts', args=[request.POST.get('value')]))
    else:
        category = get_object_or_404(Category, id=category_id)
        # posts = Post.objects.filter(categories=category) rudimentario
        return render(request, "blog/posts_by_category.html", {'category': category})


def search_posts(request, value):
    if request.POST:
        return redirect(reverse_lazy('posts:search_posts', args=[request.POST.get('value')]))
    else:
        search_vector = SearchVector('title', weight='A') + SearchVector('content', weight='B')
        search_query = SearchQuery(value)
        results = Post.published.annotate(
            search=search_vector,
            rank=SearchRank(search_vector, search_query)
        ).filter(search=search_query).order_by('-rank')
        return render(request, "blog/founded_posts.html", {'results': results, 'value': value})
