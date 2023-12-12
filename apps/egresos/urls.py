from django.urls import include, path

from rest_framework import routers

from apps.egresos.view.compras_view import CompraViewSet
from apps.egresos.view.gasto_view import GastoViewSet
from apps.egresos.view.salida_materia_prima_view import SalidaMateriaPrimaViewSet

router = routers.DefaultRouter()

router.register(r'compras', CompraViewSet, basename='compras')
router.register(r'gastos', GastoViewSet, basename='gastos')
router.register(r'salidamateriaprima', SalidaMateriaPrimaViewSet, basename='salidamateriaprima')

urlpatterns = [
    path('', include(router.urls)),
]
