from rest_framework import serializers

from app.models import UserRequest


class UserRequestSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserRequest
        fields = '__all__'
