from rest_framework import serializers
from .models import Temporadas, Ingredientes, Categorias, Dificultades, Recetas, IngredientesRecetas

class IngredientesSerializers(serializers.ModelSerializer):
    
    # temporada_nombre = serializers.CharField(source='TempId_fk.NomTemp', read_only=True)
    TempId_fk = serializers.SlugRelatedField(queryset=Temporadas.objects.all(), slug_field='NomTemp')

    class Meta:
        model = Ingredientes
        fields = ['id', 'NomIng', 'TempId_fk']
        # exclude = ['is_removed', 'created', 'modified']
    
class TemporadasSerializers (serializers.ModelSerializer):
    # TempId_fk = serializers.SlugRelatedField(queryset=Temporadas.objects.all(), slug_field='NomTemp')
     class Meta:
        model = Temporadas
        fields = '__all__'
        # exclude = ['is_removed', 'created', 'modified']

class CategoriasSerializers (serializers.ModelSerializer):
    # TempId_fk = serializers.SlugRelatedField(queryset=Temporadas.objects.all(), slug_field='NomTemp')
    

    class Meta:
        model = Categorias
        fields = '__all__'
        # exclude = ['is_removed', 'created', 'modified']

class DificultadesSerializers (serializers.ModelSerializer):
    NomDif = serializers.CharField(max_length=10)
    class Meta:
        model = Dificultades
        fields = '__all__'
        # exclude = ['is_removed', 'created', 'modified']

class RecetasSerializers (serializers.ModelSerializer):
    NomRec = serializers.CharField(max_length=40)
    class Meta:
        model: Recetas 
        fields = '__all__'

class IngredientesRecetasSerializers (serializers.ModelSerializer):
    class Meta:
        model = IngredientesRecetas
        fields = '__all__'

    