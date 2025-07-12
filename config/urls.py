from django.contrib import admin
from django.urls import path , include
from accounts.views import GoogleLogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('tasks.urls')),
    path('api/' , include('apis.urls')),
    path("api-auth/", include("rest_framework.urls")),
    path("api/dj-rest-auth/", include("dj_rest_auth.urls")), 
    path('api/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/dj-rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('accounts/', include('allauth.urls')), # برای reset password و تأیید ایمیل
]
