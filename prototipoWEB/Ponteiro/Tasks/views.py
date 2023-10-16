from django.shortcuts import render
from .models import User
from django.http import HttpResponse
from django.shortcuts import redirect
import os
from shutil import copyfile
from django.conf import settings
from PIL import Image
from django.views.decorators.cache import cache_control

titlelanguage = 'pt'
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def title(request):
    global titlelanguage
    if request.GET.get('language'):
        titlelanguage = request.GET.get('language')
    return render(request, f'{titlelanguage}/titleScreen.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    global titlelanguage
    error = request.GET.get('error')
    return render(request, f'{titlelanguage}/loginScreen.html', {'error' : error})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def register(request):
    global titlelanguage
    error = request.GET.get('error')
    return render(request, f'{titlelanguage}/registerScreen.html', {'error' : error})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def registerValidate(request):
    id = request.POST.get('userid')
    name = request.POST.get('username')
    description = request.POST.get('userdescription')
    password = request.POST.get('userpass')
    language = titlelanguage
    
    newUser = User.objects.filter(id = id)
    if len(newUser) > 0:
        return redirect('/ponteiro/register/?error=1')

    if id.strip() == '' or password.strip() == '' or name.strip() == '':
        return redirect('/ponteiro/register/?error=3')
    
    if any(char in id for char in [' ', '<', '>', ':', '"', '/', '\\', '|', '?', '*']):
        return redirect('/ponteiro/register/?error=4')
    
    if len(id.strip()) < 5 or len(password.strip()) < 5 or len(name.strip()) < 5:
        return redirect('/ponteiro/register/?error=5')
    if len(id.strip()) > 20 or len(password.strip()) > 20:
        return redirect('/ponteiro/register/?error=6')
    if len(name.strip()) > 80:
        return redirect('/ponteiro/register/?error=7')
    if len(description) > 800:
        return redirect('/ponteiro/register/?error=8')

    if request.FILES.get('picture') == None:
        profile_directory = os.path.join(settings.BASE_DIR, f'media/user_profiles/{id}/profilePicture')
        os.makedirs(profile_directory, exist_ok=True)

        default_picture_path = os.path.join(settings.BASE_DIR, 'media', 'anonymous.png')
        copyfile(default_picture_path, os.path.join(profile_directory, 'anonymous.png'))

        picture = f'user_profiles/{id}/profilePicture/anonymous.png'
    else:
        picture = request.FILES.get('picture')
        try:
            img = Image.open(picture)
            img.verify()
        except Exception:
            return redirect('/ponteiro/register/?error=1')

    newUser = User(picture=picture, name=name, id=id, description=description, password=password, language=language)
    newUser.save()

    return redirect('/ponteiro/register/?error=0')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def loginValidate(request):
    id = request.POST.get('userid')
    password = request.POST.get('userpass')

    if id.strip() == '' or password.strip() == '':
        return redirect('/ponteiro/login/?error=1')

    newUser = User.objects.filter(id = id).filter(password = password)
    if len(newUser) == 0:
        return redirect('/ponteiro/login/?error=2')
    
    request.session['User'] = newUser[0].id
    return redirect(f'/ponteiro/{id}/home')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request, id):
    if request.session.get('User') == id:
        newUser = User.objects.filter(id = id)
        theme = newUser[0].theme
        language = newUser[0].language
        pictureShow = newUser[0].picture
        return render(request, f'{ language }/homeScreen.html', {'picture' : pictureShow, 'id' : id, 'theme' : theme})
    else:
        request.session.flush()
        return redirect('/ponteiro/login/?error=3')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)   
def profile(request, id):
    if request.session.get('User') == id:
        newUser = User.objects.filter(id = id)
        theme = newUser[0].theme
        language = newUser[0].language

        pictureShow = newUser[0].picture
        nameShow = newUser[0].name
        idShow = newUser[0].id
        descriptionShow = newUser[0].description
        passwordShow = newUser[0].password

        error = request.GET.get('error')
        return render(request, f'{ language }/profileScreen.html', {'picture' : pictureShow, 'name' : nameShow, 'id' : idShow, 'description' : descriptionShow, 'password' : passwordShow, 'error' : error, 'theme' : theme}) 
    else:
        request.session.flush()
        return redirect('/ponteiro/login/?error=3')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def profileedit(request, id):
    if request.session.get('User') == id:
        error = request.GET.get('error')
        newUser = User.objects.filter(id = id)
        theme = newUser[0].theme
        language = newUser[0].language
        picture = newUser[0].picture
        return render(request, f'{ language }/profileEditScreen.html', {'id' : id, 'error' : error, 'picture' : picture, 'theme' : theme})
    else:
        request.session.flush()
        return redirect('/ponteiro/login/?error=3')

