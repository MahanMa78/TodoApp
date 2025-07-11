from rest_framework import generics
from tasks.models import Task
from .serializers import TaskSerializer

class ListTask(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class DetailTask(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

