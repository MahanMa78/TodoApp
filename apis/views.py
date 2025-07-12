from rest_framework import generics , permissions
from tasks.models import Task
from .serializers import TaskSerializer

class ListTask(generics.ListCreateAPIView): # * az ListAPIView be ListCreateAPIView taghir midahim baraye inke ghabeliat hay read-write ro dashte bashim
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class DetailTask(generics.RetrieveUpdateDestroyAPIView): # * az RetrieveAPIView be RetrieveUpdateDestroyAPIView taghir midim baraye read, updated, or deleted
    permission_classes = (permissions.IsAuthenticated , )
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

