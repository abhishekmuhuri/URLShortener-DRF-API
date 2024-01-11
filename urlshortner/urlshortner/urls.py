from django.contrib import admin
from django.urls import path, include
from api.views import URLRedirection
from rest_framework import permissions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('<str:pk>', URLRedirection.as_view(), name='url_redirection'),
    path('user/', include('user.urls')),
]
