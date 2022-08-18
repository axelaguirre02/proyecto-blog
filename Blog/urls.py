from django.contrib import admin
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Principal.urls')),
    path('', include('Paginas.urls')),
    path('', include('Articulos.urls')),
]

if settings.DEBUG:

    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
