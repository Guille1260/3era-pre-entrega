from django.db import models
from django.utils import timezone

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()
    dia = models.CharField(max_length=9, choices=[  # Día de la semana, con opciones limitadas
        ('lunes', 'Lunes'),
        ('martes', 'Martes'),
        ('miércoles', 'Miércoles'),
        ('jueves', 'Jueves'),
        ('viernes', 'Viernes'),
        ('sábado', 'Sábado'),
        ('domingo', 'Domingo'),
    ],blank=False,null=False) 
    hora = models.CharField(max_length=5)  # Usamos TimeField para manejar la hora

    def __str__(self):
        return self.nombre


class Usuarios(models.Model):
    usuario = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=255)  # Cambié a 255 para manejar contraseñas encriptadas
    tipo = models.CharField(max_length=10, choices=[
        ('estudiante', 'Estudiante'),  
        ('profesor', 'Profesor'),
    ]) 

    # Esto debe encriptar la contraseña

    def __str__(self):
        return self.usuario


class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)  
    apellido = models.CharField(max_length=30)  
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Profesionales(models.Model):
    nombre = models.CharField(max_length=30)  
    apellido = models.CharField(max_length=30) 
    email = models.EmailField()  
    profesion = models.CharField(max_length=50) 
    asignatura = models.CharField(max_length=30, blank=True)  
    rol = models.CharField(max_length=9, choices=[
        ('tutor', 'Tutor'),  
        ('profesor', 'Profesor'),
    ]) 

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

