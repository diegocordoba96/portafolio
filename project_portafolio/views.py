from django.shortcuts import render
from project_portafolio.models import Project

def home(request):

    project = Project.objects.all()


    return render(request, 'home.html',{
        'project'  :   project  
        })
  
     
