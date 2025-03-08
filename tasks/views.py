from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

def index(request):
    
    form = TaskForm()
    
    tasks = Task.objects.all()
    
    context = {'tasks':tasks , "TaskForm" : form}
    
    return render(request , 'tasks.html',context )