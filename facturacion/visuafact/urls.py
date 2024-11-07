from django.contrib import admin
from django.urls import path
from visuafact.views import *

app_name = "visuafact"

urlpatterns = [
    
    path('factura', FacturaView.as_view(), name = 'factura'),
    path('factura/<int:pk>/', FacturaDetalleView.as_view(), name = 'facturadetalle'),
    # path('detallefactura', DetalleFacturaView.as_view(), name = 'detallefactura'),
    # path('detallefactura/<int:pk>/',DetalleFacturaDetalleView.as_view(), name = 'detallefacturadetalle')
]