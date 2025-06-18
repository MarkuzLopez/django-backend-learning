from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from drf_yasg.utils import swagger_auto_schema
from .serializers import RegisterSerializerAuth, LoginSerializerAuth
from drf_yasg import openapi

#schema for logout , apply command migrate
logout_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['refresh'],
    properties={
        'refresh': openapi.Schema(type=openapi.TYPE_STRING, description='Refresh token JWT'),
    },
)

@swagger_auto_schema(method='post', request_body=RegisterSerializerAuth, responses={201: RegisterSerializerAuth})
@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    """
    post:
    Crear nuevo usuario auth    
    """
    serializer = RegisterSerializerAuth(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Usuario creado correctamente"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#endpoint login personalizado
@swagger_auto_schema(method='post', request_body=LoginSerializerAuth, responses={200: 'JWT generado'})
@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    """
    post:
    Autentica al usuaior y devuelve el token JWT.
    """
    username = request.data.get('username')
    password =  request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    return Response({"detail": "Credenciales invalidas"}, status=status.HTTP_401_UNAUTHORIZED)

@swagger_auto_schema(method='post', request_body=logout_schema, operation_description="Logout seguro con blacklist")
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    try:
        refresh_token =  request.data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist() # se invalida
        return Response({"message": "Session cerrada correctamente"}, status=status.HTTP_205_RESET_CONTENT)
    except KeyError: 
        return Response({"message": "session cerrada correctamente"}, status=400)
    except TokenError:
        return Response({"error": "Token invalido ya usado"}, status=400)


# Endpoint protegido
@swagger_auto_schema(method='get', responses={200: "OK"})
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    """
    get:
    Vista protegida, requiere token JWT válido.
    """
    return Response({"message": f"Hola {request.user.username}, accediste al endpoint protegido."})
