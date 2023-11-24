from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profesor

# Create your tests here.
class RegistrarTestCase(TestCase):
    def setUp(self):
        self.profesor = Profesor.objects.create(nombre="Juan",apellido="Perez")
        self.url = reverse('eliminar_profesor', args=[self.profesor.nombre])

    def test_eliminar_profesor(self):
        respuesta = self.client.get(self.url)
        self.assertEqual(respuesta.status_code, 200)
        self.assertTemplateUsed(respuesta, 'leer_profesores.html')
        self.assertQuerysetEqual(Profesor.objects.all(), [])