from django.contrib import admin
from django.urls import path
from webcook.views import *

app_name = "webcook"

urlpatterns = [
    
    path('ingredientes', IngredientesView.as_view(), name='ingredientes'),
    path('ingredientes/<int:pk>/', IngredientesDetalleView.as_view(), name='ingredientedetalle'),
    path('temporadas', TemporadasView.as_view(), name = 'temporadas'),
    path('temporadas/<int:pk>/', TemporadasDetalleView.as_view(), name= 'temporadadetalle'),
    path('categorias', CategoriasView.as_view(), name = 'categorias'),
    path('categorias/<int:pk>/', CategoriasDetalleView.as_view(), name = 'categoriadetalle'),
    path('dificultades', DificultadesView.as_view(), name="dificultades"),
    path('dificultades/<int:pk>/', DificultadesDetalleView.as_view(), name='dificultaddetalle'),
    path('recetas', RecetasView.as_view(), name = 'recetas'),
    path('recetas/<int:pk>/', RecetasDetalleView.as_view(), name= 'recetadetalle'),
    path('ingredientesrecetas', IngredientesRecetasView.as_view(), name = 'ingredientes_receta'),
    path('ingredientesrecetas/<int:pk>/', IngredientesRecetasDetalleView.as_view(), name='ingrediente_recetadetalle'),

]
