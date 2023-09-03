from django.urls import path
from .views import (
    CustomUserAPIView,
    UserListCreateAPIView,
    UserRetrieveUpdateDestroyAPIView,
    UserCreateView,
    UserListView,
    UserDetailView,
    UserUpdateView,
    UserDeleteView,
    UserList,
    UserFilterView,
)

urlpatterns = [
    path('api/users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('api/users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-retrieve-update-destroy'),
    path('api/users/create/', UserCreateView.as_view(), name='user-create'),
    path('api/users/<int:pk>/detail/', UserDetailView.as_view(), name='user-detail-view'),
    
    # Добавлены новые пути для пагинации и фильтрации
    path('api/users/paginated/', UserList.as_view(), name='user-list-paginated'),
    path('api/users/filtered/', UserFilterView.as_view(), name='user-list-filtered'),
]
