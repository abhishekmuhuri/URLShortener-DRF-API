from django.contrib import admin
from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    ## shortenURL Endpoints
    path('shortenURL/<str:pk>', views.urlAPI.as_view()),
    path('shortenURL', views.urlAPI.as_view()),
    ## List
    path('ShortURLList',views.ShortURLList.as_view()),
    ## User Endpoints
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('users/create',views.UserAPI.as_view()),
    ## Token
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
