from django.contrib import admin
from .models import User, Group

@admin.register(User)
class userAdmin(admin.ModelAdmin):
    readonly_fields = ('picture', 'name', 'id', 'description', 'password')

@admin.register(Group)
class userAdmin(admin.ModelAdmin):
    readonly_fields = ('picture', 'name', 'id', 'description')

# Register your models here.
