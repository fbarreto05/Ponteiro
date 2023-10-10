from django.shortcuts import render
from .models import User
from django.http import HttpResponse
from django.shortcuts import redirect

def title(request):
    return render(request, 'titleScreen.html')

def login(request):
    return render(request, 'loginScreen.html')

def register(request):
    return render(request, 'registerScreen.html')

def registerValidate(request):
    login = request.POST.get('userlogin')
    password = request.POST.get('userpass')
    newUser = User.objects.filter(login = login)

    if len(newUser) > 0:
        return HttpResponse("A conta não foi cadastrada, já existe outra conta com o mesmo identificador.")
    
    if len(login.strip()) == 0 or len(password.strip()) == 0:
        return HttpResponse("A conta não foi cadastrada, há campos obrigatórios que não foram preenchidos.")
    
    if len(login) < 5 or len(password) < 5:
        return HttpResponse("A conta não foi cadastrada, o identificador e a senha precisam ter, no mínimo 5 caracteres.")
    if len(login) > 20 or len(password) > 20:
        return HttpResponse("A conta não foi cadastrada, o identificador e a senha devem obedecer o limite de 20 caracteres")

    newUser = User()
    newUser.login = login
    newUser.password = password
    newUser.save()

    return HttpResponse(f"Cadastrado com sucesso! {newUser.login} {newUser.password} ")

def loginValidate(request):
    login = request.POST.get('userlogin')
    password = request.POST.get('userpass')

    newUser = User.objects.filter(login = login).filter(password = password)

    if len(newUser) == 0:
        return HttpResponse("Não foi encontrada nenhuma conta com essas credenciais.")
    
    request.session['User'] = newUser[0].login
    return render(request, 'welcome.html', {'login' : login})

def logout(request):
    request.session.flush()
    return redirect('/ponteiro/')

# Create your views here.
