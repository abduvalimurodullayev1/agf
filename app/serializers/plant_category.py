from rest_framework import serializers

from app.models import Category, CategoryImage, CategoryInnerDescription


class PlantCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PlantCategoryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryImage
        fields = '__all__'


class PlantCategoryInnerDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryInnerDescription
        fields = "__all__"
