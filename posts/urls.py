from django.urls import path
from . import views
from .views import PostCreateView

urlpatterns = [
    
    path('posts/', views.PostListCreateAPIView.as_view(), name='post-list-create'),
    path('<int:pk>/', views.PostRetrieveUpdateDestroyAPIView.as_view(), name='post-detail'),
    path('create/', views.PostCreateView.as_view(), name='post-create'),
    path('all/', views.PostListView.as_view(), name='post-list'),
    path('<int:pk>/detail/', views.PostDetailView.as_view(), name='post-detail-view'),
]
