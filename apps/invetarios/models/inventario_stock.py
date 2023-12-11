from django.db import models
from django.db.models import Sum
from decimal import Decimal

from apps.default.models.base_model import BaseModel
from apps.ingresos.models.entrada import Entrada


class InventarioStock(BaseModel):
    codigo = models.CharField(max_length=50)
    descripcion = models.TextField()
    entrada_kg = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    entrada_cm = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    salida_kg = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    salida_cm = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    stock_kg = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    stock_cm = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ponderado_stock = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def calcular_entrada_kg(self):
        return Entrada.objects.filter(codigo=self.codigo).aggregate(Sum('entrada_kg'))['entrada_kg__sum'] or 0

    def calcular_entrada_cm(self):
        return Entrada.objects.filter(codigo=self.codigo).aggregate(Sum('entrada_cm'))['entrada_cm__sum'] or 0

    def calcular_salida_kg(self):
        pass

    def calcular_salida_cm(self):
        pass

    def actualizar_stock(self):
        self.stock_kg = self.calcular_entrada_kg() - self.calcular_salida_kg()
        self.stock_cm = self.calcular_entrada_cm() - self.calcular_salida_cm()
        self.save()

    def calcular_ponderado_stock(self):
        return self.stock_kg * Decimal('4025.32')

    def save(self, *args, **kwargs):
        self.entrada_kg = self.calcular_entrada_kg()
        self.entrada_cm = self.calcular_entrada_cm()
        self.stock_kg = self.entrada_kg - (self.salida_kg or 0)
        self.stock_cm = self.entrada_cm - (self.salida_cm or 0)
        self.ponderado_stock = self.calcular_ponderado_stock()
        super().save(*args, **kwargs)
