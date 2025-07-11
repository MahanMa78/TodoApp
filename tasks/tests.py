from django.test import TestCase
from .models import Task
from accounts.models import CustomUser


class TaskModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.task = Task.objects.create(
            author = CustomUser.objects.create_user(username='mahan', password='password'),
            title = "First task",
            body = "A body of text here",
        )
        
    def test_model_content(self):
        self.assertEqual(self.task.title,"First task")
        self.assertEqual(self.task.body , "A body of text here")
        self.assertEqual(str(self.task),"First task")
