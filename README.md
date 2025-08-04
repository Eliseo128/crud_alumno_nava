
Proyecto: Crud Alumno Django con bootstrap.  
Carpeta de trabajo: CrudAlumno.  
Carpeta del proyecto: Backend\_alu  
Carpeta aplicación: app\_alu.  
Explicación documentada para cada punto del procedimiento  
procedimiento:

1. Instrucciones para crear el entorno virtual y su activación.  
2. instrucción para seleccionar intérprete de python.  
3. Instrucción para instalar Django.  
4. Crear la carpeta “static” dentro de la carpeta app\_alu.  
5. Crear la carpeta templates dentro de app\_alu.  
6. Crear los archivos, base.html, header.html, footer.html, inicio.html,agregar\_alumno.html, info\_alumno.html, actualizar\_alumno  
7. En el archivo inicio.html (título, tabla para mostrarlos alumnos con botones de acción de actualizar y borrar, y al final de la tabla el botón agregar alumno.  
8. realizar las configuraciones en [setting.py](http://setting.py) y [urls.py](http://urls.py) del proyecto.  
9. Utilizar un formato elegante.  
10. No utilizar [forms.py](http://forms.py)  
11. Crear las funciones en [views.py](http://views.py) para realizar las operaciones del CRUD.  
12. Al final crear un glosario de términos utilizados con su explicación.  
13. Tecnologías utilizadas para el frontend y backend.  
14. Realiza un resumen.  
15. link de referencias.  
16. Enseguida envio el [models.py](http://models.py) y [urls.py](http://urls.py) de app\_alu.  
17. el modelo

class Alumno(models.Model):  
    ESPECIALIDAD\_CHOICES \= \[  
        ('RH', 'Recursos Humanos'),  
        (ELO', 'Electrónica'),  
        ('POG', 'Programación'),  
        ('GE', 'Gericultura')  
    \]  
    nombre \= models.CharField(max\_length=30)  
    especialidad \= models.CharField(max\_length=100, choices=ESPECIALIDAD\_CHOICES, default='RH')  
    matricula \= models.CharField(max\_length=10, unique=True)

18. El urls.py

from django.urls import path  
from . import views

urlpatterns \= \[  
    path("", views.inicio, name='inicio'),  
    path("agregar/", views.agregar\_alumno, name='agregar\_alumno'),  
    path("actualizar/\<int:student\_id\>/", views.actualizar\_alumno, name="actualizar\_alumno"),  
    path("borrar/\<int:id\>/", views.borrar\_alumno, name="borrar\_alumno"),  
\]

19. Al inicio crear la estructura de carpetas y archivos.  
20. No se te olvide crear los archivos html para las operaciones del CRUD.

    



¡Excelente proyecto! Aquí tienes una guía completa y documentada para desarrollar tu CRUD de Alumnos utilizando Django y Bootstrap, siguiendo al pie de la letra tus especificaciones.

---

### **Proyecto: CRUD de Alumnos con Django y Bootstrap**

Este documento detalla el proceso de creación de una aplicación web para la gestión de alumnos (Crear, Leer, Actualizar, Borrar) utilizando el framework Django para el backend y Bootstrap para un diseño frontal limpio y responsivo.

---

### **Estructura Final de Carpetas y Archivos**

Antes de comenzar, visualicemos la estructura que vamos a construir. Esto nos dará un mapa claro del proyecto.

```
CrudAlumno/
├── Backend_alu/
│   ├── Backend_alu/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py  <-- Configuraremos aquí
│   │   ├── urls.py      <-- Configuraremos aquí
│   │   └── wsgi.py
│   ├── app_alu/
│   │   ├── migrations/
│   │   ├── static/      <-- Carpeta para CSS, JS, imágenes
│   │   │   └── css/
│   │   │       └── style.css (Opcional)
│   │   ├── templates/   <-- Carpeta para HTML
│   │   │   ├── agregar_alumno.html
│   │   │   ├── actualizar_alumno.html
│   │   │   ├── base.html
│   │   │   ├── footer.html
│   │   │   ├── header.html
│   │   │   └── inicio.html
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py    <-- Definiremos el modelo aquí
│   │   ├── tests.py
│   │   ├── urls.py      <-- Definiremos las rutas de la app aquí
│   │   └── views.py     <-- Escribiremos la lógica aquí
│   └── manage.py
└── venv/                  <-- Entorno virtual
```

---

### **Procedimiento Detallado**

#### **Paso 1: Crear el Entorno Virtual**

Un entorno virtual es una carpeta que contiene una instalación de Python independiente. Esto nos permite aislar las dependencias de nuestro proyecto para no generar conflictos con otros proyectos.

1.  Abre una terminal o línea de comandos.
2.  Navega hasta la carpeta donde quieres crear tu proyecto (por ejemplo, `Documentos/Proyectos/`).
3.  Crea la carpeta de trabajo principal y entra en ella.

    ```bash
    mkdir CrudAlumno
    cd CrudAlumno
    ```

4.  Crea el entorno virtual. Usaremos el módulo `venv` que viene con Python. Le llamaremos `venv`.

    ```bash
    # En Windows
    python -m venv venv

    # En macOS / Linux
    python3 -m venv venv
    ```

#### **Paso 2: Activar el Entorno Virtual y Seleccionar Intérprete**

Para usar el entorno, primero debemos activarlo.

*   **Activación en la terminal:**

    ```bash
    # En Windows (cmd.exe)
    venv\Scripts\activate

    # En Windows (PowerShell)
    venv\Scripts\Activate.ps1

    # En macOS / Linux
    source venv/bin/activate
    ```

    Una vez activado, verás `(venv)` al inicio de la línea de tu terminal.

*   **Seleccionar Intérprete en VS Code (Recomendado):**
    1.  Abre la carpeta `CrudAlumno` en Visual Studio Code.
    2.  Abre la Paleta de Comandos: `Ctrl+Shift+P` (o `Cmd+Shift+P` en Mac).
    3.  Escribe y selecciona: `Python: Select Interpreter`.
    4.  Elige el intérprete que tiene la ruta a tu entorno virtual (`./venv/Scripts/python.exe` o `./venv/bin/python`). VS Code a menudo lo sugiere como "Recomendado".

#### **Paso 3: Instalar Django y Crear el Proyecto**

Con el entorno activado, instalamos Django y creamos la estructura del proyecto y la aplicación.

```bash
# Instalar Django
pip install django

# Crear el proyecto Django llamado Backend_alu
# El punto (.) al final evita crear una carpeta extra del mismo nombre
django-admin startproject Backend_alu .

# Crear la aplicación llamada app_alu
python manage.py startapp app_alu
```

#### **Paso 4: Crear Carpetas `static` y `templates`**

Dentro de la carpeta de la aplicación (`app_alu`), crearemos los directorios para los archivos estáticos (CSS, JS) y las plantillas (HTML).

```bash
# Desde la carpeta raíz (CrudAlumno)
# Crear la carpeta templates
mkdir app_alu/templates

# Crear la carpeta static
mkdir app_alu/static
```

#### **Paso 5: Configuración del Proyecto (`settings.py` y `urls.py`)**

Ahora, conectaremos todo en los archivos de configuración principales.

**A. Archivo `Backend_alu/settings.py`:**

1.  **Registrar la aplicación:** Añade `'app_alu'` a la lista `INSTALLED_APPS`.

    ```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'app_alu', # <-- AÑADIR ESTA LÍNEA
    ]
    ```

2.  **Configurar la carpeta de plantillas:** Dile a Django dónde buscar los archivos HTML.

    ```python
    import os # Asegúrate de que 'import os' esté al principio del archivo

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            # AÑADIR ESTA LÍNEA
            'DIRS': [os.path.join(BASE_DIR, 'app_alu/templates')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
    ```

3.  **Configurar la carpeta de archivos estáticos (opcional pero recomendado):**

    ```python
    # Al final del archivo settings.py
    STATIC_URL = 'static/'

    # AÑADIR ESTAS LÍNEAS
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'app_alu/static'),
    ]
    ```

**B. Archivo `Backend_alu/urls.py`:**

Configura la URL principal del proyecto para que redirija las peticiones a nuestra aplicación `app_alu`.

```python
from django.contrib import admin
from django.urls import path, include # <-- Importar 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_alu.urls')), # <-- AÑADIR ESTA LÍNEA
]
```

#### **Paso 6: Definir el Modelo (`app_alu/models.py`)**

Este archivo define la estructura de la tabla `Alumno` en la base de datos. Pega el código que proporcionaste.

```python
# app_alu/models.py
from django.db import models

class Alumno(models.Model):
    ESPECIALIDAD_CHOICES = [
        ('RH', 'Recursos Humanos'),
        ('ELO', 'Electrónica'),
        ('POG', 'Programación'),
        ('GE', 'Gericultura')
    ]
    nombre = models.CharField(max_length=30)
    especialidad = models.CharField(max_length=100, choices=ESPECIALIDAD_CHOICES, default='RH')
    matricula = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.nombre
```

#### **Paso 7: Realizar Migraciones**

Las migraciones son la forma en que Django aplica los cambios de tus modelos (como crear una nueva tabla) a la base de datos.

```bash
# Crea el archivo de migración basado en los cambios del models.py
python manage.py makemigrations

# Aplica la migración a la base de datos
python manage.py migrate
```

#### **Paso 8: Crear las Plantillas HTML (`app_alu/templates/`)**

Ahora creamos los archivos HTML. Usaremos la herencia de plantillas de Django para no repetir código.

**`base.html` (Plantilla Maestra)**
Contiene la estructura HTML base, incluyendo Bootstrap y bloques que otras plantillas llenarán.

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF--8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Sistema de Alumnos{% endblock %}</title>
    <!-- Bootstrap 5.3 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">

    {% include 'header.html' %}

    <main class="container mt-4">
        {% block content %}
        <!-- El contenido de cada página irá aquí -->
        {% endblock %}
    </main>

    {% include 'footer.html' %}

    <!-- Bootstrap 5.3 JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

**`header.html` (Cabecera)**

```html
<header class="bg-primary text-white p-4 text-center shadow-sm">
    <h1>Gestión de Alumnos - CBTis 168</h1>
</header>
```

**`footer.html` (Pie de Página)**

```html
<footer class="container-fluid bg-dark text-white text-center p-3 mt-5">
    <p>&copy; 2023 Mi Proyecto CRUD. Todos los derechos reservados.</p>
</footer>
```

**`inicio.html` (Página Principal - Leer)**
Muestra la lista de alumnos en una tabla.

```html
{% extends 'base.html' %}

{% block title %}Inicio - Lista de Alumnos{% endblock %}

{% block content %}
<div class="card shadow">
    <div class="card-header bg-dark text-white">
        <h2 class="h4 mb-0">Listado de Alumnos Registrados</h2>
    </div>
    <div class="card-body">
        <div class="table-responsive">
            <table class="table table-striped table-hover">
                <thead class="table-dark">
                    <tr>
                        <th>Nombre Completo</th>
                        <th>Matrícula</th>
                        <th>Especialidad</th>
                        <th>Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    {% for alumno in alumnos %}
                    <tr>
                        <td>{{ alumno.nombre }}</td>
                        <td>{{ alumno.matricula }}</td>
                        <td>{{ alumno.get_specialidad_display }}</td> <!-- Muestra el nombre legible -->
                        <td>
                            <a href="{% url 'actualizar_alumno' alumno.id %}" class="btn btn-warning btn-sm">Actualizar</a>
                            
                            <!-- Formulario para Borrar con método POST para seguridad -->
                            <form action="{% url 'borrar_alumno' alumno.id %}" method="post" style="display: inline;">
                                {% csrf_token %}
                                <button type="submit" class="btn btn-danger btn-sm" onclick="return confirm('¿Estás seguro de que deseas eliminar a este alumno?');">Borrar</button>
                            </form>
                        </td>
                    </tr>
                    {% empty %}
                    <tr>
                        <td colspan="4" class="text-center">No hay alumnos registrados.</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>
    <div class="card-footer text-end">
        <a href="{% url 'agregar_alumno' %}" class="btn btn-success">
            <i class="fas fa-plus"></i> Agregar Nuevo Alumno
        </a>
    </div>
</div>
{% endblock %}
```

**`agregar_alumno.html` (Formulario para Crear)**

```html
{% extends 'base.html' %}

{% block title %}Agregar Alumno{% endblock %}

{% block content %}
<div class="card shadow mx-auto" style="max-width: 600px;">
    <div class="card-header bg-success text-white">
        <h2 class="h4 mb-0">Registrar Nuevo Alumno</h2>
    </div>
    <div class="card-body">
        <form action="{% url 'agregar_alumno' %}" method="POST">
            {% csrf_token %}
            <div class="mb-3">
                <label for="nombre" class="form-label">Nombre Completo:</label>
                <input type="text" name="nombre" id="nombre" class="form-control" required>
            </div>
            <div class="mb-3">
                <label for="matricula" class="form-label">Matrícula:</label>
                <input type="text" name="matricula" id="matricula" class="form-control" required>
            </div>
            <div class="mb-3">
                <label for="especialidad" class="form-label">Especialidad:</label>
                <select name="especialidad" id="especialidad" class="form-select" required>
                    {% for value, display in especialidades %}
                        <option value="{{ value }}">{{ display }}</option>
                    {% endfor %}
                </select>
            </div>
            <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                <a href="{% url 'inicio' %}" class="btn btn-secondary">Cancelar</a>
                <button type="submit" class="btn btn-primary">Guardar Alumno</button>
            </div>
        </form>
    </div>
</div>
{% endblock %}
```

**`actualizar_alumno.html` (Formulario para Actualizar)**

```html
{% extends 'base.html' %}

{% block title %}Actualizar Alumno{% endblock %}

{% block content %}
<div class="card shadow mx-auto" style="max-width: 600px;">
    <div class="card-header bg-warning text-dark">
        <h2 class="h4 mb-0">Actualizar Datos del Alumno</h2>
    </div>
    <div class="card-body">
        <form method="POST">
            {% csrf_token %}
            <div class="mb-3">
                <label for="nombre" class="form-label">Nombre Completo:</label>
                <input type="text" name="nombre" id="nombre" class="form-control" value="{{ alumno.nombre }}" required>
            </div>
            <div class="mb-3">
                <label for="matricula" class="form-label">Matrícula:</label>
                <input type="text" name="matricula" id="matricula" class="form-control" value="{{ alumno.matricula }}" required>
            </div>
            <div class="mb-3">
                <label for="especialidad" class="form-label">Especialidad:</label>
                <select name="especialidad" id="especialidad" class="form-select" required>
                    {% for value, display in especialidades %}
                        <option value="{{ value }}" {% if alumno.especialidad == value %}selected{% endif %}>
                            {{ display }}
                        </option>
                    {% endfor %}
                </select>
            </div>
            <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                <a href="{% url 'inicio' %}" class="btn btn-secondary">Cancelar</a>
                <button type="submit" class="btn btn-primary">Actualizar Alumno</button>
            </div>
        </form>
    </div>
</div>
{% endblock %}
```
*Nota: El archivo `info_alumno.html` no se ha creado ya que no está en las URLs, pero podría ser una página de solo lectura si se desea.*

#### **Paso 9: Definir las URLs de la Aplicación (`app_alu/urls.py`)**

Crea este archivo si no existe y pega el código que proporcionaste, asegurándote de que los nombres de las vistas coincidan.

```python
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
```

#### **Paso 10: Crear las Funciones en `views.py`**

Aquí reside la lógica del CRUD. Django recibirá las peticiones, estas funciones las procesarán y devolverán una respuesta (generalmente, renderizando un HTML).

```python
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
```

---

### **Finalización del Proyecto**

#### **Tecnologías Utilizadas**

*   **Backend:**
    *   **Python:** Lenguaje de programación principal.
    *   **Django:** Framework web de alto nivel para un desarrollo rápido y seguro.
    *   **Django ORM:** Mapeador Objeto-Relacional para interactuar con la base de datos (SQLite por defecto) usando objetos de Python.
*   **Frontend:**
    *   **HTML5:** Lenguaje de marcado para la estructura de las páginas.
    *   **Bootstrap 5:** Framework de CSS para crear diseños responsivos y elegantes rápidamente.
    *   **Django Template Language:** Sistema de plantillas para generar HTML dinámicamente.

#### **Glosario de Términos Utilizados**

*   **CRUD:** Acrónimo de **C**reate (Crear), **R**ead (Leer), **U**pdate (Actualizar), **D**elete (Borrar). Son las cuatro operaciones básicas de la persistencia de datos.
*   **Entorno Virtual (venv):** Un directorio aislado que contiene una instalación de Python y paquetes específicos para un proyecto, evitando conflictos de dependencias.
*   **Django:** Un framework web de Python que sigue el patrón de arquitectura Modelo-Vista-Plantilla (MVT).
*   **Framework:** Un conjunto de herramientas y librerías que proporciona una estructura base para desarrollar software.
*   **ORM (Object-Relational Mapping):** Técnica que permite interactuar con una base de datos relacional (como si fueran tablas) utilizando un lenguaje de programación orientado a objetos (como Python). El `models.py` de Django es su ORM.
*   **Migración:** Un archivo generado por Django que describe los cambios en los modelos para ser aplicados a la base de datos.
*   **Plantilla (Template):** Un archivo (generalmente HTML) que contiene la estructura de la vista, con marcadores de posición para datos dinámicos.
*   **Vista (View):** Una función en Django que procesa una solicitud web y devuelve una respuesta. Es la lógica de negocio de la aplicación.
*   **URL Dispatcher:** El sistema de Django que, basado en la URL solicitada, decide qué vista debe ejecutar.
*   **Bootstrap:** Un popular framework de frontend para diseñar sitios web responsivos y visualmente atractivos con componentes pre-construidos.
*   **CSRF Token (`{% csrf_token %}`):** Medida de seguridad de Django para proteger los formularios contra ataques de Falsificación de Solicitud en Sitios Cruzados.

#### **Resumen del Proyecto**

Se ha construido una aplicación web completa que permite gestionar un listado de alumnos. El proyecto utiliza Django para toda la lógica de backend, incluyendo la definición del modelo de datos, el manejo de peticiones HTTP y la interacción con la base de datos a través de su ORM. No se utilizó el sistema de formularios de Django (`forms.py`) para manejar la validación y renderizado, optando por procesar los datos del formulario manualmente desde el objeto `request` en las vistas. Para el frontend, se empleó Bootstrap 5 para garantizar una interfaz de usuario moderna, limpia y adaptable a diferentes dispositivos, utilizando la herencia de plantillas de Django para mantener el código HTML organizado y reutilizable.

#### **Link de Referencias**

*   **Documentación oficial de Django:** [https://docs.djangoproject.com/en/stable/](https://docs.djangoproject.com/en/stable/)
*   **Documentación oficial de Bootstrap:** [https://getbootstrap.com/docs/5.3/getting-started/introduction/](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
*   **Guía de instalación de Python:** [https://www.python.org/downloads/](https://www.python.org/downloads/)
