from rest_framework import generics , permissions
from tasks.models import Task
from .serializers import TaskSerializer , UserSerializer
from django.contrib.auth import get_user_model 
from rest_framework import viewsets

from .permissions import IsAuthorOrReadOnly

#* yadam bashe baadan baraash tarif konam ke faghat task haie ke on shakhs neveshte ro namayesh bede
# class ListTask(generics.ListCreateAPIView): # * az ListAPIView be ListCreateAPIView taghir midahim baraye inke ghabeliat hay read-write ro dashte bashim
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
    
# class DetailTask(generics.RetrieveUpdateDestroyAPIView): # * az RetrieveAPIView be RetrieveUpdateDestroyAPIView taghir midim baraye read, updated, or deleted
#     # permission_classes = (permissions.IsAuthenticated , ) #TODO ---> in marbot be khode django hast
#     permission_classes = (IsAuthorOrReadOnly ,) #! in ro ma khodemon sakhtim ---> faghat on ke chizi neveshte mitone taghirat bede
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
    
    
# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


# ! viewsets:
class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    