from django.contrib import admin
from .models import Post,Category


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish', 'image', 'post_categories', 'status')
    search_fields = ('title', 'content')
    date_hierarchy = 'publish'
    list_filter = ('status', 'categories__name')

    def post_categories(self, obj):
        return ', '.join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorias"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
    search_fields = ('name',)
    date_hierarchy = 'created'


