from django.urls import path
from .views import PhotographyListView, photos_by_category, DrawingListView, drawings_by_category, PoemListView, \
        PoemDetailView, poems_by_category, search_poems


portfolio_patterns = ([
        path('photography/', PhotographyListView.as_view(), name='photography_list'),
        path('photography/category/<int:category_id>/', photos_by_category, name="photos_by_category"),
        path('drawing/', DrawingListView.as_view(), name='drawing_list'),
        path('drawing/category/<int:category_id>/', drawings_by_category, name='drawings_by_category'),
        path('poem/', PoemListView.as_view(), name='poem_list'),
        path('poem/<int:poem_id>/<slug:page_slug>/', PoemDetailView.as_view(), name='poem_detail'),
        path('poem/category/<int:category_id>/', poems_by_category, name="poems_by_category"),
        path('poem/search/<value>', search_poems, name="search_poems")
    ], "projects")
