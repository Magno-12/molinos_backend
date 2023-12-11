from django.urls import include, path

from rest_framework import routers

from apps.authentication.views.auth_view import AuthenticationViewSet

router = routers.DefaultRouter()

router.register(r'authentication', AuthenticationViewSet, basename='authentication')

urlpatterns = [
    path('', include(router.urls)),
]
