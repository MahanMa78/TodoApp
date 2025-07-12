from rest_framework import generics , permissions
from tasks.models import Task
from .serializers import TaskSerializer

from .permissions import IsAuthorOrReadOnly

class ListTask(generics.ListCreateAPIView): # * az ListAPIView be ListCreateAPIView taghir midahim baraye inke ghabeliat hay read-write ro dashte bashim
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class DetailTask(generics.RetrieveUpdateDestroyAPIView): # * az RetrieveAPIView be RetrieveUpdateDestroyAPIView taghir midim baraye read, updated, or deleted
    # permission_classes = (permissions.IsAuthenticated , ) #TODO ---> in marbot be khode django hast
    permission_classes = (IsAuthorOrReadOnly ,) #! in ro ma khodemon sakhtim ---> faghat on ke chizi neveshte mitone taghirat bede
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

