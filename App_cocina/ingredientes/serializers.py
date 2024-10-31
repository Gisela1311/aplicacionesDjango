from rest_framework import serializers
from .models import Temporadas, Ingredientes, Categorias, Dificultades

class IngredientesSerializers(serializers.ModelSerializer):
    
    # temporada_nombre = serializers.CharField(source='TempId_fk.NomTemp', read_only=True)
    TempId_fk = serializers.SlugRelatedField(queryset=Temporadas.objects.all(), slug_field='NomTemp')

    class Meta:
        model = Ingredientes
        fields = ['id', 'NomIng', 'TempId_fk']
        # exclude = ['is_removed', 'created', 'modified']
    
class TemporadasSerializers (serializers.ModelSerializer):
    class Meta:
        model = Temporadas
        fields = '__all __'
        # exclude = ['is_removed', 'created', 'modified']

class CategoriasSerializers (serializers.ModelSerializer):
    NomCat = serializers.CharField(max_length=10)

    class Meta:
        model = Categorias
        fields = '__all __'
        # exclude = ['is_removed', 'created', 'modified']

class DificultadesSerializers (serializers.ModelSerializer):
    NomDif = serializers.CharField(max_length=10)
    class Meta:
        model = Dificultades
        fields = '__all __'
        # exclude = ['is_removed', 'created', 'modified']
    