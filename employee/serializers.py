from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Employee


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Employee
        fields = ['id', 'user', 'department', 'position']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        employee = Employee.objects.create(user=user, **validated_data)
        return employee

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user

        instance.department = validated_data.get('department', instance.department)
        instance.position = validated_data.get('position', instance.position)
        instance.save()

        user.username = user_data.get('username', user.username)
        user.email = user_data.get('email', user.email)
        user.save()

        return instance
