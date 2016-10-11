from django.shortcuts import render

from django.http import HttpResponse
from .forms import FormUser, UploadFileForm
from .models import Userprofile, File
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

#import datetime

def user_profile(request, param_pk):

    user = User.objects.filter(pk=param_pk)

    formFiles = UploadFileForm(request.POST or None)
    context1 = {
        "formFiles" : formFiles
    }

    context = {
        "user" : user
    }

    return render(request, 'profile.html', context)

def profile(request):

    users = User.objects.all()

    context = {
        "users" : users
    }

    return render(request, 'profile.html', context)



def uploadFile(request):

    user = get_object_or_404(File, user=request.user)

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            #handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('uploadfile.html')
        else:
            pass
    else:
        form = UploadFileForm()

    return render(request, 'uploadfile.html', {'formFile': form})


def files(request):

    formFiles = UploadFileForm(request.POST or None)
    context = {
        "formFiles" : formFiles
    }

    return render(request, 'profile.html', context)







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
