from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Categoria(models.Model):

    nombre = models.CharField(max_length=100, verbose_name='Nombre:')
    descripcion = models.CharField(max_length=255, verbose_name='Descripcion:')
    creado = models.DateTimeField(auto_now_add=True, verbose_name='Creado')

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nombre


class Articulo(models.Model):

    titulo = models.CharField(max_length=150, verbose_name='Titulo:')
    contenido = RichTextField(verbose_name='Contenido')
    imagen = models.ImageField(default='null', verbose_name='Imagen:', upload_to='articulos')
    publico = models.BooleanField(verbose_name='Publico')
    usuario = models.ForeignKey(User, editable=False, on_delete=models.CASCADE, verbose_name='Usuario')
    categorias = models.ManyToManyField(Categoria, blank=True, verbose_name='Categorias:')
    creado = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    actualizado = models.DateTimeField(auto_now=True, verbose_name='Actualizado')

    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"
        ordering = ['-creado']

    def __str__(self):
        return self.titulo

