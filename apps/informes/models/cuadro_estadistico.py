from django.db import models

from apps.default.models.base_model import BaseModel


class CuadroEstadistico(BaseModel):
    descripcion = models.CharField(max_length=255)
    ventas_mes = models.DecimalField(max_digits=15, decimal_places=2)
    ponderado_materia_prima = models.DecimalField(max_digits=15, decimal_places=2)
    costos_produccion = models.DecimalField(max_digits=15, decimal_places=2)
    gastos_construccion_taller_callao = models.DecimalField(max_digits=15, decimal_places=2)
    ventas_ano_anterior = models.DecimalField(max_digits=15, decimal_places=2)
    ventas_ano_actual = models.DecimalField(max_digits=15, decimal_places=2)

    @property
    def sub_total_ganancias(self):
        return self.ventas_mes - self.ponderado_materia_prima

    @property
    def sub_total_rentabilidad(self):
        return self.sub_total_ganancias - self.costos_produccion

    @property
    def rentabilidad_neta(self):
        return self.sub_total_rentabilidad - self.gastos_construccion_taller_callao

    @property
    def porcentaje_rentabilidad_neta(self):
        return self.rentabilidad_neta / self.ventas_mes if self.ventas_mes != 0 else 0

    @property
    def crecimiento_ventas_absoluto(self):
        return self.ventas_ano_actual - self.ventas_ano_anterior

    @property
    def crecimiento_ventas_porcentual(self):
        return (self.crecimiento_ventas_absoluto / self.ventas_ano_anterior) if self.ventas_ano_anterior != 0 else 0
