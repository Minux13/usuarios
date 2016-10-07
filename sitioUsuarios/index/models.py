from __future__ import unicode_literals
#from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

"""class Usuarios_registrado(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    time_register = models.DateTimeField(auto_now_add=True, auto_now=False)
    time_actualization = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self): #Python 3 __str__
        return self.nombre

class Userprofile(models.Model):
    user = models.Forenkey(User, on_delete=models.CASCADE)
    documents = models.Field(upload_tp= documentos/)

    def __unicode__(self): #Python 3 __str__
        return self.user

"""

class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    """lastname = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    time_register = models.DateTimeField(auto_now_add=True, auto_now=False)
    time_actualization = models.DateTimeField(auto_now_add=False, auto_now=True)"""

    def __unicode__(self): #Python 3 __str__
        return self.user
