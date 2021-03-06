from django.urls import path
from . import views

app_name = 'crud_app'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page for adding a new task
    path('agregar/', views.agregar, name='agregar'),
    # Page for delete a Task
    path('eliminar/<int:tarea_id>', views.eliminar, name='eliminar'),
    # Page for editing an entry.
    path('editar/<int:tarea_id>/', views.editar, name='editar'),
]