from django.shortcuts import render

from django.http import HttpResponse
from .forms import FormUser, UploadFileForm
from .models import Userprofile, File
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404



#import datetime

def user_profile(request, param_pk):

    user = User.objects.get(pk=param_pk)

    files = File.objects.filter(user=param_pk)


    print "\n\n\n\n\n\n"

    print type(param_pk)
    pkinteger = int(param_pk)
    print type(pkinteger)

    print "\n\n\n\n\n\n"

    users = User.objects.all()
    nameUser = users[1]
    #nameUser = users.first_name
    #formFiles = UploadFileForm(request.POST or None)

    print user


    context = {
        "user" : user,
        "files": files,
        "nameUser": nameUser,
    }

    return render(request, 'archivosusuario.html', context)

def profile(request):

    users = User.objects.all()

    context = {
        "users" : users
    }

    return render(request, 'profile.html', context)



def uploadFile(request):

    #user = get_object_or_404(File, user=request.user)

    if request.method == 'POST':
        #form = UploadFileForm(request.POST, request.FILES, instance=user)
        form = UploadFileForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            #Obtengo de la tabla User

            if request.user.is_authenticated:
                    pdfFile = form.cleaned_data["file"]
                    userId = request.user.id
            else:
                pass

            #userrr = User.objects.get(id=user_id)
            #  #f.save()
            obj = File.objects.create(pdf=pdfFile, user=userId)
            #obj2 = File.objects.create(user=name)  #create es un objetos model manager, crea y guarda en la base de datos
            #handle_uploaded_file(request.FILES['file'])
            #return HttpResponseRedirect('uploadfile.html')
            return HttpResponse('profile.html')
        else:
            pass
    else:
        form = UploadFileForm()

    return render(request, 'profile.html', {'formFile': form})


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
