from django import forms
from .models import Profile, Project, Rating
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['owner','created',]

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        exclude = ['rater',]
