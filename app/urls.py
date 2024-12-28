from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

# View simples para a página inicial
def home(request):
    return HttpResponse("Bem-vindo ao Blog API!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # Rota para a página inicial
     path('api/', include('categories.urls')),
    # path('api/', include('posts.urls')),  # Inclua as URLs do app `posts`
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:  # Apenas no modo de desenvolvimento
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)