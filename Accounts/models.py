from django.db import models
from django.contrib.auth.models import User


class SignUpModel(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password= models.CharField(max_length=100)
   
    def __str__(self):
        return self.username
    
class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    caption = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    def __str__(self):
        return self.user.username
