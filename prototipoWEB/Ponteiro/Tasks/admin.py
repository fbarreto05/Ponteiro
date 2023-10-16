from django.contrib import admin
from .models import User

@admin.register(User)
class userAdmin(admin.ModelAdmin):
    readonly_fields = ('picture', 'name', 'id', 'description', 'password', 'theme', 'language')

# Register your models here.
