from django.shortcuts import render
from .models import Project
# Create your views here.
def index():
    projects = Project.projects()
    return render(request,'index.html',{"projects":projects})

def project():    