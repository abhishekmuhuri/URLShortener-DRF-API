from django.contrib import admin
from django.urls import path, include
from api.views import URLRedirection
from . import views

urlpatterns = [
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path('logout', views.logout_request,name='logout'),
    path('test', views.test,name='test'),
]

