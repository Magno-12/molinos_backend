from django.db import models

from apps.default.models.base_model import BaseModel


class Gasto(BaseModel):
    fecha_negocio = models.DateField()
    nombre_completo = models.CharField(max_length=255)
    cedula_nit = models.CharField(max_length=20, null=True, blank=True)
    contacto = models.CharField(max_length=20, null=True, blank=True)
    descripcion = models.TextField()
    fv_rc = models.CharField(max_length=50, null=True, blank=True)
    cantidad = models.IntegerField()
    centro_costos = models.CharField(max_length=255)
    medio_pago = models.CharField(max_length=50)
    valor_bruto = models.DecimalField(max_digits=15, decimal_places=2)
    rtefte = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    iva = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    neto = models.DecimalField(max_digits=15, decimal_places=2)

    @property
    def calcular_neto(self):
        rtefte = self.rtefte if self.rtefte else 0
        iva = self.iva if self.iva else 0
        return self.valor_bruto - rtefte + iva
