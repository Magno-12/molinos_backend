from django.db import models
from decimal import Decimal

from apps.default.models.base_model import BaseModel


class GastosComprasConstruccion(BaseModel):
    fecha_negocio = models.DateField()
    nombre_completo = models.CharField(max_length=255, null=True, blank=True)
    cedula_nit = models.CharField(max_length=20, null=True, blank=True)
    contacto = models.CharField(max_length=255, null=True, blank=True)
    descripcion = models.TextField()
    fv_rc = models.CharField(max_length=50, null=True, blank=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    centro_de_costos = models.CharField(max_length=255)
    medio_pago = models.CharField(max_length=255)
    valor_bruto = models.DecimalField(max_digits=15, decimal_places=2)
    rtefte = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    iva = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    neto = models.DecimalField(max_digits=15, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def calcular_neto(self):
        """Calcula el neto si no se ha proporcionado."""
        if self.iva is None:
            self.iva = self.valor_bruto * Decimal('0.19')
        if self.rtefte is None:
            self.rtefte = self.valor_bruto * Decimal('0.035')
        self.neto = self.valor_bruto + self.iva - self.rtefte
        return self.neto
