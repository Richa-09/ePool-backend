from django.contrib import admin
from django.urls import path, include
from app import urls
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(urls)),
    path('auth/', obtain_auth_token)
]
