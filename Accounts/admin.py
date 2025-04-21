from django.contrib import admin
from .models import ProfileModel , SignUpModel 
# Register your models here.

admin.site.register(ProfileModel)
admin.site.register(SignUpModel)