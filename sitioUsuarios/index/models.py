from __future__ import unicode_literals

from django.db import models

class Usuarios_registrado(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    time_register = models.DateTimeField(auto_now_add=True, auto_now=False)
    time_actualization = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self): #Python 3 __str__
        return self.nombre
