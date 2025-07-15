"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include ,re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Todo API Project",
      default_version='v1',
      description= "A sample blog about Todo WebAplication",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="mahan@email.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('tasks.urls')),
    path('api/' , include('apis.urls')),
    path("api-auth/", include("rest_framework.urls")), 
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


"""
        Django for apis/ page-168(176)
        path("api/schema/", SpectacularAPIView.as_view(), name="schema")
        
        in ravesh dynamic hast baraye taghirat api ke schema ro namayesh bede baraye computer ( A schema is a machine-readable document that outlines all available API endpoints, URLs, and
        the HTTP verbs (GET, POST, PUT, DELETE, etc.). This is great but not very readable for a human.)
        
        Enter documentation which is something added to a schema that makes it easier for humans to
        read and consume.
        
    """