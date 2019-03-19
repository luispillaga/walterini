from django import template
from core.models import Profile


register = template.Library()


@register.simple_tag
def get_profile():
    try:
        profile = Profile.objects.get(isPublished=True)
    except Profile.DoesNotExist:
        profile = None
    return profile
