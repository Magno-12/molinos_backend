from rest_framework import serializers

from apps.users.models.customer import Customer
from apps.users.serializers.user_serializer import UserSerializer


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Customer
        fields = ['id', 'user', 'red_customer_quit']
