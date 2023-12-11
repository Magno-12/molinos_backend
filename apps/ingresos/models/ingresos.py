from django.db import models
from decimal import Decimal

from apps.default.models.base_model import BaseModel


class Ingreso(models.Model):
    fecha_negocio = models.DateField()
    nombre_completo = models.CharField(max_length=255)
    cedula_nit = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    descripcion = models.TextField()
    entrada_kg = models.DecimalField(max_digits=10, decimal_places=2)
    precio_entrada = models.DecimalField(max_digits=15, decimal_places=2)
    # Asumiendo que hay campos para los totales de salida en Kg de diferentes materiales
    salida_material_1_kg = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salida_material_2_kg = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salida_material_3_kg = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # Otros campos que podrían ser relevantes para los cálculos
    descuento = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def calcular_costo_total(self):
        """Calcula el costo total basado en la suma de los totales de salida de materiales."""
        return sum([self.salida_material_1_kg, self.salida_material_2_kg, self.salida_material_3_kg])

    def calcular_utilidad(self):
        """Calcula la utilidad basada en la fórmula identificada."""
        costo_total = self.calcular_costo_total()
        return self.precio_entrada - costo_total

    def calcular_porcentaje_utilidad(self):
        """Calcula el porcentaje de utilidad."""
        costo_total = self.calcular_costo_total()
        return (self.calcular_utilidad() / costo_total) * 100 if costo_total > 0 else 0

    def calcular_balance_final(self):
        """Calcula el balance final tras aplicar descuentos y otros ajustes."""
        return self.precio_entrada - self.descuento - self.ajustes

    def save(self, *args, **kwargs):
        self.costo_total = self.calcular_costo_total()
        self.utilidad = self.calcular_utilidad()
        self.porcentaje_utilidad = self.calcular_porcentaje_utilidad()
        self.balance_final = self.calcular_balance_final()
        super().save(*args, **kwargs)
