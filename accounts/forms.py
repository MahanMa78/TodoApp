from django.contrib.auth.forms import UserCreationForm , UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields =  ("email","birth_date",)


        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields =  ("email","birth_date",'first_name' , 'last_name')