from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from apps.egresos.models.salida_materia_prima import SalidaMateriaPrima
from apps.egresos.serializers.salida_materia_prima_serializer import (
    SalidaMateriaPrimaCreateSerializer,
    SalidaMateriaPrimaGeneralSerializer
)


class SalidaMateriaPrimaViewSet(GenericViewSet):

    queryset = SalidaMateriaPrima.objects.filter(is_active=True)

    def get_serializer_class(self):
        if self.action == 'create':
            return SalidaMateriaPrimaCreateSerializer
        return SalidaMateriaPrimaGeneralSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(
                {"message": "created successfully.", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {"message": "Error creating", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None, *args, **kwargs):
        instance = get_object_or_404(self.get_queryset(), pk=kwargs['pk'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "updated successfully", "data": serializer.data},
                status=status.HTTP_200_OK
            )
        return Response(
            {"message": "Error updating", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
