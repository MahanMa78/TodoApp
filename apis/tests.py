from django.test import TestCase
from django.urls import reverse
from rest_framework import status  
from rest_framework.test import APITestCase

from tasks.models import Task


class TaskModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.task = Task.objects.create(
            title = "First task",
            body = "A body of text here",
        )
            
    def test_model_content(self):
        self.assertEqual(self.task.title,"First task")
        self.assertEqual(self.task.body , "A body of text here")
        self.assertEqual(str(self.task),"First task")       
    # TODO ---> test_model_content dar tasks/test.py ham neveshte shode da inja serfan baraye yadavari mojadad neveshte shode(haminjori neveshtam ta dagig tar bashe😁)
            
    def test_api_listview(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code ,status.HTTP_200_OK)
        self.assertEqual(Task.objects.count() ,1)
        self.assertContains(response , self.task)
        
        
    def test_api_detailview(self):
        response = self.client.get(
            reverse("task_detail" , kwargs={"pk" : self.task.id}),
            format = "json"
        )
        self.assertEqual(response.status_code , status.HTTP_200_OK)
        self.assertEqual(Task.objects.count() , 1)
        self.assertContains(response , "First task")
        