from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



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
    path('api/', include('users.urls')),  
    # path('api/', include('myblog.urls')),  
    path('api/', include('posts.urls')), 
    path('api/', include('comments.urls')),  
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
]


