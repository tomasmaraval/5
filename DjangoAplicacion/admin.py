from django.contrib import admin

from DjangoAplicacion import models

admin.site.register(models.Curso)
admin.site.register(models.Profesor)
admin.site.register(models.Estudiante)
admin.site.register(models.Entregable)
admin.site.register(models.Avatar)