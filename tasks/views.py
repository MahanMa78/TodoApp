from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

def index(request):
    
    form = TaskForm()
    
    tasks = Task.objects.all()
    
    if request.method == 'POST':
        
        form = TaskForm(request.POST)
        
        if form.is_valid():
            form.save()
        
        return redirect('/')        
                
    context = {'tasks':tasks , "TaskForm" : form}
    
    return render(request , 'tasks.html',context )