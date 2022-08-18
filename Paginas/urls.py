from django.urls import path
from . import views

urlpatterns = [
    path('pagina/<str:url>',views.pagina, name='pagina'),
]
