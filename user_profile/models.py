from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# UserProfile(id, phone_no, profile_picture, date_of_birth, User.id)

class UserProfile(models.Model):
    phone_no = models.CharField(max_length=11)
    profile_picture = models.ImageField(upload_to='./userprofile/')
    date_of_birth = models.DateField()
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    