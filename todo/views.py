from django.shortcuts import render,redirect
from .models import Task
from .forms import taskform

# Create your views here.
def task_list(request):
    task = Task.objects.all()
    form = taskform()
    if request.method =='POST':
        form = taskform(request.POST)
    if form.is_valid():
        form.save()
        return redirect  ("task_list")  
    context = {"tasks":task, "form": form}
    return render(request, "task_list.html", context)

def task_update(request, pk):
    task = Task.objects.get(id=pk)
    form = taskform(instance=task)
    if request.method == 'POST':
        form = taskform( request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    context = {"form":form}
    return render(request, "task_list.html", context)

def task_delete(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect("task_list")
    context = {"task":task}
    return render(request, "task_delete.html", context)