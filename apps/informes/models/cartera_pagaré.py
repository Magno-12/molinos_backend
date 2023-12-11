from django.db import models

from apps.default.models.base_model import BaseModel


class CarteraPagareYAnticipos(models.Model):
    fecha_negocio = models.DateField(auto_now_add=True)
    nombre_completo_razon_social = models.CharField(max_length=255)
    cedula_nit = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    descripcion = models.TextField()
    valor_pagare = models.DecimalField(max_digits=15, decimal_places=2)
    abono_inicial = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    pagos_ano = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True) # Considerar dividir en campos separados si necesario
    descuentos = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    saldo_pendiente = models.DecimalField(max_digits=15, decimal_places=2)

    def calcular_saldo_actual(self):
        pagos_totales = self.abono_inicial or 0 + self.pagos_ano or 0
        saldo_actual = self.valor_pagare - pagos_totales
        return saldo_actual
