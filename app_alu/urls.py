# app_alu/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # READ: Página de inicio que muestra todos los alumnos
    path("", views.inicio, name='inicio'),
    
    # CREATE: Ruta para mostrar el formulario y para procesar la adición de un alumno
    path("agregar/", views.agregar_alumno, name='agregar_alumno'),
    
    # UPDATE: Ruta para actualizar un alumno específico por su ID
    path("actualizar/<int:id>/", views.actualizar_alumno, name="actualizar_alumno"),
    
    # DELETE: Ruta para borrar un alumno específico por su ID
    path("borrar/<int:id>/", views.borrar_alumno, name="borrar_alumno"),
]