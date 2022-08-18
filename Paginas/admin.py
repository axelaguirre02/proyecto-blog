from atexit import register
from django.contrib import admin
from .models import Pagina


class PaginaAdmin(admin.ModelAdmin):

    readonly_fields = ('creado', 'actualizado')
    search_fields = ('titulo', 'contenido')
    list_filter = ('visibilidad',)
    list_display = ('titulo', 'visibilidad', 'creado')
    ordering = ('-creado',)

admin.site.register(Pagina, PaginaAdmin)
admin.site.site_header = 'Primer proyecto con Django'
admin.site.site_title = 'Proyecto con Django'
admin.site.index_title = 'Panel de Gestion'
