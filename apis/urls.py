from django.urls import path
# from .views import DetailTask , ListTask , UserList , UserDetail


# urlpatterns = [
#     path("<int:pk>/" , DetailTask.as_view() ,name="task_detail" ),
#     path("" , ListTask.as_view() , name='task_list'),
#     path("users/" , UserList.as_view() , name="user_list"),
#     path("users/<int:pk>/" , UserDetail.as_view() , name="user_detail"),
    
# ]
from rest_framework.routers import SimpleRouter
from .views import UserViewSet , TaskViewSet

router = SimpleRouter()
router.register("users" , UserViewSet , basename='users')
router.register("" , TaskViewSet , basename="tasks")

urlpatterns = router.urls
