from django import forms
#from .models import File

class FormUser(forms.Form):
    usuario = forms.CharField(max_length=100)
    idES = forms.IntegerField()
    contrasena = forms.CharField(widget=forms.PasswordInput())

    #email = models.EmailField()

class UploadFileForm(forms.Form):
    #title = forms.CharField(max_length=50)
    file = forms.FileField()
    name = forms.CharField(max_length=100)

    #class Meta:
     #   model = File
     #   fields = ('file')

"""class RegistroFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    edad = forms.IntegerField()

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
"""
