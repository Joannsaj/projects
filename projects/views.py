from django.shortcuts import render
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    projects = Project.projects()
    return render(request,'index.html',{"projects":projects})

@login_required(login_url='/accounts/login/')
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

def search_results(request):
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        projects = Project.search_project(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,"projects": projects})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
