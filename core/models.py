from django.db import models
from django.contrib.auth.models import User
from colorfield.fields import ColorField


def custom_skill_upload_to(instance, filename):
    try:
        old_instance = Skill.objects.get(pk=instance.pk)
    except Skill.DoesNotExist:
        old_instance = None
    if old_instance is not None:
        old_instance.image.delete()
    return 'skills/' + filename


def custom_profile_upload_to(instance, filename):
    try:
        old_instance = Profile.objects.get(pk=instance.pk)
    except Profile.DoesNotExist:
        old_instance = None
    if old_instance is not None:
        old_instance.image.delete()
    return 'profiles/' + filename


# Create your models here.
class Skill(models.Model):
    skill_name = models.CharField(verbose_name="Habilidad", max_length=100)
    image = models.ImageField(upload_to=custom_skill_upload_to, verbose_name="Logo")
    color = ColorField(default='#2c98f0', verbose_name="Color del logo")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"
        ordering = ['-created']

    def __str__(self):
        return self.skill_name


class Profile(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=100)
    last_name = models.CharField(verbose_name="Apellidos", max_length=200)
    image = models.ImageField(upload_to=custom_profile_upload_to, verbose_name="Imagen")
    profession = models.CharField(max_length=100, blank=True, verbose_name="Profesión")
    email = models.EmailField(verbose_name="Email", null=True, blank=True)
    address = models.CharField(verbose_name="Dirección", max_length=200, null=True, blank=True)
    mobile = models.CharField(verbose_name="Celular", max_length=15, blank=True, null=True)
    city = models.CharField(max_length=50, verbose_name="Ciudad", blank=True, null=True)
    biography = models.TextField(verbose_name="Biografía")
    skills = models.ManyToManyField(Skill, verbose_name="Habilidades", related_name="get_profiles")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    isPublished = models.BooleanField(default=False, verbose_name="Publicar", unique=True)

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"
        ordering = ['-created']

    def __str__(self):
        return self.name + " " + self.last_name

