from django.contrib import admin
from . models import Slide
# Register your models here.


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'image', 'color')
    search_fields = ('title', 'subtitle')
    date_hierarchy = 'created'
