from django.db import models

from apps.default.models.base_model import BaseModel


class SalidaMateriaPrima(BaseModel):
    codigo = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha = models.DateField()
    salida_kg = models.DecimalField(max_digits=10, decimal_places=2)
    salida_cm = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pondera_vta = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ponderado_salida = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Si este valor se calcula, necesitamos la fórmula
    comprobante_ingreso = models.CharField(max_length=50, null=True, blank=True)

    def calcular_ponderado_salida(self):
        return self.salida_kg * (self.pondera_vta or 1)
