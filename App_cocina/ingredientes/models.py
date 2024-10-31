from django.db import models

# Create your models here.
class Temporadas(models.Model):
    NomTemp = models.CharField(max_length=10)

    # def __str__(self):
    #     return f"{self.NomTemp}"

class Ingredientes(models.Model):
    NomIng = models.CharField(max_length=40)
    TempId_fk = models.ForeignKey(Temporadas, on_delete=models.CASCADE)

class Categorias(models.Model):
    NomCat = models.CharField(max_length=10)
    
class Dificultades(models.Model):
    NomDif = models.CharField(max_length=10)

class Recetas(models.Model):
    NomRec = models.CharField(max_length=40)
    ElRec = models.CharField(max_length=600)
    TREc = models.CharField(max_length=15)
    DifId_fk = models.ForeignKey(Dificultades, on_delete=models.CASCADE)
    CatId_fk = models.ForeignKey(Categorias, on_delete=models.CASCADE)

class IngredientesRecetas(models.Model):
    IngId_fk = models.ForeignKey(Ingredientes, on_delete= models.CASCADE)
    PesoIng = models.IntegerField(default=0)
    RecId = models.ForeignKey(Recetas, on_delete=models.CASCADE)





     