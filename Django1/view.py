from django.http import HttpResponse
from django.template import Template, Context, loader
import datetime

def saludo(request):
    return HttpResponse("Hola Django")

def hoy(request):
    dia = datetime.datetime.now()
    texto = f"Hoy es: <br> {dia}"
    return HttpResponse(texto)

def nombre(self, nombre):
    texto = f"Mi nombre es <br><br> {nombre}"
    return HttpResponse(texto)

def template(request):
    nombre = "Tomas"
    apellido = "Maraval"
    notas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    diccionario = {"nombre": nombre, "apellido": apellido, "fecha": datetime.datetime.now(), "notas": notas}
    
    html = loader.get_template("C:/Users/tomas/Downloads/pruebaDjango/pruebaDjango/templates/template1.html")

    documento = html.render(diccionario)

    return HttpResponse(documento)