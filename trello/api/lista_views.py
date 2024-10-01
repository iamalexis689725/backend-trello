from rest_framework import serializers, viewsets
from rest_framework.response import Response
from trello.models import Lista, Tablero
from rest_framework import status


class ListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lista
        fields = '__all__'


class ListaViewSet(viewsets.ModelViewSet):
    serializer_class = ListaSerializer
    queryset = Lista.objects.all()

    def list(self, request, *args, **kwargs):
        tablero_id = request.query_params.get('tablero_id', None)
        if tablero_id is not None:
            try:
                tablero = Tablero.objects.get(id=tablero_id)
                listas = Lista.objects.filter(tablero=tablero)
                serializer = self.get_serializer(listas, many=True)
                return Response(serializer.data)
            except Tablero.DoesNotExist:
                return Response({'detail': 'Tablero no encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        return super().list(request, *args, **kwargs)
