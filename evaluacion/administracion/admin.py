from django.contrib import admin
from .models import Empleado, Beneficiario

admin.site.register(Empleado)
admin.site.register(Beneficiario)