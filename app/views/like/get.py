from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app.models import Plant, Like
from app.serializers.like import LikeSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def liked_plants_list(request):
    user = request.user
    liked_plants = Like.objects.filter(user=user)
    serializer = LikeSerializer(liked_plants, many=True)
    return Response(serializer.data)