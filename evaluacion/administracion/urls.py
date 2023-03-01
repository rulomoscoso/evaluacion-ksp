from django.urls import path
from.views import EmpleadosListView, EmpleadoCreateView, BeneficiarioCreateView, \
                  EmpleadoUpdateView, BeneficiarioUpdateView, EmpleadoDetailView, \
                  EmpleadoActivaDesactivaView

urlpatterns = [
    path('empleado/lista/', EmpleadosListView.as_view(), name='lista-empleados'),
    path('empleado/crear/', EmpleadoCreateView.as_view(), name='crear-empleado'),
    path('empleado/crear/<int:pk>/beneficiario/', BeneficiarioCreateView.as_view(), name='crear-beneficiario'),
    path('empleado/edit/<int:pk>/', EmpleadoUpdateView.as_view(), name='editar-empleado'),
    path('empleado/edit/<int:pk>/beneficiario/', BeneficiarioUpdateView.as_view(), name='editar-beneficiario'),
    path('empleado/detalle/<int:pk>/', EmpleadoDetailView.as_view(), name='detalle-empleado'),
    path('empleado/activa_desactiva/<int:pk>/', EmpleadoActivaDesactivaView.as_view(), name='activa-desactiva-empleado'),
]