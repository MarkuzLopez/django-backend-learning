from django.shortcuts import render
#APIVIEW imports
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import User,  Clients
from .serializers import UserSerializer, ClientSerializer

@api_view(['GET', 'POST'])
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
    
@api_view(['GET', 'PUT', 'DELETE'])
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
