from django.shortcuts import render
#APIVIEW imports
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import User,  Clients
from .serializers import UserSerializer, ClientSerializer

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(method='get', responses={200: ClientSerializer(many=True)})
@swagger_auto_schema(method='post', request_body=ClientSerializer, responses={201: ClientSerializer})
@api_view(['GET', 'POST'])
@permission_classes([AllowAny]) #allowany es para  servicio publico
def clients_list_create(request):
    if request.method == 'GET':
        clients = Clients.objects.all()
        serializer = ClientSerializer(clients, many=True)        
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@swagger_auto_schema(method='get', responses={200: ClientSerializer})
@swagger_auto_schema(method='put', request_body=ClientSerializer, responses={200: ClientSerializer})
@swagger_auto_schema(method='delete', responses={204: 'Clienete eliminado'})
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated]) #IsAuthenticated es para servicios privados
def client_detail_update_delete(request, pk):
    try:
        client = Clients.objects.get(pk=pk)
        print('The client id', client)
    except Clients.DoesNotExist:
        return Response({'error': 'Client not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ClientSerializer(client)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # Create your views here.
class UserViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class =  UserSerializer
