from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    profile_pic = CloudinaryField('image', null=True)
    contact = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(null=True)

    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()    

    def __str__(self):
        return self.name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


class Project(models.Model):
    title = models.CharField(max_length=60)
    project_image = CloudinaryField('image')
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    @classmethod
    def projects(cls):
        projects = cls.objects.all()
        return projects