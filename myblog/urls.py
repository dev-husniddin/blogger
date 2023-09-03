from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Blog Platform API",
        default_version="v1",
        description="RESTful API for managing and accessing blog-related resources.",
        terms_of_service="https://www.your-terms-of-service-url.com/",
        contact=openapi.Contact(email="your@email.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),  # Используйте 'users.urls'
    # path('api/', include('myblog.urls')),  # Подставьте сюда путь к вашим API-маршрутам
    path('api/posts/', include('posts.urls')),  # Добавляем URL-шаблоны для постов
    path('api/comments/', include('comments.urls')),  # Добавляем URL-шаблоны для комментариев
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]


