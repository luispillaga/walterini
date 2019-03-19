from django.urls import path
from .views import PostListView, PostDetailView, posts_by_category, search_posts

posts_patterns = ([
    path('', PostListView.as_view(), name='post_list'),
    path('<int:post_id>/<slug:page_slug>/', PostDetailView.as_view(), name='post_detail'),
    path('category/<int:category_id>/', posts_by_category, name="posts_by_category"),
    path('search/<value>', search_posts, name="search_posts")
    ], "posts")
