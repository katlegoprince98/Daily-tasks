from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def index(request):
    return render(request, 'index.html')

