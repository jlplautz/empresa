"""
CRUO de funcionarios.

O PermissionRequiredMixin manda quem não entrou para o login e devolve 403 
para quem entrou mas não tem permissão.
"""

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Employee
from .forms import EmployeeForm

class EmployeeListView(PermissionRequiredMixin, ListView):
    model = Employee
    permission_required = 'person.view_employee'

class EmployeeCreateView(PermissionRequiredMixin, CreateView):
    model = Employee
    form_class = EmployeeForm
    permission_required = 'person.add_employee'
    success_url = reverse_lazy('person:employee_list')

class EmployeeUpdateView(PermissionRequiredMixin, UpdateView):
    model = Employee
    form_class = EmployeeForm
    permission_required = 'person.change_employee'
    success_url = reverse_lazy('person:employee_list')

class EmployeeDeleteView(PermissionRequiredMixin, DeleteView):
    model = Employee
    permission_required = 'person.delete_employee'
    success_url = reverse_lazy('person:employee_list')
