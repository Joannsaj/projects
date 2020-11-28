from django.contrib import admin
from .models import Profile, Project
# Register your models 
admin.site.register(Project)
admin.site.register(Profile)