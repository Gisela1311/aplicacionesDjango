from django.db import models

# Create your models here.

class Facturas(models.Model):
    NumF = models.IntegerField(verbose_name = "Número de factura")
    NomProv = models.CharField(max_length=300, verbose_name = "Nombre del proveedor")
    FechaF = models.DateField(verbose_name = "Fecha de la factura")
    DireP = models.CharField(max_length=300, verbose_name = "Dirección del proveedor") 
    CCOSTE_CHOICES = [ 
        ('COMERCIAL', 'Comercial'), 
        ('FABRICA 1', 'Fabrica 1'), 
        ('ALMACEN 2', 'Almacen 2') ] 
    CCoste = models.CharField(max_length=20, choices=CCOSTE_CHOICES, default='COMERCIAL', verbose_name = "Centro de coste")
    Mail = models.EmailField(verbose_name="Email del proveedor")
    FechaE = models.DateTimeField(auto_now_add=True)
    FechaM = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.NomProv}, {self.NumF}"


class Detalles(models.Model):
    NomP = models.CharField(max_length=300, verbose_name = "Nombre del producto") 
    Precio = models.DecimalField(max_digits=10, decimal_places=2)
    NumF = models.ForeignKey(Facturas, on_delete=models.CASCADE, related_name='detalles')

    def __str__(self):
        return f"{self.NomP} - {self.Precio}"
