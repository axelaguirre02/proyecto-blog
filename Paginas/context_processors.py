from .models import Pagina

def get_Paginas(request):

    paginas = Pagina.objects.filter(visibilidad=True).order_by('orden').values_list('titulo', 'url')
    return {
        'paginas': paginas
    }

