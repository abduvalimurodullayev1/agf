from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from app.models import UserRequest
from app.serializers.user_request import UserRequestSerializer


class UserRequestListAPIView(ListAPIView):
    serializer_class = UserRequestSerializer
    queryset = UserRequest.objects.all().order_by("-created_at")

    permission_classes = [IsAuthenticated, ]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,

    ]

    filterset_fields = ["text"]
    search_fields = ["text"]

    def get_queryset(self):
        return UserRequest.objects.filter(user=self.request.user)
