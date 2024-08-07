from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app.models import Plant, Like


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def unlike_plant(request, plant_id):
    user = request.user
    plant = get_object_or_404(Plant, id=plant_id)

    like = Like.objects.filter(user=user, plant=plant).first()
    if not like:
        return Response({'message': 'You have not liked this plant'})
    else:
        like.delete()
        return Response({'message': 'Plant unliked successfully'})