from django.contrib.auth.models import User
from django.db import models


class Tablero(models.Model):
    nombre = models.CharField(max_length=50)
    usuario = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'tableros'
    )


    def __str__(self):
        return self.nombre