from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Todo
# Create your models here:


User = get_user_model()


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

    def priority_validate(self, priority):
        if priority > 20:
            raise serializers.ValidationError("Priority must be less than or equal to 20")
        return priority


class UserTodoSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'
