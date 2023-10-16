from django.db import models

def user_profile_image_path(instance, filename):
    return f'user_profiles/{instance.id}/profilePicture/{filename}'

class User(models.Model):
    picture = models.ImageField(upload_to=user_profile_image_path, blank=True, null=True, default='media/anonymous.png')
    name = models.TextField(max_length=80, default = 'name')
    id = models.TextField(max_length=20, default = 'id', primary_key=True)
    description = models.TextField(max_length=800, default = 'description')
    password = models.TextField(max_length=20, default = 'password')
    theme = models.TextField(max_length=5, default = 'light')
    language = models.TextField(max_length=2, default = 'pt')
 
# Create your models here.
