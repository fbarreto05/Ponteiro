from django.shortcuts import render
from .models import User
from django.http import HttpResponse
from django.shortcuts import redirect

def title(request):
    return render(request, 'titleScreen.html')

def login(request):
    error = request.GET.get('error')
    return render(request, 'loginScreen.html', {'error' : error})

def register(request):
    error = request.GET.get('error')
    return render(request, 'registerScreen.html', {'error' : error})

def registerValidate(request):
    login = request.POST.get('userlogin')
    password = request.POST.get('userpass')
    newUser = User.objects.filter(login = login)

    if len(newUser) > 0:
        return redirect('/ponteiro/register/?error=1')
    
    if login.strip() == '' or password.strip() == '':
        return redirect('/ponteiro/register/?error=2')
    
    if len(login) < 5 or len(password) < 5:
        return redirect('/ponteiro/register/?error=3')
    if len(login) > 20 or len(password) > 20:
        return redirect('/ponteiro/register/?error=4')

    newUser = User(login, password)
    newUser.save()

    return redirect('/ponteiro/register/?error=0')

def loginValidate(request):
    login = request.POST.get('userlogin')
    password = request.POST.get('userpass')

    if login.strip() == '' or password.strip() == '':
        return redirect('/ponteiro/login/?error=1')

    newUser = User.objects.filter(login = login).filter(password = password)

    if len(newUser) == 0:
        return redirect('/ponteiro/login/?error=2')
    
    request.session['User'] = newUser[0].login
    return redirect(f'/ponteiro/{login}/home')

def home(request, login):
    if request.session.get('User'):
        return render(request, 'homeScreen.html', {'login' : login})
    else:
        return redirect('/ponteiro/login/?error=3')

def logout(request):
    request.session.flush()
    return redirect('/ponteiro/')

# Create your views here.
