from Articulos.models import *

def get_Categorias(request):

    categorias_en_uso = Articulo.objects.filter(publico=True).values_list('categorias', flat=True)

    categorias = Categoria.objects.filter(id__in=categorias_en_uso).values_list('id', 'nombre')

    return {
        'categorias': categorias,
        'ids': categorias_en_uso
    }
