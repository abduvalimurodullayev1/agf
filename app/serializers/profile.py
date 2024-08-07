from rest_framework import serializers

from app.models import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'image']
        extra_kwargs = {
            'phone_number': {'read_only': True}
        }
