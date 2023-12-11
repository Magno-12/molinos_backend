from django.db import models

from apps.default.models.base_model import BaseModel


class CajaSkyCreditoSky(BaseModel):
    fecha = models.DateField()
    cliente = models.CharField(max_length=255)
    descripcion = models.TextField()
    valor_negocio = models.DecimalField(max_digits=15, decimal_places=2)
    recibo = models.CharField(max_length=50)
