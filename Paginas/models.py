from django.db import models
from ckeditor.fields import RichTextField

class Pagina(models.Model):

    titulo = models.CharField(max_length=30, verbose_name="Titulo:")
    contenido = RichTextField(verbose_name="Contenido:")
    url = models.CharField(max_length=150, unique=True, verbose_name="URL:")
    orden = models.IntegerField(default=0, verbose_name='Orden:')
    visibilidad = models.BooleanField(verbose_name="Visible")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = "Pagina"
        verbose_name_plural = "Paginas"

    def __str__(self):
        return self.titulo

