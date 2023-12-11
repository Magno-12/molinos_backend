from django.db import models
from decimal import Decimal

from apps.default.models.base_model import BaseModel


class CostosDeProduccion(BaseModel):
    fecha_negocio = models.DateField()
    nombre_completo = models.CharField(max_length=255)
    cedula_nit = models.CharField(max_length=20)
    contacto = models.BigIntegerField()
    descripcion = models.TextField()
    fv_rc = models.CharField(null=True, blank=True, max_length=15)
    cantidad = models.IntegerField()
    centro_de_costos = models.CharField(max_length=255)
    medio_pago = models.CharField(max_length=255)
    valor_bruto = models.DecimalField(max_digits=15, decimal_places=2)
    rtefte = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    iva = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    neto = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.iva = self.valor_bruto * Decimal('0.19') if self.iva is None else self.iva
        self.neto = self.valor_bruto + (self.iva or 0) - (self.rtefte or 0)
        super().save(*args, **kwargs)
