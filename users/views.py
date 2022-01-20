from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout
from projects.models import Project, ProjectForProfile
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
import datetime as datetime
from django.utils import timezone
from json import dumps
from django.core.serializers.json import DjangoJSONEncoder
# Create your views here.


#user auth/in function

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
      
       
        if user:
            login(request, user)
            return redirect ('home/')
            ...
        else:
            return render(request,'users/login.html',{'error':'Invalid username or password '} ) 
    return render(request, 'users/login.html')

#user auth/out function

def logout_view(request):
    logout(request)
    return render(request, 'users/login.html')
    
@login_required(login_url= 'login')
def home(request):
    #capture last request on home page and save in a Session Variable.
    request.session['last_activity'] = dumps(datetime.datetime.now(),sort_keys=True,
    indent=1,
    cls=DjangoJSONEncoder)
    lastactivity = request.session['last_activity']
    projectsList = []
    userID= str(request.user.pk)
    profileProjects = (ProjectForProfile.objects.all())

    for i in profileProjects:
       project = Project.objects.get(pk=i.project_id)
       projectsList.append(project)
       

  
        
    return (render(request, 'users/home.html',{'projects':projectsList})) 

@receiver(user_logged_out)
def sig_user_logged_out(sender, user, request, **kwargs):
    user.profile.login = False
    user.profile.last_logout = datetime.datetime.now(tz=timezone.utc)
    user.profile.save()
@receiver(user_logged_in)
def sig_user_logged_in(sender, user, request, **kwargs):
    user.profile.login = True
    user.profile.save()


