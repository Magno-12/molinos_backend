from django.db import models
from decimal import Decimal

from apps.default.models.base_model import BaseModel


class Compra(BaseModel):
    fecha = models.DateField()
    nombre_proveedor = models.CharField(max_length=255)
    cedula_nit = models.CharField(max_length=20)
    contacto = models.CharField(max_length=255)
    descripcion = models.TextField()
    factura = models.CharField(max_length=50)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    centro_costos = models.CharField(max_length=255)
    medio_pago = models.CharField(max_length=255)
    valor_bruto = models.DecimalField(max_digits=15, decimal_places=2)
    rtefte = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    iva = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    neto = models.DecimalField(max_digits=15, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        self.iva = self.valor_bruto * Decimal('0.19') if self.iva is None else self.iva
        self.rtefte = self.valor_bruto * Decimal('0.035') if self.rtefte is None else self.rtefte
        self.neto = self.valor_bruto + self.iva - self.rtefte
        super().save(*args, **kwargs)
