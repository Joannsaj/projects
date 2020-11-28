from django.shortcuts import render
from .models import Project
from .forms import ProjectForm
# Create your views here.
def index(request):
    projects = Project.projects()
    return render(request,'index.html',{"projects":projects})

def project(request):    
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid() :
            project = form.save(commit=False)
            project.owner = request.user.profile
            project.save()
            return redirect('index')
    else:
        form = ProjectForm()
    return render(request,'project.html',{"form":form})