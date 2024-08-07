from rest_framework import serializers

from app.models import Plant, PlantImage, PlantInnerDescription


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = "__all__"


class PlantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantImage
        fields = "__all__"


class PlantInnerDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantInnerDescription
        fields = "__all__"


class ImageUploadSerializer(serializers.Serializer):
    image = serializers.ImageField()
