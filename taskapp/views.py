from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    context = {"tasks": tasks}
    return render(request, 'index.html', context)

def create_task(request):
    if request.method == "POST":
        title = request.POST["title"]
        query = Task(title=title)
        query.save()
        return redirect("/")
    

   
    
