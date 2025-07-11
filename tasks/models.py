from django.db import models
from django.conf import settings

class Task(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE ,related_name='tasks' ,  )
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(default="empty")
    
    def __str__(self):
        return self.title
    
    
