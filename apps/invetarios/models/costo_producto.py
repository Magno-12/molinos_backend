from django.db import models
from django.db.models import Sum

from apps.default.models.base_model import BaseModel


class CostoProducto(BaseModel):
    referencia = models.CharField(max_length=50)
    descripcion = models.TextField()
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    kg = models.DecimalField(max_digits=10, decimal_places=2)
    precio_por_kg = models.DecimalField(max_digits=15, decimal_places=2)
    factura_compra = models.CharField(max_length=50)
    fecha_actualizacion = models.DateField()

    def obtener_precios_por_ano(self, ano):
        return self.precios_proveedores.filter(ano=ano)

    @property
    def subtotal_compra(self):
        subtotal = self.otrosinventariostockentra_set.aggregate(Sum('valor'))['valor__sum'] or 0
        return subtotal - 4.19

    @property
    def subtotal_entrada(self):
        subtotal = self.otrosinventariostockentra_set.aggregate(Sum('entrada_kls'))['entrada_kls__sum'] or 0
        return subtotal
