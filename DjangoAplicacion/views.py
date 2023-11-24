from django.shortcuts import render, redirect
from DjangoAplicacion.models import *
from django.http import HttpResponse
from django.template import loader
from DjangoAplicacion.forms import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    return render(request, "DjangoAplicacion/inicio.html")

def index(request):
    return render(request, "DjangoAplicacion/index.html")

def padre(request):
    return render(request, "DjangoAplicacion/padre.html")

def entregables(request):
    if request.method == 'POST':
        mi_formulario = EntregablesFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            profesor = Entregable(nombre = informacion['nombre'], fecha_entrega = informacion['fecha_entrega'])
            profesor.save()
            return render(request, "DjangoAplicacion/inicio.html")
    else:
        mi_formulario = CursoFormulario()
    return render(request, "DjangoAplicacion/entregables.html", {"mi_formulario": mi_formulario})

def estudiantes(request):
    if request.method == 'POST':
        mi_formulario = EstudiantesFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            profesor = Estudiante(nombre = informacion['nombre'], apellido = informacion['apellido'], email = informacion['email'])
            profesor.save()
            return render(request, "DjangoAplicacion/inicio.html")
    else:
        mi_formulario = CursoFormulario()
        return render(request, "DjangoAplicacion/estudiantes.html", {"mi_formulario": mi_formulario})

def profesores(request):
    if request.method == 'POST':
        mi_formulario = ProfesoresFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            profesor = Profesor(nombre = informacion['nombre'], apellido = informacion['apellido'], email = informacion['email'], profesion = informacion['profesion'])
            profesor.save()
            return render(request, "DjangoAplicacion/inicio.html")
    else:
        mi_formulario = CursoFormulario()
        return render(request, "DjangoAplicacion/profesores.html", {"mi_formulario": mi_formulario})

def cursos(request):
    if request.method == 'POST':
        mi_formulario = CursoFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso = Curso(curso = informacion['curso'], camada = informacion['camada'])
            curso.save()
            return render(request, "DjangoAplicacion/inicio.html")
    else:
        mi_formulario = CursoFormulario()
        return render(request, "DjangoAplicacion/cursos.html", {"mi_formulario": mi_formulario})

def buscarCamada(request):
    return render(request, "DjangoAplicacion/buscarCamada.html")

def buscar(request):
    if "camada" in request.GET:
        camada = request.GET["camada"]
        curso = Curso.objects.filter(camada_iconteins=camada)
        return render(request, 'DjangoAplicacion/resultadosBusqueda.html', {'cursos': curso, 'camada': camada})
                      
    
    else:
        return render(request, 'DjangoAplicacion/buscar.html')
    
def leer_profesores(request):
    profesores = Profesor.objects.all()
    contexto = {'profesores': profesores}
    return render(request, 'DjangoAplicacion/leer_profesores.html', contexto)

def eliminar_profesor(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()
    profesores = Profesor.objects.all()
    contexto = {'profesores': profesores}
    return render(request, 'DjangoAplicacion/leer_profesores.html', contexto)

def editar_profesor(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre)

    if request.method == 'POST':
        mi_formulario = ProfesoresFormulario(request.POST)
        print(mi_formulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']
            profesor.save()
            return render(request, "DjangoAplicacion/inicio.html")  

    else:
        mi_formulario = ProfesoresFormulario(initial={'nombre': profesor.nombre, 
                                                      'apellido': profesor.apellido, 
                                                      'email': profesor.email, 
                                                      'profesion': profesor.profesion})
    return render(request, "DjangoAplicacion/editar_profesor.html", {"mi_formulario": mi_formulario, "profesor_nombre": profesor_nombre})

class CursoListView(ListView):
    model = Curso
    context_object_name = 'cursos'
    template_name = 'DjangoAplicacion/cursos_listas.html'

class CursoDetailView(DetailView):
    model = Curso
    template_name = 'DjangoAplicacion/curso_detalle.html'

class CursoCreateView(CreateView):
    model = Curso
    template_name = 'DjangoAplicacion/curso_crear.html'
    success_url = reverse_lazy('ListaCursos')
    fields = ['curso', 'camada']

class CursoUpdateView(UpdateView):
    model = Curso
    template_name = 'DjangoAplicacion/curso_editar.html'
    success_url = reverse_lazy('ListaCursos')
    fields = ['curso', 'camada']

class CursoDeleteView(DeleteView):
    model = Curso
    template_name = 'DjangoAplicacion/curso_borrar.html'
    success_url = reverse_lazy('ListaCursos')

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasena = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasena)
            if user is not None:
                login(request, user)
                return render(request, "DjangoAplicacion/inicio.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, "DjangoAplicacion/inicio.html", {"mensaje": "Datos incorrectos"})
    else:
        form = AuthenticationForm()

    return render(request, "DjangoAplicacion/login.html", {"form": form})

def registro(request):
    if request.method == 'POST':
        form = UserCreationFormCustom(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "DjangoAplicacion/inicio.html", {"mensaje": f"Usuario {username} creado"})
    else:
        form = UserCreationFormCustom()
    return render(request, "DjangoAplicacion/registro.html", {"form": form})

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        mi_formulario = UserEditForm(request.POST, request.FILES, instance=request.user)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            usuario.email = informacion['email']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            if mi_formulario.cleaned_data.get['imagen']:
                usuario.imagen = mi_formulario.cleaned_data['imagen']
            usuario.save()
            return render(request, "DjangoAplicacion/inicio.html")
        
    else:
        mi_formulario = UserEditForm(instance=request.user)
    return render(request, "DjangoAplicacion/editarPerfil.html", {"mi_formulario":mi_formulario})

class CambiarContraseña(LoginRequiredMixin, PasswordChangeView):
    template_name = 'DjangoAplicacion/cambiarContraseña.html'
    success_url = reverse_lazy('EditarPerfil')
    