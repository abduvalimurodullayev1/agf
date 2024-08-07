from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from app.models import Plant, PlantImage, PlantInnerDescription
from app.serializers.plant import PlantSerializer, PlantImageSerializer, PlantInnerDescriptionSerializer


class PlantListAPIView(ListAPIView):
    serializer_class = PlantSerializer
    queryset = Plant.objects.all()
    permission_classes = [IsAuthenticated]



    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,

    ]

    filterset_fields = [
        "title",

    ]
    search_fields = ["title",
                     "description",
                     "category__title",
                     ]


class PlantRetrieveAPIView(RetrieveAPIView):
    serializer_class = PlantSerializer
    queryset = Plant.objects.all()
    permission_classes = [IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,

    ]

    filterset_fields = [
        "title",
    ]
    search_fields = ["title",
                     "description",
                     "category__title",
                     ]


class PlantImageListAPIView(ListAPIView):
    serializer_class = PlantImageSerializer
    queryset = PlantImage.objects.all()

    def get_queryset(self):
        return PlantImage.objects.filter(plant=self.kwargs['plant_id'])


class PlantInnerDescriptionListAPIView(ListAPIView):
    serializer_class = PlantInnerDescriptionSerializer
    queryset = PlantInnerDescription.objects.all()
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return PlantInnerDescription.objects.filter(plant=self.kwargs['plant_id'])

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
    ]

    filterset_fields = [
        "title",
    ]
    search_fields = ["title",
                     "description",
                     "plant__title"]

