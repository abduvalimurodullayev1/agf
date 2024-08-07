from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView

from app.models import Category, CategoryImage, CategoryInnerDescription
from app.serializers.plant_category import PlantCategorySerializer, PlantCategoryImageSerializer, \
    PlantCategoryInnerDescriptionSerializer


class PlantCategoryListAPIView(ListAPIView):
    serializer_class = PlantCategorySerializer
    queryset = Category.objects.all()

    # filter_backends = [
    #     DjangoFilterBackend,
    #     SearchFilter,
    #
    # ]
    #
    # filterset_fields = [
    #     "title",
    # ]
    # search_fields = ["title",
    #                  "description"]


class PlantCategoryRetrieveAPIView(RetrieveAPIView):
    serializer_class = PlantCategorySerializer
    queryset = Category.objects.all()

    # filter_backends = [
    #     DjangoFilterBackend,
    #     SearchFilter,
    #
    # ]
    #
    # filterset_fields = [
    #     "title",
    # ]
    # search_fields = ["title",
    #                  "description"]


class PlantCategoryImageListAPIView(ListAPIView):
    serializer_class = PlantCategoryImageSerializer
    queryset = CategoryImage.objects.all()

    def get_queryset(self):
        return CategoryImage.objects.filter(category=self.kwargs['category_id'])


class CategoryInnerDescriptionListAPIView(ListAPIView):
    serializer_class = PlantCategoryInnerDescriptionSerializer
    queryset = CategoryInnerDescription.objects.all()

    # filter_backends = [
    #     DjangoFilterBackend,
    #     SearchFilter,
    #
    # ]
    #
    # filterset_fields = [
    #     "title",
    # ]
    # search_fields = ["title",
    #                  "description"]

    def get_queryset(self):
        return CategoryInnerDescription.objects.filter(category=self.kwargs['category_id'])
