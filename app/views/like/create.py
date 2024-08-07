from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app.models import Plant, Like
from app.serializers.like import LikeSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_plant(request, plant_id):
    user = request.user
    plant = get_object_or_404(Plant, id=plant_id)

    if Like.objects.filter(user=user, plant=plant).exists():
        return Response({'message': 'You have already liked this plant'})
    else:
        like = Like.objects.create(user=user, plant=plant)
        like.save()
        serializer = LikeSerializer(like)
        return Response(serializer.data)

