from django.db import transaction
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from .models import Empleado, Beneficiario
from .forms import EmpleadoForm, BeneficiarioForm

class EmpleadosListView(ListView):
    model = Empleado

class EmpleadoCreateView(CreateView):
    form_class = EmpleadoForm
    template_name = 'administracion/empleado_form.html'

    @transaction.atomic()
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class BeneficiarioCreateView(CreateView):
    form_class = BeneficiarioForm
    template_name = 'administracion/beneficiario_form.html'

    @transaction.atomic()
    def form_valid(self, form):
        beneficiario = form.save(commit=False)
        beneficiario.empleado = Empleado.objects.get(pk=self.kwargs['pk'])
        beneficiario.save()
        return HttpResponseRedirect(reverse_lazy('lista-empleados'))
    

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    
    @transaction.atomic()
    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse_lazy('detalle-empleado', kwargs={'pk':self.object.pk}))
    
    
class BeneficiarioUpdateView(UpdateView):
    model = Beneficiario
    form_class = BeneficiarioForm
    
    @transaction.atomic()
    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse_lazy('lista-empleados'))


class EmpleadoActivaDesactivaView(UpdateView):
    model = Empleado

    def get(self, request, *args, **kwargs):
        empleado = Empleado.objects.get(pk=self.kwargs['pk'])
        if empleado.estatus:
            empleado.estatus = False
        else:
            empleado.estatus = True
        empleado.save() 

        return HttpResponseRedirect(reverse_lazy('lista-empleados'))

class EmpleadoDetailView(DetailView):
    model = Empleado

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['beneficiario'] = Beneficiario.objects.get(empleado=self.object.pk)
        return context
