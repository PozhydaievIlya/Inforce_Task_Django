from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from datetime import datetime, date
from .models import Restaurant, Menu
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer, RestaurantSerializer, MenuSerializer
from django.contrib.auth.models import User


# Views for Authentication and Authorization
# JWT Register at api/register/
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


# JWT Login at api/register/
class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer


# User info at api/user/
class UserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


# Views for restaurant creation and update
class RestaurantListCreateAPIView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantListAPIView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


# Views for menu creation and update
class MenuCreateAPIView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]


class MenuListAPIView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        restaurant_id = self.request.query_params.get('restaurant_id')
        if restaurant_id:
            queryset = queryset.filter(restaurant_id=restaurant_id)
        return queryset


class MenuDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]


class CurrentDayMenuAPIView(generics.ListAPIView):
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        today = date.today()
        return Menu.objects.filter(date=today)
