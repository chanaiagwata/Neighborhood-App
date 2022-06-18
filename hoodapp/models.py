from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Neighborhood(models.Model):
    name=models.CharField(max_length=250)
    location = models.CharField(max_length=250, null=False)
    hood_pic = models.ImageField(upload_to = 'posts/')
    description = models.TextField(max_length=255)
    health_officer = models.CharField(blank=True, max_length=250)
    health_contact =models.IntegerField()
    police_officer  = models.CharField(blank=True, max_length=250)
    police_contact  = models.IntegerField()
    admin = models.ForeignKey("Profile", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    hoodname = models.CharField(blank=True, max_length=120)
    profile_pic = models.ImageField(upload_to = 'images/')
    bio = models.TextField(max_length=240, null=True)
    location = models.CharField(max_length=255, null=False)
    
    def __str__(self):
        return self.user


class Business(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=255)
    email = models.EmailField(max_length=250)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    hood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    





