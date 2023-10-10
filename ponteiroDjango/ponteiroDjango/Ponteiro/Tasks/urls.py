from django.urls import path
from . import views

urlpatterns = [
    path('', views.title, name='title'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('register/registerValidate/', views.registerValidate, name='registerValidate'),
    path('login/loginValidate/', views.loginValidate, name='loginValidate'),
    path('login/logout/', views.logout, name='logout'),
]
