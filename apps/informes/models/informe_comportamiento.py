import datetime
from django.db import models

from apps.default.models.base_model import BaseModel
from apps.informes.models.venta_mes import VentaMensual
from apps.produccion.models.costos_producción import CostosDeProduccion
from apps.produccion.models.gastos_compras_produccion import GastosComprasConstruccion
from apps.produccion.models.inventario_maquinaria import InventarioMaquinaria
from apps.ingresos.models.entrada import Entrada
from apps.ingresos.models.ingresos import Ingreso


class InformeComportamiento(BaseModel):
    descripcion = models.CharField(max_length=255)
    ventas = models.ManyToManyField(VentaMensual, related_name='informes_comportamiento')
    costos_produccion = models.ManyToManyField(CostosDeProduccion, related_name='informes_comportamiento')
    gastos_construccion = models.ManyToManyField(GastosComprasConstruccion, related_name='informes_comportamiento')
    inventario_maquinaria = models.ManyToManyField(InventarioMaquinaria, related_name='informes_comportamiento')
    entradas = models.ManyToManyField(Entrada, related_name='informes_comportamiento')
    ingresos = models.ManyToManyField(Ingreso, related_name='informes_comportamiento')

    def agregar_venta(self, valor, fecha):
        venta, created = VentaMensual.objects.get_or_create(mes=fecha, defaults={'valor': valor})
        if not created and venta.valor != valor:
            venta.valor = valor
            venta.save()
        self.ventas.add(venta)

    def obtener_ventas_mes(self, anyo, mes):
        fecha = datetime.date(anyo, mes, 1)
        return self.ventas.filter(mes__year=fecha.year, mes__month=fecha.month).first()

    def obtener_resultado_anual(self, anyo):
        return sum(self.ventas.filter(mes__year=anyo).values_list('valor', flat=True))

    def calcular_total_costos_produccion(self):
        return sum([costo.valor for costo in self.costos_produccion.all()])

    def calcular_total_gastos_construccion(self):
        return sum([gasto.valor for gasto in self.gastos_construccion.all()])

    def calcular_valor_inventario_maquinaria(self):
        return sum([inventario.valor_actual() for inventario in self.inventario_maquinaria.all()])

    def calcular_total_entradas(self):
        return sum([entrada.calcular_ponderado_compra() for entrada in self.entradas.all()])

    def calcular_total_ingresos(self):
        return sum([ingreso.calcular_balance_final() for ingreso in self.ingresos.all()])
