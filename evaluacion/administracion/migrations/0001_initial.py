# Generated by Django 4.1.7 on 2023-03-01 02:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='foto/%Y/%m/%d')),
                ('nombre', models.CharField(max_length=150)),
                ('apellido_paterno', models.CharField(max_length=150)),
                ('apellido_materno', models.CharField(max_length=150)),
                ('puesto_trabajo', models.CharField(max_length=250)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=9)),
                ('estatus', models.BooleanField(default=False)),
                ('fecha_contratacion', models.DateField()),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
            },
        ),
        migrations.CreateModel(
            name='Beneficiario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('apellido_paterno', models.CharField(max_length=150)),
                ('apellido_materno', models.CharField(max_length=150)),
                ('parentesco', models.CharField(choices=[('P', 'Padre'), ('M', 'Madre'), ('H', 'Hija(o)'), ('A', 'Abuela(o)'), ('O', 'Otro parentesco')], max_length=1)),
                ('fecha_nacimiento', models.DateField()),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femeninp')], max_length=1)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empleados', to='administracion.empleado')),
            ],
        ),
    ]