from django.db import models

class User(models.Model):
    login = models.TextField(max_length=20, default = 'admin', primary_key=True)
    password = models.TextField(max_length=20, default = 'admin')

    def __init__(self, deflogin, defpassword, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.login = deflogin
        self.password = defpassword

    
# Create your models here.
