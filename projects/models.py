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
    name = models.CharField(max_length=100 ,null=True)
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()    

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


class Project(models.Model):
    title = models.CharField(max_length=60)
    project_image = CloudinaryField('image')
    description = models.TextField()
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owner')
    created = models.DateTimeField(auto_now_add=True, null=True)
    link = models.URLField(max_length=200)
    def __str__(self):
        return self.title

    @classmethod
    def projects(cls):
        projects = cls.objects.all()
        return projects

    @classmethod
    def search_project(cls,search_term ):
        return cls.objects.filter(title__icontains=search_term).all()
    
class Rating(models.Model):
    RATING_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
    )
    design = models.DecimalField(choices = RATING_CHOICES, max_digits=3, decimal_places=2)
    usability = models.DecimalField(choices = RATING_CHOICES, max_digits=3, decimal_places=2)
    content = models.DecimalField(choices = RATING_CHOICES, max_digits=3, decimal_places=2)
    rater = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='rater')

    def __str__(self):
        return self.rater

    def overall(self):
        avg_rating = (self.design + self.usability + self.content )/3
        return avg_rating