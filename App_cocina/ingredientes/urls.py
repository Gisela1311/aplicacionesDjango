from django.contrib import admin
from django.urls import path
from ingredientes.views import *

app_name = "ingredientes"

urlpatterns = [
    path('admin', admin.site.urls),
    path('ingredientes', Ingredientes_APIView.as_view()),
    path('ingredientes/<int:pk>/', Ingredientes_APIView_Detail.as_view()),
    path('temporadas', Temporadas_APIView.as_view()),
    path('temporadas/<int:pk>/', Temporadas_APIView_Detail.as_view()),
    path('categorias', Categorias_APIView.as_view()),
    path('categorias/<int:pk>/', Categorias_APIView_Detail.as_view()),
    path('dificultades', Dificultades_APIView.as_view()),
    path('dificultades/<int:pk>/', Dificultades_APIView_Detail.as_view()),
    path('recetas', Recetas_APIView.as_view()),
    path('recetas/<int:pk>/', Recetas_APIView_Detail.as_view()),
    path('ingredientesrecetas', IngredientesRecetas_APIView.as_view()),
    path('ingredientesrecetas/<int:pk>/', IngredientesRecetas_APIView_Detail.as_view()),

]

