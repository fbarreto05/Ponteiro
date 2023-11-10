from django.contrib import admin
from .models import User, Group, groupListNode, groupLinkedList

@admin.register(User)
class userAdmin(admin.ModelAdmin):
    readonly_fields = ('picture', 'name', 'id', 'description', 'password')

@admin.register(groupListNode)
class userAdmin(admin.ModelAdmin):
    readonly_fields = ('data', 'next')

@admin.register(groupLinkedList)
class userAdmin(admin.ModelAdmin):
    readonly_fields = ('head', )
    
@admin.register(Group)
class userAdmin(admin.ModelAdmin):
    readonly_fields = ('picture', 'name', 'id', 'description')

# Register your models here.
