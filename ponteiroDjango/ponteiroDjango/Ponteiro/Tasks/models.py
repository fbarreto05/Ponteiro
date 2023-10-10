from django.db import models

class User(models.Model):
    login = models.TextField(max_length=20, default = 'admin', primary_key=True)
    password = models.TextField(max_length=20, default = 'admin')
    
# Create your models here.
