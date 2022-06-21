from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Neighborhood(models.Model):
    name=models.CharField(max_length=250)
    location = models.CharField(max_length=250, null=False)
    hood_pic = models.ImageField(upload_to = 'posts/')
    description = models.TextField(max_length=255)
    health_contact = models.CharField(blank=True, max_length=250)
    health_centers =models.IntegerField()
    police_contact  = models.CharField(blank=True, max_length=250)
    police_authorities  = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    def create_neighborhood(self):
        self.save()
        
    def delete_neighborhood(self):
        self.delete()
    
    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)
        
    
    

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    hoodname = models.CharField(blank=True, max_length=120)
    profile_pic = models.ImageField(upload_to = 'images/')
    bio = models.TextField(max_length=240, null=True)
    location = models.CharField(max_length=255, null=False)
    neighbourhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, null=True,  blank=False, related_name='members')
    
    def __str__(self):
        return self.user
    
    def create_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()


class Business(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=255)
    email = models.EmailField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    @classmethod
    def get_business_by_id(cls,id):
        business = cls.objects.filter(id= id).all()
        return business
    @classmethod
    def search_by_name(cls, search_term):
        business = cls.objects.filter(name__icontains=search_term)
        return business


class Post(models.Model):
    title = models.CharField(max_length=255)
    hood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    





