from django.db import models

from apps.default.models.base_model import BaseModel


class ComparativoIngresosCompras(BaseModel):
    fecha = models.DateField(auto_now_add=True)
    ingresos_efectivo = models.DecimalField(max_digits=15, decimal_places=2)
    ingreso_caja_sky = models.DecimalField(max_digits=15, decimal_places=2)
    compras = models.DecimalField(max_digits=15, decimal_places=2)
    gastos = models.DecimalField(max_digits=15, decimal_places=2)
    gastos_compras_callao = models.DecimalField(max_digits=15, decimal_places=2)

    @property
    def total(self):
        return self.ingresos_efectivo + self.ingreso_caja_sky + self.compras

    @property
    def subtotal_ganancia(self):
        return self.total - self.gastos - self.gastos_compras_callao
