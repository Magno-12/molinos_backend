from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.exceptions import TokenError

from apps.users.models.user import User
from apps.authentication.serializers.authentication_serializer import (
        AuthenticationSerializer,
        LogoutSerializer,
)


class AuthenticationViewSet(GenericViewSet):

    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'login':
            return AuthenticationSerializer
        else:
            return LogoutSerializer

    @action(detail=False, methods=['post'])
    def login(self, request):
        """
        Logs in an existing user using their email and password.

        Takes email and password as input.

        If the provided email and password are correct,
        returns a new refresh and access token for the user.
        The refresh token can be used to generate new access tokens.
        ---
        Body:
            {
                "email": "str",
                "password": "str"
            }

        responses:
            {
                "refresh": "refresh_token",
                "access": "access_token",
                "user": {
                    "id": "user_id",
                    "username": "username",
                    "email": "email",
                    "role": "role"
                }
            }
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.validated_data

        try:
            user = User.objects.get(email=user_data['email'])
        except User.DoesNotExist:
            raise AuthenticationFailed("User with the provided email does not exist")

        if not user.check_password(user_data['password']):
            raise AuthenticationFailed("Incorrect password")

        refresh = RefreshToken.for_user(user)

        data = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "role": user.role,
            }
        }
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def logout(self, request):
        """
        Logs out the current user.

        If the user is logged in,
        deletes their refresh token.
        This prevents them from generating new access tokens.

        responses:
            {
                "detail": "Successfully logged out"
            }
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        refresh_token = request.data.get('refresh')

        if refresh_token:
            try:
                RefreshToken(refresh_token).blacklist()
            except RefreshToken.InvalidToken:
                logout(request)
                return Response({"detail": "Refresh token is invalid"},
                                status=status.HTTP_400_BAD_REQUEST)

        return Response({"detail": "Successfully logged out"},
                        status=status.HTTP_200_OK)
