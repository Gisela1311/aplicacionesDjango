from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Factura, DetalleFactura
from django.http import Http404

# Create your views here.

class FacturaView(generic.ListView):
    template_name = "visuafact/factura.html"
    context_object_name = "lista_factura"

    def get_queryset(self):
        return Factura.objects.all()

class FacturaDetalleView(generic.DetailView):
    model= Factura
    template_name = "visuafact/facturadetalle.html"
    context_object_name = 'factura'

    # def get(self, request, pk, format=None):
    #     dato = get_object_or_404(Factura, id = pk)
    #     detalle = DetalleFactura.objects.all()
    #     return render(request, "visuafact/facturadetalle.html", {"factura":dato, "detalle":detalle})
    
    
    def get(self, request, pk): 
        self.object = self.get_object() 
        detalles = self.object.detalles.all() 
        return render(request, self.template_name, { 
            'factura': self.object, 
            'detalles': detalles,
            })

    # COPLIOT sugiere usar esta función pero no hemos visto el uso de *args y *kwargs

    # def get_context_data(self, **kwargs): 
    #     context = super().get_context_data(**kwargs) 
    #     context['detalles'] = self.object.detalles.all() # Utiliza 'detalles' como related_name en el modelo DetalleFactura 
    #     return context
    
# class DetalleFacturaView(generic.ListView):
#     template_name = "visuafact/detallefactura.html"
#     context_object_name = "lista_detallefactura"

#     def get_queryset(self):
#         return DetalleFactura.objects.all()

# class DetalleFacturaDetalleView(generic.DateDetailView):
#     model= DetalleFactura
#     template_name = "visuafact/facturadetalledetalle.html"

#     def get(self, request, pk, format=None):
#         dato = get_object_or_404(DetalleFactura, id = pk)
#         return render(request, "visuafact/facturadetalledetalle.html", {"detallefactura":dato})


