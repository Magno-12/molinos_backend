from django.db import models
from django.db.models import Sum
from django.utils.functional import cached_property

from apps.default.models.base_model import BaseModel


class InformeDiarioItem(BaseModel):
    fecha = models.DateField()
    fv = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    cantidad = models.IntegerField(default=0)
    venta_directa = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    venta_credito = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    subtotal = models.DecimalField(max_digits=15, decimal_places=2, default=0, editable=False)
    acumulado = models.DecimalField(max_digits=15, decimal_places=2, default=0, editable=False)

    class Meta:
        ordering = ['fecha', 'id']

    def save(self, *args, **kwargs):
        self.subtotal = self.venta_directa + self.venta_credito
        super().save(*args, **kwargs)


class InformeDiario(BaseModel):
    numero_informe = models.IntegerField()
    fecha_informe = models.DateField()
    items = models.ManyToManyField(InformeDiarioItem, related_name='informes')

    @cached_property
    def total_subtotal(self):
        return self.items.aggregate(Sum('subtotal'))['subtotal__sum'] or 0

    @cached_property
    def total_acumulado(self):
        last_item = self.items.last()
        if last_item:
            return last_item.acumulado
        return 0

    def actualizar_acumulados(self):
        acumulado = 0
        for item in self.items.all():
            item.acumulado = acumulado + item.subtotal
            item.save()
            acumulado += item.subtotal
