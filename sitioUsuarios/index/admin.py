"""from django.contrib import admin
from .models import Usuario
# Register your models here.
class AdminUsuario(admin.ModelAdmin):
    list_display = ["__unicode__", "email", "time_register", "time_actualization"]
    class Meta:
        model = Usuarios_registrado

admin.site.register(Usuarios_registrado, AdminUsuario)
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Userprofile

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class UsuarioInline(admin.StackedInline):
    model = Userprofile
    can_delete = False
    verbose_name_plural = 'usuario'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UsuarioInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
