import os
from tempfile import NamedTemporaryFile

from drf_yasg.utils import swagger_auto_schema
from inference_sdk import InferenceHTTPClient
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Plant, PlantImage, PlantInnerDescription
from app.serializers.plant import ImageUploadSerializer


class PlantIdentificationView(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=ImageUploadSerializer,
        responses={status.HTTP_200_OK: "Image uploaded successfully",
                   status.HTTP_400_BAD_REQUEST: "Unable to classify",
                   status.HTTP_404_NOT_FOUND: "Plant not found"}
    )
    def post(self, request, *args, **kwargs):
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            image = serializer.validated_data['image']

            # Save the image to a temporary file
            with NamedTemporaryFile(delete=False, suffix='.jpg') as temp_file:
                temp_file.write(image.read())
                temp_file_path = temp_file.name

            # Process the image using your image recognition API
            CLIENT = InferenceHTTPClient(
                api_url="https://classify.roboflow.com",
                api_key="PNYglHVOWDE1C4viiWgs"
            )
            result = CLIENT.infer(temp_file_path, model_id="227-yc1vm/1")

            # Remove the temporary file
            os.unlink(temp_file_path)

            # If the confidence is high enough, retrieve plant information
            if result['confidence'] > 0.7:
                plant_title = result['top'].lower()

                try:
                    # Use icontains to perform case-insensitive filtering by title

                    plant = Plant.objects.filter(title_en__icontains=plant_title).first()
                    if not plant:
                        return Response({"error": "Sorry, there is no information about Plant"},
                                        status=status.HTTP_404_NOT_FOUND)
                    plant_info = [
                        {
                            "title_uz": plant.title_uz,
                            "title_en": plant.title_en,
                            "title_ru": plant.title_ru,

                            'description_uz': plant.description_uz,
                            'description_en': plant.description_en,
                            'description_ru': plant.description_ru,
                        }
                    ]
                    # Assuming you have a serializer for your Plant model
                    plant_images = PlantImage.objects.filter(plant=plant).all()

                    plant_inner_descriptions = PlantInnerDescription.objects.filter(plant=plant).all()

                    descriptions = []
                    for description in plant_inner_descriptions:
                        translation_list = []
                        # Assuming you have fields for each language like title_en, title_fr, title_es, etc.
                        translation_list.append([description.title_uz, description.description_uz])
                        translation_list.append([description.title_en, description.description_en])
                        translation_list.append([description.title_ru, description.description_ru])
                        descriptions.append(translation_list)

                    plant_data = {
                        "plant_category_uz": plant.category.title_uz,
                        "plant_category_en": plant.category.title_en,
                        "plant_category_ru": plant.category.title_ru,
                        'plant_info': plant_info,
                        'images': [image.image.url for image in plant_images],
                        'descriptions': descriptions
                    }
                    return Response({'success': True, 'plant': plant_data})
                except Plant.DoesNotExist:
                    return Response({'success': False, 'error': 'Plant not found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'success': False, 'error': 'Unable to classify'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'success': False, 'error': 'Missing image'}, status=status.HTTP_400_BAD_REQUEST)
