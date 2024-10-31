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

# class Recetas 

# class IngredientesRecetas
     