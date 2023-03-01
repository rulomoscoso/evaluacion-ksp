from django import forms
from django.forms import ModelForm
from .models import Empleado, Beneficiario


class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_materno': forms.TextInput(attrs={'class': 'form-control'}),
            'puesto_trabajo': forms.TextInput(attrs={'class': 'form-control'}),
            'salario': forms.TextInput(attrs={'class': 'form-control'}),
            'estatus': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'fecha_contratacion': forms.DateInput(attrs={'type':'date'})
        }



class BeneficiarioForm(ModelForm):
    class Meta:
        model = Beneficiario
        fields = '__all__'
        exclude = ['empleado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_materno': forms.TextInput(attrs={'class': 'form-control'}),
            'parentesco': forms.Select(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'type':'date'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
        }