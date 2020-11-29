from django.shortcuts import render
from .models import Project, Profile
from .forms import ProjectForm, ProfileForm
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProjectSerializer, ProfileSerializer

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

@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        projects = Project.search_project(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,"projects": projects})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def profile(request, username):
    projects = request.user.profile.project.all()
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('index')
    else:
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'profile.html', { 'profile_form': profile_form, 'projects': projects, })

@login_required(login_url='/accounts/login/')
def get_profile(request, username):
    user = get_object_or_404(User, username=username)
    projects = user.profile.project.all()

    if request.user == user:
        return redirect('profile', username=request.user.username)
    
    return render(request, 'user_profile.html', {'user':user, 'projects':projects})

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)

class ProjectList(APIView):
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)        