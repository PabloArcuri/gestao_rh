from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('apps.core.urls')),
    path('funcionarios/', include('apps.funcionarios.urls')),
    path('departamentos/', include('apps.departamentos.urls')),
    path('documentos/', include('apps.documentos.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('empresa/', include('apps.empresas.urls')),
    path('registro_hora_extra/', include('apps.registro_hora_extra.urls')),
    path('admin/', admin.site.urls),
  
    
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
