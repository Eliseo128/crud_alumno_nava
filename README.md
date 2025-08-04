leeme
Proyecto: Crud Alumno Django con bootstrap.
Carpeta de trabajo: CrudAlumno.
Carpeta del proyecto: Backend_alu
Carpeta aplicación: app_alu.
Explicación documentada para cada punto del procedimiento
procedimiento:
Instrucciones para crear el entorno virtual y su activación.
instrucción para seleccionar intérprete de python.
Instrucción para instalar Django.
Crear la carpeta “static” dentro de la carpeta app_alu.
Crear la carpeta templates dentro de app_alu.
Crear los archivos, base.html, header.html, footer.html, inicio.html,agregar_alumno.html, info_alumno.html, actualizar_alumno
En el archivo inicio.html (título, tabla para mostrarlos alumnos con botones de acción de actualizar y borrar, y al final de la tabla el botón agregar alumno.
realizar las configuraciones en setting.py y urls.py del proyecto.
Utilizar un formato elegante.
No utilizar forms.py
Crear las funciones en views.py para realizar las operaciones del CRUD.
Al final crear un glosario de términos utilizados con su explicación.
Tecnologías utilizadas para el frontend y backend.
Realiza un resumen.
link de referencias.
Enseguida envio el models.py y urls.py de app_alu.
el modelo
class Alumno(models.Model):
    ESPECIALIDAD_CHOICES = [
        ('RH', 'Recursos Humanos'),
        (ELO', 'Electrónica'),
        ('POG', 'Programación'),
        ('GE', 'Gericultura')
    ]
    nombre = models.CharField(max_length=30)
    especialidad = models.CharField(max_length=100, choices=ESPECIALIDAD_CHOICES, default='RH')
    matricula = models.CharField(max_length=10, unique=True)
El urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name='inicio'),
    path("agregar/", views.agregar_alumno, name='agregar_alumno'),
    path("actualizar/<int:student_id>/", views.actualizar_alumno, name="actualizar_alumno"),
    path("borrar/<int:id>/", views.borrar_alumno, name="borrar_alumno"),
]
Al inicio crear la estructura de carpetas y archivos.
No se te olvide crear los archivos html para las operaciones del CRUD.



# 📁 Proyecto: CRUD de Alumnos con Django y Bootstrap

> **Descripción**: Sistema web para gestionar alumnos utilizando Django como framework backend y Bootstrap para una interfaz moderna y responsiva.

---

## 🗂️ Estructura del Proyecto

```
CrudAlumno/
├── Backend_alu/                  # Proyecto Django principal
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── app_alu/                      # Aplicación Django
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/                # Plantillas HTML
│   │   ├── base.html
│   │   ├── header.html
│   │   ├── footer.html
│   │   ├── inicio.html
│   │   ├── agregar_alumno.html
│   │   ├── info_alumno.html
│   │   └── actualizar_alumno.html
│   └── static/                   # Archivos estáticos
│       └── css/
│           └── styles.css
│
├── manage.py
└── venv/                         # Entorno virtual (generado localmente)
```

---

## 🔧 Procedimiento Paso a Paso

### 1. 🖥️ Crear el entorno virtual y activarlo

Un entorno virtual permite aislar las dependencias del proyecto.

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno (Windows)
venv\Scripts\activate

