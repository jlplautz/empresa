from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .forms import customerUserChangeForm, CustomUserCreationForm
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserChangeForm
    form = CustomUserChangeForm
    ordering = ('email',)
    list_display=('email', 'first_name', 'last_name', 'is_staff')
    search_field = ('email', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Dados pessoais', {'fields': ('first_name', 'last_name')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email', 'password', 'password2')}),
    )

