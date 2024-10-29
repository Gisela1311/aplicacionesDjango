from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import IngredientesSerializers
from .models import Ingredientes
from rest_framework import status
from django.http import Http404
# Create your views here.
 
class Ingredientes_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        ingrediente = Ingredientes.objects.all()
        serializer = IngredientesSerializers(ingrediente, many=True)
        
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = IngredientesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
class Ingredientes_APIView_Detail(APIView):
    def get_object(self, pk):
        try:
            return Ingredientes.objects.get(pk=pk)
        except Ingredientes.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        ingrediente = self.get_object(pk)
        serializer = IngredientesSerializers(ingrediente) 
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        ingrediente = self.get_object(pk)
        serializer = IngredientesSerializers(ingrediente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        ingrediente = self.get_object(pk)
        ingrediente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 