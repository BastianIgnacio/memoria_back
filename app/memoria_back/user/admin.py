from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from user.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email','username','password')}),
        ('Informacion Personal', {'fields': ('nombre','apellido','rol','telefono')}),
        ('Informacion Tienda', {'fields': ('refTienda',)}),
        ('Permisos', {'fields': ('is_active','is_staff','is_superuser','groups','user_permissions')})
        )