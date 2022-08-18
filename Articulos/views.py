from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Categoria, Articulo


@login_required(ingreso_url='ingreso')
def lista(request):

    articulos = Articulo.objects.all()
    paginator = Paginator(articulos, 2)

    pagina = request.GET.get('pagina')
    pagina_articulos = paginator.get_page(pagina)

    return render(request, 'articulos/lista.html', {'articulos': pagina_articulos})


@login_required(ingreso_url='ingreso')
def categoria(request, categoria_id):

    categoria = get_object_or_404(Categoria, id=categoria_id)
    articulos = Articulo.objects.filter(categorias=categoria)

    return render(request, 'categorias/categoria.html', {'categoria': categoria, 'articulos': articulos})


def articulo(request, articulo_id):

    articulo = get_object_or_404(Articulo, id=articulo_id)

    return render(request, 'articulos/articulo.html', {'articulo': articulo})

