from django.contrib import admin
from .models import Photography, Category, Poem, Drawing


# Register your models here.
@admin.register(Photography)
class PhotographyAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'published', 'created')
    readonly_fields = ('created', 'updated')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
    readonly_fields = ('created', 'updated')


@admin.register(Poem)
class PoemAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    readonly_fields = ('created', 'updated')


@admin.register(Drawing)
class DrawingAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'created')
    readonly_fields = ('created', 'updated')
