from django.db import models
from colorfield.fields import ColorField


def custom_slide_upload_to(instance, filename):
    try:
        old_instance = Slide.objects.get(pk=instance.pk)
    except Slide.DoesNotExist:
        old_instance = None
    if old_instance is not None:
        old_instance.image.delete()
    return 'slides/' + filename


# Create your models here.
class Slide(models.Model):
    title = models.CharField(verbose_name="Título", max_length=100)
    subtitle = models.CharField(verbose_name="Subtítulo", max_length=200)
    image = models.ImageField(verbose_name="Imagen", upload_to=custom_slide_upload_to)
    color = ColorField(default='#000000')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Sliders"
        ordering = ['-created']

    def __str__(self):
        return self.title

