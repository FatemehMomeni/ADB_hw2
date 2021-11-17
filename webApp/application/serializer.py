from rest_framework import serializers
from .models import Users


class SingUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['name', 'family', 'birth_date', 'tel', 'address', 'gender']


class RegisteredUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['name', 'family']

