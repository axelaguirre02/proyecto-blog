from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from Paginas.models import Pagina


@login_required(ingreso_url='ingreso')
def pagina(request, url):

    pagina = Pagina.objects.get(url=url)

    return render(request, 'paginas/pagina.html', {'pagina': pagina})

