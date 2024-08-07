from rest_framework.generics import RetrieveAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated

from app.models import User
from app.serializers.profile import ProfileSerializer


class ProfileRetrieveAPIView(RetrieveAPIView):
    serializer_class = ProfileSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

    def get_object(self):
        user = self.request.user
        return user
