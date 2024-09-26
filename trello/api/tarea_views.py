from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework import status
from trello.models import Tarea, Lista

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'


class TareaViewSet(viewsets.ModelViewSet):
    serializer_class = TareaSerializer
    queryset = Tarea.objects.all()

    def list(self, request, *args, **kwargs):
        # Obtener el parámetro de consulta 'lista_id'
        lista_id = request.query_params.get('lista_id', None)
        if lista_id is not None:
            try:
                lista = Lista.objects.get(id=lista_id)
                tareas = Tarea.objects.filter(lista=lista)
                serializer = self.get_serializer(tareas, many=True)
                return Response(serializer.data)
            except Lista.DoesNotExist:
                return Response({'detail': 'Lista no encontrada.'}, status=status.HTTP_404_NOT_FOUND)

        # Si no se proporciona 'lista_id', devuelve todas las tareas
        return super().list(request, *args, **kwargs)
