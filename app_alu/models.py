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