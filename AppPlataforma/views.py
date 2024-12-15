from django.shortcuts import redirect, render
from .models import Curso,Profesionales,Estudiante
# Create your views here.
def inicio(request):
    curso = Curso.objects.all()
    profesional = Profesionales.objects.all()
    return render(request,"AppPlataforma/index.html",{"cursos": curso, "profesionales": profesional})

def cursos(request):
    curso = Curso.objects.all()
    
    return render(request,"AppPlataforma/Cursos.html", {"cursos": curso})

def estudiantes(request):
    estudiante = Estudiante.objects.all()
    return render(request,"AppPlataforma/Estudiantes.html",{"estudiantes": estudiante})

def profesionales(request):
    profesional = Profesionales.objects.all()
    return render(request,"AppPlataforma/Profesionales.html",{"profesionales": profesional})

def blog(request):
    return render(request,"AppPlataforma/Blog.html")

def iniciosesion(request):
    return render(request,"AppPlataforma/IniciarSesion.html")

def nuevacuenta(request):
    return render(request,"AppPlataforma/NuevaCuenta.html")

def addcurso(request):
    if request.method == 'POST':
        
        nombre_curso = request.POST.get('curso')
        comision = request.POST.get('comision')
        dia = request.POST.get('dia')
        hora = request.POST.get('hora')

        nuevo_curso = Curso(nombre=nombre_curso, comision=comision, dia=dia, hora=hora)
        nuevo_curso.save()
        
        return redirect('NuevoCurso') 

    return render(request, 'AppPlataforma/components/Addcurso.html')  # Asegúrate de cambiar 'tu_template.html' al nombre correcto de tu template
