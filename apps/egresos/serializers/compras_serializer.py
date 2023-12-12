from rest_framework import serializers

from apps.egresos.models.compra import Compra


class CompraCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = [
            'fecha', 'nombre_proveedor', 'cedula_nit', 'contacto',
            'descripcion', 'factura', 'cantidad', 'centro_costos',
            'medio_pago', 'valor_bruto',
        ]


class CompraGeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = [
            'id', 'fecha', 'nombre_proveedor', 'cedula_nit', 'contacto',
            'descripcion', 'factura', 'cantidad', 'centro_costos',
            'medio_pago', 'valor_bruto', 'rtefte', 'iva', 'neto'
        ]
