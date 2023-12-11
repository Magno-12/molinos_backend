from django.db import models
from django.db.models import Sum

from apps.default.models.base_model import BaseModel


class OtrosInventarioStockEntra(BaseModel):
    codigo = models.CharField(max_length=50)
    descripcion = models.TextField()
    longitud_cm = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fecha = models.DateField()
    entrada_kls = models.DecimalField(max_digits=10, decimal_places=2)
    ponderado_compra = models.DecimalField(max_digits=15, decimal_places=2)
    factura_compra = models.CharField(max_length=50, null=True, blank=True)

    @staticmethod
    def calcular_totales():
        total_entrada_kls = OtrosInventarioStockEntra.objects.aggregate(Sum('entrada_kls'))
        total_ponderado_compra = OtrosInventarioStockEntra.objects.aggregate(Sum('ponderado_compra'))
        return total_entrada_kls, total_ponderado_compra
