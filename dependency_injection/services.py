from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response

from apps.users.models.user import User
from apps.users.serializers.user_serializer import UserSerializer
from dependency_injection.interface import UserService


class UserServiceImpl(UserService):
    def create_user(self, user_data):
        required_fields = ['username', 'email', 'password', 'role']
        if not all(k in user_data for k in required_fields):
            missing_fields = ', '.join(
                        [field for field in required_fields if field not in user_data]
                )
            return Response(
                {"detail": f"Missing required fields: {missing_fields}"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if User.objects.filter(username=user_data.get('username')).exists():
            return Response(
                {"detail": "Username already exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if User.objects.filter(email=user_data.get('email')).exists():
            return Response(
                {"detail": "Email already exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            validate_password(user_data.get('password'))
        except ValidationError as e:
            return Response(
                {"password": e.messages}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(
            username=user_data.get('username'),
            email=user_data.get('email'),
            password=user_data.get('password'),
            role=user_data.get('role')
        )
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
