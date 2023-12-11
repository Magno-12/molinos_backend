from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.users.models.user import User
from apps.users.serializers.user_serializer import (UserCreateSerializer,
                                                    UserSerializer)
from dependency_injection.di_container import dependency_container


class UserViewSet(GenericViewSet):
    queryset = User.objects.filter(is_active=True)

    def get_serializer_class(self):
        if self.action == 'create_user':
            return UserCreateSerializer
        else:
            return UserSerializer

    def get_object(self, pk):
        try:
            return self.queryset.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound(detail="Object not found")

    def list(self, request):
        """
        List all users.

        ---
        response:
            Response: Serialized data of all users.
            Example JSON:
            {
                "data": [
                    {
                        "id": "str",
                        "username": "str",
                        "email": "str",
                        "role": "str"
                    },
                    ...
                ]
            }
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def create_user(self, request):
        """
        Create a new user.

        ---
        Body:
            {
                "username": "str",
                "email": "str",
                "password": "str",
                "role": "str"
            }

        response:
            Response: Serialized data of the created user.
            Example JSON:
            {
                "data": {
                    "id": "str",
                    "username": "str",
                    "email": "str",
                    "role": "str"
                }
            }
        """
        user_service = dependency_container.get_user_service()
        response = user_service.create_user(request.data)

        if isinstance(response, User):
            serializer = self.get_serializer(response)
            data = {"data": serializer.data}
            return Response(data, status=status.HTTP_201_CREATED)

        return response

    def retrieve(self, request, pk=None):
        """
        Retrieve a specific user by its primary key.

        ---
        Args:
            pk (str): Primary key of the user.

        response:
            Response: Serialized data of the retrieved user.
            Example JSON:
            {
                "data": {
                    "id": "str",
                    "username": "str",
                    "email": "str",
                    "role": "str"
                }
            }
        """
        obj = self.get_object(pk)
        serializer = self.get_serializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        """
        Partially update a specific user by its primary key.

        ---
        Args:
            pk (str): Primary key of the user.

        Body:
            {
                "username": "str",
                "email": "str",
                "role": "str"
            }

        response:
            Response: Serialized data of the partially updated user.
            Example JSON:
            {
                "data": {
                    "id": "str",
                    "username": "str",
                    "email": "str",
                    "role": "str"
                }
            }
        """
        obj = self.get_object(pk)
        serializer = self.get_serializer(obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
