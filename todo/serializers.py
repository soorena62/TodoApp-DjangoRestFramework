from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Todo
# Create your models here:


User = get_user_model()


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


class UserTodoSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'
