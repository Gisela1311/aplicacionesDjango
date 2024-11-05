from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views import generic
from ingredientes.models import Ingredientes, Temporadas, Dificultades, Categorias, Recetas, IngredientesRecetas
from django.http import Http404


# Create your views here.

class CategoriasView(generic.ListView):
    template_name = "webcook/categorias.html"
    context_object_name = "lista_categorias"

    def get_queryset(self):
        return Categorias.objects.all()

class CategoriasDetalleView(generic.DateDetailView):
    model= Categorias
    template_name = "webcook/categoriadetalle.html"

    def get(self, request, pk, format=None):
        categoria = get_object_or_404(Categorias, id = pk)
        return render(request, "webcook/categoriadetalle.html", {"categoria":categoria})

class IngredientesView(generic.ListView):
    template_name = "webcook/ingredientes.html"
    context_object_name = "lista_ingredientes"

    def get_queryset(self):
        return Ingredientes.objects.all()

class IngredientesDetalleView(generic.DateDetailView):
    model= Ingredientes
    template_name = "webcook/ingredientedetalle.html"

    def get(self, request, pk, format=None):
        ingrediente = get_object_or_404(Ingredientes, id = pk)
        return render(request, "webcook/ingredientedetalle.html", {"ingrediente":ingrediente})
    
class TemporadasView(generic.ListView):
    template_name = "webcook/temporadas.html"
    context_object_name = "lista_temporadas"

    def get_queryset(self):
        return Temporadas.objects.all()

class TemporadasDetalleView(generic.DateDetailView):
    model= Temporadas
    template_name = "webcook/temporadadetalle.html"

    def get(self, request, pk, format=None):
        temporada = get_object_or_404(Temporadas, id = pk)
        return render(request, "webcook/temporadadetalle.html", {"temporada":temporada})
    
class DificultadesView(generic.ListView):
    template_name = "webcook/dificultades.html"
    context_object_name = "lista_dificultades"

    def get_queryset(self):
        return Dificultades.objects.all()

class DificultadesDetalleView(generic.DateDetailView):
    model= Dificultades
    template_name = "webcook/dificultaddetalle.html"

    def get(self, request, pk, format=None):
        dificultad = get_object_or_404(Dificultades, id = pk)
        return render(request, "webcook/dificultaddetalle.html", {"dificultad":dificultad})
    
class RecetasView(generic.ListView):
    template_name = "webcook/recetas.html"
    context_object_name = "lista_recetas"

    def get_queryset(self):
        return Recetas.objects.all()

class RecetasDetalleView(generic.DateDetailView):
    model= Recetas
    template_name = "webcook/recetadetalle.html"

    def get(self, request, pk, format=None):
        receta = get_object_or_404(Recetas, id = pk)
        return render(request, "webcook/recetadetalle.html", {"receta":receta})
    
class IngredientesRecetasView(generic.ListView):
    template_name = "webcook/ingredientes_receta.html"
    context_object_name = "lista_ingredientes_receta"

    def get_queryset(self):
        return IngredientesRecetas.objects.all()

class IngredientesRecetasDetalleView(generic.DateDetailView):
    model= IngredientesRecetas
    template_name = "webcook/ingrediente_recetadetalle.html"

    def get(self, request, pk, format=None):
        ingredientereceta = get_object_or_404(IngredientesRecetas, id = pk)
        return render(request, "webcook/ingrediente_recetadetalle.html", {"ingredientereceta":ingredientereceta})