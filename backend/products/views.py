from django.shortcuts import render
#apiview
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from .models import Product
from .serializers import ProductSerializer

# Create your views here.
# endpoint get and post
@swagger_auto_schema(method='get', responses={200: ProductSerializer(many=True)})
@swagger_auto_schema(method='post', request_body=ProductSerializer, responses={201: ProductSerializer})
@api_view(['GET', 'POST'])
def product_list_create(request):
    """
    get:
    Devuelve una lista de productos.

    post:
    Crea un nuevo producto.
    """
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)    
    
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@swagger_auto_schema(method='get', responses={200: ProductSerializer})
@swagger_auto_schema(method='put', request_body=ProductSerializer, responses={200: ProductSerializer})
@swagger_auto_schema(method='delete', responses={204: 'Product eliminado'})
@api_view(['GET', 'PUT', 'DELETE'])
def product_delete_put(request, pk):
    """_summary_
    get:
    Retorna un producto por ID
    
    put: 
    Actualiza los datos de un producto
    
    delete:
    Elimia producto por ID

    Args:
        request (_type_): _description_
        pk (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
      product = Product.objects.get(pk=pk)      
    except Product.DoesNotExist:
        return Response({'error': 'Producto no enconrtrado'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)