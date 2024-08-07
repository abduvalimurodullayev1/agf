from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from app.models import User


class RegisterModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "phone_number", 'password']
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password")
        hashed_password = make_password(password)
        user = User.objects.create(**validated_data,
                                   password=hashed_password)
        return user
