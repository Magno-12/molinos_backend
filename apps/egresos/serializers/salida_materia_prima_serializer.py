from rest_framework import serializers

from apps.egresos.models.salida_materia_prima import SalidaMateriaPrima


class SalidaMateriaPrimaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalidaMateriaPrima
        fields = [
            'codigo', 'descripcion', 'fecha', 'salida_kg', 
            'salida_cm', 'pondera_vta'
        ]


class SalidaMateriaPrimaGeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalidaMateriaPrima
        fields = [
            'id', 'codigo', 'descripcion', 'fecha', 'salida_kg', 
            'salida_cm', 'pondera_vta', 'ponderado_salida', 'comprobante_ingreso'
        ]
