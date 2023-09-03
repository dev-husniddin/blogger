from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .pagination import CommentPagination
from .filters import CommentFilter
from drf_yasg.utils import swagger_auto_schema
from .models import Comment
from rest_framework import viewsets

class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


class CommentCreateView(CreateAPIView):
    serializer_class = CommentSerializer

class CommentListView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = CommentPagination
    filter_class = CommentFilter 

class CommentDetailView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentUpdateView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDeleteView(DestroyAPIView):
    queryset = Comment.objects.all()

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

#     @swagger_auto_schema(
#         method='get',
#         operation_summary="Get a list of comments",
#         operation_description="Retrieve a list of all comments.",
#         responses={
#             status.HTTP_200_OK: CommentSerializer(many=True),
#         },
#     )
#     def list(self, request, *args, **kwargs):
#         """
#         Get a list of comments.

#         This endpoint allows you to retrieve a list of all comments.
#         """
#         return super().list(request, *args, **kwargs)

#     @swagger_auto_schema(
#         method='post',
#         operation_summary="Create a new comment",
#         operation_description="Create a new comment by providing comment details in the request data.",
#         responses={
#             status.HTTP_201_CREATED: CommentSerializer(),
#             status.HTTP_400_BAD_REQUEST: "Invalid request data",
#         },
#     )
#     def create(self, request, *args, **kwargs):
#         """
#         Create a new comment.

#         This endpoint allows you to create a new comment.
#         """
#         return super().create(request, *args, **kwargs)

#     @swagger_auto_schema(
#         method='put',
#         operation_summary="Update a comment",
#         operation_description="Update an existing comment's details.",
#         responses={
#             status.HTTP_200_OK: CommentSerializer(),
#             status.HTTP_400_BAD_REQUEST: "Invalid request data",
#             status.HTTP_404_NOT_FOUND: "Comment not found",
#         },
#     )
#     def update(self, request, *args, **kwargs):
#         """
#         Update a comment.

#         This endpoint allows you to update an existing comment's details.
#         """
#         return super().update(request, *args, **kwargs)

#     @swagger_auto_schema(
#         method='delete',
#         operation_summary="Delete a comment",
#         operation_description="Delete an existing comment.",
#         responses={
#             status.HTTP_204_NO_CONTENT: "Comment deleted successfully",
#             status.HTTP_404_NOT_FOUND: "Comment not found",
#         },
#     )
#     def destroy(self, request, *args, **kwargs):
#         """
#         Delete a comment.

#         This endpoint allows you to delete an existing comment.
#         """
#         return super().destroy(request, *args, **kwargs)
