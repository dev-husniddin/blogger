from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from .pagination import PostPagination
from .filters import PostFilter
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework import viewsets

class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

class PostListView(generics.ListAPIView):  # Используйте generics.ListAPIView
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination
    filter_class = PostFilter  # Добавляем фильтр

class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     @swagger_auto_schema(
#         method='get',
#         operation_summary="Get a list of posts",
#         operation_description="Retrieve a list of all posts.",
#         responses={
#             status.HTTP_200_OK: PostSerializer(many=True),
#         },
#     )
#     def list(self, request, *args, **kwargs):
#         """
#         Get a list of posts.

#         This endpoint allows you to retrieve a list of all posts.
#         """
#         return super().list(request, *args, **kwargs)

#     @swagger_auto_schema(
#         method='post',
#         operation_summary="Create a new post",
#         operation_description="Create a new post by providing post details in the request data.",
#         responses={
#             status.HTTP_201_CREATED: PostSerializer(),
#             status.HTTP_400_BAD_REQUEST: "Invalid request data",
#         },
#     )
#     def create(self, request, *args, **kwargs):
#         """
#         Create a new post.

#         This endpoint allows you to create a new post.
#         """
#         return super().create(request, *args, **kwargs)

#     @swagger_auto_schema(
#         method='put',
#         operation_summary="Update a post",
#         operation_description="Update an existing post's details.",
#         responses={
#             status.HTTP_200_OK: PostSerializer(),
#             status.HTTP_400_BAD_REQUEST: "Invalid request data",
#             status.HTTP_404_NOT_FOUND: "Post not found",
#         },
#     )
#     def update(self, request, *args, **kwargs):
#         """
#         Update a post.

#         This endpoint allows you to update an existing post's details.
#         """
#         return super().update(request, *args, **kwargs)

#     @swagger_auto_schema(
#         method='delete',
#         operation_summary="Delete a post",
#         operation_description="Delete an existing post.",
#         responses={
#             status.HTTP_204_NO_CONTENT: "Post deleted successfully",
#             status.HTTP_404_NOT_FOUND: "Post not found",
#         },
#     )
#     def destroy(self, request, *args, **kwargs):
#         """
#         Delete a post.

#         This endpoint allows you to delete an existing post.
#         """
#         return super().destroy(request, *args, **kwargs)
