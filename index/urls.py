from django.contrib import admin
from django.urls import (path, include)
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('book.urls')),
    path('users/', include('user.urls')),
    path('api_token/', obtain_auth_token)
]
