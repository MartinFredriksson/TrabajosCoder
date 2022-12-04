from django.db import models


class hermanos(models.Model):

    Nombre = models.CharField(max_length=12)
    Apellido = models.CharField(max_length=15)

   

