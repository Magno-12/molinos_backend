from rest_framework import serializers

from apps.egresos.models.gasto import Gasto


class GastoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gasto
        fields = [
            'fecha_negocio', 'nombre_completo', 'cedula_nit', 'contacto',
            'descripcion', 'fv_rc', 'cantidad', 'centro_costos',
            'medio_pago', 'valor_bruto'
        ]


class GastoGeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gasto
        fields = [
            'id', 'fecha_negocio', 'nombre_completo', 'cedula_nit', 'contacto',
            'descripcion', 'fv_rc', 'cantidad', 'centro_costos',
            'medio_pago', 'valor_bruto', 'rtefte', 'iva', 'calcular_neto'
        ]
