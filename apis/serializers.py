from rest_framework import serializers
from django.contrib.auth import get_user_model 
from tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'id',
            'author',
            'title',
            'body',
            'completed',
            'created'
        )
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "username",'email' , "first_name" , 'last_name')