from django.db import models
from core.models import Profile
from django.utils.timezone import now
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorias"
        ordering = ['-created']

    def __str__(self):
        return self.name


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


def custom_post_upload_to(instance, filename):
    try:
        old_instance = Post.objects.get(pk=instance.pk)
    except Post.DoesNotExist:
        old_instance = None
    if old_instance is not None:
        old_instance.image.delete()
    return 'posts/' + filename


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Borrador'),
        ('published', 'Publicado'),
    )
    title = models.CharField(max_length=250, verbose_name="Título")
    content = RichTextUploadingField(verbose_name="Contenido", external_plugin_resources=[(
        'youtube',
        '/static/core/vendor/ckeditor_plugins/youtube/youtube/',
        'plugin.js',
    )],)
    publish = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    image = models.ImageField(verbose_name="Imagen (800x600)", upload_to=custom_post_upload_to)
    author = models.ForeignKey(Profile, verbose_name="Autor", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categorias", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name="Estado")
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"
        ordering = ['-publish']

    def __str__(self):
        return self.title


