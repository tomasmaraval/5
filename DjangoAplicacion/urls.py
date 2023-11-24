from django.shortcuts import render
from django.urls import path
from DjangoAplicacion.views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', inicio, name='inicio'),
    path('cursos/', cursos, name='cursos'),
    path('profesores/', profesores, name='profes'),
    path('estudiantes/', estudiantes, name='alumnos'),
    path('entregables/', entregables, name='entregables'),
    path('buscar/', buscar, name='buscar'),
    path('buscar_camada/', buscarCamada, name='buscarCamada'),
    path('leer_profesores/', leer_profesores, name='leer_profesores'),
    path('eliminar_profesor/<profesor_nombre>', eliminar_profesor, name='eliminar_profesor'),
    path('editar_profesor/<profesor_nombre>', editar_profesor, name='editar_profesor'),
    path('cursos/lista', CursoListView.as_view(), name='ListaCursos'),
    path('cursos/crear', CursoCreateView.as_view(), name='CrearCurso'),
    path('cursos/<pk>', CursoDetailView.as_view(), name='DetalleCurso'),
    path('cursos/<pk>/editar', CursoUpdateView.as_view(), name='EditarCurso'),
    path('cursos/<pk>/borrar', CursoDeleteView.as_view(), name='BorrarCurso'),
    path('login/', login_request, name='Login'),
    path('registro/', registro, name='Registro'),
    path('logout/', LogoutView.as_view(template_name='DjangoAplicacion/logout.html'), name='Logout'),
    path('editarPerfil/', editarPerfil, name='EditarPerfil'),
    path('cambiarContraseña', CambiarContraseña.as_view(), name='cambiarContraseña'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)