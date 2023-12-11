from django.db import models

from apps.default.models.base_model import BaseModel


class CuentaPorPagar(BaseModel):
    fecha = models.DateField(auto_now_add=True)
    nombre_proveedor = models.CharField(max_length=255)
    cedula_nit = models.CharField(max_length=20)
    contacto = models.CharField(max_length=255)
    descripcion = models.TextField()
    fv_rc_rem = models.CharField(max_length=50)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    centro_costos = models.CharField(max_length=255)
    medio_pago = models.CharField(max_length=50)
    valor_kg = models.DecimalField(max_digits=10, decimal_places=2)
    valor_bruto = models.DecimalField(max_digits=15, decimal_places=2)
    abonos = models.DecimalField(max_digits=15, decimal_places=2)
    fecha_abonos = models.DateField(null=True, blank=True)

    def calcular_por_pagar(self):
        return self.valor_bruto - self.abonos
