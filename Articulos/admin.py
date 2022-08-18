from django.contrib import admin
from .models import *


class CategoriaAdmin(admin.ModelAdmin):

    readonly_fields = ('creado',)
    search_fields = ('nombre', 'descripcion')
    list_display = ('nombre', 'creado')
    ordering = ('-creado',)


class ArticuloAdmin(admin.ModelAdmin):

    readonly_fields = ('usuario', 'creado', 'actualizado')
    search_fields = ('titulo', 'contenido')
    list_filter = ('publico',)
    list_display = ('titulo', 'publico', 'creado')
    ordering = ('-creado',)

    def save_model(self, request, obj, form, change):

        if not obj.usuario_id:
            obj.usuario_id = request.user.id

        obj.save()


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Articulo, ArticuloAdmin)
