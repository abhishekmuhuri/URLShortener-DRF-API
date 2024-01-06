from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('shortenURL/<str:pk>/',views.urlAPI.as_view()),
    path('shortenURL',views.urlAPI.as_view())
]
