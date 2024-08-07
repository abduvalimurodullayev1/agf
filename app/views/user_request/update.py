from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from app.models import UserRequest
from app.serializers.user_request import UserRequestSerializer


class UserRequestUpdateAPIView(UpdateAPIView):
    serializer_class = UserRequestSerializer
    queryset = UserRequest.objects.all()

    permission_classes = [IsAuthenticated, ]
