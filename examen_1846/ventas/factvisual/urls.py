from django.contrib import admin
from django.urls import path
from factvisual.views import *

app_name = "factvisual"

urlpatterns = [
    
    path('facturas', FacturasView.as_view(), name = 'facturas'),
    path('facturas/<int:pk>/', FacturasDetalleView.as_view(), name = 'facturasdetalle'),
   
]