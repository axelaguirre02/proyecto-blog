from django.urls import path
from . import views

urlpatterns = [
    path('articulos/', views.lista, name='articulos'),
    path('categoria/<int:categoria_id>', views.categoria, name='categoria'),
    path('articulo/<int:articulo_id>', views.articulo, name='articulo'),
]
