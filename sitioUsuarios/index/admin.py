from django.contrib import admin
from .models import Usuarios_registrado
# Register your models here.
class AdminUsuario(admin.ModelAdmin):
    list_display = ["__unicode__", "email", "time_register", "time_actualization"]
    class Meta:
        model = Usuarios_registrado

admin.site.register(Usuarios_registrado, AdminUsuario)
