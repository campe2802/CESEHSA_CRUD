
from django.shortcuts import render, redirect
from .models import Tarea
from .forms import TareaForm

# Create your views here.

def index(request):
    tareas = Tarea.objects.all()
    context = {
        'tareas': tareas
    }
    return render(request,'crud/home.html', context)

def agregar(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TareaForm()
    else:
        # POST data submitted; process data.
        form = TareaForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud_app:index')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'crud/agregar.html', context)