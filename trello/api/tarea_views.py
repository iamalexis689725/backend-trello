from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend  # Asegúrate de esta importación
from rest_framework import filters
from trello.models import Tarea, Lista

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'


class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ['archivado']

    def list(self, request, *args, **kwargs):
        lista_id = request.query_params.get('lista_id', None)
        archivado = request.query_params.get('archivado', None)
        # Filtro las tareas por lista_id y archivado
        tareas = Tarea.objects.all()
        if lista_id is not None:
            try:
                lista = Lista.objects.get(id=lista_id)
                tareas = tareas.filter(lista=lista)
            except Lista.DoesNotExist:
                return Response({'detail': 'Lista no encontrada.'}, status=status.HTTP_404_NOT_FOUND)
        if archivado is not None:
            tareas = tareas.filter(archivado=archivado.lower() == 'true')
        serializer = self.get_serializer(tareas, many=True)
        return Response(serializer.data)
