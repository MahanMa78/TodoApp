from django.test import TestCase
from .models import Task
from accounts.models import CustomUser

from django.contrib.auth import get_user_model

class TaskModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username = 'mahan',
            email = 'mahan@email.com',
            password = 'password',
        )
        
        cls.task = Task.objects.create(
            # author = CustomUser.objects.create_user(username='mahan', password='password') , TODO --> ham ba in ravesh va ham ba ravesh ziri mishe
            author = cls.user,
            title = "First task",
            body = "A body of text here",
        )
        
    def test_model_content(self):
        self.assertEqual(self.task.author.username , 'mahan')
        self.assertEqual(self.task.author.email , 'mahan@email.com')
        self.assertEqual(self.task.title,"First task")
        self.assertEqual(self.task.body , "A body of text here")
        self.assertEqual(str(self.task),"First task")
