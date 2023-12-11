from django.db import models
import datetime

from apps.default.models.base_model import BaseModel


class InventarioMaquinaria(BaseModel):
    fecha_adquisicion = models.DateField()
    item = models.IntegerField()
    equipo = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    descripcion = models.TextField()
    cantidad = models.IntegerField()
    centro_costos = models.CharField(max_length=255)
    costo_unitario = models.DecimalField(max_digits=15, decimal_places=2)
    costo_peritaje = models.DecimalField(max_digits=15, decimal_places=2)
    costo_entrada = models.DecimalField(max_digits=15, decimal_places=2)

    def valor_total_inventario(self):
        return self.costo_entrada * self.cantidad

    def depreciacion_anual(self, anos_depreciacion=5):
        """Calcula la depreciación anual asumiendo una vida útil en años."""
        return self.valor_total_inventario() / anos_depreciacion if anos_depreciacion > 0 else 0

    def valor_actual(self):
        """Calcula el valor actual del equipo basado en la depreciación anual."""
        anos_transcurridos = datetime.date.today().year - self.fecha_adquisicion.year
        depreciacion = self.depreciacion_anual() * anos_transcurridos
        return max(self.valor_total_inventario() - depreciacion, 0)
