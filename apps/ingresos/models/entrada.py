from django.db import models
import decimal

from apps.default.models.base_model import BaseModel


class Entrada(BaseModel):
    codigo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)
    longitud_cm = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fecha = models.DateField()
    entrada_kg = models.DecimalField(max_digits=10, decimal_places=2)
    ponderado_compra = models.DecimalField(max_digits=15, decimal_places=2)

    def calcular_kg(self):
        """Calcula los kilogramos basados en la longitud y una fórmula específica."""
        return self.longitud_cm * decimal.Decimal("0.24") * 1 * 16

    def actualizar_descripcion(self):
        """Actualiza la descripción utilizando una búsqueda (simulada) de otra hoja."""
        pass

    def calcular_ponderado_compra(self):
        """Calcula el ponderado de compra."""
        return self.entrada_kg * decimal.Decimal("3246.29")

    def save(self, *args, **kwargs):
        self.entrada_kg = self.calcular_kg()
        self.ponderado_compra = self.calcular_ponderado_compra()
        super().save(*args, **kwargs)
