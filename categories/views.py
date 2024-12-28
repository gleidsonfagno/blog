# # Importa classes genéricas fornecidas pelo Django REST Framework para criar views rapidamente.
# from rest_framework import generics

# # Importa o modelo Category do arquivo models.py. Este é o modelo que será manipulado pelas views.
# from .models import Category

# # Importa o serializer correspondente, que será usado para converter instâncias do modelo em JSON e vice-versa.
# from .serializers import CategorySerializer

# # Define uma view para listar todas as categorias e criar novas categorias.
# class CategoryListCreateView(generics.ListCreateAPIView):
#     # Define o queryset, que é o conjunto de dados do modelo Category que será usado nesta view.
#     # Aqui, estamos buscando todas as categorias no banco de dados.
#     queryset = Category.objects.all()

#     # Define a classe serializer que será usada para validar e formatar os dados.
#     # O serializer é responsável por transformar objetos do modelo em JSON e validar dados enviados.
#     serializer_class = CategorySerializer

# # Define uma view para obter os detalhes de uma categoria específica, atualizá-la ou excluí-la.
# class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
#     # Define o queryset, similar à view anterior, mas aqui será filtrado por ID automaticamente.
#     # Quando um ID específico é passado na URL, o Django REST Framework busca esse objeto no banco.
#     queryset = Category.objects.all()

#     # Define a classe serializer para manipular os dados de entrada e saída, assim como na view anterior.
#     serializer_class = CategorySerializer

from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
