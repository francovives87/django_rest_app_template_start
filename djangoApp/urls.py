# spAgency/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Incluir las rutas de la app 'users' para autenticación JWT y registro
    path('api/auth/', include('apps.users.urls')),  # Prefijo 'api/auth/' para autenticación
]

# Añadir el manejo de archivos estáticos y multimedia solo en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