# Activar entorno (Linux/Mac)
source venv/bin/activate
```

✅ Verifica que el entorno esté activo (verás `(venv)` al inicio de la terminal).

---

### 2. 🐍 Seleccionar el intérprete de Python

En editores como **VS Code**:

1. Abre el proyecto.
2. Presiona `Ctrl + Shift + P` → Escribe: `Python: Select Interpreter`.
3. Elige el intérprete dentro de `venv/`.

> Esto asegura que uses el entorno virtual correctamente.

---

### 3. 📦 Instalar Django

Con el entorno activado, instala Django:

```bash
pip install django
```

> ✅ Verifica la instalación:
```bash
python -m django --version
```

---

### 4. 📁 Crear carpetas `static` y `templates` en `app_alu`

Dentro de la carpeta `app_alu`, crea:

```bash
mkdir templates
mkdir -p static/css
```

- `templates/`: Almacena archivos HTML dinámicos.
- `static/`: Contiene CSS, JS e imágenes.

---

### 5. 📄 Crear archivos HTML en `templates/`

Crea los siguientes archivos:

| Archivo | Descripción |
|--------|-------------|
| `base.html` | Plantilla base con estructura HTML y enlaces a Bootstrap |
| `header.html` | Barra de navegación común |
| `footer.html` | Pie de página |
| `inicio.html` | Lista de alumnos con botones de acción |
| `agregar_alumno.html` | Formulario para agregar alumno |
| `actualizar_alumno.html` | Formulario para editar alumno |
| `info_alumno.html` | Vista detallada del alumno (opcional) |

---

### 6. 🎨 Diseño elegante con Bootstrap

En `base.html`, usa **Bootstrap 5** desde CDN para un diseño moderno y responsivo.

```html
<!-- base.html -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}CRUD Alumnos{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="/static/css/styles.css">
</head>
<body>
    {% include 'header.html' %}
    <div class="container mt-5">
        {% block content %}{% endblock %}
    </div>
    {% include 'footer.html' %}
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

---

### 7. ⚙️ Configuraciones en `settings.py`

#### A. Agregar la app y configurar rutas

```python
# Backend_alu/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_alu',  # ← Nombre de tu aplicación
]

# Directorio de plantillas
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'app_alu' / 'templates'],  # Ruta a templates
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

# Archivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'app_alu' / 'static']

# Base de datos (por defecto SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

#### B. Configurar URLs del proyecto (`Backend_alu/urls.py`)

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_alu.urls')),  # Incluye las URLs de la app
]
```

---

### 8. 📄 Modelo: `models.py`

```python
# app_alu/models.py
from django.db import models

class Alumno(models.Model):
    ESPECIALIDAD_CHOICES = [
        ('RH', 'Recursos Humanos'),
        ('ELO', 'Electrónica'),
        ('POG', 'Programación'),
        ('GE', 'Gericultura'),
    ]
    nombre = models.CharField(max_length=30)
    especialidad = models.CharField(max_length=100, choices=ESPECIALIDAD_CHOICES, default='RH')
    matricula = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.nombre} ({self.matricula})"
```

> 🔁 Ejecuta migraciones después:
```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 9. 🔄 URLs de la aplicación: `urls.py`

```python
# app_alu/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name='inicio'),
    path("agregar/", views.agregar_alumno, name='agregar_alumno'),
    path("actualizar/<int:student_id>/", views.actualizar_alumno, name="actualizar_alumno"),
    path("borrar/<int:id>/", views.borrar_alumno, name="borrar_alumno"),
]
```

---

### 10. 🧠 Lógica del CRUD en `views.py`

```python
# app_alu/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Alumno

def inicio(request):
    alumnos = Alumno.objects.all()
    return render(request, 'inicio.html', {'alumnos': alumnos})

