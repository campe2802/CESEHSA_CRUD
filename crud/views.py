
from django.shortcuts import render, redirect
from .models import Tarea
# from .forms import TareaForm

# Create your views here.

def index(request):
    tareas = Tarea.objects.all()
    context = {
        'tareas': tareas
    }
    return render(request, 'crud/home.html', context)
