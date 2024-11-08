from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Facturas, Detalles
from django.http import Http404

# Create your views here.

class FacturasView(generic.ListView):
    template_name = "factvisual/facturas.html"
    context_object_name = "lista_facturas"

    def get_queryset(self):
        return Facturas.objects.all()

class FacturasDetalleView(generic.DetailView):
    model= Facturas
    template_name = "factvisual/facturasdetalle.html"
    context_object_name = 'facturas'

    
        
    def get(self, request, pk): 
        self.object = self.get_object() 
        detalles = self.object.detalles.all()
        total = self.object.detalles.all().aggregate(Sum("Precio"))['Precio__sum']
        return render(request, self.template_name, { 
            'facturas': self.object, 
            'detalles': detalles,
            'total' : total
            })