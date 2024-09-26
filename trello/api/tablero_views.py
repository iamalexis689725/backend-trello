from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework import status
from trello.models import Tablero


class TableroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tablero
        fields = '__all__'


class TableroViewSet(viewsets.ModelViewSet):
    serializer_class = TableroSerializer
    queryset = Tablero.objects.all()

    def list(self, request, *args, **kwargs):
        # Si se proporciona un ID de usuario en la URL, filtra por usuario
        user_id = request.query_params.get('user_id', None)
        if user_id is not None:
            try:
                user = User.objects.get(id=user_id)
                tableros = Tablero.objects.filter(usuario=user)
                serializer = self.get_serializer(tableros, many=True)
                return Response(serializer.data)
            except User.DoesNotExist:
                return Response({'detail': 'Usuario no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        # Si no se proporciona un ID de usuario, devuelve todos los tableros
        return super().list(request, *args, **kwargs)