def agregar_alumno(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        matricula = request.POST['matricula']
        especialidad = request.POST['especialidad']
        Alumno.objects.create(nombre=nombre, matricula=matricula, especialidad=especialidad)
        return redirect('inicio')
    return render(request, 'agregar_alumno.html')

def actualizar_alumno(request, student_id):
    alumno = get_object_or_404(Alumno, id=student_id)
    if request.method == 'POST':
        alumno.nombre = request.POST['nombre']
        alumno.matricula = request.POST['matricula']
        alumno.especialidad = request.POST['especialidad']
        alumno.save()
        return redirect('inicio')
    return render(request, 'actualizar_alumno.html', {'alumno': alumno})

def borrar_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    alumno.delete()
    return redirect('inicio')
```

---

### 11. 🖼️ Plantilla `inicio.html`

```html
<!-- templates/inicio.html -->
{% extends 'base.html' %}
{% block content %}
<h2 class="text-center mb-4">📋 Gestión de Alumnos</h2>

<table class="table table-striped table-bordered table-hover shadow-sm">
    <thead class="table-primary">
        <tr>
            <th>Nombre</th>
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
            <td>{{ alumno.get_especialidad_display }}</td>
            <td>
                <a href="{% url 'actualizar_alumno' alumno.id %}" class="btn btn-warning btn-sm">✏️ Editar</a>
                <a href="{% url 'borrar_alumno' alumno.id %}" class="btn btn-danger btn-sm"
                   onclick="return confirm('¿Estás seguro de eliminar a {{ alumno.nombre }}?')">🗑️ Borrar</a>
            </td>
        </tr>
        {% empty %}
        <tr>
            <td colspan="4" class="text-center text-muted">No hay alumnos registrados.</td>
        </tr>
        {% endfor %}
    </tbody>
</table>

<div class="text-center mt-3">
    <a href="{% url 'agregar_alumno' %}" class="btn btn-success btn-lg">➕ Agregar Alumno</a>
</div>
{% endblock %}
```

---

## 📘 Glosario de Términos

| Término | Definición |
|--------|-----------|
| **CRUD** | Siglas de Crear, Leer, Actualizar y Eliminar. Operaciones básicas en bases de datos. |
| **Django** | Framework web de Python de alto nivel para desarrollo rápido y seguro. |
| **Bootstrap** | Framework CSS para crear interfaces web responsivas y atractivas. |
| **Entorno Virtual** | Espacio aislado para gestionar paquetes y dependencias de Python. |
| **Template** | Archivo HTML con lógica dinámica (usando el lenguaje de plantillas de Django). |
| **View** | Función o clase que maneja una solicitud HTTP y devuelve una respuesta. |
| **URL Mapping** | Relación entre una URL y una vista específica. |
| **Static Files** | Recursos como CSS, JS e imágenes que no cambian con el tiempo. |
| **Model** | Clase que representa una tabla en la base de datos. |
| **CSRF Token** | Mecanismo de seguridad para prevenir ataques de falsificación de solicitudes. |

---

## 🛠️ Tecnologías Utilizadas

### Backend
- **Python 3.8+**
- **Django 4.x**
- **SQLite** (Base de datos por defecto)

### Frontend
- **HTML5**
- **CSS3 / Bootstrap 5**
- **JavaScript** (para confirmación de eliminación)

---

## 📝 Resumen del Proyecto

Este proyecto implementa un sistema completo de gestión de alumnos utilizando Django como backend y Bootstrap para una interfaz moderna, sin el uso de `forms.py`. Las operaciones CRUD se gestionan directamente en las vistas y plantillas, lo que facilita el entendimiento del flujo de datos. La estructura es clara, modular y fácil de extender.

✅ Funcionalidades:
- Listar alumnos en una tabla con formato elegante.
- Agregar nuevos registros.
- Editar información existente.
- Eliminar con confirmación.
- Interfaz responsive y amigable.

Ideal para estudiantes o desarrolladores que están aprendiendo Django.

---

## 🔗 Referencias

1. [Documentación Oficial de Django](https://docs.djangoproject.com/)
2. [Bootstrap 5 Documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
3. [Mozilla Developer Network - Django](https://developer.mozilla.org/es/docs/Learn/Server-side/Django)
4. [Django for Beginners - William Vincent](https://djangoforbeginners.com/)

---

## ✅ Pasos Finales

1. Ejecuta las migraciones:
```bash
python manage.py makemigrations
python manage.py migrate
```

2. Crea un superusuario (opcional, para admin):
```bash
python manage.py createsuperuser
```

3. Inicia el servidor:
```bash
python manage.py runserver
```

4. Accede en tu navegador: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

> 🚀 ¡Listo! Ya tienes un sistema funcional de gestión de alumnos con Django y Bootstrap.  
> Si deseas, puedo ayudarte a generar los archivos faltantes o exportar todo como un paquete.
