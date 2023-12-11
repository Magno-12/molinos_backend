from django.db import models

from apps.default.models.base_model import BaseModel


class PrecioProveedorPorAno(BaseModel):
    producto = models.ForeignKey('CostoProducto', on_delete=models.CASCADE, related_name='precios_proveedores')
    ano = models.IntegerField()
    precio_compra = models.DecimalField(max_digits=15, decimal_places=2)
    proveedor = models.CharField(max_length=255)
