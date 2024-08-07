from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from app.models import UserRequest
from app.serializers.user_request import UserRequestSerializer


class UserRequestCreateAPIView(CreateAPIView):
    serializer_class = UserRequestSerializer
    queryset = UserRequest.objects.all()

    permission_classes = [IsAuthenticated]
