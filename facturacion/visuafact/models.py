from django.db import models

# Create your models here.

class Factura(models.Model):
    NumF = models.IntegerField()
    Cliente = models.CharField(max_length=300)
    FechaF = models.DateField()
    Mail = models.EmailField()
    Dirc= models.CharField(max_length=300)
    ESTADO_CHOICES = [ 
        ('PENDIENTE', 'Pendiente'), 
        ('PAGADA', 'Pagada'), 
        ('CANCELADA', 'Cancelada') ] 
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='PENDIENTE')
    FechaC = models.DateTimeField(auto_now_add=True)
    FechaM = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Factura {self.NumF} - {self.Cliente}"

class DetalleFactura(models.Model):
    NomP = models.CharField(max_length=300)
    Precio = models.DecimalField(max_digits=10, decimal_places=2)
    Tipo = models.CharField(max_length=100)
    PrecioIVA= models.DecimalField(max_digits=10, decimal_places=2)
    NumF = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name='detalles')

    def __str__(self):
        return f"{self.NomP} - {self.Precio}"