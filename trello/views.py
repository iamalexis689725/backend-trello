from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from trello.api import UsuarioSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes


@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])

    if not user.check_password(request.data['password']):
        return Response({"error": "Invalid password"}, status=status.HTTP_401_UNAUTHORIZED)

    token, created = Token.objects.get_or_create(user=user)
    serializer = UsuarioSerializer(instance=user)

    return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_200_OK)




@api_view(['POST'])
def register(request):
    # Asegúrate de que el email está en la solicitud
    if 'email' not in request.data:
        return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)

    # Crea un nuevo usuario con los datos de la solicitud
    user = User(
        username=request.data['username'],
        email=request.data['email'],  # Asigna el email aquí
    )
    user.set_password(request.data['password'])  # Asegúrate de encriptar la contraseña
    user.save()

    token = Token.objects.create(user=user)

    # Serializa los datos del usuario
    serializer = UsuarioSerializer(instance=user)

    return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    serializer = UsuarioSerializer(instance=request.user, context={'request': request})
    return Response(serializer.data, status=status.HTTP_200_OK)

