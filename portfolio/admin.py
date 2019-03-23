from django.contrib import admin
from .models import Photography, Category, Poem, Drawing


# Register your models here.
@admin.register(Photography)
class PhotographyAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'published', 'created')
    search_fields = ('title',)
    date_hierarchy = 'created'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
    search_fields = ('name',)
    date_hierarchy = 'created'


@admin.register(Poem)
class PoemAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'published')
    search_fields = ('title', 'content')
    date_hierarchy = 'created'


@admin.register(Drawing)
class DrawingAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'created', 'published')
    search_fields = ('title',)
    date_hierarchy = 'created'
