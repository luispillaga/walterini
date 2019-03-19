from django.db import models
from ckeditor.fields import RichTextField


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


def custom_photography_upload_to(instance, filename):
    try:
        old_instance = Photography.objects.get(pk=instance.pk)
    except Photography.DoesNotExist:
        old_instance = None
    if old_instance is not None:
        old_instance.image.delete()
    return 'photographs/' + filename


class Photography(models.Model):
    title = models.CharField(verbose_name="Título", max_length=100)
    image = models.ImageField(verbose_name="Imagen", upload_to=custom_photography_upload_to)
    categories = models.ManyToManyField(Category, verbose_name="Categorias", related_name="get_photographs")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    published = models.BooleanField(default=True, verbose_name="Publicar")

    class Meta:
        verbose_name = "Fotografía"
        verbose_name_plural = "Fotografías"
        ordering = ['-created']

    def __str__(self):
        return self.title


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(published=True)


class Poem(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(verbose_name="Contenido", config_name='poem', external_plugin_resources=[(
        'lineheight',
        '/static/core/vendor/ckeditor_plugins/lineheight/lineheight/',
        'plugin.js',
    )],)
    categories = models.ManyToManyField(Category, verbose_name="Categorias", related_name="get_poems")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    published = models.BooleanField(default=True, verbose_name="Publicar")
    objects = models.Manager()
    is_published = PublishedManager()

    class Meta:
        verbose_name = "Poema"
        verbose_name_plural = "Poemas"
        ordering = ['created']

    def __str__(self):
        return self.title


def custom_drawing_upload_to(instance, filename):
    try:
        old_instance = Drawing.objects.get(pk=instance.pk)
    except Drawing.DoesNotExist:
        old_instance = None
    if old_instance is not None:
        old_instance.image.delete()
    return 'drawings/' + filename


class Drawing(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    image = models.ImageField(verbose_name="Imagen", upload_to=custom_drawing_upload_to)
    categories = models.ManyToManyField(Category, verbose_name="Categorias", related_name="get_drawings")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    published = models.BooleanField(default=True, verbose_name="Publicar")

    class Meta:
        verbose_name = "Dibujo"
        verbose_name_plural = "Dibujos"
        ordering = ['created']

    def __str__(self):
        return self.title
