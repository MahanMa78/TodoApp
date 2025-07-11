from django.urls import path
from .views import DetailTask , ListTask


urlpatterns = [
    path("<int:pk>/" , DetailTask.as_view() ,name="task_detail" ),
    path("" , ListTask.as_view() , name='task_list'),
]
