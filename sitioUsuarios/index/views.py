from django.shortcuts import render

from django.http import HttpResponse
from .forms import FormUser
from .models import Userprofile
#import datetime

def index(request):
    form = FormUser(request.POST or None)
    context = {
        "form" : form
    }

    #if formulario.is_valid():
    if form.is_valid():
        dataForm = form.cleaned_data
        input_name = dataForm.get("user")
        input_pass = dataForm.get("")
        #print input_name
        addDB = Userprofile.objects.create(user=input_name)
    #now = datetime.datetime.now()
    #html = "<html><body><h1>It is now </h1></body></html>" % now
    return render(request, 'index.html', context)
    #return HttpResponse(html)
