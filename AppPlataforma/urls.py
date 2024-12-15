
from django.urls import path
from AppPlataforma import views

urlpatterns = [
    path('',views.inicio , name="Home"),
    path('cursos/',views.cursos,name="Cursos"),
    path('estudiantes/',views.estudiantes, name="Estudiantes"),
    path('profesionales/',views.profesionales , name="Profesionales"),
    path('Blog/',views.blog , name="Blog"),
    path('iniciosesion/',views.iniciosesion , name="Loggin"),
    path('nuevacuenta/',views.nuevacuenta , name="NuevaCuenta"),
    path('addcurso/', views.addcurso, name="NuevoCurso")
    
]