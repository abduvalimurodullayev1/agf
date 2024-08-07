# from rest_framework.generics import ListAPIView, RetrieveAPIView
#
# from app.models import Blog, BlogImage
# from app.serializers.blog import BlogModelSerializer, BlogImageSerializer
#
#
# class BlogListAPIView(ListAPIView):
#     serializer_class = BlogModelSerializer
#     queryset = Blog.objects.all().order_by("-created_at")
#
#     # permission_classes = [IsAuthenticated]
#
#
# class BlogRetrieveAPIView(RetrieveAPIView):
#     serializer_class = BlogModelSerializer
#     queryset = Blog.objects.all()
#
#     #     permission_classes = [IsAuthenticated]
#
#
# # --------------------------------------------------------- Blog Image -------------------------------------------------
#
#
# class BlogImageListAPIView(ListAPIView):
#     serializer_class = BlogImageSerializer
#     queryset = BlogImage.objects.all().order_by("-id")
#
#     #     permission_classes = [IsAuthenticated]
#
#
#
#
# class BlogImageRetrieveAPIView(RetrieveAPIView):
#     serializer_class = BlogImageSerializer
#     queryset = BlogImage.objects.all()
#
#     #     permission_classes = [IsAuthenticated]
