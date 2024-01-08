from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    ## shortenURL Endpoints
    path('shortenURL/<str:pk>/', views.urlAPI.as_view()),
    path('shortenURL', views.urlAPI.as_view()),
    ## User Endpoints
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('users/create',views.UserAPI.as_view()),
]
