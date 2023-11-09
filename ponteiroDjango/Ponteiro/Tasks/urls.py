from django.urls import path
from . import views

urlpatterns = [
    path('', views.title, name='title'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('register/registerValidate/', views.registerValidate, name='registerValidate'),
    path('login/loginValidate/', views.loginValidate, name='loginValidate'),
    
    path('<str:id>/home/', views.home, name='home'),
    path('<str:id>/home/createGroup/', views.createGroup, name='creategroup'),
    path('<str:id>/home/createGroupValidate/', views.createGroupValidate, name='creategroupValidate'),
    path('<str:id>/home/groupSearch/', views.groupSearch, name='groupsearch'),
    path('<str:id>/home/groupSearchValidate/', views.groupSearchValidate, name='groupsearchValidate'),
    path('<str:id>/<str:groupID>_group/', views.showGroup, name='showGroup'),
    path('<str:id>/<str:groupID>_group/enter/', views.enterGroup, name='enterGroup'),


    path('<str:id>/profile/', views.profile, name='profile'),
    path('<str:id>/profile/edit/', views.profileedit, name='profileedit'),
    path('<str:id>/profile/editValidate/', views.profileeditValidate, name='profileeditValidate'),
    path('<str:id>/profile/delete', views.profiledelete, name='profiledelete'),

    path('<str:id>/userSearch/', views.userSearch, name='userSearch'),
    path('<str:id>/searchValidate/', views.searchValidate, name='searchValidate'),
    path('<str:id>/<str:searchid>_profile/', views.userSearchProfile, name='userSearchProfile'),

    path('<str:id>/notifications/', views.notifications, name='notifications'),

    path('<str:id>/config/', views.homeconfig, name='homeconfig'),
    path('<str:id>/configvalidate/', views.homeconfigvalidate, name='homeconfigvalidate'),

    path('<str:id>/logout/', views.logout, name='logout'),
] 
