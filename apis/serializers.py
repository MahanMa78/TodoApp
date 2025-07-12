from rest_framework import serializers
from tasks.models import Task
from dj_rest_auth.registration.serializers import RegisterSerializer
from accounts.models import CustomUser

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
        
        
# class CustomRegisterSerializer(RegisterSerializer):
#     birth_date = serializers.DateField(required=False)
#     phone_number = serializers.CharField(required = False)
    
#     def get_cleaned_data(self):
#         data = super().get_cleaned_data()
#         data['birth_date'] = self.validated_data.get('birth_date', '')
#         data['phone_number'] = self.validated_data.get('phone_number' , '')
#         return data

class CustomRegisterSerializer(RegisterSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"
    