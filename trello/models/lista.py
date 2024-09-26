from django.db import models
from trello.models import Tablero


class Lista(models.Model):
    nombre = models.CharField(max_length=50)
    tablero = models.ForeignKey(
        Tablero,
        on_delete = models.CASCADE,
        related_name = 'Listas'
    )


    def __str__(self):
        return self.nombre