@cache_control(no_cache=True, must_revalidate=True, no_store=True) 
def profileeditValidate(request, id):
    if request.session.get('User') == id:
        user_instance = User.objects.get(id=id)

        if 'picture' in request.FILES:
            picture = request.FILES['picture']
            try:
                img = Image.open(picture)
                img.verify()
            except Exception:
                return redirect(f'/ponteiro/{id}/profile/edit/?error=1')
            imgpath = user_instance.picture.path
            user_instance.picture = picture

        if 'description' in request.POST:
            user_description = request.POST['description']
            if user_description:
                if (user_description == user_instance.description):
                    return redirect(f'/ponteiro/{id}/profile/edit/?error=4')
                if len(user_description) <= 800:
                    user_instance.description = user_description
                else:
                    return redirect(f'/ponteiro/{id}/profile/edit/?error=2')

        if 'password' in request.POST:
            user_password = request.POST['password']
            if user_password:
                if (user_password == user_instance.password):
                    return redirect(f'/ponteiro/{id}/profile/edit/?error=4')
                if len(user_password.strip()) <= 20 and len(user_password.strip()) >= 5:
                    user_instance.password = user_password
                else:
                    return redirect(f'/ponteiro/{id}/profile/edit/?error=3')

        if (not('picture' in request.FILES) and len(user_description.strip()) == 0 and len(user_password.strip()) == 0):
            return redirect(f'/ponteiro/{id}/profile/edit/?error=4')
        user_instance.save()
        
        if 'picture' in request.FILES:
            os.remove(imgpath)

        return redirect(f'/ponteiro/{id}/profile/edit/?error=0')

    else:
        request.session.flush()
        return redirect('/ponteiro/login/?error=3')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def profiledelete(request, id):
    if request.session.get('User') == id:
        imgpath = User.objects.filter(id = id)[0].picture.path
        dirpath = os.path.dirname(imgpath)
        rootpath = os.path.dirname(dirpath)
        os.remove(imgpath)
        os.rmdir(dirpath)
        os.rmdir(rootpath)
        User.objects.filter(id = id).delete()
        request.session.flush()
        return redirect('/ponteiro/login/?error=0')
    else:
        request.session.flush()
        return redirect('/ponteiro/login/?error=3')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def userSearch(request, id):
    if request.session.get('User') == id:
        newUser = User.objects.filter(id = id)
        theme = newUser[0].theme
        language = newUser[0].language
        pictureShow = newUser[0].picture
        error = request.GET.get('error')
        return render(request, f'{ language }/userSearchScreen.html', {'picture' : pictureShow, 'id' : id,'error' : error, 'theme' : theme})
    else:
        request.session.flush()
        return redirect('/ponteiro/login/?error=3')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)   
def searchValidate(request, id):
    if request.session.get('User') == id:
        userSearchId = request.POST.get('usersearchid')

        if userSearchId == '':
            return redirect(f'/ponteiro/{id}/userSearch/?error=1')
        newUser = User.objects.filter(id = userSearchId).exclude(id = id)
        if len(newUser) == 0:
            return redirect(f'/ponteiro/{id}/userSearch/?error=2')
        else:
            return redirect(f'/ponteiro/{id}/{newUser[0].id}_profile')
    else:
        request.session.flush()
        return redirect('/ponteiro/login/?error=3')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)   
def userSearchProfile(request, id, searchid):
    if request.session.get('User') == id:
        yourUser = User.objects.filter(id = id)
        theme = yourUser[0].theme
        language = yourUser[0].language
        picture = yourUser[0].picture

        newUser = User.objects.filter(id = searchid)
        pictureShow = newUser[0].picture
        nameShow = newUser[0].name
        idShow = newUser[0].id
        descriptionShow = newUser[0].description

        return render(request, f'{ language }/userSearchProfileScreen.html', {'picture' : picture, 'pictureSearched' : pictureShow, 'name' : nameShow, 'id' : id, 'idSearched' : idShow, 'description' : descriptionShow, 'theme' : theme})
    else:
        request.session.flush()
        return redirect('/ponteiro/login/?error=3')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)  
def notifications(request, id):
    if request.session.get('User') == id:
        newUser = User.objects.filter(id = id)
        screen = request.GET.get('screen')
        language = newUser[0].language
        picture = newUser[0].picture
        theme = newUser[0].theme
        return render(request, f'{ language }/notificationsScreen.html', {'picture' : picture, 'id' : id, 'theme' : theme, 'screen' : screen})
    else:
        request.session.flush()
        return redirect('/ponteiro/login/?error=3')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def homeconfig(request, id):
    if request.session.get('User') == id: 
        newUser = User.objects.filter(id = id)
        theme = newUser[0].theme
        language = newUser[0].language
        pictureShow = newUser[0].picture
        return render(request, f'{ language }/homeConfigScreen.html', {'picture' : pictureShow, 'id' : id, 'theme' : theme})
    else:
        request.session.flush()
        return redirect('/ponteiro/login/?error=3')
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def homeconfigvalidate(request, id):
    if request.session.get('User') == id:
        user_instance = User.objects.get(id=id)
        theme = request.GET.get('themechange')
        language = request.GET.get('languagechange')

        if theme:
            user_instance.theme = theme
        if language:
            user_instance.language = language
        user_instance.save()
        return redirect(f'/ponteiro/{ id }/config')
    else:
        request.session.flush()
        return redirect('/ponteiro/login/?error=3')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request, id):
    if request.session.get('User') == id:
        request.session.flush()
        return redirect('/ponteiro')
    else:
        request.session.flush()
        return redirect('/ponteiro/login/?error=3')

# Create your views here.