from django.contrib import admin
from . models import Profile, Skill


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'profession', 'email', 'city', 'isPublished')
    search_fields = ('name', 'last_name')
    date_hierarchy = 'created'


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill_name', 'image', 'color')
    search_fields = ('skill',)
    date_hierarchy = 'created'
