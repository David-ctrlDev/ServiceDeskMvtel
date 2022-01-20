# Create your views here.

from django.shortcuts import redirect, render
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from requirements.models import *
from .forms import  ServiceFormPetitioner
from django.http import HttpResponseRedirect
import datetime as datetime
from json import dumps
from django.core.serializers.json import DjangoJSONEncoder




@login_required(login_url= 'login')
def services_page(request):
    #capture last request on service page and save in a Session Variable.
    request.session['last_activity'] = dumps(datetime.datetime.now(),sort_keys=True,
    indent=1,
    cls=DjangoJSONEncoder)
    services =Service.objects.all().order_by('-created', '-id')
    return render(request, 'requirements/services.html', {'services': services})
    
@login_required(login_url= 'login')
def get_name(request):
     #capture last request on new service page and save in a Session Variable.
    request.session['last_activity'] = dumps(datetime.datetime.now(),sort_keys=True,
    indent=1,
    cls=DjangoJSONEncoder)
    
    lastactivity = request.session['last_activity']
    print(lastactivity)
    #fecha_dt = datetime.datetime.strptime(lastactivity,'%Y-%m-%d')
    #print(fecha_dt)
    
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ServiceFormPetitioner(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ServiceFormPetitioner()

    return render(request, 'requirements/newService.html', {'form': form})
@login_required(login_url= 'login')
def registersucces(request):
    
  
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ServiceFormPetitioner(request.POST)
        # check whether it's valid:        
        if form.is_valid():
            data = form.cleaned_data
            project=(data['project'])
            # process the data in form.cleaned_data as required
            service = Service()
            service.project =Project.objects.get(pk=project)
            service.responsable = User.objects.get(pk = request.user.id)
            service.description = data['description']
            service.registerDate = data['registerDate']
            service.petitioner = data['petitioner']
            service.petitionerMail = data['petitionerMail']
            service.petitionerPhone = data['petitionerPhone'] 
            service.campus = data['campus']
            service.save()
            # redirect to a new URL:
            return HttpResponseRedirect('viewsucces')
        
        else:
            print("stoy entrando")
            form = ServiceFormPetitioner()

        return render(request, 'requirements/newService.html', {'form': form})


def view_succes(request):
 #capture last request on succes service page and save in a Session Variable.
    request.session['last_activity'] = dumps(datetime.datetime.now(),sort_keys=True,
    indent=1,
    cls=DjangoJSONEncoder)
    return render(request, 'requirements/services/create.html')