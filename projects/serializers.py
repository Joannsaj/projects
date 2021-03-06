from rest_framework import serializers
from .models import Profile, Project

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('profile_pic', 'contact', 'user', 'bio', 'name')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title', 'project_image', 'description', 'owner', 'created', 'link')        