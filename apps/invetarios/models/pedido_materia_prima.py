from django.db import models

from apps.default.models.base_model import BaseModel


class PedidoMateriaPrima(BaseModel):
    proveedor = models.CharField(max_length=255)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Asumiendo que la cantidad puede no estar siempre presente
    producto = models.CharField(max_length=255)
    observaciones = models.TextField(null=True, blank=True)
