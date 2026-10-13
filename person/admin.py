from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'role', 'active')
    list_filter = ('role', 'active')
    search_fields = ('name', 'email')
    