from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    birth_date = models.DateField(null = True , blank=True)
    phone_number = models.CharField(max_length=20 , null=True , blank=True)
    
    def __str__(self):
        return self.username