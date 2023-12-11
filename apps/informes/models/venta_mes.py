from django.db import models

from apps.default.models.base_model import BaseModel


class VentaMensual(BaseModel):
    mes = models.DateField()
    valor = models.DecimalField(max_digits=15, decimal_places=2)
