from django.urls import path

from app.views.auth.login import LoginAPIView
from app.views.auth.logout import LogoutAPIView
from app.views.auth.register import RegisterApiView
from app.views.data import PlantIdentificationView
from app.views.like.create import like_plant
from app.views.like.delete import unlike_plant
from app.views.like.get import liked_plants_list
from app.views.plan.get import PlantListAPIView, PlantRetrieveAPIView, PlantImageListAPIView, \
    PlantInnerDescriptionListAPIView
from app.views.plant_category.get import PlantCategoryListAPIView, PlantCategoryRetrieveAPIView, \
    PlantCategoryImageListAPIView, CategoryInnerDescriptionListAPIView
from app.views.profile.get import ProfileRetrieveAPIView
from app.views.profile.update import UpdateProfileApiView
from app.views.user_request.create import UserRequestCreateAPIView
from app.views.user_request.get import UserRequestListAPIView

urlpatterns = [
    path('register/', RegisterApiView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),

    #  Blog urls

    # path("list_blog/", BlogListAPIView.as_view(), name="list_blog"),
    # path("list_blog_image/", BlogImageListAPIView.as_view(), name="list_blog_image"),
    #
    # path("get_blog/<int:pk>/", BlogRetrieveAPIView.as_view(), name="get_blog"),
    # path("get_blog_image/<int:pk>/", BlogImageRetrieveAPIView.as_view(), name="get_blog_image"),

    # User Requests Urls
    path("create_user_request/", UserRequestCreateAPIView.as_view(), name="create_user_request"),
    path("list_user_request/", UserRequestListAPIView.as_view(), name="list_user_request"),

    # Plant Category

    path("list_plant_category/", PlantCategoryListAPIView.as_view(), name="list_plant_category"),
    path("get_plant_category/<int:pk>/", PlantCategoryRetrieveAPIView.as_view(), name="get_plant_category"),

    path("list_plant_category_image/<int:category_id>/", PlantCategoryImageListAPIView.as_view(),
         name="list_plant_category_image"),

    path("list_plant_category_inner_description/<int:category_id>/", CategoryInnerDescriptionListAPIView.as_view(),
         name="list_plant_category_inner_description"),

    # Plant urls

    path("list_plants/", PlantListAPIView.as_view(), name="list_plants"),
    path("get_plant/<int:pk>/", PlantRetrieveAPIView.as_view(), name="get_plant"),

    path("list_plant_images/<int:plant_id>/", PlantImageListAPIView.as_view(), name="list_plant_images"),
    path("list_plant_inner_descriptions/<int:plant_id>/", PlantInnerDescriptionListAPIView.as_view(),
         name="list_plant_inner_descriptions"),

    # Like
    path("create_like/<int:plant_id>/", like_plant, name="create_like"),
    path("delete_like/<int:plant_id>/", unlike_plant, name="delete_like"),
    path("liked_plants/", liked_plants_list, name="liked_plants"),
    # UserProfile

    path('update_user_profile/', UpdateProfileApiView.as_view(), name='update_user_profile'),
    path('get_user_profile/', ProfileRetrieveAPIView.as_view(), name='get_userprofile'),
    path('plant-identification/', PlantIdentificationView.as_view(), name='plant_identification'),

]
