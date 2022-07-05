from django.shortcuts import render,redirect
from .forms import todolistform
from .models import todolist
# Create your views here.

def index(request):
    tasks = todolist.objects.all()
    ctx = {
        'tasks':tasks
    }
    return render(request,'home.html',ctx)
def create(request):
    form = todolistform()
    if request.method=='POST':
        form = todolistform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    ctx = {
        'forms':form
    }
    return render(request,'create.html',ctx)
def update(request,pk):
    tasks = todolist.objects.get(id=pk)
    form = todolistform(instance=tasks)
    if request.method=='POST':
        form =todolistform(request.POST,instance=tasks)
        if form.is_valid():
            form.save()
            return redirect('home')
    ctx = {
        "form":form
    }
    return render(request,'update.html',ctx)
def delete(request,pk):
    task=todolist.objects.get(id=pk)
    task.delete()
    return redirect('home')
