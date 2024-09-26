from django.db import models
from trello.models import Lista


class Tarea(models.Model):
    texto = models.CharField(max_length=50)
    lista = models.ForeignKey(
        Lista,
        on_delete = models.CASCADE,
        related_name = 'Tareas'
    )
    orden_Tarea = models.IntegerField()
    archivado = models.BooleanField()


    def __str__(self):
        return self.nombre