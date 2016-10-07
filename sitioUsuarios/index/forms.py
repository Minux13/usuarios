from django import forms

class RegistroFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    #email = models.EmailField()


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
