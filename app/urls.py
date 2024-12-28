from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bem-vindo ao Blog API!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('api/', include('categories.urls')),
]

# Adicionar configuração para servir arquivos de mídia durante o desenvolvimento e produção
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
