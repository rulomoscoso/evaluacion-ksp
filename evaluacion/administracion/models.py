from django.db import models
from django.urls import reverse_lazy

class Empleado(models.Model):
    foto = models.ImageField(upload_to='foto/%Y/%m/%d')
    nombre = models.CharField(max_length=150)
    apellido_paterno = models.CharField(max_length=150) 
    apellido_materno = models.CharField(max_length=150)
    puesto_trabajo = models.CharField(max_length=250)
    salario = models.DecimalField(max_digits=9, decimal_places=2)
    estatus = models.BooleanField(default=False)
    fecha_contratacion = models.DateField()

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse_lazy('crear-beneficiario', kwargs={'pk': self.pk})
    
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'


class Beneficiario(models.Model):
    MASCULINO = 'M'
    FEMENINO = 'F'
    SEXO = [
        (MASCULINO, 'Masculino'),
        (FEMENINO, 'Femenino'),
    ]

    PADRE = 'P'
    MADRE = 'M'
    HIJO = 'H'
    ABUELO = 'A'
    OTRO = 'O'
    PARENTESCO = [
        (PADRE, 'Padre'),
        (MADRE, 'Madre'),
        (HIJO, 'Hija(o)'),
        (ABUELO, 'Abuela(o)'),
        (OTRO, 'Otro parentesco')
    ]
    empleado = models.ForeignKey('Empleado', on_delete=models.CASCADE, related_name='empleados')
    nombre = models.CharField(max_length=150)
    apellido_paterno = models.CharField(max_length=150) 
    apellido_materno = models.CharField(max_length=150)
    parentesco = models.CharField(max_length=1, choices=PARENTESCO)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Beneficiario'
        verbose_name_plural = 'Beneficiarios'


