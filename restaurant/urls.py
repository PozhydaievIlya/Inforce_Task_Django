from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import *

urlpatterns = [
    path('api/menu/', MenuListAPIView.as_view(), name='menu-list'),
    path('api/menu/create/', MenuCreateAPIView.as_view(), name='menu-create'),
    path('api/menu/<int:pk>/', MenuDetailAPIView.as_view(), name='menu-detail'),
    path('api/menu/today/', CurrentDayMenuAPIView.as_view(), name='current-day-menu'),
    path('api/restaurants/create', RestaurantListCreateAPIView.as_view(), name='restaurant-list-create'),
    path('api/restaurants/<int:pk>/', RestaurantRetrieveUpdateDestroyAPIView.as_view(), name='restaurant-detail'),
    path('api/restaurants/', RestaurantListAPIView.as_view(), name='restaurant-list'),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/', UserView.as_view(), name='user'),
]
