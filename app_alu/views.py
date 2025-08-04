# app_alu/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Alumno

# CREATE (Crear) y READ (Leer - parte del formulario)
def agregar_alumno(request):
    especialidades = Alumno.ESPECIALIDAD_CHOICES
    
    if request.method == 'POST':
        # Obtenemos los datos del formulario
        nombre = request.POST.get('nombre')
        matricula = request.POST.get('matricula')
        especialidad = request.POST.get('especialidad')
        
        # Creamos una nueva instancia de Alumno y la guardamos
        Alumno.objects.create(
            nombre=nombre,
            matricula=matricula,
            especialidad=especialidad
        )
        # Redirigimos a la página de inicio para ver la lista actualizada
        return redirect('inicio')
        
    # Si es un GET, solo mostramos el formulario
    return render(request, 'agregar_alumno.html', {'especialidades': especialidades})

# READ (Leer - lista principal)
def inicio(request):
    # Obtenemos todos los objetos Alumno de la base de datos
    alumnos = Alumno.objects.all()
    # Pasamos los alumnos a la plantilla para que los muestre
    return render(request, 'inicio.html', {'alumnos': alumnos})

# UPDATE (Actualizar)
def actualizar_alumno(request, id):
    # Obtenemos el alumno específico o mostramos un error 404 si no existe
    alumno = get_object_or_404(Alumno, id=id)
    especialidades = Alumno.ESPECIALIDAD_CHOICES

    if request.method == 'POST':
        # Actualizamos los campos del alumno con los datos del formulario
        alumno.nombre = request.POST.get('nombre')
        alumno.matricula = request.POST.get('matricula')
        alumno.especialidad = request.POST.get('especialidad')
        alumno.save() # Guardamos los cambios en la base de datos
        return redirect('inicio')
    
    # Si es GET, pasamos el alumno y las especialidades a la plantilla de actualización
    context = {
        'alumno': alumno,
        'especialidades': especialidades
    }
    return render(request, 'actualizar_alumno.html', context)

# DELETE (Borrar)
def borrar_alumno(request, id):
    # Obtenemos el alumno a borrar
    alumno = get_object_or_404(Alumno, id=id)
    
    # Solo permitimos borrar vía POST por seguridad
    if request.method == 'POST':
        alumno.delete() # Borramos el objeto de la base de datos
        return redirect('inicio')
    
    # Si alguien intenta acceder por GET, lo redirigimos
    return redirect('inicio')